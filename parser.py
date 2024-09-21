import ply.yacc as yacc
from lexer import tokens  # Importa los tokens del archivo lexer

# ---------------------------
#  ANALIZADOR SINTÁCTICO (YACC)
# ---------------------------
precedence = (
    ('right', 'IGUAL'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
)

nombres = {}

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR IGUAL expresion PUNTOCOMA'
    nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    print(f"Resultado: {t[1]}")

def p_expresion_binaria(t):
    '''expresion : expresion SUMA expresion
                 | expresion RESTA expresion
                 | expresion MULT expresion
                 | expresion DIV expresion'''
    if t[2] == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_numero(t):
    'expresion : NUMERO'
    t[0] = t[1]

def p_error(t):
    print(f"Error de sintaxis en '{t.value}'")

parser = yacc.yacc()
