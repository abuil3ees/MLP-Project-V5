import streamlit as st

st.image("logo.png", width=400)
st.title("Leadership Readiness Tool")

summary = st.sidebar.text_area(
    "Case study/Problem statement:",
    placeholder="Write your case study or problem statement here..."
)

# Define the 8 behaviors and their questions using the new text
behaviors = {
    "1. We Trust and Respect One Another": [
        {
            "question": "For the team affected by the change, do team members demonstrate mutual trust and respect?",
            "type": "Yes/No"
        },
        {
            "question": "Are there regular opportunities for open and honest communication regarding this change and are they used?",
            "type": "Scale"
        },
        {
            "question": "How confident are employees that leadership values their input regarding the change?",
            "type": "Scale"
        },
        {
            "question": "Are actions taken by leadership perceived as fair and equitable, as it pertains to this transition?",
            "type": "Scale"
        },
        {
            "question": "Do employees feel they can rely on their colleagues for support during the transition?",
            "type": "Yes/No"
        }
    ],
    "2. We Are Inclusive and Take Care of Each Other": [
        {
            "question": "For this project, is inclusivity considered when making decisions that impact employees?",
            "type": "Yes/No"
        },
        {
            "question": "Are employee well-being programs actively promoted and used during this project?",
            "type": "Scale"
        },
        {
            "question": "How supported do employees feel by their managers during this change?",
            "type": "Scale"
        },
        {
            "question": "Are team members encouraged to share diverse perspectives to leaders of this change?",
            "type": "Yes/No"
        },
        {
            "question": "Is there a culture of teamwork and collaboration in regards to this scope?",
            "type": "Scale"
        }
    ],
    "3. We Listen and Communicate Transparently": [
        {
            "question": "Did leadership effectively communicate this change?",
            "type": "Yes/No"
        },
        {
            "question": "Are employees confident in leadership’s transparency for this project?",
            "type": "Yes/No"
        },
        {
            "question": "Are mechanisms in place to collect feedback and are they utilized during this project transition?",
            "type": "Scale"
        },
        {
            "question": "Is feedback from employees or customers addressed in a timely manner?",
            "type": "Yes/No"
        },
        {
            "question": "Are regular town halls or Q&A sessions conducted?",
            "type": "Yes/No"
        }
    ],
    "4. We Embrace Change and Learn Continuously": [
        {
            "question": "Are employees provided with resources to adapt to new roles and do they use them?",
            "type": "Scale"
        },
        {
            "question": "How willing are employees to embrace the change and learn?",
            "type": "Scale"
        },
        {
            "question": "Are lessons learned during this transition documented and used?",
            "type": "Yes/No"
        },
        {
            "question": "Is leadership promoting a culture of continuous learning for this project?",
            "type": "Scale"
        },
        {
            "question": "Are knowledge-sharing sessions encouraged and utilized?",
            "type": "Scale"
        }
    ],
    "5. We Strive to Improve and Innovate Courageously": [
        {
            "question": "For this project, are innovative ideas encouraged and implemented?",
            "type": "Yes/No"
        },
        {
            "question": "Are process improvements identified?",
            "type": "Yes/No"
        },
        {
            "question": "How confident is leadership in fostering evolution of this change or project?",
            "type": "Scale"
        },
        {
            "question": "Are there structured programs to support this innovation?",
            "type": "Yes/No"
        }
    ],
    "6. We Keep Sustainability Top of Mind in Everything We Do": [
        {
            "question": "Are sustainability goals integrated into transformation processes for this project's ability to create continuous efficiency within the company?",
            "type": "Yes/No"
        },
        {
            "question": "Are there metrics for this identified sustainability and are they being frequently updated?",
            "type": "Yes/No"
        },
        {
            "question": "Are employees and stakeholders aligned on sustainability priorities?",
            "type": "Scale"
        },
        {
            "question": "For this change or project, are actions being taken to reduce environmental/social impact?",
            "type": "Yes/No"
        },
        {
            "question": "Are suppliers and partners evaluated for sustainability as it effects this change?",
            "type": "Yes/No"
        }
    ],
    "7. We Create Value for Customers": [
        {
            "question": "Are mechanisms in place to minimize customer disruptions as this transition takes place?",
            "type": "Yes/No"
        },
        {
            "question": "Is there a process to identify and address customer gaps through the implementation of the project?",
            "type": "Yes/No"
        },
        {
            "question": "Do employees and leadership collaborate to balance customer needs for this transition?",
            "type": "Scale"
        },
        {
            "question": "Are customer satisfaction metrics tracked and improving for this transition?",
            "type": "Yes/No"
        },
        {
            "question": "Is customer feedback actively used for decision-making through the implementation of the project?",
            "type": "Scale"
        }
    ],
    "8. We Drive Performance, Celebrate Successes, and Win Together": [
        {
            "question": "For this change, are performance goals clearly defined and aligned?",
            "type": "Yes/No"
        },
        {
            "question": "How frequently are milestones and achievements recognized for the project?",
            "type": "Scale"
        },
        {
            "question": "Is there a formal process to document lessons learned during the execution of this project?",
            "type": "Yes/No"
        },
        {
            "question": "Do employees feel leadership fosters collaboration and motivation while executing this change?",
            "type": "Scale"
        },
        {
            "question": "Are incentives and recognition programs aligned with contributions that benefit this execution?",
            "type": "Yes/No"
        }
    ]
}

