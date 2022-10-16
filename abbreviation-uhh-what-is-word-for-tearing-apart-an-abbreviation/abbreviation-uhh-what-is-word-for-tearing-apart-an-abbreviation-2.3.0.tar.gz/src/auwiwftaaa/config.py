import os
from pathlib import Path
from .start import color

__all__ = [
    "message",
    "date_format",
    "categories"
]

message = color.reset + '"' + color.bright_white + "{quote}" + color.reset + '"' + " *-" + color.bright_red + "{author}" + color.reset + ", " + color.bright_yellow + "{date}" + color.reset + "*"
date_format = "%d %b %Y"

history_file_dir = Path.home()
history_file_name = ".auwiwftaaa_history"
history_file_path = os.path.join(history_file_dir, history_file_name)

categories = {
    "random": {
        "a": [
            "ass", "arse", "a",
            "anal", "analling", "aunt",
            "anime", "aelp", "aelpxy",
            "are", "annoying", "apple",
            "away", "ask", "asked",
            "asking", "annoy", "annoyed"
        ],
        "b": [
            "bouncy", "butt", "boyfriend",
            "balls", "balling", "blowjob",
            "breasts", "boobs", "breast",
            "boob", "bust", "busting",
            "boy", "bruh", "bro",
            "brother", "bouncing", "boys",
            "babe", "boo", "bae",
            "bad", "baby", "babies",
            "bitch", "bitching", "bish",
            "boom", "blast", "booming",
            "branch"
        ],
        "c": [
            "crazy", "clitoris", "cum",
            "cumming", "coming", "come",
            "condom", "cunt", "cat",
            "craft", "chick", "chicken",
            "coder", "code", "coding",
            "chips", "chat", "cookie",
            "cookies", "crash", "car"
        ],
        "d": [
            "dick", "dad", "duck",
            "ducking", "dildo", "duccy",
            "ducc", "dumb", "dream",
            "dreaming", "drunk", "drink",
            "drinking", "down", "dipshit",
            "dumbfuck", "dog", "doctor",
            "diesease", "dingus", "die",
            "death", "dying", "do",
            "dark", "ducking", "dance",
            "dancing", "discord", "draw",
            "drawing"
        ],
        "e": [
            "erecting", "erection", "e",
            "ejecting", "eject", "erect",
            "ex", "erect", "eat",
            "eating"
        ],
        "f": [
            "freaking", "fucking", "fancy",
            "fingering", "freak", "fuck",
            "fap", "fapping", "fart",
            "farting", "frick", "fricking",
            "fry", "fried", "finger",
            "fly", "flying"
        ],
        "g": [
            "googly", "go", "gay",
            "gaymer", "gaying", "gamer",
            "gaming", "girl", "girlfriend",
            "girls", "good", "grammar",
            "grandmother", "grandfather", "genius",
            "gorgeus"
        ],
        "h": [
            "haitch", "haitching", "haitchpea",
            "hecking", "horny", "heck",
            "hammer", "hammering", "h",
            "hug", "hack", "hacking",
            "hub", "hugging", "heal",
            "heaven", "high"
        ],
        "i": [
            "impostor", "indian", "internet",
            "image", "inspect", "inspection"
        ],
        "j": [
            "jerk", "jerking", "jeans"
        ],
        "k": [
            "kiss", "kissing", "kissed",
            "keeps", "keep", "king",
            "keeping"
        ],
        "l": [
            "laughing", "laugh", "lesbian",
            "lubricating", "left", "lick",
            "like", "liking", "licking",
            "live","life", "living",
            "loud", "lie", "lied",
            "lying", "light", "love",
            "luck", "lucky", "low"
        ],
        "m": [
            "masturbating", "masturbation", "mom",
            "my", "meow", "minecraft",
            "mine", "moan", "moaning",
            "middle"
        ],
        "n": [
            "nipples", "nigga", "nutty",
            "nutting", "nut", "none",
            "null", "night"
        ],
        "o": [
            "oral", "oralling", "ovary",
            "orgasm", "out", "ovulating",
            "off", "owo", "of"
        ],
        "p": [
            "pea", "pee", "peeing",
            "pp", "penis", "poop",
            "poo", "pooping", "python",
            "porn", "pizza", "pant",
            "pants", "pornhub", "pog",
            "pogger", "poggers", "prank",
            "pussy", "puss", "puff",
            "puffy", "puck", "pranked",
            "pranking", "prak", "programming",
            "program", "progamer", "pro",
            "professional", "programmar",
            "potato"
        ],
        "q": [
            "question", "questioning", "quiet",
            "quest", "queen"
        ],
        "r": [
            "rainbow", "right", "rule34",
            "redacted", "rule", "ruling",
            "roast", "roasted", "roasting"
        ],
        "s": [
            "start", "starting", "sex",
            "sexing", "sperm", "spam",
            "semen", "squirt", "sqd",
            "squirting", "spamming", "squid",
            "shit", "shitting", "shut",
            "shutting", "sister", "step-sis",
            "step-bro", "step-sister", "step-brother",
            "step-mom", "step-mother", "step-dad",
            "step-father", "single", "simple",
            "stroke", "streak", "sing",
            "song", "sang", "sunk",
            "ship", "stop", "sparkler",
            "speak", "speaking", "scream",
            "screaming", "sus", "suspect",
            "sussy"
        ],
        "t": [
            "time", "timing", "tit",
            "tits", "troll", "trolling",
            "tasty", "taste", "tasting",
            "the", "that", "thing",
            "toast", "toasty", "toasting",
            "toasted"
        ],
        "u": [
            "urine", "urinating", "undefined",
            "up", "uwu", "unlucky"
        ],
        "v": [
            "vagina", "vulva", "vibrator",
            "vibrating", "virgin", "video"
        ],
        "w": [
            "wank", "wink", "wanking",
            "winking", "work", "working",
            "wrong", "watch", "watching",
            "waste", "wasting", "what",
            "why", "who", "which"
        ],
        "x": [
            "xonia", "xylophone"
        ],
        "y": [
            "yellow", "you", "your",
            "youtube", "youtuber", "yum",
            "yummy", "yuck", "yucky",
            "yell", "yelling"
        ],
        "z": [
            "zombie", "zombieing", "zombert"
        ]
    },
    "lmao/lmfao": {
        "a": [
            "ass", "ass", "ass",
            "ass", "ass", "ass",
            "ass", "ass", "arse",
            "a", "aunt", "ass",
            "ass", "ass", "ass",
            "ass", "ass", "ass",
            "ass", "ass", "ass",
            "ass", "ass", "ass"
        ],
        "b": [
            "bouncy", "bouncy", "butt",
            "butt", "butt", "balls",
            "boobs", "breasts", "balls",
            "balls", "bouncing", "busting",
            "bro", "boy", "boys"
        ],
        "c": [
            "crazy", "cunt", "cumming",
            "condom", "cum", "cum", "cum"
        ],
        "d": [
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "dad", "ducking", "ducking",
            "ducking", "ducking", "ducking",
            "ducking", "ducking", "ducking",
            "duck", "duck", "duck",
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "dick", "dick", "dick"
        ],
        "e": [
            "e", "e", "erecting",
            "erecting", "erecting", "erecting",
            "erecting", "erecting", "erecting",
            "erection"
        ],
        "f": [
            "fancy", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "freaking", "freaking", "fapping",
            "fapping", "fucking", "fapping",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking"
        ],
        "g": [
            "googly","googly", "gay",
            "gay", "gaming", "girl",
            "girls"
        ],
        "h": [
            "haitch", "h", "haitching",
            "haitchpea", "hecking", "hecking",
            "hecking", "hecking", "hecking",
            "hecking", "hecking", "hecking",
            "hecking", "hecking", "hecking",
            "horny", "horny", "horny",
            "horny", "horny", "horny",
            "hammering"
        ],
        "i": [
            "indian", "impostor", "indian"
        ],
        "j": [
            "jerking", "jeans"
        ],
        "k": [
            "kissing"
        ],
        "l": [
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "licking",
            "licking", "licking", "laughing",
            "laughing", "licking", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "licking", "licking", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing"
        ],
        "m": [
            "my", "my", "my",
            "my", "my", "my",
            "my", "my", "mine",
            "my", "my", "my",
            "my", "my", "my",
            "my", "my", "my"
        ],
        "n": [
            "nigga", "nutting", "nutting",
            "nut"
        ],
        "o": [
            "off", "out", "owo",
            "off", "off", "off",
            "off", "off", "off",
            "off", "off", "off",
            "off", "off", "off",
            "off", "off", "off",
            "off", "off", "off",
            "off", "off", "off",
            "off", "off", "off"
        ],
        "p": [
            "pizza", "pizza", "penis",
            "penis", "penis", "penis",
            "pants", "pants", "pants"
        ],
        "q": [
            "questioning"
        ],
        "r": [
            "rule34", "redacted"
        ],
        "s": [
            "starting", "sex", "squirting",
            "sexing", "squirting", "shitting"
        ],
        "t": [
            "tasty", "taste", "tasting",
            "trolling"
        ],
        "u": [
            "uwu","urinating"
        ],
        "v": [
            "vagina", "vibrating", "vibrating",
            "vibrating", "vibrating", "vibrating",
            "vibrating", "vibrating", "vibrating",
            "vibrating"
        ],
        "w": [
            "wasting", "wanking", "wanking",
            "wanking", "wanking", "wanking",
            "wanking", "wanking"
        ],
        "x": [
            "xonia"
        ],
        "y": [
            "yellow", "you", "you",
            "your", "your", "your",
            "your", "your", "your",
            "your", "your", "your",
            "your", "your", "your"
        ],
        "z": [
            "zombie"
        ]
    },
    "lol": {
        "a": [
            "a", "ass", "ass",
            "ass", "ass", "ass",
            "ass", "ass", "ass",
            "aelp", "aelpxy", "ass",
            "ass", "ass", "ass"
        ],
        "b": [
            "bouncy", "bouncy", "bouncy",
            "bouncy", "bouncy", "bouncy",
            "bouncy", "balls", "bouncy",
            "buttt", "bouncy", "balls",
            "bouncy", "bouncy", "bouncy",
            "balls", "bouncy", "bouncy",
            "bouncy", "bouncy", "balls",
            "bouncy", "bouncy", "balls"
        ],
        "c": [
            "crazy", "crazy", "crazy",
            "crazy", "crazy", "crazy",
            "crazy", "crazy", "crazy",
            "crazy", "crazy", "crazy",
            "crazy", "crazy", "craft",
        ],
        "d": [
            "dick", "dad", "ducc",
            "dick", "dick", "ducc",
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "dumb","dick", "dumb",
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "dick", "dick", "dick",
            "ducc", "dick", "dick",
            "discord"
        ],
        "e": [
            "eating","erecting","erecting",
            "e", "erecting", "erecting",
            "erecting", "erecting", "erecting",
            "erecting", "erecting", "erecting",
            "erecting", "erecting", "erecting",
            "erecting", "erecting", "erecting"
        ],
        "f": [
            "freaking", "fucking", "fancy",
            "fingering", "freak", "fuck",
            "fap", "fapping", "fart",
            "farting", "frick", "fricking",
            "fry", "fried", "finger",
            "fly", "flying",
            
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "fucking", "fucking", "fucking",
            "freaking", "freaking", "freaking",
            "freaking", "freaking", "freaking",
            "freaking", "freaking", "freaking",
            "fucking", "fucking", "fucking",
            "fapping", "fapping", "fapping",
            "fapping", "fapping", "fapping",
            "fapping", "fapping", "fapping"
        ],
        "g": [
            "gorgeus", "gorgeus", "gorgeus",
            "gorgeus", "gorgeus", "gorgeus",
            "gorgeus", "gorgeus", "gorgeus",
            "gaming", "gaming", "girl",
            "googly", "googly", "googly"
        ],
        "h": [
            "haitch", "haitchpea", "haitching",
            "haitch", "haitch", "haitch",
            "haitchpea", "haitchpea", "haitchpea",
            "haitchpea", "hecking", "hacking"
        ],
        "i": [
            "impostor", "indian", "internet"
        ],
        "j": [
            "jerk", "jerking"
        ],
        "k": [
            "kiss", "kissing", "kissed"
        ],
        "l": [
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laugh", "laugh", "laugh",
            "laugh", "laugh", "laugh",
            "laughing", "laughing", "laughing",
            "loud", "loud", "loud",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laugh", "laugh", "laugh",
            "loud", "loud", "loud",
            "loud", "loud", "loud",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "laugh", "laugh", "laugh",
            "loud", "loud", "loud",
            "laughing", "laughing", "laughing",
            "loud", "loud", "loud",
            "laughing", "laughing", "laughing",
            "loud", "loud", "loud",
            "loud", "loud", "loud",
            "laugh", "laugh", "laugh",
            "laughing", "laughing", "laughing",
            "loud", "loud", "loud",
            "laughing", "laughing", "laughing",
            "loud", "loud", "loud",
            "laugh", "laugh", "laugh",
            "loud", "loud", "loud",
            "loud", "loud", "loud",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "loud", "loud", "loud",
            "laugh", "laugh", "laugh",
            "laugh", "laugh", "laugh",
            "laughing", "laughing", "laughing",
            "laughing", "laughing", "laughing",
            "lucky"
        ],
        "m": [
            "masturbating", "masturbating", "masturbating",
            "masturbating", "masturbating", "masturbating",
            "mom", "mom", "my",
            "my", "masturbating", "masturbation",
            "masturbating", "masturbating", "masturbation",
        ],
        "n": [
            "nutting", "nutting", "nutting",
            "nipples", "nigga", "nutty",
            "nutting", "nutting", "nutting",
            "nutting", "nutting", "nutting",
            "nutting", "nut", "night",
            "nutting", "nutting", "nutting",
            "nutting", "nutting", "nutting",
            "nutting", "nutting", "nutting",
            "nutting", "nutting", "nutting",
        ],
        "o": [
            "out", "out", "out",
            "out", "out", "out",
            "owo", "out", "out",
            "out", "out", "out",
            "out", "out", "owo",
            "out", "out", "out",
            "out", "out", "out",
            "out", "out", "out",
            "out", "of", "out",
            "out", "out", "out",
            "out", "out", "off",
        ],
        "p": [
            "peeing", "peeing", "peeing",
            "pea", "pee", "peeing",
            "peeing", "peeing", "peeing",
            "peeing", "peeing", "peeing",
            "pp", "penis", "peeing",
            "peeing", "peeing", "peeing",
            "porn", "peeing", "peeing",
            "peeing", "peeing", "peeing",
            "pea", "peeing", "peeing",
            "peeing", "peeing", "peeing",
            "peeing", "peeing", "peeing",
        ],
        "q": [
            "question", "questioning", "questioning",
            "questioning", "questioning", "questioning",
        ],
        "r": [
            "rainbow", "rule34", "redacted",
            "rule", "ruling", "roasting"
        ],
        "s": [
            "starting", "sex", "squirting",
            "sexing", "squirting", "shitting",
            "sussy", "sus"
        ],
        "t": [
            "time", "timing", "tit",
            "tits", "troll", "trolling",
            "tasty", "taste", "tasting",
            "the", "that", "thing",
            "toast", "toasty", "toasting",
            "toasted"
        ],
        "u": [
            "urine", "urinating", "undefined",
            "up", "uwu", "unlucky"
        ],
        "v": [
            "vagina", "vulva", "vibrator",
            "vibrating", "virgin", "video"
        ],
        "w": [
            "wank", "wink", "wanking",
            "winking", "work", "working",
            "wrong", "watch", "watching",
            "waste", "wasting", "what",
            "why", "who", "which"
        ],
        "x": [
            "xonia", "xylophone"
        ],
        "y": [
            "yellow", "you", "you",
            "your", "your", "your",
            "your", "your", "your",
            "your", "your", "your",
            "your", "your", "your",
            "yelling", "yelling"
        ],
        "z": [
            "zombie", "zombert"
        ]
    }
}