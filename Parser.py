#César Cisneros A01152861

import ply.yacc as yacc
import lexer
import Semcube
from Structure import *
from collections.abc import Iterable
import math

tokens = lexer.tokens
#>===============Estructuras===============<#
curr_vFu = 'Global'
curr_type = None #Para poner en tipo de las funciones
curr_var = None #Para poner el nombre de los IDs en variables
fn = None
curr_row = [1]
tem = []

StFun = []

Stack = Steak() #Stacks para las funciones 
Quads = QuadL()
VarT = varTable() #Directorio tabla de Variables
Cons = CTET() #Directorio de constantes
fDir = Fdir() #Directorio de Funciones
Memory = Mem() #Directorio de memoria 
LineQ = -1 #Comienza en -1 dado a que estaremos con la posición de los arreglos y estos empiezan desde 0
jump = 0

#>===============funciones===============<#

def search(id, type): #Se dedica a buscar en el directorio de funciones, en cada uno de los tipos vamos a especificar para que se utilizan
    if type == 'cte': #Busca si existe la constante
        if not Cons.CTEL:
            return False
        for cons in Cons.CTEL:
            if cons.ID == id:
                return cons
        return False
    
    if type == 'var': #Busca si la variable existe
        if not VarT.vList:
            return False
        vList = VarT.vList.copy()
        #print(vList)
        for var in vList:
            if var.ID == id:
                return var
        return False
    if type == 'dir': #Busca por medio de la dirección
        if not VarT.vList:
            return False
        vList = VarT.vList.copy()
        for var in vList:
            #print(var.Vald)
            dab = len(var.Vald)
            #print('\n')
            #print(vList, dab)
            if (dab):
                for i in range(dab):
                    if var.Vald[i] == id:
                        return var
            else:
                if var.Vald == id:
                    return var
        return False
    if type == 'mod':
        if not fDir.fList:
            return False
        mList = fDir.fList.copy()
        for md in mList:
            if md.ID == id:
                return md
        return False

#genera cuadruplos
def GenQuad(p):
    global LineQ
    NewQ = Quad(*p)
    Quads.Add(NewQ)
    LineQ += 1

#>===============Grámatica===============<#
def p_programa(p):
    '''program : PROGRAM ID SEMICOLON pVars gtm fun mein'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7]
    GenQuad(('END', None, None, None))
    print("Compilación Completa!")
    #print(VarT.vList)
    IwannaDie()
    #print(Quads.Quads)

def p_gtm(p):
    '''gtm : '''
    GenQuad(('GoToMain', None, None, None))
    Stack.GoTo.append(LineQ)

#Declaración de variables
def p_pVars(p):
    '''pVars : vars
             | empty'''
    p[0] = p[1]
    #if global go to main else go to func
    
def p_vars(p):
    '''vars : VAR COLON vars2'''
    p[0] = p[1], p[2], p[3]

def p_vars2(p):
    '''vars2 : vare COLON type def SEMICOLON vars3'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]

def p_vars3(p):
    ''' vars3 : vars2
              | empty'''
    p[0] = p[1]

