import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
# import chromadb  # Temporarily disabled for deployment
from pydantic import SecretStr


load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0,
            api_key=SecretStr(os.getenv("GROQ_API_KEY") or ""),
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

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Prakhar Dwivedi, a 3rd-year student at IIIT Bhopal specializing in AI-powered web development, full-stack MERN applications, Next.js, Python scripting, and data visualization with Power BI. You're currently working on impactful projects that blend automation, user experience, and smart analytics to solve real-world business problems.
Youre reaching out to a potential client regarding a project theyve posted. Your goal is to write a concise, compelling cold email that highlights your capabilities in building custom, scalable AI or software solutions that optimize processes, reduce costs, or enhance user experiences—based on the job requirement.

Even though you're a student, your experience building real-world solutions like Ascend (a gamified self-growth app) or a GenAI-powered cold mail generator using LangChain and Groq proves your ability to deliver practical, results-driven outcomes.

Structure your email like this:
A warm, personalized intro.
A brief connection to the job or business problem they're facing.
How you can help: mention your technical skills (e.g., MERN, AI, Power BI), past results (e.g., 70% time reduction, 5x performance boosts), and approach.
Attach or link to relevant portfolio projects that match their need.
A friendly CTA to schedule a short call or demo.
Also, include the most relevant ones from these links to showcase your portfolio: {link_list}.
Sign off as:
Prakhar Dwivedi
MERN & GenAI Developer | IIIT Bhopal
Specializing in Automations, AI-Driven Tools, and Data Intelligence
            ### EMAIL (NO PREAMBLE):

            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))
