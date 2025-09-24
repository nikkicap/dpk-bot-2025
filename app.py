import streamlit as st
from openai import OpenAI
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------
# Setup
# ----------------------------
st.set_page_config(page_title="Puppy Training Chatbot", page_icon="🐶")
st.title("🐶 Puppy Training Chatbot")
st.write("Ask me about puppy training protocols — crate training, leash walking, play, grooming, and more.")

# Load your OpenAI API key
if "OPENAI_API_KEY" not in st.secrets:
    st.warning("Please add your OpenAI API key to Streamlit secrets to use this app.")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ----------------------------
# Knowledge Base (sample shortened for demo — expand with all 12 weeks)
# ----------------------------
knowledge_base = [
    {
        "topic": "crate training",
        "text": "Exercise puppy first (follow-me walk). Place calmly in crate. Support settling with calm presence or treat. Let out before whining or feeling trapped.",
        "video": "https://example.com/week1-crate-training-video"
    },
    {
        "topic": "follow-me walk",
        "text": "Walk in safe area off-leash; puppies naturally follow. Avoid carrying unless necessary. Redirect if distracted. Encourage exploring surfaces.",
        "video": "https://example.com/week1-follow-me-video"
    },
    {
        "topic": "loose leash walking",
        "text": "Hold leash in opposite hand; keep loose J shape. Deliver treats at nose height, pant seam line. Stop moving and lure back if puppy pulls.",
        "video": "https://example.com/week8-llw-video"
    },
    {
        "topic": "settling awake in crate",
        "text": "Toss treat in crate. Reward low when puppy lies down. Gradually increase time between treats. Slowly step further away.",
        "video": "https://example.com/week3-crate-video"
    },
    {
        "topic": "grooming intro",
        "text": "Tap puppy gently with brush, reward. Gradually increase brushing before reward. Touch paws gently, then add nail file/tap. Keep sessions short and positive.",
        "video": "https://example.com/week5-groom-video"
    }
]

# ----------------------------
# Embeddings: Convert training text into vectors
# ----------------------------
def get_embedding(text):
    resp = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return np.array(resp.data[0].embedding)

for kb in knowledge_base:
    kb["embedding"] = get_embedding(kb["text"])

# ----------------------------
# Search Function
# ----------------------------
def search_notes(query):
    query_vec = get_embedding(query)
    sims = [cosine_similarity([query_vec], [kb["embedding"]])[0][0] for kb in knowledge_base]
    best = knowledge_base[int(np.argmax(sims))]
    return best

# ----------------------------
# Chat Function
# ----------------------------
def generate_response(query):
    best = search_notes(query)

    prompt = f"""
    You are a puppy training assistant. 
    The user asked: {query}.
    Here are the trainer’s notes: {best['text']}.
    Please respond in a clear, supportive, step-by-step style for a new puppy trainer.
    Include emojis sparingly, and mention a video link if available.
    """
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a helpful puppy training assistant."},
                  {"role": "user", "content": prompt}]
    )
    answer = resp.choices[0].message.content
    if best.get("video"):
        answer += f"\n\n🎥 Demo video: {best['video']}"
    return answer

# ----------------------------
# Streamlit Chat UI
# ----------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("Your question:")

if user_input:
    st.session_state["messages"].append(("user", user_input))
    bot_response = generate_response(user_input)
    st.session_state["messages"].append(("bot", bot_response))

for role, msg in st.session_state["messages"]:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        st.markdown(f"**TrainerBot:** {msg}")
