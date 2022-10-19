import requests

from assembly_ai.walkthroughs import (submit_url_for_transcription, 
                                      get_status_of_transcription, 
                                      get_transcription)

api_key = None
audio_url = None

endpoint = "https://api.assemblyai.com/v2/transcript"
