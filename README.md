# modal-fastapi-openai-streamlit

This repository contains an AI-powered marketing campaign generator. The application uses [OpenAI's GPT-3.5 model](https://platform.openai.com/docs/models) to generate creative marketing campaign suggestions based on user prompts. The backend is built using [FastAPI](https://fastapi.tiangolo.com/) and interacts with OpenAI's API, while the frontend is a [Streamlit](https://streamlit.io/) application that provides an interactive user interface. The applications are designed for containerized deployment using the [Modal](https://modal.com/) platform. Users simply input their brand name and a short description, and the system will generate a unique marketing campaign for them.

## Installation

```
conda create --name modal-fastapi-openai-streamlit -c conda-forge python=3.10
conda activate modal-fastapi-openai-streamlit
pip install -r requirements.txt
```


## [SERVER] Modal deployment

Getting started
The nicest thing about all of this is that you don’t have to set up any infrastructure. Just:

- Create an account at modal.com
- Install the modal-client package
- Set up a token
…and you can start running jobs right away.

```
cd backend
modal serve fastapi_app.py
```

To deploy this as a permanent app, run the command

```
modal deploy fastapi_app.py
```

## [CLIENT] Streamlit app

```
streamlit run st_app.py
```