from enum import Enum, auto
import re

class AST:
    pass

class Keyword(Enum):
    FUNCTION = 'function'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    FOR = 'for'
    RETURN = 'return'
    VAR = 'var'

    @classmethod
    def parse(cls, text):
        for keyword in cls:
            if text.startswith(keyword.value + ' '):  # Add a space after the keyword
                return keyword, text[len(keyword.value):].lstrip()
        return None, text

class Id(Enum):
    IDName = auto()

    @classmethod
    def parse(cls, text):
        match = re.match(r'\b([a-zA-Z_][a-zA-Z_0-9]*)\b', text)
        if match:
            id = match.group(1)
            return (cls.IDName, id), text[len(id):]
        return None, text


class Symbol(Enum):
    OPEN_PAREN = '('
    CLOSE_PAREN = ')'
    OPEN_BRACE = '{'
    CLOSE_BRACE = '}'
    SEMICOLON = ';'
    COMMA = ','

    @classmethod
    def parse(cls, text):
        text = text.lstrip()
        for symbol in cls:
            if text.startswith(symbol.value):
                return symbol, text[len(symbol.value):]
        return None, text

class Number(Enum):
    Value = auto()

    @classmethod
    def parse(cls, text):
        match = re.match(r'\d+', text)
        if match:
            return (cls.Value, int(match.group())), text[match.end():]
        return None, text
    
class StringLiteral(Enum):
    Value = auto()

    @classmethod
    def parse(cls, text):
        match = re.match(r'\".*?\"', text)
        if match:
            return (cls.Value, match.group()), text[match.end():]
        return None, text

class Op(Enum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    EQUALS = '='

    @classmethod
    def parse(cls, text):
        for op in cls:
            if text.startswith(op.value):
                return op, text[len(op.value):]
        return None, text
# We go through the whole file and check if there's a token that matches our table of symbols
class TokenType(Enum):
    KEYWORD = Keyword
    IDENTIFICATOR = Id
    SYMBOL = Symbol
    NUMBER = Number
    OPERATION = Op
    STR_LIT = StringLiteral
    @classmethod
    def parse(cls, text):
        while text:
            for token_type in cls:
                token, remainder = token_type.value.parse(text)
                if token is not None:
                    return token, remainder
            text = text[1:]
        return None, text

# Then in your main code:
with open('filename.bre', 'r') as file:
    content = file.read()
tokens = []
for t in content.splitlines():
    print('THIS LINE IS: ', t)
    
    remainder = t
    while remainder:
        token, remainder = TokenType.parse(remainder)
        if token is not None:
            tokens.append(token)
        else:
            break
print(tokens)