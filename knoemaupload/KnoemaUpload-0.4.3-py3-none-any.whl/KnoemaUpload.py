import requests
import os, sys
import json
import smtplib

EMAIL_ADDRESS = 'ssubramanian@knoema.com'
EMAIL_PASSWORD = 'mtwnswdyohactvfm'
EMAIL_RECEIVERS = 'third-party-data-etl@knoema.com'

class KnoemaDocumentUploader():
    UPL_URL='https://tmt.knoema.com/document/upload'
    DOCID_URL = 'https://tmt.knoema.com/document/getlink?id='
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    PUBLIC_URL = 'https://tmt.knoema.com/resource/share'
    def __init__(self,filepath,cookies):
        self.filepath= filepath
        self.cookies=cookies
        self.filename=os.path.basename(filepath)
        #print(self.filename)
        
    def FileUpload(self,CLIENT,headers=headers):
        files_ = {'file': (self.filename, open(self.filepath, 'rb'))}
        #try:
        response = requests.post(KnoemaDocumentUploader.UPL_URL, cookies=self.cookies, files=files_)
        print('>>>response status code: ', response.status_code, '\n')
        text_res=response.text
        if (len(text_res)>300 and "errorBeacon" in text_res):
            subject = f'Mckinsey TMT File Upload Failed--Update {CLIENT} Cookies'
            body = f'The upload failed most likely due to stale cookie. Update the cookie for {CLIENT}'
            msg = f'Subject: {subject} \n\n Message: {body}'
            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.sendmail(EMAIL_ADDRESS,EMAIL_RECEIVERS,msg)
            print(">>>> Exiting the routine due to stale cookie")
            sys.exit()

##        except Exception as err:
##            subject = 'Mckinsey File Upload Failed--Update Cookies'
##            body = f'The upload failed most likely due to stale cookie. Update the cookie for {CLIENT}'
##            msg = f'Subject: {subject} \n\n Message: {body}\n Error Message: {err}'
##            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
##                smtp.ehlo()
##                smtp.starttls()
##                smtp.ehlo()
##                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
##                smtp.sendmail(EMAIL_ADDRESS,EMAIL_RECEIVERS,msg)
##            print(">>>> Exiting the routine due to stale cookie")
##            sys.exit()

        json_ = json.loads(response.text)
        
        if 'error' in json_.keys():
            raise Exception(str(json_['error']))
        else:
            pass
            #print('id: ', json_['id'])
            #print('path: ', json_['path'])
            #print('type: ', json_['type'])
        #print('\nFind file path from id')
        
        res = requests.get(KnoemaDocumentUploader.DOCID_URL + json_['id'],  cookies=self.cookies)
        file_url = res.json()
        
        payload = {"IsPublic": "true", "Id": json_['id']}
        r = requests.post(KnoemaDocumentUploader.PUBLIC_URL, cookies=self.cookies, data=json.dumps(payload), headers = {'Content-Type': 'application/json'})

        test_url = 'https://tmt.knoema.com/' + json_['id']
        #print(">>>Test URL for developer to delete test files",test_url)
        download_url = 'https://tmt.knoema.com/'+file_url
        print('>>>Download file url for users :', download_url)

        file = open('Download.txt', 'a')
        file.writelines(download_url + '\n')
        file.close()
        
    
