from .preprocessing import video_preprocess
def process(video_path, HR_FPS=10, DN_SAMPLE=1):
    return video_preprocess(video_path, HR_FPS, DN_SAMPLE)