# Dictionary to hold the responses
responses = {}

# Render the questions and collect responses
for behavior, questions in behaviors.items():
    st.subheader(behavior)
    for i, q in enumerate(questions):
        key = f"{behavior}_{i}"
        if q["type"] == "Yes/No":
            responses[key] = st.radio(q["question"], ["Yes", "No"], key=key, index=1)
        elif q["type"] == "Scale":
            responses[key] = st.slider(q["question"], min_value=1, max_value=10, key=key, value=5)

# Process the responses when submitted
if st.button("Submit"):
    total_score = 0
    max_score_total = 0
    behavior_scores = {}

    # Calculate per-behavior scores and overall score
    for behavior, questions in behaviors.items():
        behavior_total = 0
        behavior_max = len(questions) * 10  # each question max = 10
        for i, q in enumerate(questions):
            key = f"{behavior}_{i}"
            response = responses[key]
            if q["type"] == "Yes/No":
                # "Yes" scores 10, "No" scores 0
                behavior_total += 10 if response == "Yes" else 0
            else:
                behavior_total += response
        behavior_percentage = (behavior_total / behavior_max) * 100
        behavior_scores[behavior] = behavior_percentage
        total_score += behavior_total
        max_score_total += behavior_max

    readiness_score = (total_score / max_score_total) * 100

    # Determine overall status and corresponding traffic light image
    if readiness_score >= 80:
        status = "Green - Ready to Proceed"
        image_path = "green_light.png"
    elif readiness_score >= 50:
        status = "Yellow - Needs Improvement"
        image_path = "yellow_light.png"
    else:
        status = "Red - Do Not Proceed"
        image_path = "red_light.png"

    # Tailored recommendations for each behavior
    behavior_recommendations = {
        "1. We Trust and Respect One Another": "Focus on enhancing mutual trust and open communication during the transition. Consider team-building activities and transparent leadership practices.",
        "2. We Are Inclusive and Take Care of Each Other": "Improve inclusivity and well-being support. Encourage diverse perspectives and foster a collaborative team environment throughout the project.",
        "3. We Listen and Communicate Transparently": "Strengthen communication channels. Ensure leadership effectively communicates changes and that feedback mechanisms are actively used.",
        "4. We Embrace Change and Learn Continuously": "Invest in resources and training. Support employees in adapting to new roles and promote continuous learning with structured knowledge-sharing.",
        "5. We Strive to Improve and Innovate Courageously": "Encourage innovative ideas and rigorously identify process improvements. Establish structured programs to support innovation.",
        "6. We Keep Sustainability Top of Mind in Everything We Do": "Integrate sustainability into transformation processes and keep metrics updated. Focus on reducing environmental/social impacts and evaluate partners accordingly.",
        "7. We Create Value for Customers": "Prioritize minimizing customer disruptions and addressing gaps. Leverage customer feedback to continuously improve products and services.",
        "8. We Drive Performance, Celebrate Successes, and Win Together": "Set clear performance goals and consistently recognize achievements. Foster collaboration and ensure incentives align with contributions."
    }

    # Identify behaviors with low scores (threshold set at 70%)
    low_behaviors = {behavior: score for behavior, score in behavior_scores.items() if score < 70}

    # Build the dynamic recommendations message
    recommendations_message = ""
    if low_behaviors:
        recommendations_message += "The following areas need attention:\n\n"
        for behavior, score in low_behaviors.items():
            recommendations_message += f"**{behavior}** (Score: {score:.1f}%)\n- {behavior_recommendations.get(behavior, 'No recommendation available.')}\n\n"
    else:
        recommendations_message = "All key areas are performing well. Keep up the excellent work!"

    # Display results and recommendations in two columns
    with st.expander("View Results", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_path, width=150)
            st.markdown(f"### Final Readiness Score: {readiness_score:.2f}%")
            st.markdown(f"### Status: **{status}**")
        with col2:
            st.markdown("### Focus & Recommendations")
            st.markdown(recommendations_message)
