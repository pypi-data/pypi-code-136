import requests
from typing import Union, List
import numpy as np


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
    