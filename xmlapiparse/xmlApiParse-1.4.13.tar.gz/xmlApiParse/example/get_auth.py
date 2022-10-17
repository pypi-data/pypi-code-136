import os


print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
count = 5

from xmlApiParse.parser_xml import RKXMLRequest
#  xmlApiParse.parser_json import RKXMLRequest
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('RKEEPER_HOST')
user_name = os.getenv('RKEEPER_USERNAME')
password = os.getenv('RKEEPER_PASSWORD')

try:
    current_request = RKXMLRequest(host=host, user_name=user_name, password=password)
    print(f'Connected: {current_request.check_connection()}')
except Exception as error:
    print(f"Connection error - {error}")
