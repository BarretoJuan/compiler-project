from lexer import parse
from lexer import TokenType, Keyword, Symbol, Number, StringLiteral, Op, Id

def generate_report(filepath):
    report = ''
    tokens, unknown_tokens = parse(filepath)
    with open(filepath, 'r') as file:
        code = file.read()
    line_count = code.count('\n') + 1 # count the number of lines
    code_without_spaces_or_newlines = code.replace(' ', '').replace('\n', '')
    
    keyword_list = [token.value for token in tokens if isinstance(token, Keyword)] # get all the keywords
    op_list = [token.value for token in tokens if isinstance(token, Op)] # get all the operators
    op_count = len(op_list) # count the number of operators
    var_count = tokens.count(Keyword.VAR) # get all the variables
    loop_count = tokens.count(Keyword.FOR) + tokens.count(Keyword.WHILE) # get all the loops
    id_list = [token[1] for token in tokens if isinstance(token, tuple) and token[0] == Id.IDName] # get all the identifiers
    id_count = len(id_list) # count the number of identifiers
    number_count =[token[1] for token in tokens if isinstance(token, tuple) and token[0] == Number.Value]
    strlit_list = [token[1] for token in tokens if isinstance(token, tuple) and token[0] == StringLiteral.Value]
    strlit_count = len(strlit_list)
    symbol_list = [token.value for token in tokens if isinstance(token, Symbol)]

    # Report generation
    report += f"DETALLES DEL ARCHIVO: {filepath}\n\n"
    
    report += f"Cantidad de lineas: {line_count}\n---\n"
    report += f"Cantidad de tokens: {len(tokens)}\n---\n"
    report += f"Cantidad de tokens desconocidos: {len(unknown_tokens)}\n---\n"
    report += f"Los tokens desconocidos son: {unknown_tokens}\n---\n"
    report += f"Codigo inicial:\n{code}\n---\n"
    report += f"Codigo sin espacios:\n{code_without_spaces_or_newlines}\n---\n"

    report += f"DETALLES DEL ANÁLISIS:\n\n"

    report += f"Cantidad de palabras claves: {len(keyword_list)}\nPalabras claves encontradas: {keyword_list}\n---\n"
    report += f"Cantidad de operadores: {op_count}\nOperadores encontrados: {op_list}\n---\n"
    report += f"Cantidad de identificadores: {id_count}\nIdentificadores encontrados: {id_list}\n---\n"
    report += f"Cantidad de numeros encontrados: {len(number_count)}\nNúmeros encontrados: {number_count}\n---\n"
    report += f"Cantidad de símbolos encontrados: {len(symbol_list)}\nSímbolos encontrados: {symbol_list}\n---\n"
    report += f"Cantidad de String Literals encontrados: {strlit_count}\nString Literals encontrados: {strlit_list}\n"

    return report


def save_report_to_txt(program_filepath):
    with open('report.txt', 'w', encoding="utf-8") as file:
        file.write(generate_report(program_filepath))
    print('Reporte generado con éxito.')