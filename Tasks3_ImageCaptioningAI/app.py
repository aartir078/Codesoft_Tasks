
import gradio as gr
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

MODEL_NAME = "Salesforce/blip-image-captioning-base"

print("Loading the image captioning model...")

device = "cuda" if torch.cuda.is_available() else "cpu"

processor = BlipProcessor.from_pretrained(MODEL_NAME)
model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)
model.to(device)
model.eval()

print(f"Model loaded successfully on {device.upper()}!")


def generate_caption(image):
    if image is None:
        return "Please upload an image first."

    inputs = processor(images=image, return_tensors="pt")
    inputs = {key: value.to(device) for key, value in inputs.items()}

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=40,
            num_beams=4
        )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption.capitalize()


demo = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil", label="Upload an image"),
    outputs=gr.Textbox(label="Generated caption"),
    title="Image Captioning AI",
    description=(
        "Upload an image and let a pretrained AI model "
        "generate a natural-language description."
    ),
    examples=None
)

if __name__ == "__main__":
    demo.launch()
