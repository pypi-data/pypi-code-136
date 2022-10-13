import os
# import language_tool_python


# class ErrorParser:
#     def __init__(self, language):
#         self.parser = language_tool_python.LanguageTool(language)

#     def parse_errors(self, text):
#         return self.parser.check(text)

#     def show_errors(self, text):
#         obj = self.parse_errors(text)
#         self.analyze_obj(obj)

#     def analyze_obj(self, obj):
#         if obj:
#             for error in obj:
#                 context = error.context[error.offsetInContext:(
#                     error.offsetInContext+error.errorLength)]
#                 if len(error.replacements) > 0:
#                     replacement = error.replacements[0]
#                 else:
#                     replacement = "no suggestion"
#                 rule_id = error.ruleId
#                 sentence = error.sentence
#                 category = error.category
#                 print(f'category: {category}, {rule_id}')
#                 # print(f"erroneous part: {context}")
#                 print(f'error: {error}')
#                 # print(f'sentence: {sentence}\n')
#                 # print(f"suggestion: {replacement}")
#                 # print(f"message: {message}")
#         else:
#             print("No error detected.")


# def log_errors(path, obj, fn, total_words):
#     # output = defaultdict(list)
#     os.mkdir(path+"error_stat/")
#     os.mkdir(path+"error_example/")
#     output_file = path+"error_stat/"+fn
#     error_word_ratio = len(obj)/total_words
#     with open(output_file, 'a+') as f:
#         with open(path+"error_example/"+fn, "a+") as g:
#             for error in obj:
#                 context = error.context[error.offsetInContext:(
#                     error.offsetInContext+error.errorLength)]
#                 if len(error.replacements) > 0:
#                     replacement = error.replacements[0]
#                 else:
#                     replacement = "no suggestion"
#                 sentence = error.sentence
#                 category = error.category
#                 message = error.message
#                 # write the error example
#                 print(f'{category}', file=g)
#                 print(f'{error}', file=g)
#                 print(f'{sentence}\n', file=g)
#                 print(f"{fn}", file=f, end="")
#                 print(f"\t{len(obj)}", file=f, end="")
#                 print(f"\t{total_words}", file=f, end="")
#                 print(f"\t{error_word_ratio}", file=f, end="")
#                 print(f"\t{context}", file=f, end="")
#                 print(f"\t{replacement}", file=f, end="")
#                 print(f"\t{sentence}", file=f, end="")
#                 print(f"\t{category}", file=f, end="")
#                 print(f"\t{message}", file=f)


# if __name__ == "__main__":
#     text_tense = "Hier soir je vois une voiture rose dans la rue."
#     # errors = parse_errors(parser, text_tense)
#     # print(errors)
#     # show_errors(errors)
