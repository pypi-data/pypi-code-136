import cloudscraper, requests, json, time, os

scraper = cloudscraper.create_scraper()



class Towers:
    def __init__(self):
        pass

    def Create(betamount, difficulty, auth):
        if not difficulty in ["easy", "normal", "hard"]:
            raise KeyError("Invalid difficulty provided.")
        response = scraper.post("https://rest-bf.blox.land/games/towers/create",
                                headers={
                                    "x-auth-token": auth
                                },
                                json={
                                    "betAmount": str(betamount),
                                    "difficulty": difficulty
                                }
                                )

        if betamount < 5:
            raise Exception("Bet amount must be greater than 5")

        if response.status_code == 429:
            raise KeyError("Ratelimited: Too many requests")

        if not response.status_code == 200:
            try:
                response.json()
            except:
                raise Exception("Network error.", "error")

            if response.json()["msg"] == "You already have an active towers game!":
                raise Exception("You already have an active towers game. End it then try again.")

            else:
                raise Exception("Insuffecient funds.")

            return False
        return True

    def Choose(choice, auth):
        response = scraper.post("https://rest-bf.blox.land/games/towers/action",
                                headers={
                                    "x-auth-token": auth
                                },
                                json={
                                    "cashout": False,
                                    "tile": choice
                                }
                                )

        if response.status_code == 429:
            raise KeyError("Ratelimited: Too many requests")

        if not response.status_code == 200:
            if response.json()["msg"] == "You do not have an active towers game!":
                raise Exception("There is currently no active towers game")

        return not response.json()["exploded"]

    def Cashout(auth):
        response = scraper.post("https://rest-bf.blox.land/games/towers/action",
                                headers={
                                    "x-auth-token": auth
                                },
                                json={
                                    "cashout": True,

                                }
                                )

        if response.status_code == 429:
            raise KeyError("Ratelimited: Too many requests")

        if not response.status_code == 200:
            if not "msg" in list(response.json()):
                raise KeyError("Invalid authorization provided.")

            elif response.json()["msg"] == "You do not have an active towers game!":
                raise Exception("You do not have an active towers game.")

            elif response.json()["msg"] == "You cannot cash out yet! You must uncover at least one tile!":
                raise Exception("You cannot cash out yet! You must uncover at least one tile!")

            raise Exception("Insuffecient funds")

        return True


class Mines:
    def __init__(self):
        pass

    def Create(betamount, mines, auth):
        response = scraper.post("https://rest-bf.blox.land/games/mines/create",
                                headers={
                                    "x-auth-token": auth
                                },
                                json={
                                    "betAmount": betamount,
                                    "mines": mines
                                }
                                )

        if betamount < 5:
            raise Exception("Bet amount must be greater than 5")

        if response.status_code == 429:
            raise KeyError("Ratelimited: Too many requests")

        if not response.status_code == 200:
            try:
                response.json()
            except:
                raise Exception("Network error.", "error")
            if response.json()["msg"] == "You already have an active mines game!":
                raise Exception("You already have an active mines game. End it then try again.")

    def Choose(choice, auth):
        response = scraper.post("https://rest-bf.blox.land/games/mines/action",
                                headers={
                                    "x-auth-token": auth
                                },
                                json={
                                    "cashout": False,
                                    "mine": choice
                                }
                                )

        if response.status_code == 429:
            raise KeyError("Ratelimited: Too many requests")

        if not response.status_code == 200:
            if response.json()["msg"] == "You do not have an active mines game!":
                raise Exception("There is currently no active mines game")
        return not response.json()["exploded"]

    def Cashout(auth):
        response = scraper.post("https://rest-bf.blox.land/games/mines/action",
                                headers={
                                    "x-auth-token": auth
                                },
                                json={
                                    "cashout": True,

                                }
                                )

        if not response.status_code == 200:
            if not "msg" in list(response.json()):
                raise KeyError("Invalid authorization provided.")

            elif response.json()["msg"] == "You do not have an active mines game!":
                raise Exception("You do not have an active mines game.")

            elif response.json()["msg"] == "You cannot cash out yet! You must uncover at least one tile!":
                raise Exception("You cannot cash out yet! You must uncover at least one tile!")

            return False

        return True


class Authorization:
    def __init__(self):
        pass

    def Generate(cookie):
        request = scraper.post("https://rest-bf.blox.land/user/login", json={
            "affiliateCode": "BFSB",
            "cookie": cookie
        }).json()
        if not "jwt" in list(request):
            raise KeyError("Either cookie is invalid or cookie is ip locked.")

    def validate(auth):
        request = scraper.get("https://rest-bf.blox.land/user", headers={
            "x-auth-token": auth
        }).json()
        if request["success"] == True:
            return True
        return False


class Currency:
    def __init__(self):
        pass

    def Balance(auth):
        request = scraper.get("https://rest-bf.blox.land/user", headers={
            "x-auth-token": auth
        }).json()
        if not "user" in list(request):
            raise KeyError("Invalid authorization provided.")
        return request["user"]["wallet"]

    def Affiliate(auth):
        request = scraper.get("https://rest-bf.blox.land/user/affiliates", headers={
            "x-auth-token": auth
        }).json()
        if not "affiliateMoneyAvailable" in list(request):
            raise KeyError("Invalid authorization provided.")
        return request["affiliateMoneyAvailable"]

class Crash:
    def __init__(self):
        pass

    def predict(self):
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