def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR'''
    p[0] = p[1]
    global curr_type
    curr_type = p[1]

#Define los valores y los envía a un estado de memoria
def p_def(p):
    '''def : '''
    global curr_vFu, curr_var, curr_row, curr_type
    #print(curr_row)
    if curr_var != None:
        if curr_vFu == 'Global':
            ret = search(curr_var, 'var')
            if curr_type == 'int':
                add = Memory.Gint[1]
                if (add < Memory.Gint[0]):
                    if (not ret):
                        adl = []
                        if (jump > 1) :
                            for i in range(jump):
                                adl.append(add + i)
                        else:
                            adl.append(add)
                        var (adl)
                        #print("\"%s\" Sent To address: %s " % (curr_var, add))
                        pro = math.prod(curr_row)
                        Memory.Gint[1] += pro
                        varRes()
                        if (add >= Memory.Gint[0]):
                            print ("Exceso de memoria global variables INT")
                            quit()
                    else:
                        print("Variable \"%s\" ya declarada" % curr_var)
                        quit()
                else:
                    print ("Exceso de memoria global variables INT")
                    quit()               
            if curr_type == 'float':
                add = Memory.Gint[0] + Memory.Gfloat[1]
                if (add < Memory.Gfloat[0]):
                    if (not ret):
                        adl = []
                        if (jump > 1) :
                            for i in range(jump):
                                adl.append(add + 1)
                        else:
                            adl.append(add)
                        var (adl)
                        #print("\"%s\" Sent To address: %s " % (curr_var, add))
                        pro = math.prod(curr_row)
                        Memory.Gfloat[1] += pro
                        varRes()
                        if (add >= Memory.Gfloat[0]):
                            print ("Exceso de memoria global variables FLOAT")
                            quit() 
                    else:
                        print("Variable \"%s\" ya declarada" % curr_var)
                        quit()
                else:
                    print ("Exceso de memoria global variables FLOAT")
                    quit()  
                curr_var = None
            if curr_type == 'char':
                add = Memory.Gfloat[0] + Memory.GString[1]
                if (add < Memory.GString[0]):
                    if (not ret):
                        adl = []
                        if (jump > 1) :
                            for i in range(jump):
                                adl.append(add + 1)
                        else:
                            adl.append(add)
                        var (adl)
                        #print("\"%s\" Sent To address: %s " % (curr_var, add))
                        pro = math.prod(curr_row)
                        Memory.GString[1] += pro
                        varRes()
                        if (add >= Memory.GString[0]):
                            print ("Exceso de memoria global variables CHAR")
                            quit() 
                    else:
                        print("Variable \"%s\" ya declarada" % curr_var)
                        quit()
                else:
                    print ("Exceso de memoria global variables CHAR")
                    quit()  
        if curr_vFu == 'Local':
            ret = search(curr_var, 'var')
            if curr_type == 'int':
                add = Memory.GString[0] + Memory.Lint[1]
                if (add < Memory.Lint[0] ):
                    if (not ret):
                        adl = []
                        if (jump > 1) :
                            for i in range(jump):
                                adl.append(add + 1)
                        else:
                            adl.append(add)
                        var (adl)
                        #print("\"%s\" Sent To address: %s " % (curr_var, adl))
                        pro = math.prod(curr_row)
                        Memory.Lint[1] += pro
                        varRes()
                        if (add >= Memory.Lint[0]):
                            print ("Exceso de memoria Local variables INT")
                            quit()
                    else:
                        print("Variable \"%s\" ya declarada" % curr_var)
                        quit()
                else:
                    print ("Exceso de memoria Local variables INT")
                    quit()  
            if curr_type == 'float':
                add = Memory.Lint[0] + Memory.Lfloat[1]
                if (add < Memory.Lfloat[0]):
                    if (not ret):
                        adl = []
                        if (jump > 1) :
                            for i in range(jump):
                                adl.append(add + 1)
                        else:
                            adl.append(add)
                        var (adl)
                        #print("\"%s\" Sent To address: %s " % (curr_var, add))
                        pro = math.prod(curr_row)
                        Memory.Lfloat[1] += pro
                        varRes()
                        if (add > Memory.Lfloat[0]):
                            print ("Exceso de memoria Local variables FLOAT")
                            quit() 
                    else:
                        print("Variable \"%s\" ya declarada" % curr_var)
                        quit()
                else:
                    print ("Exceso de memoria Local variables FLOAT")
                    quit() 
            if curr_type == 'char':
                add = Memory.Lfloat[0] + Memory.LString[1]
                if (add < Memory.LString[0]):
                    if (not ret):
                        adl = []
                        if (jump > 1) :
                            for i in range(jump):
                                adl.append(add + 1)
                        else:
                            adl.append(add)
                        var (adl)
                        #print("\"%s\" Sent To address: %s " % (curr_var, add))
                        pro = math.prod(curr_row)
                        Memory.LString[1] += pro
                        varRes()
                        if (add >= Memory.LString[0]):
                            print ("Exceso de memoria Local variables CHAR")
                            quit() 
                    else:
                        print("Variable \"%s\" ya declarada" % curr_var)
                        quit()
                else:
                    print ("Exceso de memoria Local variables CHAR")
                    quit() 
    else:
        print("Error no hay Variables")
        quit()      

def varRes(): #Resetea los valores de memoria para declaración
    global curr_var, curr_row, curr_type, jump
    curr_var = None
    jump = 0
    curr_row = [1]
    curr_type = None
#agrega la variable global en la memoria con su dirección y valores
def var(add):
    new = Vobj(curr_var, curr_type, add, curr_row, 0)
    VarT.Add(new)

def p_vare(p):
    '''vare : ID ar'''
    p[0] = p[1], p[2]
    global curr_var
    curr_var = p[1]

def p_ar(p):
    '''ar : L_SQ siz R_SQ
           | empty'''
    if p[1] == None:
        p[0] = p[1]
        #Manda el ID directo
    else:
        p[0] = p[1], p[2], p[3]
        #Genera  el tamaño del arreglo

def p_siz(p) :
    '''siz : CTEI mat'''
    p[0] = p[1], p[2]
#Revisa si es una matriz
def p_mat(p) :
    '''mat : DOT CTEI
           | empty'''
    global curr_row, jump
    if p[1] == None:
        p[0] = p[1]
        #Manda p[-1]
        curr_row = [p[-1]]
        #print(curr_row)
        if (curr_row <= 0):
            print("Error, los arreglos deben de ser mayores a 1")
            quit()
        if (curr_row == 1) :
            print("El arreglo pasa a ser variable.")
        jump = curr_row[0]

    else:
        p[0] = p[1], p[2]
        #manda p[-2] en las dimensiones
        curr_row = [p[-1], p[2]]
        if (curr_row[0] <= 0 or curr_row[1] <= 0):
            print("Error, los arreglos deben de ser mayores a 1")
            quit()
        if ((curr_row) == 1):
            print("La matriz pasa a ser arreglo")
        jump = curr_row[0] * curr_row[1]
#function modules
def p_fun(p):
    '''fun : Fun fuc
           | empty'''
    p[0] = p[1]
def p_fuc(p):
    '''fuc : fun'''
    p[0] = p[1]
#>>>>>>>>>>>>>>>>DEVELOP<<<<<<<<<<<<<<<
#<<<<<<<<<<<<<<<<<<<<<<<<<MODULOS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def p_Fun(p):
    '''Fun : FUNC Ftype ID mst L_PAR param paran R_PAR SEMICOLON pVars bloq endfun''' #endfun
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11]
#Funión Tipo
def p_Ftype(p):
    '''Ftype : type
            | VOID'''
    p[0] = p[1]
    #fDir.add(p[1])
    #print(curr_vFu, StFun)

def p_mst(p):
    '''mst : '''
    global curr_vFu, StFun
    curr_vFu = 'Local'
    StFun.append((p[-2], p[-1]))
    ty = StFun[-1][0]
    id= StFun[-1][1]
    #print(ty, id)
    #print(id)
    if search(id, 'var'):
        print("El Nombre \"%s\" ya está reservado" %id)
        quit()
    for mod in fDir.fList:
            if mod.ID == id:
                print("El modulo \"%s\" ya existe" %id)
                quit()
    if ty == 'int':
        add = Memory.Gint[1]
        if (add < Memory.Gint[0] ):
            defi(id, ty, add)
            #print("\"%s\" Sent To address: %s " % (id, add))
            Memory.Gint[1] += 1
            if (add >= Memory.Gint[0]):
                print ("Exceso de memoria Local variables INT")
                quit()
        else:
            print ("Exceso de memoria Local variables INT")
            quit()
    if ty == 'float':
        add = Memory.Gint[0] + Memory.Gfloat[1]
        if (add < Memory.Gfloat[0] ):
            defi(id, ty, add)
            #print("\"%s\" Sent To address: %s " % (id, add))
            Memory.Gfloat[1] += 1
            if (add >= Memory.Gfloat[0]):
                print ("Exceso de memoria Local variables FLOAT")
                quit()
        else:
            print ("Exceso de memoria Local variables FLOAT")
            quit()
    if ty == 'char':
        add = Memory.Gfloat[0] + Memory.GString[1]
        if (add < Memory.GString[0] ):
            defi(id, ty, add)
            #print("\"%s\" Sent To address: %s " % (id, add))
            Memory.GString[1] += 1
            if (add >= Memory.GString[0]):
                print ("Exceso de memoria Local variables CHAR")
                quit()
        else:
            print ("Exceso de memoria Local variables CHAR")
            quit()
    mod = Fobj(id, ty, VarT, None, LineQ +1, 0)
    fDir.add(mod)

def defi(id, ty, add):
    #print(id, ty, add)
    new = Vobj(id, ty, [add], 1, 0)
    VarT.Add(new)
       
#Declaración de parametros funciones
def p_param(p):
    '''param : ID COLON type xparam
             | empty'''
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2], p[3], p[4]
    #print(p[0])

def p_xparam(p):
    '''xparam : COMMA ID COLON type xparam
            | empty'''
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2], p[3], p[4], p[5]

    #print(p[0])

#Punto Neuralgico creación de parametros
def p_paran(p):
    '''paran : '''
    if p[-1] == None:
        fDir.fList[-1].val = []
    else:
        parm = []
        ty = p[-1]
        fl= [id for id in list(flatcock(ty)) if id != None]
        #print (fl)
        for it in range(0, len(fl), 1):
            if fl[it] == 'int':
                add = Memory.GString[0] + Memory.Lint[1]
                adl = []
                adl.append(add)
                Memory.Lint[1] += 1
                parm.append((fl[it-2], fl[it], adl))
                #print(parm)
            if fl[it] == 'float':
                add = Memory.Lint[0] + Memory.Lfloat[1]
                adl = []
                adl.append(add)
                Memory.Lfloat[1] += 1
                parm.append((fl[it-2], fl[it], adl))
                #print(parm)
            if fl[it] == 'char':
                add = Memory.Lfloat[0] + Memory.LString[1]
                adl = []
                adl.append(add)
                Memory.LString[1] += 1
                parm.append((fl[it-2], fl[it], adl))
                #print(parm)
        for it in range(0, len(parm), 1):
            new = Vobj(parm[it][0], parm[it][1], parm[it][2], curr_row, 0)
            VarT.Add(new)
        fDir.fList[-1].val= parm
        #print(fDir.fList[-1])
    #GenQuad(('GoToFun', None, None, None))
    #Stack.GoTo.append(LineQ)

def p_endfun(p):
    '''endfun : '''
    size = [[0, 0, 0], [0, 0, 0, 0]] #[local [int, float, char], temp [int, float, char, bool]]
    tmp = VarT
    var = []
    #print(tmp.vList[1])
    for i in range(len(tmp.vList)) :
        for j in range(len(tmp.vList[i].Vald)) :
            if tmp.vList[i].Vald[j] < 6000:
                if not var:
                    var.append(tmp.vList[i])
                elif tmp.vList[i].Vald != var[-1]:
                    var.append(tmp.vList[i])
            if tmp.vList[i].Vald[j] >= 6000 and tmp.vList[i].Vald[j] < 8000:
                size[0][0] += 1
            elif tmp.vList[i].Vald[j] >= 8000 and tmp.vList[i].Vald[j] < 10000:
                size[0][1] += 1
            elif tmp.vList[i].Vald[j] >= 10000 and tmp.vList[i].Vald[j] < 12000:
                size[0][2] += 1
            elif tmp.vList[i].Vald[j] >= 12000 and tmp.vList[i].Vald[j] < 14000:
                size[1][0] += 1
            elif tmp.vList[i].Vald[j] >= 14000 and tmp.vList[i].Vald[j] < 16000:
                size[1][1] += 1
            elif tmp.vList[i].Vald[j] >= 16000 and tmp.vList[i].Vald[j] < 18000:
                size[1][2] += 1
            elif tmp.vList[i].Vald[j] >= 18000 and tmp.vList[i].Vald[j] < 20000:
                size[1][3] += 1
    
    fDir.fList[-1].var = tmp.vList
    fDir.fList[-1].siz = size
    varRes()
    Memory.clear()
    VarT.vList=var
    GenQuad(('EndModule', None, None, None))
        

def flatcock(ty):
    for it in ty:
        if isinstance(it, Iterable) and not isinstance(it, str):
            for x in flatcock(it):
                yield x
        else:
            yield it

#main function
def p_mein(p):
    '''mein : MAIN pmain L_PAR R_PAR bloq''' #endm
    p[0] = p[1], p[2], p[3], p[4], p[5]

    #Sizee

def p_pmain(p) :
    '''pmain : '''
    nd = Stack.GoTo.pop()
    Quads.Quads[nd].Top = LineQ + 1
    StFun.append((None, p[-1]))


#bloque
def p_bloq(p):
    '''bloq : L_COR statbloq R_COR'''
    p[0] = p[1], p[2], p[3]

def p_statbloq(p):
    '''statbloq : estatuto statbloq
                | empty'''
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2]

def p_estatuto(p):
    '''estatuto : cond
                | whil
                | prin
                | asign
                | mcall
                | read
                | ret'''
    p[0] = p[1]

#>>>>>>>>>>>>>>>>DEVELOP<<<<<<<<<<<<<<<
def p_mcall(p):
    '''mcall : Mcall SEMICOLON'''
    p[0] = p[1], p[2]
#Function calls
def p_Mcall (p) :
    ''' Mcall : ID chkmod L_PAR era cparam parck R_PAR'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6],
    #Revisar si existe el ID en la función
