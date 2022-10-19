
import cloudscraper

scraper = cloudscraper.create_scraper(delay=10)


def account(auth):
    acc = scraper.get(f'https://rest-bf.blox.land/user', headers={'x-auth-token': auth}).json()
    if acc['success'] == True:
        user = acc['user']
        id = user['robloxId']
        subacc = scraper.get(f'https://rest-bf.blox.land/user/lookup/{id}').json()
        accountsuccess = {'success': True, 'acc': acc , 'subacc' : subacc}
        return accountsuccess
    else:
        error = acc['error']
        accountsuccess = {'success': False, 'error': error}