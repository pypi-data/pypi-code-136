import tempfile
import zipfile
from pathlib import Path
import uuid
from tqdm import tqdm
import requests


def download_large_file(url, local_file_path):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        
        total_size_in_bytes = int(r.headers.get('content-length', 0))
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        
        with open(str(local_file_path), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                progress_bar.update(len(chunk))
                f.write(chunk)
                
    return local_file_path


def download_model_from_s3(public_url, directory_path):
    directory_path = Path(directory_path)
    
    if not directory_path.exists():
        directory_path.mkdir(parents=True, exist_ok=True) 
    
    temp_path = Path(tempfile.gettempdir()) / "{}.zip".format(uuid.uuid4())
    download_large_file(public_url, temp_path)
    
    with zipfile.ZipFile(temp_path, 'r') as zip_ref:
        zip_ref.extractall(str(directory_path))
