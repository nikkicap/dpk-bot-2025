import streamlit as st

# ----------------------------
# Hard-Coded Knowledge Base (Weeks 1–12)
# ----------------------------
knowledge_base = {
    # Week 1
    "follow-me walk": {
        "answer": [
            "1. Walk in a safe area off-leash; puppies naturally follow.",
            "2. Avoid carrying the puppy unless necessary.",
            "3. Redirect if they wander toward a distraction.",
            "4. Encourage exploring different surfaces."
        ],
        "video": "https://example.com/week1-follow-me-video"
    },
    "crate training": {
        "answer": [
            "1. Exercise puppy first (follow-me walk).",
            "2. Place calmly in crate; block door gently if needed.",
            "3. Support settling with calm presence or treat.",
            "4. Let out before whining or feeling trapped."
        ],
        "video": "https://example.com/week1-crate-training-video"
    },
    "feeding in crate": {
        "answer": [
            "1. Hold puppy, slide bowl to back of crate.",
            "2. Release puppy to eat, close door.",
            "3. Let out when finished, before they bark."
        ],
        "video": "https://example.com/week1-feeding-video"
    },
    "housebreaking": {
        "answer": [
            "1. Take puppy to same outdoor potty spot each time.",
            "2. Praise for toileting outside.",
            "3. Watch closely; toilet after naps, play, eating/drinking.",
            "4. Crate when unsupervised; clean accidents fully."
        ],
        "video": "https://example.com/week1-potty-video"
    },

    # Week 2
    "body handling": {
        "answer": [
            "1. Cradle puppy on back for 1 minute.",
            "2. Pet until relaxed; release as soon as they soften.",
            "3. Add nose-to-tail touches: ears, mouth, belly, paws, tail, genitals.",
            "4. Repeat daily for 3–5 minutes."
        ],
        "video": "https://example.com/week2-body-video"
    },
    "waiting for food bowl": {
        "answer": [
            "1. Put kibble in hand + bowl.",
            "2. Place bowl on ground, cover with foot.",
            "3. Puppy sits → say 'yep' → lift foot → release to eat.",
            "4. Repeat until puppy waits consistently."
        ],
        "video": "https://example.com/week2-food-video"
    },

    # Week 3
    "settling awake in crate": {
        "answer": [
            "1. Start when puppy is calm.",
            "2. Toss treat in crate; reward low when puppy lies down.",
            "3. Gradually lengthen time between treats.",
            "4. Slowly step further away, return if puppy stirs."
        ],
        "video": "https://example.com/week3-crate-video"
    },

    # Week 4
    "loose leash walking intro": {
        "answer": [
            "1. Start without leash.",
            "2. Deliver treats at puppy’s nose height, pant seam line.",
            "3. Keep treat hand thumb at chin between rewards.",
            "4. Stop feet and use treat if pup drifts."
        ],
        "video": "https://example.com/week4-llw-video"
    },

    # Week 5
    "hide and seek": {
        "answer": [
            "1. Wait until puppy is distracted.",
            "2. Step behind object, let them search.",
            "3. If wrong way, step out and call.",
            "4. Celebrate big when they find you!"
        ],
        "video": "https://example.com/week5-hide-video"
    },
    "puppy play": {
        "answer": [
            "1. No bite, no chase play only.",
            "2. Encourage tug with toys.",
            "3. Bubble one pup, let other explore.",
            "4. Re-bubble, then release to play tug together."
        ],
        "video": "https://example.com/week5-play-video"
    },
    "grooming intro": {
        "answer": [
            "1. Tap puppy gently with brush, reward.",
            "2. Gradually increase brushing before reward.",
            "3. Touch paws gently, then add nail file/tap.",
            "4. Keep sessions short and positive."
        ],
        "video": "https://example.com/week5-groom-video"
    },

    # Week 6
    "distraction game": {
        "answer": [
            "1. Say 'Yep!' and reward when pup notices distraction but doesn’t move.",
            "2. Start with people, then sounds, dropped items, and food bowls.",
            "3. Keep it fun, reward early, repeat daily."
        ],
        "video": "https://example.com/week6-distraction-video"
    },
    "sleep outside crate": {
        "answer": [
            "1. Only for housebroken pups.",
            "2. First 2 nights: settle in bed 10 mins, then crate for night.",
            "3. Later nights: allow to stay out if calm.",
            "4. Stop if accidents or destruction appear."
        ],
        "video": "https://example.com/week6-crate-video"
    },

    # Week 7
    "threshold distractions": {
        "answer": [
            "1. Use Distraction Game before doors/cars.",
            "2. Wait until puppy processes calmly.",
            "3. Then move through threshold together."
        ],
        "video": "https://example.com/week7-threshold-video"
    },
    "tub intro": {
        "answer": [
            "1. Use empty tub with towel for grip.",
            "2. Let puppy problem-solve, help lightly if needed.",
            "3. Goal: puppy jumps in without assistance."
        ],
        "video": "https://example.com/week7-tub-video"
    },

    # Week 8
    "harness use": {
        "answer": [
            "1. Always clip leash to harness front loop.",
            "2. Never walk puppy on flat collar.",
            "3. Lure puppy through harness neck loop with treats."
        ],
        "video": "https://example.com/week8-harness-video"
    },
    "loose leash walking": {
        "answer": [
            "1. Hold leash in opposite hand; keep 'J' shape.",
            "2. Deliver treats with inside hand at nose height.",
            "3. Stop moving and lure back if puppy drifts."
        ],
        "video": "https://example.com/week8-llw-video"
    },
    "wet tub training": {
        "answer": [
            "1. Start with just-wet tub bottom.",
            "2. Increase water gradually, up to 1 inch.",
            "3. Help lightly but let puppy try alone."
        ],
        "video": "https://example.com/week8-tub-video"
    },

    # Week 9
    "automatic settle": {
        "answer": [
            "1. Sit with leash short, wait 10 seconds.",
            "2. Reward when puppy lies down.",
            "3. Jackpot the first independent down.",
            "4. Change chairs and repeat."
        ],
        "video": "https://example.com/week9-settle-video"
    },
    "bath water intro": {
        "answer": [
            "1. Only start if puppy jumps into 1 inch water.",
            "2. Slowly drip/pour water on back.",
            "3. Keep short (1 minute), fun, repeat."
        ],
        "video": "https://example.com/week9-bath-video"
    },

    # Week 10
    "llw troubleshooting": {
        "answer": [
            "1. Reward only when puppy looks at environment, not just handler.",
            "2. Use sniff breaks as rewards — trainer decides timing.",
            "3. If pulling, turn hips and walk other way.",
            "4. Praise when leash slackens."
        ],
        "video": "https://example.com/week10-llw-video"
    },
    "bath half body": {
        "answer": [
            "1. Puppy should already accept some water.",
            "2. Slowly bathe more of body, about half.",
            "3. Keep sessions short (~1 min), positive."
        ],
        "video": "https://example.com/week10-bath-video"
    },

    # Week 11
    "peas or carrots settle": {
        "answer": [
            "1. Praise when puppy lays down automatically.",
            "2. Wait 10+ seconds, reward for staying.",
            "3. Gradually increase settle length each rep."
        ],
        "video": "https://example.com/week11-settle-video"
    },
    "automatic sit greet": {
        "answer": [
            "1. Handler approaches → puppy auto-sits.",
            "2. Add gentle petting while puppy stays seated.",
            "3. Add strangers → puppy sits automatically for greeting."
        ],
        "video": "https://example.com/week11-greet-video"
    },

    # Week 12
    "health check": {
        "answer": [
            "1. Examine nose, eyes, mouth, ears, coat, skin.",
            "2. Check body for lumps/changes.",
            "3. Inspect feet (pads, between toes).",
            "4. Look at genitals for abnormalities.",
            "5. Use knuckle trick to assess weight."
        ],
        "video": "https://example.com/week12-health-video"
    },
    "public settle": {
        "answer": [
            "1. Puppy should auto-settle 5+ minutes in public.",
            "2. Don’t cue — let them think to lay down.",
            "3. Jackpot first time it happens on their own."
        ],
        "video": "https://example.com/week12-settle-video"
    }
}

# ----------------------------
# Streamlit Chatbot UI
# ----------------------------
st.set_page_config(page_title="Puppy Training Chatbot", page_icon="🐶")
st.title("🐶 Puppy Training Chatbot")
st.write("Ask me about puppy training protocols (crate, walks, food bowl, play, bath, etc.).")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("Your question:")

if user_input:
    response = None
    video = None
    for key in knowledge_base:
        if key in user_input.lower():
            response = knowledge_base[key]["answer"]
            video = knowledge_base[key].get("video")
            break

    if response:
        st.session_state["messages"].append(("user", user_input))
        st.session_state["messages"].append(("bot", response))
        if video:
            st.session_state["messages"].append(("bot", [f"🎥 Watch the demo here: {video}"]))
    else:
        st.session_state["messages"].append(("user", user_input))
        st.session_state["messages"].append(("bot", ["Sorry, I don’t have that in my notes yet. Try another keyword."]))

# Display chat
for role, msg in st.session_state["messages"]:
    if role == "user":
        st.markdown(f"**You:** {msg}")
    else:
        for line in msg:
            st.markdown(f"**TrainerBot:** {line}")
