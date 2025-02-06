import streamlit as st

st.image("logo.png", width=400)
st.title("Leadership Readiness Tool")

summary = st.sidebar.text_area(
    "Case study/Problem statement:",
    placeholder="Write your case study or problem statement here..."
)

behaviors = {
    "1. We Trust and Respect One Another": [
        {"question": "Do team members demonstrate mutual trust and respect?", "type": "Yes/No"},
        {"question": "Are there regular opportunities for open and honest communication?", "type": "Yes/No"},
        {"question": "How confident are employees that leadership values their input?", "type": "Scale"},
        {"question": "Are actions taken by leadership perceived as fair and equitable?", "type": "Scale"},
        {"question": "Do employees feel they can rely on their colleagues for support?", "type": "Yes/No"}
    ],
    "2. We Are Inclusive and Take Care of Each Other": [
        {"question": "Is inclusivity considered when making decisions that impact employees?", "type": "Yes/No"},
        {"question": "Are employee well-being programs actively promoted?", "type": "Yes/No"},
        {"question": "How supported do employees feel by their managers?", "type": "Scale"},
        {"question": "Are team members encouraged to share diverse perspectives?", "type": "Yes/No"},
        {"question": "Is there a culture of teamwork and collaboration?", "type": "Scale"}
    ],
    "3. We Listen and Communicate Transparently": [
        {"question": "Are mechanisms in place to collect feedback during transitions?", "type": "Yes/No"},
        {"question": "How effectively does leadership communicate changes?", "type": "Scale"},
        {"question": "Are employees confident in leadership’s transparency?", "type": "Scale"},
        {"question": "Is feedback from employees or customers addressed in a timely manner?", "type": "Yes/No"},
        {"question": "Are regular town halls or Q&A sessions conducted?", "type": "Yes/No"}
    ],
    "4. We Embrace Change and Learn Continuously": [
        {"question": "Are employees provided with resources to adapt to new roles?", "type": "Yes/No"},
        {"question": "How willing are employees to embrace change and learn?", "type": "Scale"},
        {"question": "Are lessons learned during transitions documented and used?", "type": "Yes/No"},
        {"question": "Is leadership promoting a culture of continuous learning?", "type": "Scale"},
        {"question": "Are knowledge-sharing sessions encouraged?", "type": "Yes/No"}
    ],
    "5. We Strive to Improve and Innovate Courageously": [
        {"question": "Are innovative ideas encouraged and implemented?", "type": "Yes/No"},
        {"question": "How frequently are process improvements identified?", "type": "Scale"},
        {"question": "Are employees empowered to take risks and innovate?", "type": "Yes/No"},
        {"question": "How confident is leadership in fostering innovation?", "type": "Scale"},
        {"question": "Are there structured programs to support innovation?", "type": "Yes/No"}
    ],
    "6. We Keep Sustainability Top of Mind in Everything We Do": [
        {"question": "Are sustainability goals integrated into transformation processes?", "type": "Yes/No"},
        {"question": "How frequently are sustainability metrics reviewed?", "type": "Scale"},
        {"question": "Are employees and stakeholders aligned on sustainability priorities?", "type": "Scale"},
        {"question": "Are actions being taken to reduce environmental/social impact?", "type": "Yes/No"},
        {"question": "Are suppliers and partners evaluated for sustainability?", "type": "Yes/No"}
    ],
    "7. We Create Value for Customers": [
        {"question": "Are mechanisms in place to minimize customer disruptions?", "type": "Yes/No"},
        {"question": "Is there a process to identify and address customer gaps?", "type": "Yes/No"},
        {"question": "Do employees and leadership collaborate to balance customer needs?", "type": "Scale"},
        {"question": "Are customer satisfaction metrics tracked and improving?", "type": "Yes/No"},
        {"question": "Is customer feedback actively used for decision-making?", "type": "Scale"}
    ],
    "8. We Drive Performance, Celebrate Successes, and Win Together": [
        {"question": "Are performance goals clearly defined and aligned?", "type": "Yes/No"},
        {"question": "How frequently are milestones and achievements recognized?", "type": "Scale"},
        {"question": "Is there a formal process to document lessons learned?", "type": "Yes/No"},
        {"question": "Do employees feel leadership fosters collaboration and motivation?", "type": "Scale"},
        {"question": "Are incentives and recognition programs aligned with contributions?", "type": "Yes/No"}
    ]
}

responses = {}

for behavior, questions in behaviors.items():
    st.subheader(behavior)
    for i, q in enumerate(questions):
        key = f"{behavior}_{i}"
        if q["type"] == "Yes/No":
            responses[key] = st.radio(q["question"], ["Yes", "No"], key=key, index=1)
        elif q["type"] == "Scale":
            responses[key] = st.slider(q["question"], min_value=1, max_value=10, key=key, value=5)

if st.button("Submit"):
    total_score = 0
    max_score = len(responses) * 10
    for value in responses.values():
        if isinstance(value, str):
            total_score += 10 if value == "Yes" else 0
        elif isinstance(value, int):
            total_score += value

    readiness_score = (total_score / max_score) * 100

    if readiness_score >= 80:
        status = "Green - Ready to Proceed"
        image_path = "green_light.png"
        focus_message = (
            "Your leadership readiness is excellent. Your team demonstrates strong trust, transparent communication, "
            "and a high capacity for innovation. Continue to reinforce these strengths while maintaining your focus on "
            "continuous improvement and proactive risk management."
        )
    elif readiness_score >= 50:
        status = "Yellow - Needs Improvement"
        image_path = "yellow_light.png"
        focus_message = (
            "Your team shows moderate readiness. Key areas for improvement include enhancing team trust, ensuring "
            "clear and consistent communication, and building capabilities in innovation. Consider targeted training, "
            "regular feedback sessions, and structured team-building activities to bridge these gaps."
        )
    else:
        status = "Red - Do Not Proceed"
        image_path = "red_light.png"
        focus_message = (
            "Your team's readiness is below the desired level. Immediate attention is required to address critical issues, "
            "such as establishing trust, improving communication, and aligning leadership actions with team expectations. "
            "Focus on comprehensive interventions, including coaching, mentoring, and possibly external consultancy to drive significant improvements."
        )

    with st.expander("View Results", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_path, width=150)
            st.markdown(f"### Final Readiness Score: {readiness_score:.2f}%")
            st.markdown(f"### Status: **{status}**")
        with col2:
            st.markdown("### Focus & Recommendations")
            st.markdown(f"{focus_message}")
