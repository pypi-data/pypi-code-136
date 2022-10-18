from tokenizer import *
from datasets import *
import os
import json
import time
from g2pk import G2p
from inko import Inko
import random
from hangul_utils import split_syllables, join_jamos
import hangul_jamo
import configparser
import gensim
import fasttext
myInko = Inko()
g2p = G2p()
config = configparser.ConfigParser()
current_file = os.path.dirname(__file__)
config.read(current_file+'/resources/config.ini', encoding='utf-8')
max_error = int(config['system']['max_error'])


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
                    tokens = tokenize(sentence[i])
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
                                converted = converge_token(
                                    converted_token[count])
                                target = converge_token(target_token[count])
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
                    each_result["source"] = converge_token(
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


class ErrorClassification:

    def __init__(self):
        self.token = token

    def spacing_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        error_list_one = ["MM", "ETM", "ETN"]
        error_list_two = ["XSN", "XSV", "XSA"]
        for token_num in range(1, len(token) - 1):
            # 명사, 관형어(관형사, 체언 또는 체언의 곡용형, 용언의 활용형)+명사 , 관형어 의존명사 (보통은 관형어 뒤에는 의존명사나 명사가 나옴)
            # 가장 흔한 오류임으로 먼저 체크
            if token[token_num][1][0] == "N":
                if token[token_num][0][:2] != "##":
                    if token[token_num - 1][1][0] == "N" or token[token_num - 1][1] == [i for i in error_list_one]:
                        target_token.append(list(token[token_num]))
                        token[token_num][0] = "##" + str(token[token_num][0])
                        converted_token.append(token[token_num])
                        convert_count -= 1
            # 다음으로 흔한 오류인 조사 또는 접사를 띄어써서 생기는 오류
            elif token[token_num][1][0] == "J":
                if len(token[token_num][0][2:]) > 1 or token[token_num][1] == [a for a in error_list_two]:
                    target_token.append(list(token[token_num]))
                    token[token_num][0] = str(token[token_num][0][2:])
                    converted_token.append(token[token_num])
                    convert_count -= 1
            elif token[token_num - 1][1] == "XPN" and token[token_num][0][:2] == '##':
                target_token.append(list(token[token_num]))
                token[token_num][0] = str(token[token_num][0][2:])
                converted_token.append(token[token_num])
                convert_count -= 1
            if convert_count == 0:
                break
        # 제일 흔하지 않은 오류인 단어 띄어쓰기
        if not target_token and convert_count != 0:
            while convert_count < 2:
                word = random.choice([a for a in token if len(a[0]) > 2])
                if word[0][:2] == "##":
                    target_token.append(list(word))
                    word[0] = str(word[0][2:])
                    converted_token.append(word)
                    convert_count -= 1

        return token, target_token, converted_token

    # 문장속의 토큰중 품사가 “S-” 로 시작하는 랜덤하게 고른 토큰을 같은 품사표 내에서 랜덤하게 변경한다.
    def punctuation_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        words = [word for word in token if word[1] == "SF" or word[1] == "SC"]
        for word in words:
            if word[1] == "SF":
                target_token.append(list(word))
                word[0] = "##" + str(
                    random.choice([x for x in punctuation.get("SF") if x != target_token[0][2:]]))
                converted_token.append(word)
                convert_count -= 1
            elif word[1] == "SC":
                target_token.append(list(word))
                word[0] = "##" + str(
                    random.choice([x for x in punctuation.get("SC") if x != target_token[0][2:]]))
                converted_token.append(word)
                convert_count -= 1
            if convert_count == 2:
                break
        return token, target_token, converted_token

    # 만들어진 두음법칙 표를 이용하여 문장속 단어들 중 두음법칙표의 맞는 표현과 동일한 글자를 두음법칙 적용 이전의 틀린 형태로 변경한다.
    def phonetic_first_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        correct_phonetic, error_phonetic = phonetic_data()
        for word in token:
            for phonetic in correct_phonetic:
                if phonetic == list(word[0])[0] and len(list(word[0])) >= 2:
                    characters = random.choice(
                        error_phonetic[correct_phonetic.index(phonetic)])
                    target_token.append(list(word))
                    convert = list(word[0])
                    convert[0] = characters
                    word[0] = ''.join(convert)
                    converted_token.append(word)
                    convert_count -= 1
                    if convert_count == 0:
                        break
            if convert_count == 0:
                break
        return token, target_token, converted_token

    # 토큰의 행태소 품사가 "X"로 시작하면 율>률 또는 양>량 식으로 바꿔준다.
    def phonetic_last_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        correct_phonetic, error_phonetic = phonetic_data()
        for word in token:
            for phonetic in phonetic_last:
                if phonetic == list(word[0])[-1] and word[1][0] == "X":
                    characters = phonetic_last[phonetic]
                    target_token.append(list(word))
                    convert = list(word[0])
                    convert[-1] = characters
                    word[0] = ''.join(convert)
                    converted_token.append(word)
                    convert_count -= 1
                    break
            if convert_count == 0:
                break
        return token, target_token, converted_token

    # 문장속 토큰들 중 조사인 토큰들을 제거한다.
    def remove_josa_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            if word[1][0] == "J":
                target_token.append(list(word))
                word[0] = "##"
                word[1] = "None"
                converted_token.append(word)
                convert_count -= 1
            if convert_count == 0:
                break
        return token, target_token, converted_token

    # 랜덤한 자음을 받침이나 어두에 추가한다.
    # 받침도 고쳐보기
    def addition_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            if random.choice([0, 1]) == 1:
                words = word[0]
                result = []
                check = True
                for character in words:
                    if hangul_jamo.is_syllable(character):
                        jamos = list(hangul_jamo.decompose_syllable(character))
                        if jamos[2] == None and check:
                            jamos[2] = random.choice(trailing_consonant_data)
                            character = (hangul_jamo.
                                         compose_jamo_characters(jamos[0], jamos[1], jamos[2]))
                            target_token.append(list(word))
                            check = False
                            convert_count -= 1
                        elif jamos[0] == "ㅇ" and check:
                            jamos[0] = random.choice(consonant_data)
                            character = (hangul_jamo.
                                         compose_jamo_characters(jamos[0], jamos[1], jamos[2]))
                            target_token.append(list(word))
                            check = False
                            convert_count -= 1
                        result.append(character)
                    else:
                        result.append(character)
                if not check:
                    word[0] = "".join(result)
                    converted_token.append(word)
                if convert_count == 0:
                    break
        return token, target_token, converted_token

    # 랜덤하게 문자를 선택해 자음과 모음을 분리한다.
    def separation_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            check = False
            result = []
            characters = word[0]
            for character in characters:
                if not check and hangul_jamo.is_syllable(character) and random.choice([0, 1]) == 1:
                    target_token.append(list(word))
                    character = hangul_jamo.decompose(character)
                    result.append(character)
                    check = True
                else:
                    result.append(character)
            if check:
                word[0] = "".join(result)
                convert_count -= 1
                converted_token.append(word)
            if convert_count == 0:
                break
        return token, target_token, converted_token

    # 랜덤하게 고른 문자를 myInko 를 활용하여 영어 타자로 변경한다
    def typing_language_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            if word[1][0] != "S" and random.choice([0, 1]) == 1:
                target_token.append(list(word))
                word[0] = myInko.ko2en(word[0])
                converted_token.append(word)
                convert_count -= 1
            if convert_count == 0:
                break
        return token, target_token, converted_token

    # 문장의 한 종류의 조사를 다른 종류의 조사로 변경 (글자 수 동일)
    def postposition_diff_josa_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            if word[1][0] == "J":
                target_token.append(list(word))
                josa_type = random.choice(
                    [x for x in josa_keys if x != word[1]])
                word[0], word[1] = "##" + random.choice(
                    [x for x in josa().get(josa_type) if x != word[0][2:] and len(x) == len(word[0][2:])]), josa_type
                converted_token.append(word)
                convert_count -= 1
            if convert_count == 0:
                break
        return token, target_token, converted_token

    # 문장의 한 종류의 조사를 같은 종류의 다른 조사로 변경 (글자 수 동일)
    def postposition_same_josa_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            if word[1][0] == "J":
                target_token.append(list(word))
                word[0] = "##" + random.choice(
                    [x for x in josa().get(word[1]) if x != word[0][2:] and len(x) == len(word[0][2:])])
                convert_count -= 1
                converted_token.append(word)
            if convert_count == 0:
                break
        return token, target_token, converted_token

    # 부사를 추출했을때 (이/히) 라면 그 반대로 변환
    def busa_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            if word[1] == "MAG":
                if word[0][-1] == "이":
                    target_token.append(list(word))
                    characters = list(word[0])
                    characters[-1] = "히"
                    word[0] = ''.join(characters)
                    converted_token.append(word)
                    convert_count -= 1
                elif word[0][-1] == "히":
                    target_token.append(list(word))
                    characters = list(word[0])
                    characters[-1] = "이"
                    word[0] = ''.join(characters)
                    converted_token.append(word)
                    convert_count -= 1
            if convert_count == 0:
                break
        return token, target_token, converted_token

    # 받침의 자음이 ‘ㅅ’일 경우 ‘ㅅ’을 생략 한다.
    def middle_shiot_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            result = []
            check = True
            for character in word[0]:
                if hangul_jamo.is_syllable(character) and len(list(word[0])) >= 2:
                    jamos = list(hangul_jamo.decompose_syllable(character))
                    if jamos[2] == "ㅅ":
                        jamos[2] = None
                        target_token.append(list(word))
                        character = (hangul_jamo.compose_jamo_characters(
                            jamos[0], jamos[1], jamos[2]))
                        result.append(character)
                        check = False
                    else:
                        result.append(character)
                else:
                    result.append(character)
            if not check:
                word[0] = "".join(result)
                converted_token.append(word)
                convert_count -= 1
            if convert_count == 0:
                break
        return token, target_token, converted_token

    # 한 단어에 두 음절의 어미가 동일한 된소리인 경우 뒤의 된소리를 예사소리로 변경한다.
    def overlapping_sound_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            characters = list(word[0])
            if len(word[0]) >= 2:
                if word[0][0] == word[0][1]:
                    if len(characters) == 2 and hangul_jamo.is_syllable(characters[1]):
                        jamos_one = list(
                            hangul_jamo.decompose_syllable(characters[0]))
                        jamos_two = list(
                            hangul_jamo.decompose_syllable(characters[1]))
                        if jamos_one[0] == jamos_two[0]:
                            for key in duen_sori_list:
                                if jamos_two[0] == key:
                                    target_token.append(list(word))
                                    jamos_two[0] = duen_sori_list[key]
                                    characters[1] = (
                                        hangul_jamo.compose_jamo_characters(jamos_two[0], jamos_two[1], jamos_two[2]))
                                    word[0] = "".join(characters)
                                    converted_token.append(word)
                                    convert_count -= 1
                                if convert_count == 0:
                                    break
                        if convert_count == 0:
                            break
        return token, target_token, converted_token

    """ 랜덤하게 고른 문자를 g2pk를 이용하여 소리 나는 대로 변경한다
        골라진 토큰에 뒤에 연결되는 토큰이 있는지 확인하고 있다면 converge_word 리스트에 모아둔 다음에 
        모아진 토큰들을 합체 해준 상태에서 g2pk를 썻을때 안쓴 문장과 동일하지 않은 경우에
        모은 토큰들을 결과로 return """

    def grapheme_to_phonem_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word_num in range(len(token)):
            target_tokens = []
            converted_tokens = []
            converge_word = []
            if random.choice([0, 1]) == 1:
                check = True
                n = 1
                converge_word.append(token[word_num])
                if token[word_num][0][:2] != "##" and token[word_num][1][0] != "S":
                    token[word_num].append(len(token[word_num][0]))
                    target_tokens.append(list(token[word_num]))
                    converted_tokens.append(token[word_num])
                    while check:
                        try:
                            if token[word_num + n][0][:2] == "##":
                                token[word_num +
                                      n].append(len(token[word_num + n][0]) - 2)
                                target_tokens.append(list(token[word_num + n]))
                                converted_tokens.append(token[word_num + n])
                                converge_word.append(token[word_num + n])
                                n += 1
                            else:
                                check = False
                        except:
                            check = False
                    converge_word = converge_token(
                        converge_word).strip()
                    word_g2p = g2p(converge_word)
                    if word_g2p != converge_word:
                        m = 0
                        for num in range(len(converted_tokens)):
                            if m == 0:
                                text = ''.join(
                                    word_g2p[m:m + converted_tokens[num][4]])
                            else:
                                text = "##" + ''.join(
                                    word_g2p[m:m + converted_tokens[num][4]])
                            converted_tokens[num][0] = text
                            m += converted_tokens[num][4]
                            token[word_num + num][0] = converted_tokens[num][0]
                        target_token.append(target_tokens)
                        converted_token.append(converted_tokens)
                        convert_count -= 1
                    else:
                        target_tokens = []
                        converted_tokens = []
                        converge_word = []
                    if convert_count == 0:
                        break
        return token, target_token, converted_token

    def final_suffix_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            if word[1] == "EF":
                target_token.append(list(word))
                ef_choice = random.choice(
                    [ef for ef in ef_data() if ef[0][0] == word[0][2]])
                word[0] = "##" + ef_choice
                converted_token.append(word)
                convert_count -= 1
            if convert_count == 0:
                break
        return token, target_token, converted_token

    def mag_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            similarity_max = [0, ""]
            if word[1] == "MAG":
                target_token.append(list(word))
                for mag in mag_data():
                    try:
                        similarity = kor_model.similarity(word[0], mag)
                        if similarity >= similarity_max[0] and mag != word[0]:
                            similarity_max = similarity, mag
                    except:
                        continue
                word[0] = similarity_max[1]
                converted_token.append(word)
                convert_count -= 1
                if convert_count == 0:
                    break
        return token, target_token, converted_token

    def maj_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            similarity_max = [0, ""]
            if word[1] == "MAJ":
                target_token.append(list(word))
                for maj in maj_data():
                    try:
                        similarity = kor_model.similarity(word[0], maj)
                        if similarity >= similarity_max[0] and maj != word[0]:
                            similarity_max = similarity, maj
                    except:
                        continue
                word[0] = similarity_max[1]
                converted_token.append(word)
                convert_count -= 1
                if convert_count == 0:
                    break
        return token, target_token, converted_token

    def polite_speech_error(token):
        convert_count = max_error
        target_token = []
        converted_token = []
        for word in token:
            if word[1] == "JKB":
                if word[0] == "##에게":
                    target_token.append(list(word))
                    word[0] = "##께"
                    converted_token.append(word)
                    convert_count -= 1
                elif word[0] == "##께":
                    target_token.append(list(word))
                    word[0] = "##에게"
                    converted_token.append(word)
                    convert_count -= 1
            elif word[1] == "JKS":
                if word[0] == "##이" or "##가":
                    target_token.append(list(word))
                    word[0] = "##께서"
                    converted_token.append(word)
                    convert_count -= 1
                elif word[0] == "##께서":
                    target_token.append(list(word))
                    word[0] = random.choice(["##이", "##가"])
                    converted_token.append(word)
                    convert_count -= 1
            if convert_count == 0:
                break
        return token, target_token, converted_token