#Parameters for Function calls
def p_chkmod(p):
    '''chkmod : '''
    global fn
    fn = search(p[-1], 'mod')
    if not fn:
        print("Error, el Modulo \"%s\" no está declarado" %p[-1])
        quit()
    #print (fn)
def p_era(p):
    '''era : '''
    global fn
    GenQuad(('ERA', fn.ID, None, fn.siz))
    f = fn.siz
    if f :
        f = fn.siz[0]
        for j in range(len(f)):
            if j == 0:
                add = Memory.GString[0] + Memory.Lint[1]
                if (add > Memory.Lint[0]):
                    print ("Exceso de memoria Local INT")
                    quit()
                Memory.Lint[1] += f[j]
            elif j == 1:
                add = Memory.Lint[0] + Memory.Lfloat[1]
                if (add > Memory.Lfloat[0]):
                        print ("Exceso de memoria Local INT")
                        quit()
                Memory.Lfloat[1] += f[j]
                    
            elif j == 2:
                add = Memory.Lfloat[0] + Memory.LString[1]
                if (add > Memory.LString[0]):
                        print ("Exceso de memoria Local INT")
                        quit()
                Memory.LString[1] += f[j]
        f = fn.siz[1]
        for j in range(len(f)):
            if j == 0:
                for k in range(f[j]):
                    add = Memory.LString[0] + Memory.Tint[1]
                    if (add > Memory.Tint[0]):
                        print ("Exceso de memoria Temporal INT")
                        quit()
                    cT('int', [add])
                    Memory.Tint[1] += 1
            elif j == 1:
                for k in range(f[j]):
                    add = Memory.Tint[0] + Memory.Tfloat[1]
                    if (add > Memory.Tfloat[0]):
                            print ("Exceso de memoria Temporal Float")
                            quit()
                    cT('float', [add])
                    Memory.Tfloat[1] += 1
                    
            elif j == 2:
                for k in range(f[j]):
                    add = Memory.Tfloat[0] + Memory.Tstring[1]
                    if (add > Memory.Tstring[0]):
                            print ("Exceso de memoria Temporal CHAR")
                            quit()
                    cT('char', [add])
                    Memory.Tstring[1] += 1
            elif j == 3:
                for k in range(f[j]):
                    add = Memory.Tstring[0] + Memory.Tbool[1]
                    if (add > Memory.Tbool[0]):
                            print ("Exceso de memoria Temporal BOOL")
                            quit()
                    cT('bool', [add])
                    Memory.Tbool[1] += 1
    tem.append(Memory.Tbool[1])
