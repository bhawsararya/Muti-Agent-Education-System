from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/sd-turbo",
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")
pipe.enable_attention_slicing()

def generate_image(prompt):
    image = pipe(
        prompt=prompt,
        num_inference_steps=1,
        guidance_scale=0.0,
        height=512,
        width=512
    ).images[0]

    return image