# ColdMailer 🧊📧

ColdMailer is an AI-powered cold email generation tool built using **LangChain**, **Python**, and **Jupyter Notebook**. It leverages modern GenAI tools and web scraping to help users craft professional, targeted outreach emails tailored to specific contexts and clients.

![image](https://github.com/user-attachments/assets/5f783ba4-eda3-4655-ba5f-291250451422)
![image](https://github.com/user-attachments/assets/5bc1f01f-db2b-4a15-8d3a-4c55e8209c35)

---

## ✨ Features

- 🔍 **Automated Data Extraction**: Uses `WebBaseLoader` to scrape key information from websites.
- 🧠 **Smart Prompting**: Integrates large language models (LLMs) for personalized cold email generation.
- 📊 **JSON Parsing**: Processes and structures scraped data using `jsonparser` and `pandas`.
- 🧪 **Notebook-based Prototyping**: Built in Jupyter for flexibility, experimentation, and analysis.
- 🤩 **Modular Design**: Clean and customizable components for different industries or use cases.

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Jupyter Notebook**
- **Pandas**
- **WebBaseLoader**
- **jsonparser**
- **Groq (LLM integration)**

---

## 📁 Project Structure

```
ColdMailer/
│
├── .ipynb_checkpoints/         # Notebook checkpoints
├── ColdMailer_Generator.ipynb  # Main notebook
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/prakharDvedi/ColdMailer.git
cd ColdMailer
```

### 2. Install Dependencies

Ensure you have Python 3.9+ and run:

```bash
pip install -r requirements.txt
```

### 3. Run the Notebook

Use Jupyter:

```bash
jupyter notebook ColdMailer_Generator.ipynb
```

---

## 🧠 How It Works

1. **Input a Company/Client Website URL**
2. **WebBaseLoader** fetches relevant information.
3. **LLM (via LangChain)** generates a context-aware cold email.
4. Output: A well-written, personalized email ready to send.

---

## 📌 Use Cases

- Freelancers and consultants reaching out to potential clients
- Startups initiating B2B partnerships
- Sales reps targeting leads with AI-generated intros
- Resume or internship cold emails for students

---

## ⚠️ Disclaimer

This tool uses AI to generate content. Please review and customize all emails before sending to ensure accuracy and relevance.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or add.

---

## 📬 Contact

Made with ❤️ by [Prakhar Dwivedi](https://github.com/prakharDvedi)  
Reach out for collaborations, feedback, or just to connect!
