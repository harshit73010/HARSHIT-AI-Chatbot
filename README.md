# HARSHIT-AI-Chatbot
AI chatbot built using Python and Streamlit with the Hugging Face Inference API. It uses the Llama-3.1-8B-Instruct model to generate intelligent responses and demonstrates how to integrate large language models into web applications.


##  How to Run the Project

Follow these steps to run the chatbot on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/harshit-ai-chatbot.git
cd harshit-ai-chatbot
```

### 2. Install required dependencies

Make sure Python is installed, then install numpy,pandas,streamlit,OpenAi,hugging face libraries

### 3. Add your Hugging Face API Key

Open **app.py** and replace the API key with your own:

```python
client = InferenceClient(api_key="YOUR_HF_API_KEY")
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

### 5. Open in browser

After running the command, Streamlit will provide a local URL such as:

```
http://localhost:8501
```

Open this link in your browser to start chatting with the AI chatbot.
