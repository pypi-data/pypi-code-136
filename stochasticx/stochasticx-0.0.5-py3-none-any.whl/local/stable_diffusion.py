import requests
from typing import Union, List
import numpy as np
from stochasticx.local.download_models import download_model_from_s3
import tempfile
from pathlib import Path
import uuid

from diffusers import StableDiffusionPipeline
from typing import Union, List
import time
import sys

try:
    import torch
except:
    print("[+] Install PyTorch following the official instructions: https://pytorch.org/get-started/locally/")
    sys.exit()
    

def inference(
    url: str,
    prompt: Union[str, List[str]],
    img_height: int = 512,
    img_width: int = 512,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5,
    num_images_per_prompt: int = 1,
    seed: int = None
):
    response = requests.post(
        url=url,
        json={
            "prompt": prompt,
            "img_height": img_height,
            "img_width": img_width,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "num_images_per_prompt": num_images_per_prompt,
            "seed": seed
        }
    )
    
    response.raise_for_status()
    data = response.json()
    
    images = np.array(data.get("images"))
    time = data.get("generation_time_in_secs")
    
    return images, time
    
    
def init():
    temp_dir = Path(tempfile.gettempdir()) / str(uuid.uuid4())
    
    download_model_from_s3(
        "https://stochasticai.s3.amazonaws.com/stable-diffusion/pytorch_model.zip".format(type),
        str(temp_dir)
    )
    
    pytorch_model_path = temp_dir / "pytorch_model"
    
    pipe = StableDiffusionPipeline.from_pretrained(
        str(pytorch_model_path), 
        revision="fp16", 
        torch_dtype=torch.float16,
        use_auth_token=True
    )
    
    if torch.cuda.is_available():
        pipe = pipe.to("cuda")
        
    return pipe


def generate_images(
    model: StableDiffusionPipeline,
    prompt: Union[str, List[str]],
    img_height: int = 512,
    img_width: int = 512,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5,
    num_images_per_prompt: int = 1,
    seed: int = None,
    return_time=False
):
    """Do inference
    
    :param model: the Stable Diffusion pipeline
    :param prompt: the prompt
    :param img_height: height of the generated image, defaults to 512
    :param img_width: width of the generated image, defaults to 512
    :param num_inference_steps: the number of denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference, defaults to 50
    :param guidance_scale: guidance scale, defaults to 7.5
    :param num_images_per_prompt: the number of images to generate per prompt, defaults to 1
    :param seed: Seed to make generation deterministic, defaults to None
    :param return_time: specify if time taken to generate the images should be returned, defaults to False
    :return: the output images and the time (if return time is True)
    """
    generator = None
    if seed is not None:
        generator = torch.Generator(device='cuda')
        generator = generator.manual_seed(seed)

    start_time = time.time()
    with torch.autocast("cuda"):
        output = model(
            prompt=prompt,
            height=img_height,
            width=img_width,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            num_images_per_prompt=num_images_per_prompt,
            generator=generator
        )
    end_time = time.time()
    
    if return_time:
        return output.images, end_time - start_time
    
    return output.images