import json
import subprocess

from cachetools.func import ttl_cache
import ffmpeg
import jmespath


FPS_PATH = jmespath.compile("streams[?codec_type=='video'].r_frame_rate")
FRC_PATH = jmespath.compile("streams[?codec_type=='video'].nb_read_frames")


def h264_to_mp4(input_name, output_name, frame_rate=10):
    (
        ffmpeg
        .input(input_name, format="h264", r=str(frame_rate))
        .output(output_name, **{"format": "mp4", "c:v": "copy", "r": str(frame_rate)})
        .run(quiet=False)
    )


@ttl_cache(ttl=60 * 60 * 4)
def get_video_file_details(path):
    ffprobe_out = subprocess.run([
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration:stream=nb_read_frames,r_frame_rate,codec_type",
        "-count_frames",
        "-of",
        "json=compact=1",
        path,
    ], capture_output=True, check=True)
    probe_data = json.loads(ffprobe_out.stdout)
    fps = eval(FPS_PATH.search(probe_data)[0])  # pylint: disable=W0123
    frame_count = int(FRC_PATH.search(probe_data)[0])
    return {
        "fps": fps,
        "frame_count": frame_count,
        "duration":frame_count / fps
    }
