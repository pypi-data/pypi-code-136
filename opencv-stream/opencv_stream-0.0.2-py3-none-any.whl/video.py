import cv2


class CV_Video:

    def __init__(self, cap, window_name="video", waitkey=1) -> None:
        
      self.__cap = cap
      self.__tasks = []
      self.window_name=window_name
      self.waitkey = waitkey
      
    def from_webcam():
       
       return CV_Video(
           cap = cv2.VideoCapture(0) 
       )
    
    def on_next_frame(self, func):
       self.__tasks.append(func)  
        
    def from_video_input(path):
        
        return CV_Video(
            cap=cv2.VideoCapture(path)
        ) 
    
    def __step(self, frame):
        
        for fn in self.__tasks: 
            
            fn(frame)
            
            cv2.imshow(self.window_name, frame)
            cv2.waitKey(self.waitkey)
        
    
    def start(self):
        
        while True:
            
            ret, frame = self.__cap.read()
            
            if not ret: return
            self.__step(frame)    
        
    
    