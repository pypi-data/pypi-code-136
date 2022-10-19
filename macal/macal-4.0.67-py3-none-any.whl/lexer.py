#
# Product:   Macal
# Author:    Marco Caspers
# Date:      07-09-2022
#


import string
import typing
from . import types
from . import location
from . import token
from . import exceptions
from . import __about__

TABSIZE = 4

class Lexer:
    def __init__(self) -> None:
        self.length: int = None
        self.source: str = None
        self.filename: str = None



    def Lex(self, source: str, filename: str) -> typing.List[token.LexToken]:
        if source is None:
            exceptions.LexError(message="No source code to analyze.", filename=filename, loc=None)
        if filename is None:
            exceptions.LexError(message="No filename provided.", filename=filename, loc=None)
        tokens = []
        loc = location.SourceLocation(1,1)
        self.source = source
        self.filename = filename
        self.length = len(source)
        index = 0
        stuck = 0
        interpolate = False
        skip = False
        in_expr = False
        terminator = ''
        while index < self.length:
            (result, token, index, loc, interpolate, in_expr, skip, terminator) = self.getToken(index, loc, interpolate, in_expr, skip, terminator)
            if result: 
                tokens.append(token)
            if index == stuck:
                raise exceptions.LexError(message="Stuck in lexer analysis loop",loc = loc, filename = filename )
            else:
                stuck = index
            if index < self.length and result is False and skip is False:
                raise exceptions.LexError(message="Unexpected end of file",loc = loc, filename = filename )
            skip = False
        return tokens



    def Current(self, index: int) -> str:
        if index < self.length:
            return self.source[index]
        return None



    def Next(self, index: int) -> typing.Tuple[int, str]:
        index += 1
        if index >= 0 and index < self.length:
            return (index, self.source[index])
        return (index, None)



    def Peek(self, index: int, offset: int) -> str:
        if index + offset < self.length and index+offset >= 0:
            return self.source[index+offset]
        return None



    def getStringToken(self, start: int, loc: location.SourceLocation) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation]:
        current = self.Current(start)
        if current is None:
            raise exceptions.LexError(message="Unexpected nil in string.", filename=self.filename, loc=loc)
        if current not in ['"', "'"]:
            return (False, None, start, loc)
        terminator = current
        (index, current) = self.Next(start)
        line = loc.Line
        col = loc.Column
        while current != terminator and current is not None:
            (index, current) = self.Next(index)
            if current == '\\':
                col += 1
                (index, current) = self.Next(index)
            if current == '\n':
                line += 1
                col = 1
        (index, _) = self.Next(index)
        col += 1
        tok = token.LexToken(index=start, loc=loc, lexeme = self.applyEscapes(self.source[start+1:index-1]), type = types.LexTokenTypes.String) # +1 -1 should omit the terminators in the Lexeme.
        return (True, tok, index, location.SourceLocation(line, col))



    def getInterpolationPart(self, start: int, loc: location.SourceLocation, interpolate: bool, in_expr: bool, skip: bool, terminator: str) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation, bool, bool]:
        if interpolate is False:
            return (False, None, start, loc, interpolate, in_expr, skip, terminator)
        index = start
        current = self.Current(index)
        if current is None:
            raise exceptions.LexError(message="Unexpected nil in string.", filename=self.filename, loc=loc)
        if current == '{':
            if self.Peek(index, 1) != '{':
                in_expr = True
                (index, current) = self.Next(index)
                return (False, None, index, location.SourceLocation(loc.Line, loc.Column+1), interpolate, in_expr, skip, terminator)
        if current == '}':
            if self.Peek(index, 1) != '}':
                in_expr = False
                skip = True
                (index, current) = self.Next(index)
                return (False, None, index, location.SourceLocation(loc.Line, loc.Column+1), interpolate, in_expr, skip, terminator)
        if in_expr is True:
            return (False, None, index, loc, interpolate, in_expr, skip, terminator)
        if current == terminator:
            skip = False
            in_expr = False
            interpolate = False          
            terminator = ''
            tok = token.LexToken(index=index, loc=loc, lexeme = '$', type = types.LexTokenTypes.InterpolationEnd)
            return (True, tok, index+1, location.SourceLocation(loc.Line, loc.Column+1), interpolate, in_expr, skip, terminator)        
        line = loc.Line
        col = loc.Column
        startedWithTerminator = 0
        if terminator == '':
            terminator = current
            if terminator not in ['"', "'"]:
                raise exceptions.LexError(f'Invalid string terminator ("{terminator}") found.', filename = self.filename, loc=loc)
            (index, current) = self.Next(index)
            col += 1
            startedWithTerminator = 1
        while current != terminator and current != '{' and current is not None:
            (index, current) = self.Next(index)
            col += 1
            if current == '\\':
                col += 1
                (index, current) = self.Next(index)
            if current == '{' and self.Peek(index, 1) == '{':
                col += 2
                (index, current) = self.Next(index)
                (index, current) = self.Next(index)
            if current == '\n':
                line += 1
                col = 1
        if current == '{' and self.Peek(index, 1) != '{':
            in_expr = True
            tok = token.LexToken(index=index, loc=loc, lexeme = self.applyEscapes(self.source[start+startedWithTerminator:index]), type = types.LexTokenTypes.String)
            (index, _) = self.Next(index)
            col += 1
            result = True
            skip = False
            if index == start+2:
                skip = True
                result = False
                tok = None
            return (result, tok, index, location.SourceLocation(line, col), interpolate, in_expr, skip, terminator)       
        tok = token.LexToken(index=start, loc=loc, lexeme = self.applyEscapes(self.source[start+startedWithTerminator:index]), type = types.LexTokenTypes.String)
        return (True, tok, index, location.SourceLocation(line, col), interpolate, in_expr, skip, terminator)
           


    def getInterpolation(self, start: int, loc: location.SourceLocation) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation]:
        current = self.Current(start)
        if current is None:
            raise exceptions.LexError(message="Unexpected None in current.", filename=self.filename, loc=location)
        if current != '$':
            return (False, None, start, loc, False)
        tok = token.LexToken(index=start, loc=loc, lexeme = current, type = types.LexTokenTypes.InterpolationStart)
        (index, _) = self.Next(start)
        return (True, tok, index, location.SourceLocation(loc.Line, loc.Column+1), True)



    def getNumberToken(self, start: int, loc: location.SourceLocation) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation]:
        current = self.Current(start)
        if current is None:
            raise exceptions.LexError(message="Unexpected None in current.", filename=self.filename, loc=location)
        if not current.isdigit():
            return (False, None, start, loc)
        dot = False
        col = loc.Column
        line = loc.Line
        index = start
        while current.isalnum() or current == '_':
            (index, current) = self.Next(index)
            col += 1
            if current == '.' and not dot:
                dot = True
                (index, current) = self.Next(index)
                col += 1
        tok = token.LexToken(index=start, loc=loc, lexeme = self.source[start:index], type = types.LexTokenTypes.Number)
        return (True, tok, index, location.SourceLocation(line, col))
        


    def getIdentifier(self, start: int, loc: location.SourceLocation) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation]:
        current = self.Current(start)
        if current is None:
            raise exceptions.LexError(message="Unexpected None in current.", filename=self.filename, loc=location)
        if not current.isalpha() and current != '_':
            return (False, None, start, loc)
        index = start
        col = loc.Column
        line = loc.Line
        while current.isalnum() or current == '_':
            (index, current) = self.Next(index)
            col += 1
        tok = token.LexToken(index=start, loc=loc, lexeme = self.source[start:index], type = types.LexTokenTypes.Identifier)
        return (True, tok, index, location.SourceLocation(line, col))



    def getOperator(self, start: int, loc: location.SourceLocation) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation]:
        current = self.Current(start)
        if current is None:
            raise exceptions.LexError(message="Unexpected None in current.", filename=self.filename, loc=location)
        index = start
        col = loc.Column
        line = loc.Line
        if current in ['-','+','*','=','>','<', '!', '%', '^']:
            if self.Peek(start, 1) == '=' or (current == '=' and self.Peek(start, 1) == '>'):
                (index, current) = self.Next(index)
                col += 1            
        elif current == '/':
            if self.Peek(start,1) == '=':
                (index, current) = self.Next(index)
                col += 1
            elif self.Peek(start, 1) in ['/', '*']:
                return (False, None, start, loc)
        else:
            return (False, None, start, loc)
        (index, _) = self.Next(index)
        col += 1
        tok = token.LexToken(index=start, loc=loc, lexeme = self.source[start:index], type = types.LexTokenTypes.Operator)
        return (True, tok, index, location.SourceLocation(line, col))



    def getPunctuation(self, start: int, loc: location.SourceLocation) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation]:
        current = self.Current(start)
        if current is None:
            raise exceptions.LexError(message="Unexpected None in current.", filename=self.filename, loc=loc)
        if current in ['.',',',':',';','(',')','[',']','{','}']:
            tok = token.LexToken(index=start, loc=loc, lexeme = current, type = types.LexTokenTypes.Punctuation)
            (index, _) = self.Next(start)
            return (True, tok, index, location.SourceLocation(loc.Line, loc.Column+1))
        return (False, None, start, loc)


    
    def getWhitespace(self, start: int, loc: location.SourceLocation) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation]:
        current = self.Current(start)
        if current is None:
            raise exceptions.LexError(message="Unexpected None in current.", filename=self.filename, loc=loc)
        if not current in string.whitespace:
            return (False, None, start, loc)
        col = loc.Column
        line = loc.Line
        index = start
        while current in string.whitespace:
            col += 1
            if current == '\n':
                line += 1
                col = 1
            if current == '\t':
                col += TABSIZE - 1
            (index, current) = self.Next(index)
            if index >= self.length or current is None:
                break
        tok = token.LexToken(index=start, loc=loc, lexeme = self.source[start:index], type = types.LexTokenTypes.Whitespace)
        return (True, tok, index, location.SourceLocation(line, col))        



    def getComment(self, start: int, loc: location.SourceLocation) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation]:
        current = self.Current(start)
        if current is None:
            raise exceptions.LexError(message="Unexpected None in current.", filename=self.filename, loc=loc)
        if current != '/':
            return (False, None, start, loc)
        col = loc.Column
        line = loc.Line        
        if self.Peek(start, 1) in ['*', '/']:
            (index, current) = self.Next(start)
            col += 1
            if current == '*':
                while current != None:
                    (index, current) = self.Next(index)
                    col += 1
                    if current == '\n':
                        line += 1
                        col = 1
                    if current == '*' and self.Peek(index, 1) == '/':
                        (index, current) = self.Next(index) # skip *
                        (index, current) = self.Next(index) # skip /
                        col += 2
                        break
            else:
                while current != '\n' and current is not None:
                    (index, current) = self.Next(index)
                    col += 1
            tok = token.LexToken(index=start, loc=loc, lexeme = self.source[start:index], type = types.LexTokenTypes.Comment)
            return (True, tok, index, location.SourceLocation(line, col))        
        else:    
            return (False, None, start, loc)



    def getToken(self, start: int, loc: location.SourceLocation, interpolate: bool, in_expr: bool, skip: bool, 
            terminator: str) -> typing.Tuple[bool, token.LexToken, int, location.SourceLocation, bool, bool, bool, str]:
        # when interpolate is true we are basically picking appart a string and we don't want to skip whitespace nor 
        # try to interpret another string, unless we are in the expression part of the interpolated string.
        index = start
        if interpolate is False or in_expr:
            (result, tok, index, loc) = self.getWhitespace(index, loc)
            if result: return (result, tok, index, loc, interpolate, in_expr, skip, terminator)
            (result, tok, index, loc) = self.getStringToken(index, loc)
            if result: return (result, tok, index, loc, interpolate, in_expr, skip, terminator)
        (result, tok, index, loc, interpolate, in_expr, skip, terminator) = self.getInterpolationPart(index, 
            loc, interpolate, in_expr, skip, terminator)
        if result:
            return (result, tok, index, loc, interpolate, in_expr, skip, terminator)
        if skip == False: (result, tok, index, loc) = self.getNumberToken(index, loc)
        if result: return (result, tok, index, loc, interpolate, in_expr, skip, terminator)
        if skip == False: (result, tok, index, loc) = self.getOperator(index, loc)
        if result: return (result, tok, index, loc, interpolate, in_expr, skip, terminator)
        if skip == False: (result, tok, index, loc) = self.getIdentifier(index, loc)
        if result: return (result, tok, index, loc, interpolate, in_expr, skip, terminator)
        if skip == False: (result, tok, index, loc) = self.getPunctuation(index, loc)
        if result: return (result, tok, index, loc, interpolate, in_expr, skip, terminator)
        if skip == False: (result, tok, index, loc) = self.getComment(index, loc)
        if result: return (result, tok, index, loc, interpolate, in_expr, skip, terminator)
        if skip == False: (result, tok, index, loc, interpolate) = self.getInterpolation(index, loc)
        if result: return (result, tok, index, loc, interpolate, in_expr, skip, terminator)
        return (False, None, index, loc, interpolate, in_expr, skip, terminator)



    @staticmethod
    def applyEscapes(source: str) -> str:
        index = 0
        length = len(source)
        destination = ''
        while index < length:
            if source[index] == '\\' and index+1 < length:
                if (source[index+1] in ['a','b','n','r','t','0']):
                    if source[index+1] == 'a': destination=f"{destination}\a"
                    elif source[index+1] == 'b': destination=f"{destination}\b"
                    elif source[index+1] == 'n': destination=f"{destination}\n"
                    elif source[index+1] == 'r': destination=f"{destination}\r"
                    elif source[index+1] == 't': destination=f"{destination}\t"
                    else: destination=f"{destination}\0"
                else: destination = f"{destination}{source[index+1]}"
                index += 1
            else: destination=f"{destination}{source[index]}"
            index += 1
        return destination
