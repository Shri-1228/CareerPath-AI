import streamlit as st
import google.generativeai as genai
import os
from markdown_pdf import MarkdownPdf, Section

# 1. Setup API Key Securely
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

st.set_page_config(page_title="CareerPath AI", page_icon="🚀")

st.title("🚀 CareerPath AI: Resume Builder")
st.subheader("Transform your details into a professional resume instantly.")

# 2. User Input Form
with st.form("resume_form"):
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
    with col2:
        phone = st.text_input("Phone Number")
        linkedin = st.text_input("LinkedIn URL")
    
    education = st.text_area("Education (College, Degree, Year)")
    skills = st.text_area("Top Skills (e.g. Python, Java, SQL)")
    experience = st.text_area("Experience (Leave blank if you are a Fresher)")

    # This is the line that fixes the "Missing Submit Button" error
    submit = st.form_submit_button("Generate Resume")

# 3. AI Logic
if submit:
    if not full_name:
        st.error("Please enter your name.")
    else:
        prompt = f"""
        Act as an expert resume writer. Create a professional markdown resume for:
        Name: {full_name}
        Email: {email} | Phone: {phone} | LinkedIn: {linkedin}
        
        Education: {education}
        Skills: {skills}
        Experience: {experience if experience else "I am a fresher, focus on my academic projects and education."}
        
        Instructions: Use professional bullet points. Use hierarchical headings.
        """
        
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            resume_text = response.text
            
            st.success("Resume Generated!")
            st.markdown(resume_text)
            
            # 4. PDF Rendering
            pdf = MarkdownPdf(toc_level=1)
            pdf.add_section(Section(resume_text))
            pdf.save("resume.pdf")
            
            with open("resume.pdf", "rb") as f:
                st.download_button("Download PDF", f, "resume.pdf")
                
        except Exception as e:
            st.error(f"Error: {e}")