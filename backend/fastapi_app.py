# SOURCES
# Fastapi app: https://gist.github.com/SidJain1412/205f3e9ab54c24144599ec625591bd5b
# Modal deployment: https://github.com/modal-labs/modal-examples/blob/main/07_web_endpoints/fastapi_app.py


# Import the required libraries
from fastapi import FastAPI
from pydantic import BaseModel
from modal import App, Image, asgi_app, Secret
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# Set up the Modal deployment
web_app = FastAPI()
app = App("example-fastapi-app")

# Define the image for deployment, installing necessary libraries
image = (
    Image.debian_slim()
    .pip_install(
        "fastapi",
        "openai",
        "pydantic",
        "python-dotenv",
    )
)

# Define a Pydantic model for the data the API will receive
class Item(BaseModel):
    prompt: str

# Define a function to get a response from OpenAI based on a prompt
def get_response_openai(prompt):
    try:
        prompt = prompt
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are an expert creative marketer. Create a campaign for the brand the user enters. Respond in markdwon format."},
                {"role": "user", "content": prompt},
            ],
        )
    except Exception as e:
        print("Error in creating campaigns from openAI:", str(e))
        return 503
    return response.choices[0].message.content

# Define a route that will respond to a GET request with a simple message
@web_app.get("/ping")
async def ping():
    return "pong"

# Define a route that will respond to a POST request with a marketing campaign based on the received data
@web_app.post("/campaign")
async def handle_campaign(item: Item):
    return {"campaign_text" : get_response_openai(item.prompt)}

# Set up the deployment details for the Modal platform
@app.function(image=image, secrets=[Secret.from_dotenv()])
@asgi_app()
def fastapi_app():
    return web_app


# Deploy the application if this script is run directly
if __name__ == "__main__":
    app.deploy("webapp")