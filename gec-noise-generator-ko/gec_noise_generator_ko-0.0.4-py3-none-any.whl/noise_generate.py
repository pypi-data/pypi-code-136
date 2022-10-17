from error_classification import ErrorClassification
import time
from tokenizer import Tokenizer
from datasets import error_label
import os
import json


class NoiseGenerate:

    def __init__(self, data_directory, error_type):
        self.data_directory = data_directory
        self.error_type = error_type

    def noise_generate(data_directory, error_type):
        sentence = open(data_directory, 'rt', encoding='UTF-8').readlines()
        save_path = "/".join(os.path.dirname(__file__).split("/")
                             [:-1]) + "/results/"
        id = data_directory.split("/")[-1]
        with open(save_path + id + "_error.json", 'w', encoding="UTF-8") as error:
            with open(save_path + id + "_noised.json", 'w', encoding="UTF-8") as noised:
                for i in range(len(sentence)):
                    try:
                        result = []
                        each_result = {}
                        each_result["id"] = id + "." + str(i)
                        tokens = Tokenizer.tokenize(sentence[i])
                        each_result["source"] = []
                        each_result["target"] = sentence[i].strip()
                        each_result["token"] = []
                        each_result["GEC"] = []
                        for e_type in error_type:
                            error_gen = getattr(ErrorClassification, e_type)
                            noised_sentence, target_token, converted_token = error_gen(
                                tokens)
                            tokens = noised_sentence
                            if not converted_token:
                                continue
                            for count in range(len(converted_token)):
                                gec = {}
                                if e_type == "grapheme_to_phonem_error":
                                    gec["id"] = noised_sentence.index(
                                        converted_token[count][0])
                                    converted = Tokenizer.converge_token(
                                        converted_token[count])
                                    target = Tokenizer.converge_token(target_token[count])
                                    gec["source"] = converted.strip()
                                    gec["target"] = target.strip()
                                    gec["label"] = error_label[e_type]
                                    gec["begin"] = target_token[count][0][2]
                                    gec["end"] = target_token[count][-1][3]
                                else:
                                    gec["id"] = noised_sentence.index(
                                        converted_token[count])
                                    gec["source"] = converted_token[count][0].strip()
                                    gec["target"] = target_token[count][0].strip()
                                    gec["label"] = error_label[e_type]
                                    gec["begin"] = target_token[count][2]
                                    gec["end"] = target_token[count][3]
                                each_result["GEC"].append(gec)
                        each_result["source"] = Tokenizer.converge_token(
                            noised_sentence).strip()
                        for tok in range(len(noised_sentence)):
                            token_dic = {}
                            token_dic["id"] = tok
                            token_dic["source"] = noised_sentence[tok][0].strip()
                            token_dic["begin"] = noised_sentence[tok][2]
                            token_dic["end"] = noised_sentence[tok][3]
                            each_result["token"].append(token_dic)
                        result.append(each_result)
                        if each_result["source"] != each_result["target"]:                        
                            json.dump(result, noised, ensure_ascii=False, indent=4)
                    except:
                        error.write("Error at sentence number : {} \n Error Sentence is : {}".format(
                            i, sentence[i]))
                noised.close
                error.close
