from gensim.models.keyedvectors import KeyedVectors
import os
import fasttext
import csv
import time

current_file = os.path.dirname(__file__)
kor_model = KeyedVectors.load_word2vec_format(
    current_file + '/resources/wiki.ko.vec', limit=50000)

consonant_data = ["ㄱ", "ㄴ", "ㄷ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ",
                  "ㅍ", "ㅎ", "ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ"]
trailing_consonant_data = ["ㄲ", "ㄳ", "ㄵ", "ㄶ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅄ",
                           "ㅆ", "ㄱ", "ㄴ", "ㄷ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
vowel_data = ["ㅏ", "ㅑ", "ㅓ", "ㅕ", "ㅗ", "ㅛ", "ㅜ", "ㅠ", "ㅡ", "ㅣ", "ㅐ",
              "ㅒ", "ㅔ", "ㅖ", "ㅘ", "ㅙ", "ㅚ", "ㅝ", "ㅞ", "ㅟ", "ㅢ"]
josa_keys = ["JKC", "JKG", "JKO", "JKB", "JKV", "JKQ", "JC", "JKS", "JX"]
punctuation_type = ["SF", "SP", "SS"]
punctuation = {"SF": ["!", "?", "."], "SC": [",", "·", ":", "/", "\"", "\'"]}
# "SS": ["―","(", ")", "{", "}", "[", "]", "<", ">", "≪", "≫", "『" , "』", "「", "」"],
# "SE": ["..."],
# "SO": ["-"]}
phonetic_last = {"율": "률", "양": "량", "률": "율", "량": "양"}
duen_sori_list = {"ㄲ": "ㄱ", "ㄸ": "ㄷ", "ㅃ": "ㅂ", "ㅆ": "ㅅ", "ㅉ": "ㅈ"}
error_label = {"spacing_error": "SP", "punctuation_error": "PU", "phonetic_first_error": "PF",
               "phonetic_last_error": "PL",
               "remove_josa_error": "RJ", "addition_error": "AD", "separation_error": "SE",
               "typing_language_error": "TL", "grapheme_to_phonem_error": "G2P",
               "postposition_diff_josa_error": "PPD", "postposition_same_josa_error": "PPS", "busa_error": "BS",
               "middle_shiot_error": "MS", "overlapping_sound_error": "OS", "final_suffix_error": "FS",
               "mag_error": "MAG", "maj_error": "MAJ", "polite_speech_error": "PS"}


def read_data(file_name):
    file = open(file_name, 'rt', encoding='UTF-8-sig')
    data = csv.reader(file)
    one_data = []
    two_data = []
    for line in data:
        one_data.append(line[0])
        two_data.append(line[1])
    file.close
    return one_data, two_data


def read_single_data(file_name):
    file = open(file_name, 'rt', encoding="UTF-8-sig")
    data = csv.reader(file)
    one_data = []
    for line in data:
        one_data.append(line[0])
    file.close
    return one_data


def josa():
    josa_data_directory = current_file + "/resources/josa_data.csv"
    josa_text, josa_sort = read_data(josa_data_directory)
    josa_dic = {}
    for josa_type in josa_keys:
        josa_list = []
        for num in range(len(josa_text)):
            if josa_type == josa_sort[num]:
                josa_list.append(josa_text[num])
        josa_dic[josa_type] = josa_list
    return josa_dic


def phonetic_data():
    phonetic_data_directory = current_file + "/resources/phonetic_data.csv"
    phonetic_data = read_data(phonetic_data_directory)
    correct_phonetic = phonetic_data[1]
    error_phonetic = phonetic_data[0]
    return correct_phonetic, error_phonetic


def ef_data():
    ef_data_directory = current_file + "/resources/ef_data.csv"
    ef_list = read_single_data(ef_data_directory)
    return ef_list


def mag_data():
    mag_data_directory = current_file + "/resources/mag_data.csv"
    mag_list = read_single_data(mag_data_directory)
    return mag_list


def maj_data():
    maj_data_directory = current_file + "/resources/maj_data.csv"
    maj_list = read_single_data(maj_data_directory)
    return maj_list
