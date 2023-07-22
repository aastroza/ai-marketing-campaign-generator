# modal-fastapi-openai-streamlit
Modal.com deployment backend, Streamlit app


## Installation

```
conda create --name modal-fastapi-openai-streamlit -c conda-forge python=3.10
conda activate modal-fastapi-openai-streamlit
pip install -r requirements.txt
```


## Modal deployment

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