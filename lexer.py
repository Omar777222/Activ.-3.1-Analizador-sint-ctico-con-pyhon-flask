import ply.lex as lex

# ---------------------------
#  ANALIZADOR LÉXICO (LEX)
# ---------------------------
tokens = ('IGUAL', 'SUMA', 'RESTA', 'MULT', 'DIV', 'IDENTIFICADOR', 'NUMERO', 'PUNTOCOMA', 'FOR')

t_IGUAL = r'='
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_PUNTOCOMA = r';'

def t_FOR(t):
    r'\b[Ff][Oo][Rr]\b'  # Detecta solo 'for' como una palabra completa
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.lower() == 'for':
        t.type = 'FOR'  # Reclasificar como FOR si es "for"
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

