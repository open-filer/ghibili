import streamlit as st
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline

def load_model():
    model_id = "nitrosocke/Ghibli-Diffusion"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

def generate_ghibli_style(image, pipe):
    prompt = "Ghibli-style portrait, high quality, anime-style, detailed"
    image = pipe(prompt, image=image).images[0]
    return image

st.title("Ghibli-Style Portrait Generator")
pipe = load_model()

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_image:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Original Image", use_column_width=True)
    
    if st.button("Generate Ghibli Portrait"):
        with st.spinner("Processing..."):
            result = generate_ghibli_style(image, pipe)
            st.image(result, caption="Ghibli-Style Portrait", use_column_width=True)
