# copiolot
AI Copilot to solve problems.
First use case we're trying to solve is Jobs and Candidates matching.

# Hackathon 25 - AI Chatbot Application

## Project Overview
This project is a prototype version of AI chatbot application.

## Project Structure
- `chatbot/models/ollama.py`: Contains the `OllamaModel` class for generating responses using the Ollama library.
- `streamlit_ui/app.py`: Streamlit application for the chatbot UI.
- `chatbot/bot.py`: Initializes the chatbot model and handles conversation logic.
- `chatbot/utils/responses.py`: Utility functions for generating responses.
- `README.md`: Project documentation.

## Local Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- pipenv
- Local Ollama setup. Follow this link for Ollama local setup: [Ollama Setup](https://medium.com/@abonia/ollama-and-langchain-run-llms-locally-900931914a46)

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/hackathon-25.git
   cd hackathon-25
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the FastAPI backend:**
   ```sh
   cd langchain_p/api
   streamlit run app.py
   ```

## Usage
- Enter your message in the text input field and press Submit button.
- The chatbot will respond with an AI-generated message.

