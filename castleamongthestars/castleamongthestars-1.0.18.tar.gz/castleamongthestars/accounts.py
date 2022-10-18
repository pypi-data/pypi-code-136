
import cloudscraper

scraper = cloudscraper.create_scraper(delay=10, interpreter='nodejs',
  captcha={'provider': 'return_response'})


def account(auth):
    acc = scraper.get(f'https://api.bloxflip.com/user', headers={'x-auth-token': auth}).json()
    if acc['success'] == True:
        id = acc['robloxId']
        subacc = scraper.get(f'https://api.bloxflip.com/user/lookup/{id}').json()
        accountsuccess = {'success': True, 'acc': acc , 'subacc' : subacc}
        return accountsuccess
    else:
        error = acc['error']
        accountsuccess = {'success': False, 'error': error}