from grequests import get, post, map 
from requests import Session

#requests
class tempMailApi:
    #Accepts a token (The default is a token to create an account)
    def __init__(self, token:str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNTJiODcxZWUwM2UxNDNiZTkxOWE5Zjk0YzU4OWYzMWQiLCJtYWlsYm94IjoidmF5ZWdpdDY3OUBpbmttb3RvLmNvbSIsImlhdCI6MTY2NTc4NzU5NH0.pdKxxL4Z78RjuG5lXjsxKj-6RUJClgP2ceaeOcVeNgg') -> None:
        self.sessionClient = Session()
        self.sessionClient.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
        'Authorization': f'Bearer {token}'
    })

    #creates a new mailbox and gets a dict: token, mailbox (it is not necessary to transfer the token)
    def createNewMailBox(self) -> dict:
        return self.sessionClient.post('https://web2.temp-mail.org/mailbox').json()

    #gets the name of the mailbox (token required)
    def getMailBox(self) -> str:
        return self.sessionClient.get('https://web2.temp-mail.org/mailbox').json()['mailbox']

    #gets a list of messages [0 element is the first message] (token required)
    def getMailsList(self) -> list:
        return self.sessionClient.get('https://web2.temp-mail.org/messages').json()['messages']
    
    #get message information by id (it is not necessary to transfer the token)
    def getMailById(self, id:str) -> dict:
        return self.sessionClient.get(f'https://web2.temp-mail.org/messages/{id}').json()

#grequests
class tempMailApiMultipleData:
    #Accepts a tokenList (The default is a tokenList to create an account)
    def __init__(self, tokenList:list = ['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNTJiODcxZWUwM2UxNDNiZTkxOWE5Zjk0YzU4OWYzMWQiLCJtYWlsYm94IjoidmF5ZWdpdDY3OUBpbmttb3RvLmNvbSIsImlhdCI6MTY2NTc4NzU5NH0.pdKxxL4Z78RjuG5lXjsxKj-6RUJClgP2ceaeOcVeNgg']) -> None:
        self.headers = [{
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
        'Authorization': f'Bearer {token}'
    } for token in tokenList]

    #creates a new mailboxes and gets a dict: token, mailbox [Max qty =500!] (it is not necessary to transfer the token)
    def createNewMailBoxesMultipleData(self, qty:int) -> list:
        if qty > 500:
            return [response.json() for response in map((post(url, headers=self.headers[0]) for url in ['https://web2.temp-mail.org/mailbox' for x in range(500)]))]
            
        return [response.json() for response in map((post(url, headers=self.headers[0]) for url in ['https://web2.temp-mail.org/mailbox' for x in range(qty)]))]

    #gets the name of the mailboxes (token required)
    def getMailBoxesMultipleData(self) -> list:
        return [response.json()['mailbox'] for response in map((get('https://web2.temp-mail.org/mailbox', headers=header) for header in self.headers))]

    #gets a dict: mailbox, messages [0 element is the first message] (token required)
    def getMailsListMultipleData(self) -> list:
        return [response.json() for response in map((get('https://web2.temp-mail.org/messages', headers=header) for header in self.headers))]
    
    #gets a dict: _id, receivedAt, user, mailbox, from, subject, bodyPreview, bodyHtml, attachmentsCount, attachments, createdAt (it is not necessary to transfer the token)
    def getMailsByIdMultipleData(self, idList:list) -> list:
        return [response.json() for response in map((get(f'https://web2.temp-mail.org/messages/{id}', headers=self.headers[0]) for id in idList))]

