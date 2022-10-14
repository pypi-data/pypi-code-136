import click
from stochasticx.utils.docker import (
    start_container, 
    stop_and_remove_container,
    get_logs_container,
    get_open_ports_container
)
from stochasticx.utils.gpu_utils import is_nvidia_gpu_available
from stochasticx.local.stable_diffusion import inference
import sys
from PIL import Image
import numpy as np
from pathlib import Path
import uuid
from stochasticx.datasets.datasets import Datasets


@click.group(name="stable-diffusion")
def stable_diffusion():
    pass


@click.command(name="deploy")
@click.option(
    '--type', 
    default="pytorch", 
    show_default=True, 
    help='Model type', 
    type=click.Choice(['pytorch', 'aitemplate'], case_sensitive=False)
)
@click.option(
    '--port', 
    default="5000", 
    show_default=True, 
    help='Port'
)
def deploy(type, port):
    docker_image = "public.ecr.aws/t8g5g2q5/stable-diffusion:{}".format(type)
    
    try:
        Datasets.get_datasets()
    except:
        print("[+] Execute ---> stochasticx login")
        print("[+] Or sign up in the following URL https://app.stochastic.ai/signup")
        sys.exit()

    print("[+] Deploying Stable Diffusion model")
    print("[+] If it is the first time you deploy the model, it might take some minutes to deploy it")
    start_container(
        docker_image=docker_image,
        ports={"5000": port},
        container_name="stochasticx_stable_diffusion",
        detach=True,
        gpu=is_nvidia_gpu_available()
    )
    
    print("[+] Stable Diffusion running in the port {}".format(port))
    print("[+] Using GPU: {}".format(is_nvidia_gpu_available()))
    print("[+] Run the following command to start generating:") 
    print("\tstochasticx stable-diffusion infer --prompt 'an astronaut riding a horse'")


@click.command(name="logs")
def logs():
    print("[+] Logs")
    logs = get_logs_container("stochasticx_stable_diffusion")
    print(logs)


@click.command(name="stop")
def stop():
    print("[+] Stopping and removing stable-diffusion model")
    stop_and_remove_container("stochasticx_stable_diffusion")
    print("[+] Removed")
    
    
@click.command(name="infer")
@click.option(
    '--prompt', 
    required=True, 
    help='Prompt to generate images', 
)
@click.option(
    '--img_height', 
    default=512, 
    type=int,
    show_default=True, 
    help='The height in pixels of the generated image.'
)
@click.option(
    '--img_width', 
    default=512, 
    type=int,
    show_default=True, 
    help='The width in pixels of the generated image.'
)
@click.option(
    '--num_inference_steps', 
    default=50, 
    type=int,
    show_default=True, 
    help='The number of denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference'
)
@click.option(
    '--num_images_per_prompt', 
    default=1, 
    type=int,
    show_default=True, 
    help='The number of images to generate per prompt.'
)
@click.option(
    '--seed', 
    default=None, 
    type=int,
    show_default=True, 
    help='Seed to make generation deterministic'
)
@click.option(
    '--saving_path', 
    default="generated_images", 
    type=str,
    show_default=True, 
    help='Directory where the generated images will be saved'
)
def infer(
    prompt, 
    img_height, 
    img_width, 
    num_inference_steps,
    num_images_per_prompt,
    seed,
    saving_path
):
    # Create directory to save images if it does not exist
    saving_path = Path(saving_path)
    if not saving_path.exists():
        saving_path.mkdir(exist_ok=True, parents=True)
        
    ports = get_open_ports_container("stochasticx_stable_diffusion")
    if len(ports) == 0:
        print("[+] Before doing the inference you have to run: stochasticx stable-diffusion deploy")
        sys.exit()
    
    print("[+] Generating images...")
    images, time = inference(
        url="http://127.0.0.1:{}/predict".format(list(ports.values())[0]),
        prompt=prompt, 
        img_height=img_height, 
        img_width=img_width, 
        num_inference_steps=num_inference_steps,
        num_images_per_prompt=num_images_per_prompt,
        seed=seed
    )
    
    print("[+] Time needed to generate the images: {} seconds".format(time))
    
    pil_images = []
    for img in images:
        pil_images.append(
            Image.fromarray(np.uint8(img))
        )
        
    # Save PIL images with a random name
    for img in pil_images:
        img.save('{}/{}.png'.format(
            saving_path.as_posix(),
            uuid.uuid4()
        ))

    print("[+] Images saved in the following path: {}".format(saving_path.as_posix()))


stable_diffusion.add_command(deploy)
stable_diffusion.add_command(logs)
stable_diffusion.add_command(stop)
stable_diffusion.add_command(infer)