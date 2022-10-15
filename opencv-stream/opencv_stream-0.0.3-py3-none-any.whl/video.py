from typing import Callable
import cv2
import numpy as np

class InvalidInputError(Exception): ...

def _assert_is_type(input, expected_type:type):

    if not isinstance(input, expected_type):
        raise InvalidInputError(f"Expected a '{expected_type}', received '{type(input)}'")


class VideoStreamer:
    """
    Use this class the read videos from path or from webcam
    Use the on_next_frame method as a decorator to wrap  

    """

    def __init__(self, cap, window_name="video", waitkey=1) -> None:
        
      self.__cap = cap
      self.__tasks = []
      self.window_name=window_name
      self.waitkey = waitkey
      
    def from_webcam(cam_index:int=0,window_name:str="video", waitkey:int=1):

        _assert_is_type(cam_index, int)
       
        return VideoStreamer(
           cap = cv2.VideoCapture(cam_index),
           window_name=window_name, 
           waitkey=waitkey 
       )
    
    def on_next_frame(self, func:Callable[[np.ndarray]]):
        """
        Use as a decorator to wrap your function\n
        The cam window is drawn automatically after the function has been called.\n
        Example: \n

        stream =  VideoStreamer.from_webcam()
        @stream.on_next_frame
        def func(image):
             ...


        """
        self.__tasks.append(func)  
        
    def from_video_input(path, window_name="video", waitkey=1):

        _assert_is_type(path, str)

        return VideoStreamer(
            cap=cv2.VideoCapture(path),
           window_name=window_name, 
           waitkey=waitkey 
        ) 
    
    def __step(self, frame):
        
        for fn in self.__tasks: 
            
            fn(frame)
            
            cv2.imshow(self.window_name, frame)
            cv2.waitKey(self.waitkey)
        
    
    def start(self):
        """
        Using the method to start loading the next frames
        """
        
        while True:
            
            ret, frame = self.__cap.read()
            
            if not ret: return
            self.__step(frame)    
        
    
    