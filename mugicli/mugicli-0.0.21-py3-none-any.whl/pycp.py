import argparse
import re
from dataclasses import dataclass
from itertools import product
import sys

class Tok:
    (
        undefined,
        open_brace,
        close_brace,
        single_quotes,
        double_quotes,
        range,
        value,
    ) = range(7)

@dataclass
class T:
    type: int
    cont: str

class Lexed:
    def __init__(self):
        self.res = []
        self.tok = T(Tok.undefined, "")
    
    def flush(self, t = Tok.undefined):
        if t != Tok.undefined:
            self.tok.type = t
        if self.tok.cont != "":
            self.res.append(self.tok)
        self.clear()

    def clear(self):
        self.tok = T(Tok.undefined, "")

    def push(self, c):
        self.tok.cont += c

    def append(self, tok):
        self.res.append(tok)

def lexer(arg):

    in_braces = False
    in_single_quotes = False
    in_double_quotes = False

    lexed = Lexed()

    for i,c in enumerate(arg):

        if in_single_quotes:
            lexed.push(c)
            if c == "'":
                in_single_quotes = False
                lexed.flush()
                
        elif in_double_quotes:
            lexed.push(c)
            if c == '"':
                in_double_quotes = False
                lexed.flush()

        else:

            if c == "{":

                lexed.flush()
                lexed.append(T(Tok.open_brace, "{"))
                in_braces = True

            elif c == "}":

                lexed.flush(Tok.value if in_braces else Tok.undefined)
                lexed.res.append(T(Tok.close_brace, "}"))
                in_braces = False

            elif c == '"':

                lexed.flush()
                lexed.push(c)
                in_double_quotes = True
                    
            elif c == "'":

                lexed.flush()
                lexed.push(c)
                in_single_quotes = True

            elif c == '.':

                if in_braces and len(arg) > i+1 and arg[i+1] == '.':
                    lexed.flush(Tok.value)

                lexed.push(c)
                if lexed.tok.cont == "..":
                    lexed.flush(Tok.range)
            else:
                lexed.push(c)

    lexed.flush()

    return lexed.res

def lexer_test():
    arg = "{10..12}"
    toks = lexer(arg)

def index_of(tokens, t):
    for i, tok in enumerate(tokens):
        if tok.type == t:
            return i

def unquoted(s):
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    return s

class ExprStr:
    def __init__(self, tokens):
        self.cont = "".join([unquoted(tok.cont) for tok in tokens])
    def __repr__(self) -> str:
        return "ExprStr({})".format(self.cont)
    def eval(self):
        return [self.cont]

def is_int(v):
    try:
        int(v)
        return True
    except:
        return False

def is_letter(v):
    return len(v) == 1

class ExprRange:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def __repr__(self) -> str:
        return "ExprRange({},{})".format(self.value1, self.value2)
    def eval(self):
        if is_int(self.value1) and is_int(self.value2):
            return [str(v) for v in range(int(self.value1), int(self.value2)+1)]
        elif is_letter(self.value1) and is_letter(self.value2):
            return [chr(v) for v in range(ord(self.value1), ord(self.value2)+1)]
        else:
            return []

def parse(tokens_):
    tokens = tokens_[:]
    blocks = []
    while len(tokens):
        ix1 = index_of(tokens, Tok.open_brace)
        ix2 = index_of(tokens, Tok.close_brace)

        if ix1 is None or ix2 is None:
            blocks.append(ExprStr(tokens))
            tokens = []
            break

        if ix1 > 0:
            blocks.append(ExprStr(tokens[0:ix1]))

        ixv1 = ix1 + 1
        ixr = ix1 + 2
        ixv2 = ix1 + 3

        blocks.append(ExprRange(tokens[ixv1].cont, tokens[ixv2].cont))
        tokens = tokens[ix2+1:]
    return blocks

def evaluate(blocks):
    evaluated = [block.eval() for block in blocks]
    #print("evaluated", evaluated)
    return ["".join(item) for item in product(*evaluated)]
    
def evaluate_test():
    arg = "test\"best\"{10..12}{a..c}"
    toks = lexer(arg)
    blocks = parse(toks)
    res = evaluate(blocks)
    print(res)

def parser_test():
    arg = "test\"best\"{10..12}{a..z}"
    toks = lexer(arg)
    blocks = parse(toks)
    print(blocks)

def parse_lex_evaluate(arg):
    tokens = lexer(arg)
    print("tokens", tokens)
    blocks = parse(tokens)
    #print("blocks", blocks)
    return evaluate(blocks)

def shell_expand_args(args):
    res = []
    for arg in args:
        if "{" not in arg or "}" not in arg:
            res.append(arg)
        else:
            res += parse_lex_evaluate(arg)
    return res


def main():
    EXAMPLE_TEXT = """examples:
"""

    #parser = argparse.ArgumentParser(prog="", description="", epilog=EXAMPLE_TEXT, formatter_class=argparse.RawDescriptionHelpFormatter)
    #parser.add_argument("","",help="")
    #args = parser.parse_args()

    #lexer_test()
    #parser_test()
    #evaluate_test()
    args = sys.argv[1:]
    print("args", args)
    print("expanded", shell_expand_args(args))


if __name__ == "__main__":
    main()