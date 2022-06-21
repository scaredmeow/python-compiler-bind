import lexical

var = "hi"


def parser(expression):
    lex = lexical.lexer(expression)
    token_type = lex.type
    token_value = lex.value
    token_error = lex.error
    token_column = lex.column
    token_line = lex.line
    syntax_error = []
    lex_error_count = count = 0
    for i in token_error:
        if i != '':
            count += 1

    if 'lex-error' in token_type:
        for index, item in enumerate(token_type):
            if item == 'lex-error' and token_value[index] == 'lex-error':
                lex_error_count += 1
        syntax_error.append(
            f'Syntax Error on Ln 0, Col 0: Syntax Analyzer can\'t continue there {"is "+str(count-lex_error_count)+" Lexical Error, " if count-lex_error_count == 1 else "are "+str(count-lex_error_count)+" Lexical Errors,"} \nplease check lexical analyzer first!')
        return syntax_error

    for index, item in enumerate(token_type):
        if item == 'lex-error' and token_value[index] == 'lex-error':
            continue
        print(
            f'Line {token_line[index]}, Column {token_column[index]}: {item}: {token_value[index]}: {token_error[index]}')
    return token_type


# token_type = parser(lexemes)
# print(token_type)

# TODO: Add Parser

# Program::= comm global comm bound {comm local comm statements} comm func comm
#
# Global_declarations::= Global_declaration Global_declarations | ε
# Global_declaration::= Const_declaration | Classic_declaration | Sheriff_declaration | Agent_declaration | Roster_declaration | Map_declaration
# Const_declaration::= const id = value | const id = value, Const_declaration
# Classic_declaration::= classic id = classic_literal | classic id = neg_classic_literal | classic id = classic_literal, Classic_declaration