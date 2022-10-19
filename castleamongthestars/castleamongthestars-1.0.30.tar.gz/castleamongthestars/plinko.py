import cloudscraper

scraper = cloudscraper.create_scraper()

def autoplinko(auth, bet_amount, risk, rows):
    request = scraper.post("https://rest-bf.blox.land/games/plinko/roll", headers={"x-auth-token": auth},
                           json={"amount": bet_amount, "risk": risk, "rows": rows})
    checker = request['success']
    if checker == True:
        return request
    else:
        errorr = request['error']
        error = {'error': errorr, 'status': False}
        return error