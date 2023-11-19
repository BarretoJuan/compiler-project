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
    PRINT = 'print'
    @classmethod
    def parse(cls, text):
        for keyword in cls:
            if text.startswith(keyword.value):  # Add a space after the keyword
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
        match = re.match(r'\".*?\"|\'.*?\'', text) # matches"" or '' strings

        if match:
            return (cls.Value, match.group()), text[match.end():]
        return None, text

class Op(Enum):
    PLUS = '+'
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    EQUALS = '=',
    EQUALS_EQUALS = '=='
    GREATER_THAN = '>'
    LESS_THAN = '<'
    GREATER_THAN_OR_EQUAL = '>='
    LESS_THAN_OR_EQUAL = '<='
    NOT = '!'
    NOT_EQUALS = '!='
    AND = '&&'
    OR = '||'

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
    STRING = StringLiteral
    OP = Op

    @classmethod
    def parse(cls, text, last_keyword=None, unknown_tokens=[]):
        while text:
            for token_type in cls:
                if token_type is cls.IDENTIFICATOR:
                    if last_keyword not in {"function", "var", 'while', 'if', 'else', 'for', 'return'}:
                        continue
                    else:
                        last_keyword = None  # Reset last_keyword after parsing an identifier
                token, remainder = token_type.value.parse(text)
                if token is not None:
                    if token_type is cls.KEYWORD:
                        last_keyword = token.value  # Update last_keyword here
                    return token, remainder, last_keyword, unknown_tokens
            # Find the next whitespace or special character
            end_of_token = len(text)
            for i, char in enumerate(text):
                if char.isspace(): # finding the next whitespace and slicing the text up to that point.
                    end_of_token = i
                    break
            unknown_tokens.append(text[:end_of_token])
            text = text[end_of_token:].lstrip()  # Remove leading whitespace
        return None, text, last_keyword, unknown_tokens

def parse(filepath):
    # Open it in read mode
    with open(filepath, 'r') as file:
        content = file.read()
    tokens = [] # We will store each token in this list
    unknown_tokens = [] # We will store unknown tokens in this list
    last_keyword = None # We will store the last keyword in this variable to keep track of it
    for l in content.splitlines():
        remainder = l
        while remainder:
            token, remainder, last_keyword, unknown_tokens = TokenType.parse(remainder, last_keyword, unknown_tokens)
            if token is not None:
                tokens.append(token)
            else:
                break
    unknown_tokens = [token for token in unknown_tokens if token != '']
    print("Tokens:", tokens)
    print("Unrecognizable tokens:", unknown_tokens)

parse('filename.bre')