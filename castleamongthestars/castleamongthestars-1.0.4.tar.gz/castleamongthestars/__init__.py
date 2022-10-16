from distutils.util import check_environ
import re
from random import randint

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

class plinko:
    def __init__(self):
        pass

    def auto(auth,bet_amount,risk,rows):
        request = scraper.post("https://rest-bf.blox.land/games/plinko/roll",headers={"x-auth-token": auth},json={"amount": bet_amount,"risk": risk,"rows": rows})
        checker = request['success']
        if checker == True:
            return request
        else:
            errorr = request['error']
            error = {'error': errorr, 'status': False}
            return error

class Minese:
    def __init__(self):
        pass

    def Predict(self):
        mine1, mine2, mine3, mine4, mine5, mine6, mine7, mine8, mine9, mine10, mine11, mine12, mine13, mine14, mine15, mine16, mine17, mine18, mine19, mine20, mine21, mine22, mine23, mine24, mine25 = '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌', '❌'
        a = randint(1, 25)
        b = randint(1, 25)
        c = randint(1, 25)
        if a == 1:
            mine1 = "🟩"
        if a == 2:
            mine2 = "🟩"
        if a == 3:
            mine3 = "🟩"
        if a == 4:
            mine4 = "🟩"
        if a == 5:
            mine5 = "🟩"
        if a == 6:
            mine6 = "🟩"
        if a == 7:
            mine7 = "🟩"
        if a == 8:
            mine8 = "🟩"
        if a == 9:
            mine9 = "🟩"
        if a == 10:
            mine10 = "🟩"
        if a == 11:
            mine11 = "🟩"
        if a == 12:
            mine12 = "🟩"
        if a == 13:
            mine13 = "🟩"
        if a == 14:
            mine14 = "🟩"
        if a == 15:
            mine15 = "🟩"
        if a == 16:
            mine16 = "🟩"
        if a == 17:
            mine17 = "🟩"
        if a == 18:
            mine18 = "🟩"
        if a == 19:
            mine19 = "🟩"
        if a == 20:
            mine20 = "🟩"
        if a == 21:
            mine21 = "🟩"
        if a == 12:
            mine22 = "🟩"
        if a == 23:
            mine23 = "🟩"
        if a == 24:
            mine21 = "🟩"
        if a == 25:
            mine25 = "🟩"

        if b == 1:
            mine1 = "🟩"
        if b == 2:
            mine2 = "🟩"
        if b == 3:
            mine3 = "🟩"
        if b == 4:
            mine4 = "🟩"
        if b == 5:
            mine5 = "🟩"
        if b == 6:
            mine6 = "🟩"
        if b == 7:
            mine7 = "🟩"
        if b == 8:
            mine8 = "🟩"
        if b == 9:
            mine9 = "🟩"
        if b == 10:
            mine10 = "🟩"
        if b == 11:
            mine11 = "🟩"
        if b == 12:
            mine12 = "🟩"
        if b == 13:
            mine13 = "🟩"
        if b == 14:
            mine14 = "🟩"
        if b == 15:
            mine15 = "🟩"
        if b == 16:
            mine16 = "🟩"
        if b == 17:
            mine17 = "🟩"
        if b == 18:
            mine18 = "🟩"
        if b == 19:
            mine19 = "🟩"
        if b == 20:
            mine20 = "🟩"
        if b == 21:
            mine21 = "🟩"
        if b == 12:
            mine22 = "🟩"
        if b == 23:
            mine23 = "🟩"
        if b == 24:
            mine21 = "🟩"
        if b == 25:
            mine25 = "🟩"

        if c == 1:
            mine1 = "🟩"
        if c == 2:
            mine2 = "🟩"
        if c == 3:
            mine3 = "🟩"
        if c == 4:
            mine4 = "🟩"
        if c == 5:
            mine5 = "🟩"
        if c == 6:
            mine6 = "🟩"
        if c == 7:
            mine7 = "🟩"
        if c == 8:
            mine8 = "🟩"
        if c == 9:
            mine9 = "🟩"
        if c == 10:
            mine10 = "🟩"
        if c == 11:
            mine11 = "🟩"
        if c == 12:
            mine12 = "🟩"
        if c == 13:
            mine13 = "🟩"
        if c == 14:
            mine14 = "🟩"
        if c == 15:
            mine15 = "🟩"
        if c == 16:
            mine16 = "🟩"
        if c == 17:
            mine17 = "🟩"
        if c == 18:
            mine18 = "🟩"
        if c == 19:
            mine19 = "🟩"
        if c == 20:
            mine20 = "🟩"
        if c == 21:
            mine21 = "🟩"
        if c == 12:
            mine22 = "🟩"
        if c == 23:
            mine23 = "🟩"
        if c == 24:
            mine21 = "🟩"
        if c == 25:
            mine25 = "🟩"

        reter = {"mine1": mine1, "mine2": mine2 , "mine3": mine3 , "mine4": mine4, "mine5": mine5 , "mine6": mine6 , "mine7": mine7, "mine8": mine8 , "mine9": mine9 , "mine10": mine10, "mine11": mine11 , "mine12": mine12 , "mine13": mine13, "mine14": mine14 , "mine15": mine15 , "mine16": mine16 , "mine17": mine17 , "mine18": mine18 , "mine19": mine19, "mine20": mine20 , "mine21": mine21 , "mine22": mine22, "mine23": mine23 , "mine24": mine24 , "mine25": mine25}
        return reter

