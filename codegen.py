import gradio as gr
import google.generativeai as palm
from gradio.networking import get_file

# Replace 'YOUR_API_KEY' with your actual API key
palm.configure(api_key='YOUR_API_KEY')

# List available models
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name if models else None

def generate_code(category, prompt):
    if model:
        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0.8,
            max_output_tokens=2000,
        )
        response = completion.result
        return response
    else:
        return "No suitable models found."

# Define the Gradio UI
iface = gr.Interface(
    fn=generate_code,
    inputs=[
        gr.Radio(choices=["P&A Document", "API Document", "Java Spring Boot Code", "All"], label="Select Category"),
        gr.Textbox(label="Enter a prompt to generate code", lines=5)
    ],
    outputs=gr.Textbox(label="Generated Code", lines=10),
    interpretation="markdown"
)

# Launch the Gradio app
iface.launch(share=True)
