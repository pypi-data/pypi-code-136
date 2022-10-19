import streamlit.components.v1 as components
from PIL import Image
import base64
import io
import uuid

__version__ = "1.0"

TEMP_DIR = "../temp"


def pillow_to_base64(image: Image.Image):
    in_mem_file = io.BytesIO()
    image.save(in_mem_file, format="JPEG", subsampling=0, quality=100)
    img_bytes = in_mem_file.getvalue()  # bytes
    image_str = base64.b64encode(img_bytes).decode("utf-8")
    base64_src = f"data:image/jpg;base64,{image_str}"
    return base64_src


def local_file_to_base64(image_path: str):
    file_ = open(image_path, "rb")
    img_bytes = file_.read()
    image_str = base64.b64encode(img_bytes).decode("utf-8")
    file_.close()
    base64_src = f"data:image/jpg;base64,{image_str}"
    return base64_src


def pillow_local_file_to_base64(image: Image.Image):
    # pillow to local file
    img_path = TEMP_DIR + "/" + str(uuid.uuid4()) + ".jpg"
    image.save(img_path, subsampling=0, quality=100)
    # local file base64 str
    base64_src = local_file_to_base64(img_path)
    return base64_src


def video_compare(
    vid1: str,
    vid2: str,
    label1: str = "1",
    label2: str = "2",
    width: int = 700,
    show_labels: bool = True,
    starting_position: int = 50,
    make_responsive: bool = True,
    in_memory=False,
):
    """Create a new juxtapose component.
    Parameters
    ----------
    img1: str, PosixPath, PIL.Image or URL
        Input image to compare
    img2: str, PosixPath, PIL.Image or URL
        Input image to compare
    label1: str or None
        Label for image 1
    label2: str or None
        Label for image 2
    width: int or None
        Width of the component in px
    show_labels: bool or None
        Show given labels on images
    starting_position: int or None
        Starting position of the slider as percent (0-100)
    make_responsive: bool or None
        Enable responsive mode
    in_memory: bool or None
        Handle pillow to base64 conversion in memory without saving to local
    Returns
    -------
    static_component: Boolean
        Returns a static component with a timeline
    """
    # prepare images
    # img1_pillow = sahi.utils.cv.read_image_as_pil(img1)
    # img2_pillow = sahi.utils.cv.read_image_as_pil(img2)
    #
    # img_width, img_height = img1_pillow.size
    # h_to_w = img_height / img_width
    # height = (width * h_to_w) * 0.95
    #
    # if in_memory:
    #     # create base64 str from pillow images
    #     img1 = pillow_to_base64(img1_pillow)
    #     img2 = pillow_to_base64(img2_pillow)
    # else:
    #     # clean temp dir
    #     os.makedirs(TEMP_DIR, exist_ok=True)
    #     for file_ in os.listdir(TEMP_DIR):
    #         if file_.endswith(".jpg"):
    #             os.remove(TEMP_DIR + "/" + file_)
    #     # create base64 str from pillow images
    #     img1 = pillow_local_file_to_base64(img1_pillow)
    #     img2 = pillow_local_file_to_base64(img2_pillow)

    # load css + js
    # cdn_path = "https://cdn.knightlab.com/libs/juxtapose/latest"
    # css_block = f'<link rel="stylesheet" href="{cdn_path}/css/juxtapose.css">'
    # js_block = f'<script src="{cdn_path}/js/juxtapose.min.js"></script>'

    with open(vid1, "rb") as videoFile:
        vid1_64 = base64.b64encode(videoFile.read())
    with open(vid2, "rb") as videoFile:
        vid2_64 = base64.b64encode(videoFile.read())

    vid1_64 = 'data:video/mp4;base64,' + str(vid1_64)[2:-1]
    vid2_64 = 'data:video/mp4;base64,' + str(vid2_64)[2:-1]

    js_script = '''function trackLocation(e) {
  var rect = videoContainer.getBoundingClientRect(),
      position = ((e.pageX - rect.left) / videoContainer.offsetWidth)*100;
  if (position <= 100) {
    videoClipper.style.width = position+"%";
    clippedVideo.style.width = ((100/position)*100)+"%";
    clippedVideo.style.zIndex = 3;
	}
}
var videoContainer = document.getElementById("video-compare-container"),
videoClipper = document.getElementById("video-clipper"),
clippedVideo = videoClipper.getElementsByTagName("video")[0];
videoContainer.addEventListener( "mousemove", trackLocation, false);
videoContainer.addEventListener("touchstart",trackLocation,false);
videoContainer.addEventListener("touchmove",trackLocation,false);

let firstVidLoaded = false
let secondVidLoaded = false

function Handler(){

  let vid1 = document.getElementById("vid1");
  let vid2 = document.getElementById("vid2");
  vid1.loop = "true";
  vid1.loop = "true";

  vid1.pause();
  vid1.currentTime = 0;
  vid1.play();
  vid2.pause();
  vid2.currentTime = 0;
  vid2.play();



}
btn.onclick = function (){
  Handler()
};

'''

    css = '''body {
  background: #FFFAFA;
  margin: 2rem;
}
#video-compare-container {
  display: inline-block;
  line-height: 0;
  position: relative;
  width: 100%;
  padding-top: 42.3%;
}
#video-compare-container > video {
  width: 100%;
  position: absolute;
  top: 0; height: 100%;
}
#video-clipper {
  width: 50%; position: absolute;
  top: 0; bottom: 0;
  overflow: hidden;
}
#video-clipper video {
  width: 200%;
  postion: absolute;
  height: 100%;
}'''
    # write html block
    htmlcode = f"""
        <!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>CodePen - HTML5 Video Before-and-After Comparison Slider</title>
  <style>
  {css}
  </style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prefixfree/1.0.7/prefixfree.min.js"></script>

</head>
<body>
<!-- partial:index.partial.html -->
<div id="video-compare-container">
  <video  id="vid1" autoplay="autoplay" loop="true">
    <source src={vid2_64}>
  </video>
 <div id="video-clipper">
    <video  id="vid2" autoplay="autoplay" loop="true">
      <source src={vid1_64}>
    </video>
  </div>
  
	</div>
	<div style="text-align: center">
    <button id="btn" >Play</button>
    </div>
<!-- partial -->
  <script src='//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
  
  <script>
  {js_script}
  </script>
  
  <!--<script  src="script.js"></script> -->

</body>
</html>
        """
    static_component = components.html(htmlcode, height=720, width=1280)

    return static_component, htmlcode
