import streamlit as st

# (Inline CSS removed so that theme settings apply)

st.image("logo.png", width=400)
st.title("Leadership Readiness Tool")

summary = st.sidebar.text_area("Case study/Problem statement:",
                               placeholder="Write your case study or problem statement here...")

behaviors = {
    "1. We Trust and Respect One Another": [
        {"question": "Do team members demonstrate mutual trust and respect?", "type": "Yes/No"},
        {"question": "Are there regular opportunities for open and honest communication?", "type": "Yes/No"},
        {"question": "How confident are employees that leadership values their input?", "type": "Scale"},
        {"question": "Are actions taken by leadership perceived as fair and equitable?", "type": "Scale"},
        {"question": "Do employees feel they can rely on their colleagues for support?", "type": "Yes/No"}
    ],
    # ... (rest of the behaviors)
}

responses = {}

for behavior, questions in behaviors.items():
    st.subheader(behavior)
    for i, q in enumerate(questions):
        if q["type"] == "Yes/No":
            responses[f"{behavior}_{i}"] = st.radio(q["question"], ["Yes", "No"], index=1)
        elif q["type"] == "Scale":
            responses[f"{behavior}_{i}"] = st.slider(q["question"], min_value=1, max_value=10, value=5)

if st.button("Submit"):
    total_score = 0
    max_score = len(responses) * 10

    for key, value in responses.items():
        if isinstance(value, str):
            total_score += 10 if value == "Yes" else 0
        elif isinstance(value, int):
            total_score += value

    readiness_score = (total_score / max_score) * 100

    if readiness_score >= 80:
        status = "Green - Ready to Proceed"
        image_path = "green_light.png"
    elif readiness_score >= 50:
        status = "Yellow - Needs Improvement"
        image_path = "yellow_light.png"
    else:
        status = "Red - Do Not Proceed"
        image_path = "red_light.png"

    with st.expander("View Results", expanded=True):
        st.image(image_path, width=150)
        st.markdown(f"### Final Readiness Score: {readiness_score:.2f}%")
        st.markdown(f"### Status: **{status}**")
