import os
import subprocess

from deepgram import Deepgram

from hautils.logger import logger

DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')
YOUR_API_URL = 'https://api.deepgram.com/v1'


def video_to_audio(file_name):
    """
    The video_to_audio function converts a video file to an audio file.
    The function takes two arguments: the name of the video file and the name of
    the audio file that will be created. The function returns a string containing
    the name of the new audio file.

    :param file_name: Specify the name of the video file that is being converted to audio
    :return: The name of the audio file
    :doc-author: Trelent
    """
    audio_file = "%s.wav" % (file_name,)
    command = 'ffmpeg -y -i %s -ab 160k -ar 44100 -vn %s' % (file_name, audio_file,)
    subprocess.call(command, shell=True)
    return audio_file


async def extract_transcript(file_name):
    """
    The extract_transcript function takes a file name as input and returns the transcript of that audio file.
    The function uses Deepgram's API to extract the transcript from an audio file.


    :param file_name: Pass the file name of the audio file to be transcribed
    :return: A string containing the transcript of the audio file
    :doc-author: Trelent
    """
    logger.info("config %s - %s" % (DEEPGRAM_API_KEY, YOUR_API_URL))
    logger.info("calling extract transcript on %s" % (file_name,))
    dg_client = Deepgram({'api_key': DEEPGRAM_API_KEY, 'api_url': YOUR_API_URL})
    source = {'buffer': open(file_name, 'rb').read(), 'mimetype': 'audio/wav'}
    response = await dg_client.transcription.prerecorded(source, {'punctuate': False, })
    logger.debug(response)
    return response['results']['channels'][0]['alternatives'][0]['transcript']
