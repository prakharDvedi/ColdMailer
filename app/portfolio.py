import pandas as pd
# import chromadb  # Temporarily disabled for deployment
import uuid
# from chromadb.config import Settings  # Temporarily disabled for deployment


class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        # ChromaDB temporarily disabled for deployment
        # self.chroma_client = chromadb.PersistentClient(path="vectorstore")
        # self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        # ChromaDB temporarily disabled for deployment
        # if not self.collection.count():
        #     for _, row in self.data.iterrows():
        #         self.collection.add(
        #             documents=str(row["Techstack"]),
        #             metadatas={"links": str(row["Links"])},
        #             ids=[str(uuid.uuid4())]
        #         )
        pass

    def query_links(self, skills):
        # Return sample portfolio links instead of ChromaDB query
        # ChromaDB temporarily disabled for deployment
        # return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
        
        # Return sample portfolio links for demonstration
        sample_links = [
            {"links": "https://example.com/react-portfolio"},
            {"links": "https://example.com/python-portfolio"}
        ]
        return sample_links
