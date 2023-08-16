import os
import sys
import requests
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain

from langchain.chat_models import ChatOpenAI

sys.path.append(".")
from config import API_URL, MODEL

load_dotenv(dotenv_path=".")
HFACE_API_TOKEN = os.getenv("HFACE_API_TOKEN")


def get_caption(img_loc):
    """Creates a caption for the input image"""
    pl = pipeline("image-to-text", model=MODEL)
    caption = pl(img_loc)[0]["generated_text"]
    print(caption)
    return caption


def generate_story(scenario):
    """Creates a brief story from the input caption"""
    template = """
    You are a storyteller;
    You can generate a short story based on a brief description. The story should be no more than 20 words and it should be mildly amusing.

    DESCRIPTION: {scenario}
    STORY:
    """
    prompt = PromptTemplate(template=template, input_variables=["scenario"])

    llm_story = LLMChain(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1),
        prompt=prompt,
    )
    story = llm_story.predict(scenario=scenario)
    return story


def text_to_speech(img_stem, story):
    headers = {"Authorization": HFACE_API_TOKEN}
    payload = {"inputs": story}

    audio = requests.post(API_URL, headers=headers, json=payload)
    # save it locally
    with open(f"./speech/{img_stem}_story.flac", "wb") as f:
        f.write(audio.content)