def cT(typ, add):
    new = Vobj('temp', typ, add, [1], 0)
    VarT.Add(new)

def p_cparam(p) :
    ''' cparam : expres cxparam
               | empty'''
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2]
    #Revisar si el número de parametros total es correcto
    #Revisar si el tipo de parametro es correcto

def p_cxparam (p) :
    '''cxparam : COMMA expres cxparam
               | empty'''
    #print("Stacks")
    #print(Stack.Sy , Stack.Ty)
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2], p[3]

def p_parck(p):
    '''parck : '''
    global fn
    par = p[-1]
    #print (par)
    if par == None:
        if fn.val == None:
            GenQuad(('Gosub', fn.ID, None, fn.st))
            fn = False
            return
        else:
            print("Error, No hay argumentos, se necesitan: \"%s\" argumentos" %len(fn.val))
            quit()
    li = list(flatcock(par))
    si = len(li)
    ls = []
    #print(li)
    for i in range(si):
        if li[i]== None:
            ls.append(li[i])
    li = [ID for ID in li if ID not in ls]
    ls = []
    ty = []
    for i in range(len(li)):
        if li[i] != ',':
            ty.append(li[i])
        else :
            ls.append(ty)
            ty = []
    if ty :
        ls.append(ty)
    ty = []    
    if len(ls) != len(fn.val):
        print("Número de argumentos erroneo. Necesita \"%s\" se ingresaron \"%s\"" %(len(fn.val), len(li)))
        quit()
    
    ty = [(Stack.Ty.pop(), Stack.Sy.pop()) for i in range(len(ls))]
    ty.reverse()
    #print(fn.ID, fn.Type)
    #print(fn.var)
    #print(fn.val)
    #print(fn.st, fn.siz)
    #ty => (type [], (Value, address))
    #fn.val => (ID, Type, Address)
    for i in range(len(ty)):
        Semcube.validate(fn.val[i][1], ty[i][0], '=') 
        GenQuad(('Param', ty[i][1][1], None, fn.val[i][2][0]))
    GenQuad(('Gosub', fn.ID, None, fn.st))
    #print (VarT.vList[-1].Vald[0])
    dir = tem.pop()
    GenQuad(('=', fn.st, None, dir))
    #Stack.GoTo.append(LineQ)
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<CONTINUE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        
#>>>>>>>>>>>>>>>>DONE<<<<<<<<<<<<<<<
#Conditional
def p_cond(p):
    '''cond : IF L_PAR expres conval R_PAR THEN bloq condex conf SEMICOLON'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10]
    #Check express if bool

def p_conval(p):
    '''conval : '''
    ty = Stack.Ty.pop()
    if (ty != 'bool'):
        print("error, necesita ser un Booleano y se agrego: \"%s\"" %Stack.Sy[-1])
        quit()
    else:
        sy = Stack.Sy.pop()
        GenQuad(('GoToF', sy[1], None, None))
        #print (Quads.Quads[-1])
        Stack.GoTo.append(LineQ)

def p_conf(p):
    '''conf : '''
    nd = Stack.GoTo.pop()
    Quads.Quads[nd].Top = LineQ + 1
    #print(Quads.Quads[nd])

def p_condex(p):
    '''condex : ELSE jum bloq
              | empty'''
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2], p[3]
    #GoToF

def p_jum(p):
    '''jum : '''
    GenQuad(('GoTo', None, None, None))
    nd = Stack.GoTo.pop()
    #print(Quads.Quads[-1])
    Stack.GoTo.append(LineQ)
    Quads.Quads[nd].Top = LineQ + 1
    #print(Quads.Quads[nd])

#Ciclo While
def p_whil(p):
    '''whil : WHILE L_PAR wju expres conval R_PAR DO bloq back'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]

