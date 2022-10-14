# https://alpha2phi.medium.com/yolo-using-fastapi-websocket-and-react-2b2d28e9f7ed

import numpy as np
import cv2
import base64
from .option import Option

@Option.wrap
def base64_to_image(uri:str):
   
   split_uri = uri.split(',') 
   
   encoded_data = split_uri[0] if len(split_uri) == 0 else split_uri[0]
   
   nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
   
   img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   
   return img

def image_to_base64(img: np.ndarray) -> bytes:
    """ Given a numpy 2D array, returns a JPEG image in base64 format """

    # using opencv 2, there are others ways
    img_buffer = cv2.imencode('.jpg', img)[1]
    return base64.b64encode(img_buffer).decode('utf-8')
    
