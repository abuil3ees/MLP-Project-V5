import streamlit as st

st.image("logo.png", width=400)
st.title("Leadership Readiness Tool")

summary = st.sidebar.text_area(
    "Case study/Problem statement:",
    placeholder="Write your case study or problem statement here..."
)

# Define behaviors and their 5 questions each (total 40 questions)
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

# Dictionary to hold responses
responses = {}

# Display questions and collect responses
for behavior, questions in behaviors.items():
    st.subheader(behavior)
    for i, q in enumerate(questions):
        key = f"{behavior}_{i}"
        if q["type"] == "Yes/No":
            responses[key] = st.radio(q["question"], ["Yes", "No"], key=key, index=1)
        elif q["type"] == "Scale":
            responses[key] = st.slider(q["question"], min_value=1, max_value=10, key=key, value=5)

# When "Submit" is pressed, compute overall and per-behavior scores
if st.button("Submit"):
    total_score = 0
    max_score_total = len(responses) * 10  # Each question max is 10
    
    # Dictionary to store behavior-specific scores
    behavior_scores = {}
    
    # Calculate overall score and per-behavior scores
    for behavior, questions in behaviors.items():
        behavior_total = 0
        for i in range(len(questions)):
            key = f"{behavior}_{i}"
            response = responses[key]
            if isinstance(response, str):
                behavior_total += 10 if response == "Yes" else 0
            else:
                behavior_total += response
        behavior_percentage = (behavior_total / (len(questions) * 10)) * 100
        behavior_scores[behavior] = behavior_percentage
        total_score += behavior_total

    readiness_score = (total_score / max_score_total) * 100

    # Determine overall status and traffic light image
    if readiness_score >= 80:
        status = "Green - Ready to Proceed"
        image_path = "green_light.png"
    elif readiness_score >= 50:
        status = "Yellow - Needs Improvement"
        image_path = "yellow_light.png"
    else:
        status = "Red - Do Not Proceed"
        image_path = "red_light.png"
    
    # Define tailored recommendations for each behavior
    behavior_recommendations = {
        "1. We Trust and Respect One Another": "Consider holding regular team-building sessions and open forums to reinforce mutual trust and respect.",
        "2. We Are Inclusive and Take Care of Each Other": "Focus on creating inclusive policies and improving support programs to ensure every team member feels valued.",
        "3. We Listen and Communicate Transparently": "Enhance communication channels by organizing frequent town halls and establishing structured feedback mechanisms.",
        "4. We Embrace Change and Learn Continuously": "Invest in training and development initiatives and create platforms for sharing lessons learned.",
        "5. We Strive to Improve and Innovate Courageously": "Encourage innovation by rewarding creative ideas and setting up cross-functional collaboration projects.",
        "6. We Keep Sustainability Top of Mind in Everything We Do": "Integrate sustainability metrics into your regular reviews and engage teams in green initiatives.",
        "7. We Create Value for Customers": "Review customer feedback in-depth and adjust strategies to improve customer service and product offerings.",
        "8. We Drive Performance, Celebrate Successes, and Win Together": "Set clear performance targets, recognize team achievements, and foster a collaborative work culture."
    }
    
    # Identify behaviors that scored low (threshold can be adjusted; here we use 70%)
    low_behaviors = {behavior: score for behavior, score in behavior_scores.items() if score < 70}
    
    # Build dynamic recommendations message
    recommendations_message = ""
    if low_behaviors:
        recommendations_message += "The following areas need attention:\n\n"
        for behavior, score in low_behaviors.items():
            recommendations_message += f"**{behavior}**: Score: {score:.1f}%\n- {behavior_recommendations.get(behavior, '')}\n\n"
    else:
        recommendations_message = "All key areas are performing well. Continue reinforcing your strengths!"

    # Display results and tailored recommendations in two columns
    with st.expander("View Results", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_path, width=150)
            st.markdown(f"### Final Readiness Score: {readiness_score:.2f}%")
            st.markdown(f"### Status: **{status}**")
        with col2:
            st.markdown("### Focus & Recommendations")
            st.markdown(recommendations_message)
