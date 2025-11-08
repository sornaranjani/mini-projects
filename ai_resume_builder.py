# Ai_resume_builder.py

import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# ------------------------------
# Load API key from .env
# ------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("⚠️ API key not found! Please add OPENAI_API_KEY to your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="AI Resume Builder", page_icon="🧠", layout="wide")

st.title("🧠 AI Resume Builder")
st.write("Generate a professional, ATS-friendly resume using AI. Fill in your details below.")


# Collect user details
with st.form("resume_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    job_title = st.text_input("Job Title (e.g., Data Analyst, Web Developer, Teacher)")
    summary = st.text_area("Professional Summary (optional)")
    skills = st.text_area("Skills (comma-separated, e.g., Python, HTML, Communication)")
    experience = st.text_area("Work Experience (describe your roles and achievements)")
    education = st.text_area("Education (degree, institution, year)")
    projects = st.text_area("Projects (optional)")

    submit = st.form_submit_button("✨ Generate Resume")

# ------------------------------
# Generate Resume with AI
# ------------------------------
if submit:
    with st.spinner("Generating your AI-powered resume..."):
        user_data = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Job Title: {job_title}
        Summary: {summary}
        Skills: {skills}
        Experience: {experience}
        Education: {education}
        Projects: {projects}
        """

        prompt = f"""
        You are ResumeWriterGPT, an expert in professional resume creation.
        Using the following user details, write a polished, ATS-friendly resume
        in proper format with clear sections.

        {user_data}

        The format should be:

        [Full Name]
        [Email] | [Phone]

        PROFESSIONAL SUMMARY
        <2-3 sentences>

        SKILLS
        - skill1
        - skill2
        - skill3

        EXPERIENCE
        <well-written bullet points for each role>

        EDUCATION
        <degree, institution, year>

        PROJECTS (if any)
        <2 lines per project>
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a professional resume writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            resume_text = response.choices[0].message.content.strip()
            st.success("✅ Resume generated successfully!")
            st.text_area("Your AI-Generated Resume:", value=resume_text, height=500)

            # Download option
            st.download_button(
                label="📄 Download Resume (TXT)",
                data=resume_text,
                file_name=f"{name.replace(' ', '_')}_Resume.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ Error generating resume: {str(e)}")
