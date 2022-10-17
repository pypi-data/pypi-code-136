import cloudscraper

scraper = cloudscraper.create_scraper()


def crashpredict():
    def lol():
        r = scraper.get("https://rest-bf.blox.land/games/crash").json()["history"]
        yield [r[0]["crashPoint"], [float(crashpoint["crashPoint"]) for crashpoint in r[-2:]]]

    for game in lol():
        games = game[1]
        lastgame = game[0]
        avg = sum(games) / len(games)
        chance = 1
        for game in games:
            chance = chance = 95 / game
            prediction = (1 / (1 - (chance)) + avg) / 2

            reter = {'chance': int(chance), 'prediction': int(prediction)}
            return reter
