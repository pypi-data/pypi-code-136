from __future__ import absolute_import
from mecab import MeCab
mec = MeCab()


""" 띄어쓰기 단위로 토크나이징 및 각 토큰에 시작과 끝을 부여
    token은 리스트로 네가지 정보다 담기는데 [단어, 형태소, 시작점, 끝점] """


def tokenize(text):
    pos = []
    begin = 0
    end = 0
    for st in text.split(" "):
        count = 0
        token = mec.pos(st)
        for token_num in range(len(token)):
            position = []
            tk = list(token[token_num])
            position.append(begin)
            end = begin + len(tk[0])
            position.append(end)
            tk.extend(position)
            begin += len(tk[0])
            if count > 0:
                tk[0] = '##' + tk[0]
                pos.append(tk)
            else:
                pos.append(tk)
                count += 1
    return pos


def g2p_tokenize(text):
    return mec.pos(text)


def converge_token(token):
    converged_text = ""
    for word in token:
        if word[0][:2] != "##":
            converged_text += " " + str(word[0])
        else:
            converged_text += str(word[0][2:])
    return converged_text
