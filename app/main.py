import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import pdfplumber

from chains import Chain
from utils import clean_text


def extract_text_from_pdf(resume_file):
    if resume_file is None:
        return ""
    with pdfplumber.open(resume_file) as pdf:
        return "\n".join(
            page.extract_text() for page in pdf.pages if page.extract_text()
        )


def create_streamlit_app(llm, clean_text):
    st.set_page_config(layout="centered", page_title="ColdMailer", page_icon="📧")
    st.markdown(
        """
        <div style='text-align: center; margin-bottom: 1.5em;'>
            <h1 style='color: #4F8BF9; margin-bottom: 0.2em;'>📧 ColdMailer</h1>
            <h4 style='color: #b0b8c1; font-weight: 400;'>AI-Powered Cold Email Generator for Job Outreach</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

    col1, col2 = st.columns([4, 1], gap="small")
    with col1:
        name = st.text_input("Your Name", value="Prakhar Dwivedi")
        college = st.text_input(
            "Your College/Post", value="IIIT Bhopal, 3rd-year student"
        )
        unique = st.text_input(
            "Something unique about you", value="AI hackathon winner"
        )
        resume_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
        url_input = st.text_input(
            "Enter a Job/Career Page URL:",
            value="https://careers.nike.com/software-engineer/job/R-61123",
            placeholder="Paste the job posting link here...",
            label_visibility="visible",
        )
    with col2:
        st.markdown("<div style='height: 1.9em'></div>", unsafe_allow_html=True)
        submit_button = st.button("🚀 Generate Email", use_container_width=True)

    st.markdown("")

    if submit_button:
        with st.spinner("Scraping job description and generating your custom email..."):
            try:
                loader = WebBaseLoader([url_input])
                data = clean_text(loader.load().pop().page_content)
                resume_text = extract_text_from_pdf(resume_file)
                jobs = llm.extract_jobs(data)
                for job in jobs:
                    email = llm.write_mail(job, resume_text, name, college, unique)
                    st.success("Here's your personalized cold email:")
                    st.markdown(
                        f"""
                        <div style='background: #232634; border-radius: 8px; padding: 1.2em 1em; margin-bottom: 1em; border: 1px solid #4F8BF9; color: #fff;'>
                        <pre style='font-size: 1em; font-family: inherit; white-space: pre-wrap; color: #fff;'>{email}</pre>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            except Exception as e:
                st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    create_streamlit_app(chain, clean_text)
