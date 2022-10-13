import sys
import traceback
import requests


def url_file(redgifs_url, filename):
    """
    It takes a RedGifs URL and a filename, and downloads the video to the filename
    
    :param redgifs_url: The URL of the RedGifs video you want to download
    :param filename: The name of the file to save the video as
    :return: The URL of the HD video.
    """
    sys.stdout.reconfigure(encoding='utf-8')
    API_URL_REDGIFS = 'https://api.redgifs.com/v1/gifs/'
    try:
        print("redgifs_url = {}".format(redgifs_url))

        #Get RedGifs video ID
        redgifs_ID = redgifs_url.split('/watch/', 1)
        redgifs_ID = redgifs_ID[1]
        print("redgifs_ID = {}".format(redgifs_ID))
        
        sess = requests.Session()
        
        request = sess.get(API_URL_REDGIFS + redgifs_ID)
        print(request)
        
        if request is None:
            return
        else:
            rawData = request.json()
            #Get HD video url
            try:
                hd_video_url = rawData['gif']['urls']['hd']
                print("URL = {}".format(hd_video_url))
                
                with sess.get(hd_video_url, stream=True) as r:
                    with open(filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192): 
                            f.write(chunk)

                return hd_video_url
            except:
                # gfyItem
                hd_video_url = rawData['gfyItem']['content_urls']['mp4']['url']
                print("URL = {}".format(hd_video_url))
                
                with sess.get(hd_video_url, stream=True) as r:
                    with open(filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192): 
                            f.write(chunk)

                return hd_video_url
    except Exception:
        traceback.print_exc()
        return

test = url_file('https://redgifs.com/watch/blondnauticalxoni', 'a.mp4')