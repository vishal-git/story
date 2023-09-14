# Convert your Picture into an Amusing Little Story

This app can be used to convert an image into an amusing little story / caption using LLM.

## Instructions to Launch the App 🚀

<details><summary><b>Show instructions</b></summary>

Once you make a copy of this codebase on your computer, activate a Python virtual environment using the following command:

`python -m venv .venv --prompt doc-parser`

Once the Python virtual environment is created, activate it and install all dependencies from `requirements.txt`.

`source .venv/bin/activate`

`pip install -r requirements.txt`

Once all dependencies are installed, you can launch the app using the following command:

`streamlit run src/app.py`

In a few seconds the app will be lanuched in your browser. If that doesn't happen automatically, you can copy the URL that's printed in the output.

</details>

## Secrets 🔑

<details><summary><b>Show config settings</b></summary>

This app makes a call to the OpenAI API. You will need to get the API key from [OpenAI] and store it locally in the `.env` file.

<p align='center'>
	<img src='./img/api-key.png', alt='API Keys', width='650'>
</p>

[OpenAI]:      https://openai.com
</details>
