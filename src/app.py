import streamlit as st
from utils import get_caption, generate_story, text_to_speech


def main():
    st.set_page_config(page_title="Storify Your Image", page_icon="\U0001F642")
    st.header("Turn your image into an amusing little story.")
    img = st.file_uploader("Upload an image:", type="jpg")

    if img:
        # get the image bytes
        img_bytes = img.getvalue()
        img_name = img.name
        img_stem = img.name.split(".")[0]

        # save the image locally
        with open(f"./img/{img_name}", "wb") as f:
            f.write(img_bytes)
        # display image on the app
        st.image(img, caption="Your image.", use_column_width=True)

        # step 1: get caption from image
        caption = get_caption(f"./img/{img_name}")
        # step 2: generate story from the caption using llm
        story = generate_story(caption)
        # step 3: convert story into speech
        text_to_speech(img_stem, story)

        # display caption, story, and speech on the app
        with st.expander("caption"):
            st.write(caption)
        with st.expander("story"):
            st.write(story)

        st.audio(f"./speech/{img_stem}_story.flac")


if __name__ == "__main__":
    main()
