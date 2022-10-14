from act.act_ast import ActDefinition, ActBlock, ActStatement, ActReference, ActCondition
from act.lex import lex_act, Token


class UnexpectedTokenError(Exception):
    def __init__(self, token, expected):
        self.token = token
        self.expected = expected
        msg = 'Unexpected token {}, expected {} (at {}, {})'.format(token.token, expected, token.line, token.column)
        super().__init__(msg)


class PeekableGenerator(object):

    def __init__(self, generator):
        self.empty = False
        self.peek = None
        self.generator = generator
        try:
            self.peek = self.generator.__next__()
        except StopIteration:
            self.empty = True

    def __iter__(self):
        return self

    def __next__(self):
        """
        Return the self.peek element, or raise StopIteration
        if empty
        """
        if self.empty:
            raise StopIteration()
        to_return = self.peek
        try:
            self.peek = self.generator.__next__()
        except StopIteration:
            self.peek = None
            self.empty = True
        return to_return


def parse(data):
    """
    Parse an ACT formatted document into an AST
    :param data: string containing an ACT document
    :return: magma_controller.act.act_ast.ActBlock
    """
    tokens = PeekableGenerator(lex_act(data))
    steps = []
    while True:
        try:
            step = _parse_step(tokens)
        except StopIteration:
            break
        steps.append(step)

    root = ActBlock(name='act', contents=steps)
    return root


def _parse_step(tokens, allow_rbrace=False):
    token = tokens.__next__()

    if token.token == Token.TRBRACE and allow_rbrace:
        token = tokens.__next__()
        if token.token != Token.TNEWLINE:
            raise UnexpectedTokenError(token, Token.TNEWLINE)
        return None

    if token.token == Token.TSTRING:
        if tokens.peek.token == Token.TCOLON:
            # name: value
            name = token.value
            tokens.__next__()
            value = []
            while True:
                if tokens.peek.token == Token.TSTRING:
                    token = tokens.__next__()
                    value.append(token.value)
                elif tokens.peek.token == Token.TINTEGER:
                    token = tokens.__next__()
                    value.append(token.value)
                elif tokens.peek.token == Token.TNEWLINE:
                    tokens.__next__()
                    break
                else:
                    raise UnexpectedTokenError(tokens.peek, [Token.TSTRING, Token.TINTEGER, Token.TNEWLINE])
            return ActDefinition(name=name, value=' '.join(value))
        elif tokens.peek.token == Token.TLBRACE:
            # name {
            name = token.value
            tokens.__next__()  # Consume LBRACE
            token = tokens.__next__()
            if token.token != Token.TNEWLINE:
                raise UnexpectedTokenError(token, Token.TNEWLINE)
            contents = []
            while True:
                value = _parse_step(tokens, allow_rbrace=True)
                if value is None:
                    break
                contents.append(value)
            return ActBlock(name=name, contents=contents)
        elif tokens.peek.token == Token.TLPAREN:
            # name (condition) {
            name = token.value
            tokens.__next__()  # Consume LPAREN
            token = tokens.__next__()

            # Currently supports a single condition
            a = ActReference(name=token.value)
            token = tokens.__next__()
            if token.token != Token.TEQUALS:
                raise UnexpectedTokenError(token, Token.TEQUALS)
            token = tokens.__next__()
            if token.token not in [Token.TINTEGER, Token.TQUOTE, Token.TSTRING]:
                raise UnexpectedTokenError(token, [Token.TINTEGER, Token.TQUOTE, Token.TSTRING])
            if token.token == Token.TINTEGER:
                b = token.value
            elif token.token == Token.TSTRING:
                b = ActReference(name=token.value)
            else:
                parts = []
                while True:
                    t = tokens.__next__()
                    if t.token == Token.TINTEGER:
                        parts.append(t.value)
                    elif t.token == Token.TSTRING:
                        parts.append(t.value)
                    elif t.token == Token.TQUOTE:
                        break
                    else:
                        raise UnexpectedTokenError(token, [Token.TINTEGER, Token.TSTRING, Token.TQUOTE])
                b = ' '.join(parts)
            con = ActCondition(a=a, b=b, method='==')

            token = tokens.__next__()
            if token.token != Token.TRPAREN:
                raise UnexpectedTokenError(token, Token.TRPAREN)
            token = tokens.__next__()
            if token.token != Token.TLBRACE:
                raise UnexpectedTokenError(token, Token.TLBRACE)
            token = tokens.__next__()
            if token.token != Token.TNEWLINE:
                raise UnexpectedTokenError(token, Token.TNEWLINE)

            contents = []
            while True:
                value = _parse_step(tokens, allow_rbrace=True)
                if value is None:
                    break
                contents.append(value)
            return ActBlock(name=name, contents=contents, condition=con)
        else:
            # statement
            value = [token.value]
            while True:
                if tokens.peek.token == Token.TSTRING:
                    token = tokens.__next__()
                    value.append(token.value)
                elif tokens.peek.token == Token.TINTEGER:
                    token = tokens.__next__()
                    value.append(token.value)
                elif tokens.peek.token == Token.TNEWLINE:
                    tokens.__next__()
                    break
                else:
                    raise UnexpectedTokenError(tokens.peek, [Token.TSTRING, Token.TINTEGER, Token.TNEWLINE])
            return ActStatement(statement=' '.join(value))
    else:
        raise UnexpectedTokenError(token, [Token.TSTRING])


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='file to parse')
    args = parser.parse_args()
    with open(args.file) as handle:
        raw = handle.read()
    print(parse(raw))
