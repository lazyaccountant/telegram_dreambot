import requests
from PIL import Image
import io
from keys import hf_key

token = hf_key


def query(payload, model):
	API_URL = f"https://api-inference.huggingface.co/models/{model}"
	headers = {"Authorization": f"Bearer {token}"}

	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def text2image(prompt: str):

	image_bytes = query({
		"inputs": prompt,
		"wait_for_model": "True"
		},
		model="stabilityai/stable-diffusion-xl-base-1.0")

	img_bytes = io.BytesIO(image_bytes)
	image = Image.open(img_bytes)
	image.save("test.jpeg")

	return image


def text2anime(prompt: str):

	image_bytes = query({
		"inputs": prompt,
		"wait_for_model": "True"
		},
		model="cagliostrolab/animagine-xl-3.1")

	img_bytes = io.BytesIO(image_bytes)
	image = Image.open(img_bytes)
	image.save("test.jpeg")

	return image

if __name__ == "__main__":
	text2image()