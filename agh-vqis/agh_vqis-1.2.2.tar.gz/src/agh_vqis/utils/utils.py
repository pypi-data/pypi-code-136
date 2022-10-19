import sys
import os
import subprocess
import csv
import shutil

# For content-aware scene detection:
from scenedetect.detectors.content_detector import ContentDetector
from scenedetect.scene_manager import SceneManager
# For caching detection metrics and saving/loading to a stats file
from scenedetect.stats_manager import StatsManager
from scenedetect.video_manager import VideoManager


#

def get_resolution(video_path):
    """
    Gets the video resolution of a video using ffprobe
    :param video_path: full path to the analysed video
    :return: Tuple (width,height)
    """
    if not os.path.exists(video_path):
        sys.stderr.write("ERROR: filename %r was not found!" % (video_path,))
        return -1
    out = subprocess.check_output(
        ["ffprobe", video_path, "-v", "error", "-show_entries", "stream=width,height", "-of",  "default=noprint_wrappers=1"])
    width = out.decode("utf-8").split('\n')[0].split('=')[1].split('\r')[0]
    height = out.decode("utf-8").split('\n')[1].split('=')[1].split('\r')[0]
    #print(width)
    #print(height)
    resolution = (width, height)
    return resolution

def get_FPS(video_path):
    """
    Calculates the FPS of the input video based on ffprobe.
    Based on: https://askubuntu.com/questions/110264/how-to-find-frames-per-second-of-any-video-file
    :param video_path: full path to the analysed video
    :return: FPS value or -1 if not detected or file not found
    """

    if not os.path.exists(video_path):
        sys.stderr.write("ERROR: filename %r was not found!" % (video_path,))
        return -1
    out = subprocess.check_output(
        ["ffprobe", video_path, "-v", "0", "-select_streams", "v", "-print_format", "flat", "-show_entries",
         "stream=r_frame_rate"])
    rate = out.decode("utf-8").split('"')[1].split('/')
    if len(rate) == 1:
        return float(rate[0])
    if len(rate) == 2:
        return float(rate[0]) / float(rate[1])
    return -1


def my_system_call(call):
    """
    Executes the given string system call using subprocess package. Returns any errors risen by subprocess
    to the console.
    :param call: String system call
    """
    try:
        subprocess.check_call(call, shell=True)
    except subprocess.CalledProcessError as e:
        print("ERROR: " + str(e.output))


def find_scenes(video_path, threshold=30.0):
    """
    Detects scenes in the provided video file.
    :param video_path: full path to the analysed video
    :param threshold: threshold used by the pyscenedetect. Default 30.
    :return: List of detected scenes in the video
    """
    # type: (str) -> List[Tuple[FrameTimecode, FrameTimecode]]
    video_manager = VideoManager([video_path])
    stats_manager = StatsManager()
    # Construct our SceneManager and pass it our StatsManager.
    scene_manager = SceneManager(stats_manager)

    # Add ContentDetector algorithm (each detector's constructor
    # takes detector options, e.g. threshold).
    scene_manager.add_detector(ContentDetector(threshold=threshold))

    # We save our stats file to {VIDEO_PATH}.stats.csv.
    # stats_file_path = '%s.stats.csv' % video_path

    scene_list = []

    try:
        # If stats file exists, load it.
        # if os.path.exists(stats_file_path):
        # Read stats from CSV file opened in read mode:
        # with open(stats_file_path, 'r') as stats_file:
        # stats_manager.load_from_csv(stats_file)

        # Set downscale factor to improve processing speed.
        video_manager.set_downscale_factor()

        # Start video_manager.
        video_manager.start()

        # Perform scene detection on video_manager.
        scene_manager.detect_scenes(frame_source=video_manager)

        # Obtain list of detected scenes.
        scene_list = scene_manager.get_scene_list()
        # Each scene is a tuple of (start, end) FrameTimecodes.

        # We only write to the stats file if a save is required:
        # if stats_manager.is_save_required():
        # base_timecode = video_manager.get_base_timecode()
        # with open(stats_file_path, 'w') as stats_file:
        # stats_manager.save_to_csv(stats_file, base_timecode)

    finally:
        video_manager.release()

    return scene_list


def get_shots_data(scene_list_out, df):
    """
    This is the main function responsible for extraction of data related to TA and SA per shot.
    :param scene_list_out: List of scenes
    :param df: dataframe with vqis
    :return: A dictionary containing: (1) the shot number (2) frames range in form of a dictionary containing the first
            and the last shot of the frame, (3) Average Temporal Activity for the shot, (4) average spatial activity
            for the shot.
    """
    shot_number = 0
    shots_data = []

    for i, scene in enumerate(scene_list_out):

        ta_sum = 0
        sa_sum = 0
        first_frame_number = scene[0].get_frames() + 1,
        last_frame_number = scene[1].get_frames()

        first_frame_number = int(first_frame_number[0])

        shot_frames_number = last_frame_number - first_frame_number

        # print("TEST: ", last_frame_number)
        # print(
        #    'Scene %2d: Start Frame %d, End Frame %d' % (
        #        i + 1,
        #        scene[0].get_frames() + 1,
        #        scene[1].get_frames()))

        line_count = 0

        # TODO: This part can be optimized!!
        # MITSU_csv = open(MITSU_output_path)
        # csv_reader = csv.reader(MITSU_csv, delimiter=delimiter)
        # for row in csv_reader:

        for i in df.index:
            if first_frame_number <= line_count <= last_frame_number:
                # print("test: " + str(int(row[0])) + " SA: " + row[2] + " TA: " + row[7])
                ta_sum += float(df['TA:'][i])
                sa_sum += float(df['SA:'][i])

            line_count += 1

        shot = {
            'shot_number': shot_number,
            'frames_range': "{0}, {1}".format(first_frame_number, last_frame_number),
            'TA': float(ta_sum / shot_frames_number),
            'SA': float(sa_sum / shot_frames_number)
        }
        #print(shot)
        shots_data.append(shot)
        shot_number += 1

        ta_sum = 0
        sa_sum = 0

    return shots_data


def make_dir(dir_name):
    """
    This function creates a directory
    :param dir_name: Name of the directory to create
    :return: Nothing
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def my_file_copy(src, dst):
    """
    This function copies a file from source to destination with exception handling
    :param src: Source file
    :param dst: Destination file
    :return: Nothing
    """
    try:
        shutil.copy(src, dst)
    except shutil.Error as e:
        print('Error: %s' % e)
        print("Src: " + src + "Dst: " + dst)
        exit()
        exit()
    except IOError as e:
        print('Error: %s' % e.strerror)
        print("Src: " + src + "Dst: " + dst)
