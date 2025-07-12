import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

# import chromadb  # Temporarily disabled for deployment


load_dotenv()


class Chain:
    def __init__(self):
        if not os.getenv("GROQ_API_KEY"):
            raise ValueError("GROQ_API_KEY environment variable is required")
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0,
        )
        # self.chroma_client = chromadb.Client()  # Temporarily disabled for deployment

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(str(res.content))
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, resume_text, name, college, unique):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### RESUME:
            {resume_text}

            ### INSTRUCTION:
            You are {name}, {college}. {unique}.
            You're reaching out to a potential client regarding a project they've posted. Your goal is to write a concise, compelling cold email that highlights your capabilities and relevant experience based on your resume and the job requirement.

Mention your relevant experience, unique strengths, and any notable achievements or projects that demonstrate your ability to deliver results. Use your resume above to reference your skills and experience that match the client's needs.

Structure your email like this:
A warm, personalized intro.
A brief connection to the job or business problem they're facing.
How you can help: mention your technical skills, past results, and approach.
A friendly CTA to schedule a short call or demo.
Sign off as:
{name}
{college}
{unique}
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke(
            {
                "job_description": str(job),
                "resume_text": resume_text,
                "name": name,
                "college": college,
                "unique": unique,
            }
        )
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
