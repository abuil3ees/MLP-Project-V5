import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets integration
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Leadership Readiness Responses").sheet1

# Apply custom CSS for green radio button selection dots
st.markdown("""
    <style>
        div[role="radiogroup"] > div > div[data-baseweb="radio"] input:checked + div {
            background-color: #008000 !important;
            border-color: #008000 !important;
        }
        div[role="radiogroup"] > div > div[data-baseweb="radio"] label {
            color: black !important;
            background-color: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

# Display the logo
st.image("logo.png", width=400)

# Title
st.title("Leadership Readiness Tool")

# Add a text box for summary input
summary = st.text_area("Case study/Problem statement:", placeholder="Write your case study or problem statement here...")

# Define behaviors and their 5 questions each
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
    ]
}

# Dictionary to store responses
responses = {}

# Display the questions
for behavior, questions in behaviors.items():
    st.subheader(behavior)
    for i, q in enumerate(questions):
        if q["type"] == "Yes/No":
            responses[f"{behavior}_{i}"] = st.radio(q["question"], ["Yes", "No"], index=1)
        elif q["type"] == "Scale":
            responses[f"{behavior}_{i}"] = st.slider(q["question"], min_value=1, max_value=10, value=5)

# Add a Submit button
if st.button("Submit"):
    total_score = sum([10 if v == "Yes" else v for v in responses.values()])
    max_score = len(responses) * 10
    readiness_score = (total_score / max_score) * 100

    # Determine traffic light status and image
    if readiness_score >= 80:
        status = "Green - Ready to Proceed"
        image_path = "green_light.png"
    elif readiness_score >= 50:
        status = "Yellow - Needs Improvement"
        image_path = "yellow_light.png"
    else:
        status = "Red - Do Not Proceed"
        image_path = "red_light.png"

    # Identify weakest behavior for targeted feedback
    lowest_behavior = min(behaviors.keys(), key=lambda b: sum([responses.get(f"{b}_{i}", 0) for i in range(len(behaviors[b]))]) / len(behaviors[b]))
    feedback_suggestions = {
        "1. We Trust and Respect One Another": "⚠️ Focus on building trust through open communication and fair leadership decisions.",
        "2. We Are Inclusive and Take Care of Each Other": "⚠️ Ensure diversity and inclusivity in decision-making and team support.",
        "3. We Listen and Communicate Transparently": "⚠️ Improve transparency in leadership decisions and increase employee feedback mechanisms.",
        "4. We Embrace Change and Learn Continuously": "⚠️ Strengthen training and learning opportunities for employees adapting to change.",
        "5. We Strive to Improve and Innovate Courageously": "⚠️ Encourage innovation by fostering a risk-friendly work environment."
    }
    personalized_feedback = feedback_suggestions.get(lowest_behavior, "✅ Keep up the good work!")

    # Display results with traffic light and feedback
    with st.expander("View Results", expanded=True):
        st.image(image_path, width=150)
        st.markdown(f"### Final Readiness Score: {readiness_score:.2f}%")
        st.markdown(f"### Status: **{status}**")
        st.markdown(f"### Focus Areas: \n{personalized_feedback}")
    
    st.success("Responses have been saved to Google Sheets.")
