# Ghibli-Style Portrait Generator

## Overview
The **Ghibli-Style Portrait Generator** is a web application built with **Streamlit** that transforms user-uploaded images into **Studio Ghibli-style portraits** using a pre-trained Stable Diffusion model.

## Features
- Upload an image (JPG, JPEG, PNG)
- Generate a **Ghibli-style** version of the uploaded image
- Uses **Stable Diffusion** for high-quality AI-generated portraits
- Supports **CUDA acceleration** for faster processing on GPUs

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed.

### Install Dependencies
Run the following command:
```bash
pip install streamlit torch diffusers transformers accelerate Pillow
```

## Usage
Run the application using:
```bash
streamlit run app.py
```
Then, open the **localhost URL** provided in the terminal.

## Model Used
This application uses the **Stable Diffusion** model fine-tuned for **Ghibli-style** portraits:  
🔗 [nitrosocke/Ghibli-Diffusion](https://huggingface.co/nitrosocke/Ghibli-Diffusion)

## License
This project is for educational purposes. Follow **Hugging Face's model usage guidelines** when using AI-generated images.

---
Enjoy creating your **Ghibli-style** portraits! 🚀

