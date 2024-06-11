import streamlit as st

# App Title
st.title("Exercise Guidance for Fall Prevention")

# Introduction
st.write("""
This application helps healthcare providers follow the AHRQ guidelines for fall prevention through exercise recommendations. By inputting patient-specific information, providers can receive tailored advice to help reduce the risk of falls in older adults.
""")

# Collecting Patient Information
st.header("Patient Information")

age = st.number_input("Age", min_value=0, max_value=120, value=65)
sex = st.selectbox("Sex", options=["Male", "Female", "Other"])
history_of_falls = st.selectbox("History of Falls", options=["Yes", "No"])
mobility_aid = st.selectbox("Uses Mobility Aid", options=["Yes", "No"])
balance_problems = st.selectbox("Balance Problems", options=["Yes", "No"])
muscle_weakness = st.selectbox("Muscle Weakness", options=["Yes", "No"])
vision_problems = st.selectbox("Vision Problems", options=["Yes", "No"])
medications = st.multiselect("Select Medications", ["Antidepressants", "Antihypertensives", "Sedatives", "None"])

# Provide Recommendations Based on Guidelines
st.header("Recommendations")

recommendations = []

if age >= 65:
    recommendations.append("Regular exercise focusing on strength and balance, such as Tai Chi or yoga.")
if history_of_falls == "Yes" or balance_problems == "Yes":
    recommendations.append("Include balance training exercises to improve stability.")
if muscle_weakness == "Yes":
    recommendations.append("Incorporate resistance training to enhance muscle strength.")
if vision_problems == "Yes":
    recommendations.append("Ensure regular eye check-ups and use prescribed visual aids.")
if medications:
    recommendations.append("Review medications with healthcare provider to identify any that may increase fall risk.")

if recommendations:
    st.write("### Exercise Recommendations:")
    for rec in recommendations:
        st.write(f"- {rec}")
else:
    st.write("No specific exercise recommendations based on the provided information.")

st.write("""
### General Guidelines:
1. **Strength Training**: Engage in exercises that strengthen the legs and core.
2. **Balance Exercises**: Perform activities that improve balance, such as standing on one leg.
3. **Flexibility**: Incorporate stretching exercises to maintain flexibility.
4. **Aerobic Activity**: Participate in moderate aerobic activities like walking or swimming.
5. **Regular Review**: Regularly review exercise plans with a healthcare provider to ensure they remain appropriate and effective.

Refer to the full [AHRQ guidelines](https://cds.ahrq.gov/cdsconnect/artifact/exercise-guidance-primary-care-fall-prevention) for detailed information.
""")
