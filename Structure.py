#César Cisneros A01152861
#Aquí se irán guardando los objetos que se utilizaran para el compilador, este puede deshacerse y hacer cada uno de estos un objeto diferente para mantener más consistente
#Como establece la librería de Python __repr__ nos sirve para escribir una representación del objeto dado. 

class Vobj: #Se guardan los valores de cada uno de los elementos del programa.
    def __init__(self, ID, Type, Vald, Arr, val):
        self.ID = ID  #Guarda el nombre
        self.Type = Type #El tipo de Variable
        self.Vald = Vald # manda a una dirección de memoria
        #En caso de ser un arreglo
        self.Arr = Arr #Describe el tamaño del arreglo
        self.val = val #Machete

    def __repr__(self):
        return f'({self.ID}, {self.Type}, {self.Vald}, {self.Arr})'

class varTable: #Tabla de variables se almacenan los objetos cuando se almacena una nueva variable
    def __init__(self):
        self.vList = []
    def Add(self, value):
        self.vList.append(value)
    def peek(self) :
        if self.vList :
            return self.vList[-1]
    def __repr__(self):
       return f'({self.vList})'
    

class CTEO:  #Se gurdan los valores de las constantes 
    def __init__(self, ID, Vald):
        self.ID = ID #Nombre
        self.Vald = Vald #Dirección
    def __repr__(self):
       return f'({self.ID}, {self.Vald})'

class CTET: #Tabla para las constantes
    def __init__(self):
        self.CTEL= [] #crea instancia de la lista
    def Add(self, value):
        self.CTEL.append(value) #Agrega elementos a la lista
    def peek(self) :
        if self.CTEL :
            return self.CTEL[-1]


class Fobj: #Se Guardan los elementos de entrada en la direccion de una función
    def __init__ (self, ID, Type, var, val, st, siz):
        self.ID = ID
        self.Type = Type
        #En caso de ser un arreglo
        self.var = var #Las variables que maneja el modulo
        self.val = val #Valores del modulo
        self.st = st #Donde empieza el modulo
        self.siz = siz #Tamaño
    
    def __repr__(self):
        return f'({self.ID}, {self.Type},{self.var}, {self.val},{self.st}, {self.siz})'

class Fdir: #Guarda el directorio de las funciones o modulos
    def __init__(self):
        self.fList = []
    def add(self, val):
        self.fList.append(val)
    def peek(self) :
        if self.fList :
            return self.fList[-1]


class Quad: #Este es para generar un analisis por cuadruplos como nos enseñaron en la clase
    def __init__(self, op, Lop, Rop, Top)  :
        self.op = op #Operando
        self.Lop = Lop  #Elemento Izquierda
        self.Rop = Rop  #Elemento Derecha
        self.Top = Top  #Temporal o elemento para respuesta
    #Cada función regresa el operando del cuadruplo
    def getOp(self):
        return self.op
    def getLop(self):
        return self.Lop
    def getRop(self):
        return self.Rop
    def getTop(self):
        return self.Top
    def connon(self, val):
        if val== None:
            return None
        return val
    #imprime los contenidos del cuadruplo
    def __repr__(self):
        return f'({self.op}, {self.Lop}, {self.Rop}, {self.Top}) \n'

class QuadL: #Crea la lista para los cuadruplos
    def __init__(self):
        self.Quads = []
    def Add(self, Quad):
        self.Quads.append(Quad)
    def peek(self) :
        if self.Quads :
            return self.Quads[-1]
    


class Steak: #se Guardan los objetos para hacer un contenido similar al vector polaco junto con el uso de los cuadruplos
    def __init__ (self):
        self.Op = [] # Se guarda el operador
        self.Sy = [] # Se Guarda el Simbolo
        self.Ty = [] # Guarda los tipos de elementos
        self.GoTo = [] # Se hace el GoTo para cuando tengamos una función que nos envíe a otro lado
        self.dim = [] #se guardan las dimensiones para los arreglos

class Mem: #Se especifica la memoria del programa
    def __init__ (self):
        #Globales
        self.Gint = [2000, 0]
        self.Gfloat = [4000, 0]
        self.GString = [6000, 0]
        #Locales
        self.Lint = [8000, 0]
        self.Lfloat = [10000, 0]
        self.LString = [12000, 0]
        #Temporales
        self.Tint = [14000, 0]
        self.Tfloat = [16000, 0]
        self.Tstring = [18000, 0]
        self.Tbool = [20000, 0]
        #Constantes
        self.CTEi = [22000, 0]
        self.CTEf = [24000, 0]
        self.CTES = [26000, 0]

        

    def clear(self):
        #Locales
        self.Lint[1] = 0
        self.Lfloat[1] = 0 
        self.LString[1] = 0
        #Temporales
        self.Tint[1] = 0
        self.Tfloat [1] = 0
        self.Tstring [1] = 0
        self.Tbool[1] = 0
