# Chatbot Backend for Notion-Integrated Website

This repository hosts the backend code for a chatbot integrated with a website built using Notion. The backend is built using the Flask framework and hosted on Render. It handles API calls to OpenAI's GPT-4-mini model and returns chatbot responses, which are displayed in a chatbox embedded on the front end.

## Project Overview

- **Frontend**: The UI of the chatbot is embedded in a Notion page using HTML, CSS, and JavaScript.
- **Backend**: Flask-based backend that handles requests from the front end.
- **API Integration**: The backend communicates with OpenAI's GPT-4-mini model to process user input and return responses.
- **Hosting**: The backend is deployed on Render, which handles scaling and uptime.

## Getting Started

### 1. Clone the Repository

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/your_username/chatbot-backend.git
cd chatbot-backend
```

### 2. Install Dependencies

Before running the application, ensure all necessary Python dependencies are installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables (API Keys)

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

### 4. Run the backend locally

To test the backend locally, you can run the Flask app using the gunicorn command. The backend listens for requests and processes them through the OpenAI API. Use the following command to start the server:

```bash
gunicorn --bind 0.0.0.0:10000 api.backend:app
```
### 5. Deploy the backend to Render

To deploy this backend to Render, follow these steps:

	1.	Go to Render and create an account if you haven’t already.
	2.	Create a new web service and link it to this GitHub repository.
	3.	Set the build command to:

```bash 
pip install -r requirements.txt
```

    4.	Set the start command to:

```bash
gunicorn --bind 0.0.0.0:10000 api.backend:app
```

    5.	Add the OPENAI_API_KEY environment variable in the Environment section.

### 6. Frontend Integration with Notion

The frontend of this project is embedded in a Notion page. Since Notion doesn’t support native JavaScript or HTML directly, we embed a chatbox created using HTML, CSS, and JavaScript.

Follow these steps to integrate your frontend:

	1.	Create an HTML file that includes the chatbox design, some CSS for styling, and JavaScript to handle requests to the backend.
	2.	Push this into your github.io website 
    3.  Embed the link to the github.io website in the Notion page.


Check out my website repository for the frontend code: [AI-assistant-frontend](https://github.com/soheilzi/soheilzi.github.io)