def p_wju(p):
    '''wju : '''
    Stack.GoTo.append(LineQ + 1)
    #print(Stack.GoTo[-1])

def p_back(p):
    '''back : '''
    nd = Stack.GoTo.pop()
    bk = Stack.GoTo.pop()
    GenQuad(('GoTo', None, None, bk))
    #print (Quads.Quads[-1])
    Quads.Quads[nd].Top = LineQ + 1
    #print(Quads.Quads[-1])

#<<<<<<<<<<<<<<<<DONE>>>>>>>>>>>>>>>>>>
#Write
def p_prin(p):
    '''prin : PRINT L_PAR str ptr R_PAR SEMICOLON'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]

def p_ptr(p):
    '''ptr : COMMA str ptr
           | empty'''
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2], p[3]

def p_str(p):
    '''str : expres
            | CTES'''
    p[0] = p[1]
    if(Stack.Sy):
        po=Stack.Sy.pop()
        #print(po[1])
        GenQuad(('Print', po[1], None, None))
        #print(Quads.Quads[-1])
        po=Stack.Ty.pop()
    else:
        GenQuad(('Print', p[1], None, None))
        #print(Quads.Quads[-1])

#>>>>>>>>>>>>>>>DONE?<<<<<<<<<<<<<<<<<<
#Read
def p_read(p):
    '''read : READ COLON variable SEMICOLON'''
    global curr_var
    #print(curr_var.Vald)
    dir = curr_var.Vald[0]
    GenQuad(('Read', None, None, dir))
    #print(Stack.Ty, Stack.Sy)
    if(Stack.Sy and Stack.Ty):
        Stack.Sy.pop()
        Stack.Ty.pop()


#<<<<<<<<<<<<<<<<DONE>>>>>>>>>>>>>>>>>>
#asign
def p_asign(p):
    '''asign : variable ASSIGN expres SEMICOLON'''
    p[0] = p[1], p[2], p[3], p[4]
    #print(curr_var)
    Stack.Op.append(p[2])
    validate()
    

#Arreglo []
def p_variable(p):
    '''variable : ID ch arr va'''
    p[0] = p[1], p[2], p[3], p[4]

#Arreglo []
def p_arr(p):
    '''arr : L_SQ dim R_SQ
           | empty'''
    if p[1] == None:
        p[0] = p[1]
        #Busca si la variable p[-1] existe
        global curr_var
        ro = curr_var.Arr
        #print("Print", curr_var)
        if (ro[0] > 1):
            print("La variable \"%s\" es un arreglo favor de poner la dirección de memoria" %curr_var.ID)
            quit()
    else:
         p[0] = p[1], p[2], p[3]
         #busca si la variable p[-2] existe y es arreglo
    #print(Stack.Sy , Stack.Ty)
def p_dim(p) :
    '''dim : expres mar'''
    p[0] = p[1]

def p_mar(p) :
    '''mar : DOT expres
           | empty'''
    global curr_var
    j = search(p[-4], 'var')
    ro = j.Arr
    #print(Stack.Sy , Stack.Ty)
    #print(ro, curr_var)
    if p[1] == None:
        p[0] = p[1]
        if(ro[0] == 1):
            print("Error, la variable \"%s\" no es un arreglo" %j.ID)
            quit()
        ty = Stack.Ty.pop()
        si = Stack.Sy.pop()
        if(ty != 'int'):
            print("Error, la variable \"%s\" se ingreso \"%s\" equivale a un \"%s\" necesita un INT" %(j.ID, si[0], ty))
            quit()
        if(si[0] < 0):
            print("Error, las variables del arreglo solo pueden positivas")
            quit()

        if(si[0] > (ro[0]- 1)):
            print("Error, la variable \"%s\" excede las dimensiones, ingreso \"%s\" necesita \"%s\"" %(j.ID, si[0], ro[0]-1))
            quit()
        jump = si
        Stack.dim.append(jump)
        #di= (si[0]-1) + curr_var.Vald
        #curr_var.Vald = di
        #Verifica p[-1] la dimension
    else:
        p[0] = p[1], p[2]
        tym= Stack.Ty.pop()
        sim= Stack.Sy.pop()

        tyr= Stack.Ty.pop()
        sir= Stack.Sy.pop()
        if(len(ro)== 1):
            print("Error, la variable \"%s\" no es una matriz" %j.ID)
            quit()
        if(sim[0] < 0 or sir[0] < 0 ):
            print("Error, las variables del arreglo solo pueden positivas")
            quit()

        if(sim[0] > (ro[1] -1)):
            print("Error, la variable \"%s\" excede el limite ingreso \"%s\" tamaño máximo es \"%s\"" %(j.ID, sim[0], ro[1]-1))
            quit()
        if(sir[0] > (ro[0] -1)):
            print("Error, la variable \"%s\" excede el limite ingreso \"%s\" tamaño máximo es \"%s\"" %(j.ID, sir[0], ro[0]-1))
            quit()
        if(tym != 'int'):
            print("Error, la variable \"%s\" se ingreso \"%s\" equivale a un \"%s\" necesita un INT" %(j.ID, sim[0], tym))
            quit()
        if(tyr != 'int'):
            print("Error, la variable \"%s\" se ingreso \"%s\" equivale a un \"%s\" necesita un INT" %(j.ID, sir[0], tyr))
            quit()
        jump = sir[0] + (sim[0]*j.Arr[0])
        Stack.dim.append((j, jump))
        #print("Stack", Stack.dim)
        #di= ((sir[0]*sim[0])-1) + curr_var.Vald
        #print(di)
        #curr_var.Vald = di

#Expressions
def p_expres(p):
    '''expres : contr c'''
    p[0] = p[1], p[2]

#AND OR
def p_c(p):
    '''c : con contr c
         | empty'''
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2], p[3]
        validate()
def p_con(p):
    '''con : AND
           | OR'''
    p[0] = p[1]
    Stack.Op.append(p[1])

#conditionals
def p_contr(p):
    ''' contr : exp cn'''
    p[0] = p[1], p[2]

def p_cn(p):
    '''cn : cont exp cn
         | empty'''
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2], p[3]
        validate()

def p_cont(p):
    '''cont : EQUALS
            | EQUAL_MAJOR
            | EQUAL_MINOR
            | LESS_THAN
            | MORE_THAN
            | NOT'''
    p[0] = p[1]
    Stack.Op.append(p[1])

def p_exp(p):
    '''exp : term t'''
    p[0] = p[1], p[2]
#sum
def p_t(p):
    '''t : opt term t
         | empty'''
    if p[1] == None:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2], p[3]
        validate()

def p_Un(p):
    '''Un : ADD 
        | DEC'''
    p[0] = p[1]


def p_opt(p):
    ''' opt : PLUS
            | MINUS'''
    p[0] = p[1]
    Stack.Op.append(p[1])

#Mult
def p_term(p):
    '''term : fact f'''
    p[0] = p[1], p[2]

def p_f(p):
    '''f : fopt fact f
         | empty'''
    if p[1] == None:
            p[0] = p[1]
    else:
            p[0] = p[1], p[2], p[3]
            #validate
            validate()
            
def p_fopt(p):
    '''fopt : MULT
            | DIV'''
    p[0] = p[1]
    Stack.Op.append(p[1])

#Operations Parentesis
def p_fact(p):
    '''fact : L_PAR expres R_PAR
              | sign varcte'''
    if len(p) == 3:
        p[0] = p[1], p[2]
        #print("oper")
        #print(Stack.Sy, Stack.Ty, Stack.Op)
        if p[1] == '+':
            ty = 'int'
            cdir= cte(1, ty)
            Stack.Op.pop()
            Stack.Op.append('*')
            Stack.Ty.append(ty)
            Stack.Sy.append((1, cdir))
            validate()
        if p[1] == '-':
            ty = 'int'
            cdir= cte(-1, ty)
            Stack.Op.pop()
            Stack.Op.append('*')
            Stack.Ty.append(ty)
            Stack.Sy.append((-1, cdir))
            validate()
        if p[1] == '--':
            ty = 'int'
            cdir= cte(1, ty)
            Stack.Op.append('-')
            Stack.Ty.append(ty)
            Stack.Sy.append((1, cdir))
            validate()
        if p[1] == '++':
            ty = 'int'
            cdir= cte(1, ty)
            Stack.Op.append('+')
            Stack.Ty.append(ty)
            Stack.Sy.append((1, cdir))
            validate()
    else:
        p[0] = p[1], p[2]
        #hacer stack
####UNARY#####
#>>>>>>>>>>>>>>>>>>>>>>DEVELOP<<<<<<<<<<<<<<<<<<
def p_sign(p):
    '''sign : opt
            | Un
            | empty'''
    p[0] = p[1]

#variables
def p_varcte(p):
    '''varcte : ID ch arr va
              | CTEC apC
              | CTES apS
              | CTEI apI
              | CTEF apF
              | Mcall call'''
    if len(p) > 3:
        p[0] = p[1], p[2], p[3], p[4]
    else:
        p[0] = p[1], p[2]
    #print (p[1])
    #if ID not found error
    #Search CTE, if don't to memory

def p_call(p):
    '''call : '''
    r = Quads.Quads[-2].Lop
    ret = search(r, 'var')
    Stack.Ty.append(ret.Type)
    Stack.Sy.append((0 , ret.Vald[0]))
    #print(Stack.Sy[-1])


def p_ch(p):
    '''ch : '''
    global curr_var
    id = p[-1]
    res = search(id, 'var')
    if (res):
        #print("Go to memory \"%s\"" % res.Vald)
        curr_var = res
    else:
        print("Error variable \"%s\" no declarada" %id)
        quit()
def p_va(p):
    '''va : '''
    global curr_var
    #print (curr_var.val, curr_var.Type)
    #print(curr_var)
    #print(jump)
    #print("print stack", curr_var.val)
    #print(curr_var)
    if Stack.dim:
        j = Stack.dim.pop()
        #print("Print value", j[0].Type, j[1])
        Stack.Ty.append(j[0].Type)
        Stack.Sy.append((j[0].val, j[0].Vald[j[1]]))
    else:
        Stack.Ty.append(curr_var.Type)
        Stack.Sy.append((curr_var.val, curr_var.Vald[0]))
    #print(Stack.Sy[-1])

def p_apC(p):
    '''apC : '''
    sym = p[-1]
    ty = 'char'
    cdir = cte (sym, ty)
    Stack.Ty.append(ty)
    Stack.Sy.append((sym, cdir))
def p_apS(p):
    '''apS : '''
    sym = p[-1]
    ty = 'char'
    cdir=cte (sym, ty)
    Stack.Ty.append(ty)
    Stack.Sy.append((sym,cdir))
def p_apI(p):
    '''apI : '''
    sym = p[-1]
    ty = 'int'
    cdir= cte(sym, ty)
    #print(cdir, sym)
    Stack.Ty.append(ty)
    Stack.Sy.append((sym, cdir))
def p_apF(p):
    '''apF : '''
    sym = p[-1]
    ty = 'float'
    cdir=cte (sym, ty)
    Stack.Ty.append(ty)
    Stack.Sy.append((sym,cdir))

def cte(p, t):
    check = search(p, 'cte')
    #print (p, t)
    if (check) :
        return check.Vald
    else : 
        if t == 'int':
            add = Memory.Tbool[0] + Memory.CTEi[1]
            if (add < Memory.CTEi[0]):
                const (p, add)                
                #print("\"%s\" Sent To address: %s " % (p, add))
                Memory.CTEi[1] += 1
                if (add > Memory.CTEi[0]):
                    print ("Exceso de memoria Constantes INT")
                    quit()
                return add
        if t == 'float':
            add = Memory.CTEi[0] + Memory.CTEf[1]
            if (add < Memory.CTEf[0]):
                const (p, add)
                #print("\"%s\" Sent To address: %s " % (p, add))
                Memory.CTEf[1] += 1
                if (add >= Memory.CTEf[0]):
                    print ("Exceso de memoria Constantes FLOAT")
                    quit()
                return add
        if t == 'char':
            add = Memory.CTEf[0] + Memory.CTES[1]
            if (add < Memory.CTES[0]):
                const (p, add)
                #print("\"%s\" Sent To address: %s " % (p, add))
                Memory.CTES[1] += 1
                if (add >= Memory.CTES[0]):
                    print ("Exceso de memoria Constantes CHAR")
                    quit()
                return add

def const(con, add):
    new = CTEO(con, add)
    Cons.Add(new)

def validate():
    op = Stack.Op.pop()
    rigT = Stack.Ty.pop()
    lefT = Stack.Ty.pop()
    #print (lefT, op, rigT)
    TemT = Semcube.validate(lefT, rigT, op) 
    if (op != '='):
        Stack.Ty.append(TemT)
        der = Stack.Sy.pop()
        iz = Stack.Sy.pop()
        temV = oper(op, iz[0], der[0]) #Manda el valor temporal
        #print(temV)
        tdir = temp(temV, TemT)#Manda la Dirección Temporal
        Stack.Sy.append((temV, tdir))
        GenQuad((op, iz[1], der[1], tdir))
        #print (Quads.Quads[-1])
    if (op == '='):
        global curr_var
        res = Stack.Sy.pop()
        rat = Stack.Sy.pop()
        #print(rat)
        #print(res, rat[1])
        #print(curr_var)
        curr_var = search(rat[1], 'dir')
        #print("rat var", curr_var)
        if curr_var.val :
            curr_var.val= res[0]
        #print(curr_var.Vald)
        GenQuad((op,res[1], None, rat[1]))
        #print (Quads.Quads[-1])
        #print (curr_var.ID, "=", curr_var.val)

def consT(con, add, tip):
    new = Vobj('temp', tip, add, [1], con)
    VarT.Add(new)
def temp(v, T):
    if T == 'int':
        add = Memory.LString[0] + Memory.Tint[1]
        if (add < Memory.Tint[0]):
            consT (v, [add], T)                
            #print("\"%s\" Sent To address: %s " %(v, add))
            Memory.Tint[1] += 1
            if (add > Memory.Tint[0]):
                print ("Exceso de memoria Temporal INT")
                quit()
            return add
    if T == 'float':
        add = Memory.Tint[0] + Memory.Tfloat[1]
        if (add < Memory.Tfloat[0]):
            consT (v, [add], T)
            #print("\"%s\" Sent To address: %s " %(v, add))
            Memory.Tfloat[1] += 1
            if (add >= Memory.Tfloat[0]):
                print ("Exceso de memoria Temporal Float")
                quit()
            return add
    if T == 'char':
        add = Memory.Tfloat[0] + Memory.Tstring[1]
        if (add < Memory.Tstring[0]):
            consT (v, [add], T)
            #print("\"%s\" Sent To address: %s " % (v, add))
            Memory.Tstring[1] += 1
            if (add >= Memory.Tstring[0]):
                print ("Exceso de memoria Temporal Char")
                quit()
            return add
    if T == 'bool':
        add = Memory.Tstring[0] + Memory.Tbool[1]
        if (add < Memory.Tbool[0]):
            consT (v, [add], T)
            #print("\"%s\" Sent To address: %s " % (v, add))
            Memory.Tbool[1] += 1
            if (add >= Memory.Tbool[0]):
                print ("Exceso de memoria Temporal Bool")
                quit()
            return add
def oper(op, iz, der):
    if (op == '&'):
        tem = iz and der
    if (op == '|'):
        tem = iz or der
    elif (op == '<>'):
        tem = iz != der
    if (op == '=='):
        tem = iz == der
    elif (op == '<'):
        tem = iz < der
    elif (op == '>'):
        tem = iz > der
    elif (op == '<='):
        tem = iz <= der
    elif (op == '>='):
        tem = iz >= der
    elif (op == '+'):
        tem = iz + der
    elif (op == '-'):
        tem = iz - der
    elif (op == '*'):
        tem = iz * der
    elif (op == '/'):
        if (der == 0):
            print("Error: Div 0 ")
            quit()
        else:
            tem = iz / der
    #print(iz[0], op, der[0],"=", tem)
    return tem

#>>>>>>>>>>>>>>>DEVELOP<<<<<<<<<<<<<<<<<< 
#return
def p_ret(p):
    '''ret : RETURN expres SEMICOLON'''
    p[0] = p[1], p[2], p[3]
    global curr_vFu, fn
    #print(curr_vFu)
    ret = StFun.pop()
    #print (ret[0], "asdf")
    if ret[0] == 'VOID' or ret[0] == 'MAIN': #Revisar en el Stack si es una función Void
        print("No se puede dar un valor de retorno a está función:  \"%s\""  %ret)
        quit()
    val = Stack.Ty.pop()
    Semcube.validate(ret[0], val, p[1])
    val = Stack.Sy.pop()
    #print(val)
    GenQuad(('Return', None, None, val[1]))
    r = search(ret[1], 'var')
    GenQuad(('=', val[1], None, r.Vald[0]))
    GenQuad(('EndModule', None, None, None))
    #Mandar cuadruplo Return

    
def p_empty(p):
    '''empty : '''
    pass

def p_error(p):
    print("Error en grámatica, se agrego: %s ERROR {}".format(p) % ( p.value))
    quit()

parsing = yacc.yacc()

import json
def IwannaDie():
    dic = {}
    tmp = []
    for md in fDir.fList:
        #print(md)
        m = [md.ID, md.val, md.siz]
        tmp.append(m)
    dic['modules'] = tmp
    tmp = []
    for md in Cons.CTEL:
        #print(md)
        m = [md.ID, md.Vald]
        tmp.append(m)
    dic['constants'] = tmp
    tmp = []
    for md in Quads.Quads:
        #print(md)
        m = [md.op, md.Lop, md.Rop, md.Top]
        tmp.append(m)
    #print(tmp)
    dic['Quads'] = tmp

    with open('obj.json', 'w') as file:
        json.dump(dic, file)
