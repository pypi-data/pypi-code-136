# See if we can find the mismatch causing the error and fix it in normalise
from .validate import Validate
from difflib import SequenceMatcher
from collections import namedtuple

class Diagnose:
    def __init__(self, appData = None, inputData = None):
        self.appData = appData
        self.inputData = inputData

    def fixMismatch(self, strictness = 0.8):
        keys = Validate.matchKeys(self)
        if len(keys.missingKeys) < 1:
            return print("No missing keys")

        suggestions = []
        for i, missingKey in enumerate(keys.missingKeys):
            for additionalKey in keys.additionalKeys:
                similarity = SequenceMatcher(None, missingKey, additionalKey)
                if similarity.ratio() > strictness:
                    values = namedtuple('keys', 'missingKey additionalKey')
                    suggestions.append(values(missingKey, additionalKey))
                    keys.missingKeys.pop(i)
        
        print("\nWe did not find:\n" + str(keys.missingKeys) + "\n")

        if len(suggestions) < 1:
            print("No matches, try lowering strictness")
            return self.inputData

        for i, suggestion in enumerate(suggestions):
            print("Suggestion {}: missing '{}' might be additional: '{}'".format(i + 1, suggestion.missingKey, suggestion.additionalKey))

        suggestionsToFix = list(map(int, input("Which suggestion(s) do you want to fix? (example: 1 2 3): ").split()))
        for i in suggestionsToFix:
            self.inputData = self.inputData.rename(columns={suggestions[i - 1].additionalKey: suggestions[i - 1].missingKey})
        
        return self.inputData
