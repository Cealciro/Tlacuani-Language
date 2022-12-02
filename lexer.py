#!/usr/bin/python3.8
#GLexer.py
#César Cisneros A01152861

import ply.lex as lex

reserved = {
    #Escritura general
    'PROGRAM' : 'PROGRAM',
    'MAIN' : 'MAIN',
    'FUNC' : 'FUNC',
    # Declaración Variables
    'VAR' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    # Declaración Funciones
    'VOID' : 'VOID',
    'RETURN' : 'RETURN', #Return Funcion
    'READ' : 'READ',    #Lectura
    'PRINT' : 'PRINT',  #escritura
    #Estatuto Decision
    'IF' : 'IF',
    'THEN' : 'THEN',
    'ELSE' : 'ELSE',
    #Estatuto Repeticion
    #Condicional
    'WHILE' : 'WHILE',
    'DO' : 'DO',
    #No Condicional
    'FOR' : 'FOR',
    'TO' : 'TO',
    #Expresiones
    'TRUE' : 'TRUE',
    'FALSE' : 'FALSE',
    'NOT' : 'NOT',
    #Funciones Especiales?
    'MEAN' : 'MEAN',
    'MODE' : 'MODE',
    'VARY' : 'VARY',
    'PLOTXY' : 'PLOTXY',

}
tokens = [
    'ID',
    #DATA
    'CTEI', 'CTEF',  'CTEC', 'BOOLEAN', 'CTES', 
    #MATH OP
    'PLUS', 'MINUS', 'MULT', 'DIV', 'ADD', 'DEC',
    #LOGIC OP
    'EQUALS', 'NON_EQUAL', 'EQUAL_MAJOR', 'EQUAL_MINOR', 'LESS_THAN', 'MORE_THAN', 'AND', 'OR',
    # part
    'L_PAR', 'R_PAR', 'L_SQ', 'R_SQ', 'L_COR', 'R_COR',
    #STUFF
    'COLON', 'SEMICOLON', 'DOT', 'COMMA', 'ENDL', 'ASSIGN'

] + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z_]\w*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t
# Data
def t_CTEF(t):
    r'\d+\.(\d*)?(e(\+|-)?\d+)?'
    t.value = float(t.value)
    return t

def t_CTEI(t): 
    r'\d+'
    t.value = int(t.value)
    return t
def t_CTEC (t):
    r'\'[A-Za-z_]\''
    t.type = 'CTEC'
    return t

def t_CTES(t):
    r'"([^\\"\n]+|\\.)*"'
    t.type = 'CTES'
    return t

def t_error(t):
    print("Caracter Ilegal '%s'" % t.value[0])
    t.lexer.skip(1)



#General
t_PROGRAM = r'PROGRAM'
t_VAR = r'VAR'
t_MAIN = r'MAIN'
t_FUNC = r'FUNC'
t_RETURN = r'RETURN'
#Variables
t_VOID = r'VOID'

#Conditionals
t_IF = r'IF'
t_THEN = r'THEN'
t_ELSE = r'ELSE'
#While
t_WHILE = r'WHILE'
t_DO = r'DO'
#Write n' Read
t_PRINT = r'PRINT'


# Math OP
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'\/'
t_ADD = r'\+\+'
t_DEC = r'\-\-'

# logic OP
t_EQUALS = r'\=\='
t_NON_EQUAL = r'\!\='
t_EQUAL_MAJOR = r'\>\='
t_EQUAL_MINOR = r'\<\='
t_LESS_THAN = r'\<'
t_MORE_THAN = r'\>'
t_AND = r'&'
t_OR = r'\|'

# Part
t_L_PAR = r'\('
t_R_PAR = r'\)'
t_L_SQ = r'\['
t_R_SQ = r'\]'
t_L_COR = r'\{'
t_R_COR = r'\}'

# Stuff
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_DOT = r'\.\.'
t_COMMA = r'\,'
t_ASSIGN = r'\='
#t_ENDL = r'\n'


t_ignore = ' \t\n\r\f' #Ignora los elementos de escritura: Espacio, Tabulador, New Line, Carriage Return y From Feed respectivamente


# Lexer Build
lexer = lex.lex()


#texto = input()

#lexer.input(texto)

#while True:
#    token = lexer.token()
#    if not token:
#        break
#    print(token)
