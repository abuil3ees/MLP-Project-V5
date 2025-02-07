import streamlit as st

st.image("logo.png", width=400)
st.title("Leadership Readiness Tool")

summary = st.sidebar.text_area(
    "Case study/Problem statement:",
    placeholder="Write your case study or problem statement here..."
)

# Define the 8 behaviors and their questions (total 40 questions)
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

# Predefined recommendations at the behavior level (existing summary recommendations)
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

# Detailed recommendations per question for more granular feedback
question_recommendations = {
    "1. We Trust and Respect One Another": {
        0: "Consider initiatives like team-building exercises and open dialogue sessions to build trust.",
        1: "Establish regular communication forums (meetings or briefings) to ensure open and honest dialogue.",
        2: "Increase leadership engagement by actively soliciting and addressing employee input.",
        3: "Enhance transparency and fairness in leadership decisions to build confidence.",
        4: "Promote a supportive environment through peer mentoring and collaboration activities."
    },
    "2. We Are Inclusive and Take Care of Each Other": {
        0: "Review decision-making processes to ensure inclusivity and equal representation.",
        1: "Enhance and actively promote well-being programs to support staff during the project.",
        2: "Provide additional managerial support and training to better assist employees.",
        3: "Encourage an environment where diverse perspectives are valued and sought out.",
        4: "Foster a culture of collaboration through team-building and joint problem-solving sessions."
    },
    "3. We Listen and Communicate Transparently": {
        0: "Improve communication strategies by clearly conveying change-related information.",
        1: "Build trust with employees by ensuring consistent and transparent messaging.",
        2: "Implement and promote effective feedback mechanisms to capture employee opinions.",
        3: "Address feedback promptly to show that employee and customer voices are valued.",
        4: "Increase the frequency of town halls or Q&A sessions to address concerns."
    },
    "4. We Embrace Change and Learn Continuously": {
        0: "Ensure adequate resources and training are available and accessible for role adaptation.",
        1: "Motivate employees to embrace change by demonstrating its benefits and opportunities.",
        2: "Establish a system to document lessons learned and share best practices.",
        3: "Promote continuous learning through regular training sessions and workshops.",
        4: "Facilitate knowledge-sharing sessions to disseminate insights across the team."
    },
    "5. We Strive to Improve and Innovate Courageously": {
        0: "Cultivate a culture that rewards innovative thinking and creative problem solving.",
        1: "Set up structured processes to systematically identify potential improvements.",
        2: "Boost leadership confidence by showcasing successful innovations and best practices.",
        3: "Develop formal programs to support and sustain innovation efforts."
    },
    "6. We Keep Sustainability Top of Mind in Everything We Do": {
        0: "Deepen the integration of sustainability into all transformation processes.",
        1: "Establish regular reviews and updates of sustainability metrics.",
        2: "Align internal and external stakeholders around clear sustainability priorities.",
        3: "Take proactive measures to reduce negative environmental and social impacts.",
        4: "Adopt supplier evaluation criteria that emphasize sustainability performance."
    },
    "7. We Create Value for Customers": {
        0: "Implement mechanisms that proactively minimize customer disruptions during transitions.",
        1: "Develop and maintain a process to identify and address gaps in customer service.",
        2: "Enhance collaboration between leadership and employees to better serve customer needs.",
        3: "Regularly track and analyze customer satisfaction to identify improvement areas.",
        4: "Ensure customer feedback directly informs decision-making and strategy adjustments."
    },
    "8. We Drive Performance, Celebrate Successes, and Win Together": {
        0: "Clearly define and communicate performance goals to ensure alignment.",
        1: "Increase recognition by regularly celebrating milestones and achievements.",
        2: "Establish a formal process to capture and share lessons learned from projects.",
        3: "Encourage a collaborative work environment with strong leadership support.",
        4: "Align incentive programs with actual contributions and measurable outcomes."
    }
}

# Dictionary to hold responses
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

if st.button("Submit"):
    total_score = 0
    max_score_total = 0
    behavior_scores = {}

    # Calculate scores per behavior and overall score
    for behavior, questions in behaviors.items():
        behavior_total = 0
        behavior_max = len(questions) * 10  # each question's max = 10
        for i, q in enumerate(questions):
            key = f"{behavior}_{i}"
            response = responses[key]
            if q["type"] == "Yes/No":
                behavior_total += 10 if response == "Yes" else 0
            else:
                behavior_total += response
        behavior_scores[behavior] = (behavior_total / behavior_max) * 100
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

    # Build detailed recommendations for each question per behavior
    detailed_recommendations = {}
    threshold_scale = 7  # Threshold for scale-type questions
    for behavior, questions in behaviors.items():
        recs = []
        for i, q in enumerate(questions):
            key = f"{behavior}_{i}"
            response = responses[key]
            if q["type"] == "Yes/No" and response == "No":
                rec = question_recommendations.get(behavior, {}).get(i, "")
                if rec:
                    recs.append(f"- {rec}")
            elif q["type"] == "Scale" and response < threshold_scale:
                rec = question_recommendations.get(behavior, {}).get(i, "")
                if rec:
                    recs.append(f"- {rec} (Score: {response})")
        if recs:
            detailed_recommendations[behavior] = recs

    # Build overall recommendations message
    overall_recommendations = ""
    # First, list behaviors that are below 70%
    low_behaviors = {b: score for b, score in behavior_scores.items() if score < 70}
    if low_behaviors:
        overall_recommendations += "The following areas need attention:\n\n"
        for behavior, score in low_behaviors.items():
            overall_recommendations += f"**{behavior}** (Score: {score:.1f}%)\n- {behavior_recommendations.get(behavior, 'No recommendation available.')}\n\n"
    else:
        overall_recommendations = "All key areas are performing well. Keep up the excellent work!"

    # Build detailed recommendations message string
    detailed_message = ""
    if detailed_recommendations:
        detailed_message += "Detailed Recommendations per Question:\n\n"
        for behavior, rec_list in detailed_recommendations.items():
            detailed_message += f"**{behavior}**:\n"
            for rec in rec_list:
                detailed_message += f"{rec}\n"
            detailed_message += "\n"

    # Display the results and recommendations in two columns
    with st.expander("View Results", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_path, width=150)
            st.markdown(f"### Final Readiness Score: {readiness_score:.2f}%")
            st.markdown(f"### Status: **{status}**")
        with col2:
            st.markdown("### Overall Focus & Recommendations")
            st.markdown(overall_recommendations)
            st.markdown("### Detailed Recommendations")
            st.markdown(detailed_message)
