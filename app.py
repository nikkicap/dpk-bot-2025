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
st.write("Ask me about puppy training protocols — crate training, leash walking, play, grooming, health checks, and more.")

# Load OpenAI API key (must be added in Streamlit Cloud secrets)
if "OPENAI_API_KEY" not in st.secrets:
    st.warning("Please add your OpenAI API key to Streamlit secrets to use this app.")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ----------------------------
# Knowledge Base (Weeks 1–12 condensed protocols + videos)
# ----------------------------
knowledge_base = [
    # Week 1
    {"topic": "follow-me walk", "week": 1,
     "text": "Puppies instinctively follow. Walk in safe areas off-leash, avoid carrying, redirect from hazards, encourage different surfaces.",
     "video": "https://example.com/week1-follow-me-video"},
    {"topic": "crate training basics", "week": 1,
     "text": "Exercise first, place calmly in crate, support settling, release before whining, use treats and gentle soothing.",
     "video": "https://example.com/week1-crate-training-video"},
    {"topic": "feeding in crate", "week": 1,
     "text": "Slide food bowl into back of crate while holding puppy, release to eat, let out before whining.",
     "video": "https://example.com/week1-feeding-video"},
    {"topic": "housebreaking", "week": 1,
     "text": "Take puppy to same potty spot, praise for toileting outside, watch for signs after sleep, play, eating/drinking, crate when unsupervised.",
     "video": "https://example.com/week1-potty-video"},

    # Week 2
    {"topic": "body handling", "week": 2,
     "text": "Cradle puppy on back briefly, release when relaxed. Add nose-to-tail touches: ears, mouth, belly, paws, tail, genitals.",
     "video": "https://example.com/week2-body-video"},
    {"topic": "waiting for food bowl", "week": 2,
     "text": "Cover bowl with foot until puppy sits, release when calm. Repeat until they wait consistently.",
     "video": "https://example.com/week2-food-video"},

    # Week 3
    {"topic": "settling awake in crate", "week": 3,
     "text": "Toss treat in crate, reward for lying down, lengthen time between treats, step further away gradually.",
     "video": "https://example.com/week3-crate-video"},

    # Week 4
    {"topic": "loose leash walking intro", "week": 4,
     "text": "Start without leash. Deliver treats at nose height by your pant seam. Stop feet and lure puppy back if they drift.",
     "video": "https://example.com/week4-llw-video"},

    # Week 5
    {"topic": "hide and seek", "week": 5,
     "text": "Play when puppy is distracted. Hide behind object. Step out if they go wrong way. Celebrate big when found.",
     "video": "https://example.com/week5-hide-video"},
    {"topic": "puppy play", "week": 5,
     "text": "Follow no-bite, no-chase rule. Encourage tug with toys. Bubble one pup, then let other explore before releasing both.",
     "video": "https://example.com/week5-play-video"},
    {"topic": "grooming intro", "week": 5,
     "text": "Tap with brush then reward. Increase brushing gradually. Touch paws gently, add nail file later. Keep sessions short, positive.",
     "video": "https://example.com/week5-groom-video"},

    # Week 6
    {"topic": "distraction game", "week": 6,
     "text": "Say 'Yep!' and reward when pup notices distraction but doesn’t move. Start with people, then sounds, dropped objects, food bowls.",
     "video": "https://example.com/week6-distraction-video"},
    {"topic": "sleep outside crate", "week": 6,
     "text": "For housebroken pups. First nights: settle in bed briefly, then crate. Later allow outside crate if calm. Stop if accidents/destruction.",
     "video": "https://example.com/week6-crate-video"},

    # Week 7
    {"topic": "threshold distractions", "week": 7,
     "text": "Practice distraction game at doors/cars. Wait until puppy processes calmly, then move forward together.",
     "video": "https://example.com/week7-threshold-video"},
    {"topic": "tub intro", "week": 7,
     "text": "Empty tub with towel for grip. Let puppy problem-solve, help lightly if needed. Goal: puppy jumps in independently.",
     "video": "https://example.com/week7-tub-video"},

    # Week 8
    {"topic": "harness use", "week": 8,
     "text": "Always clip leash to front harness loop. Never walk on flat collar. Lure puppy through harness with treats.",
     "video": "https://example.com/week8-harness-video"},
    {"topic": "loose leash walking", "week": 8,
     "text": "Hold leash opposite hand, keep J shape. Deliver treats with inside hand at nose height. Stop and lure back if puppy pulls.",
     "video": "https://example.com/week8-llw-video"},
    {"topic": "wet tub training", "week": 8,
     "text": "Start with just-wet tub bottom. Gradually add water up to 1 inch. Help lightly but encourage independence.",
     "video": "https://example.com/week8-tub-video"},

    # Week 9
    {"topic": "automatic settle", "week": 9,
     "text": "Sit with leash short, wait 10s. Reward when puppy lies down. Jackpot the first independent down. Change chairs and repeat.",
     "video": "https://example.com/week9-settle-video"},
    {"topic": "bath water intro", "week": 9,
     "text": "Puppy should already enter 1 inch water. Slowly drip water on back. Keep sessions short (~1 min) and fun.",
     "video": "https://example.com/week9-bath-video"},

    # Week 10
    {"topic": "llw troubleshooting", "week": 10,
     "text": "Reward only when puppy looks calmly at surroundings. Use sniff breaks as rewards you control. If pulling, turn hips and walk other way. Praise when leash slackens.",
     "video": "https://example.com/week10-llw-video"},
    {"topic": "bath half body", "week": 10,
     "text": "Gradually pour more water until half body wet. Keep sessions short (~1 min), positive, repeat often.",
     "video": "https://example.com/week10-bath-video"},

    # Week 11
    {"topic": "peas or carrots settle", "week": 11,
     "text": "Praise when puppy lays down. Wait 10s, reward for staying. Increase settle length gradually each repetition.",
     "video": "https://example.com/week11-settle-video"},
    {"topic": "automatic sit greet", "week": 11,
     "text": "Handler approaches, puppy sits automatically. Add gentle petting, then strangers. Goal: sit steady while greeted.",
     "video": "https://example.com/week11-greet-video"},

    # Week 12
    {"topic": "health check", "week": 12,
     "text": "Examine nose, eyes, mouth, ears, coat, skin, body, feet, and genitals. Use knuckle trick to check weight.",
     "video": "https://example.com/week12-health-video"},
    {"topic": "public settle", "week": 12,
     "text": "Puppy should auto-settle 5+ minutes in public. Don’t cue — let them think to lay down. Jackpot the first time.",
     "video": "https://example.com/week12-settle-video"}
]

# ----------------------------
# Embeddings
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
# Search Notes
# ----------------------------
def search_notes(query):
    query_vec = get_embedding(query)
    sims = [cosine_similarity([query_vec], [kb["embedding"]])[0][0] for kb in knowledge_base]
    best = knowledge_base[int(np.argmax(sims))]
    return best

# ----------------------------
# Chat Response
# ----------------------------
def generate_response(query):
    best = search_notes(query)
    prompt = f"""
    The user asked: {query}.
    Here are trainer’s notes: {best['text']}.
    Please respond as a supportive puppy trainer:
    - Explain clearly in 2–5 natural sentences.
    - Be concise but complete.
    - Suggest the demo video if available.
    - Mention which Week materials they can review for more.
    - If the question isn’t directly in notes, suggest the closest related protocol.
    """
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a friendly puppy training assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    answer = resp.choices[0].message.content
    if best.get("video"):
        answer += f"\n\n🎥 Demo video: {best['video']}"
    answer += f"\n📖 See Week {best['week']} materials for more."
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
