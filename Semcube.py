#Agregar <> y =
Semcube = {
    #Variable INT
    "int" : {
        "int" : {
            "*": "int",
            "/": "float",
            "+": "int",
            "-": "int",
            ">": "bool",
            "<": "bool",
            "<=": "bool",
            ">=": "bool",
            "==": "bool",
            "!=": "bool",
            "&": "ERR",
            "|": "ERR",
            "=" : "int",
            "RETURN" : "int"
        },
        "float": {
            "*": "float",
            "/": "float",
            "+": "float",
            "-": "float",
            ">": "bool",
            "<": "bool",
            "<=": "bool",
            ">=": "bool",
            "==": "bool",
            "!=": "bool",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        },
        "char": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        },
        "bool": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        }
    },
    #Variable Float
    "float" : {
        "int" : {
            "*": "float",
            "/": "float",
            "+": "float",
            "-": "float",
            ">": "bool",
            "<": "bool",
            "<=": "bool",
            ">=": "bool",
            "==": "bool",
            "!=": "bool",
            "&": "ERR",
            "|": "ERR",
            "=" : "float",
            "RETURN" : "float"
        },
        "float": {
            "*": "float",
            "/": "float",
            "+": "float",
            "-": "float",
            ">": "bool",
            "<": "bool",
            "<=": "bool",
            ">=": "bool",
            "==": "bool",
            "!=": "bool",
            "&": "ERR",
            "|": "ERR",
            "=" : "float",
            "RETURN" : "float"
        },
        "char": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        },
        "bool": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        }
    },
    #variable Char
    "char" : {
        "int" : {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        },
        "float": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        },
        "char": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "bool",
            "!=": "bool",
            "&": "ERR",
            "|": "ERR",
            "=" : "char",
            "RETURN" : "char"
        },
        "bool": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        }
    },
    #variable Bool
     "bool" : {
        "int" : {
            "*": "ERR",
            "/": "ERR",
            "+": "string",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        },
        "float": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        },
        "string": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "ERR",
            "!=": "ERR",
            "&": "ERR",
            "|": "ERR",
            "=" : "ERR",
            "RETURN" : "ERROR"
        },
        "bool": {
            "*": "ERR",
            "/": "ERR",
            "+": "ERR",
            "-": "ERR",
            ">": "ERR",
            "<": "ERR",
            "<=": "ERR",
            ">=": "ERR",
            "==": "bool",
            "!=": "bool",
            "&": "bool",
            "|": "bool",
            "=" : "bool",
            "RETURN" : "bool"
        }
    }
}

def validate(lefty, righty, op):
    if "ERR" not in Semcube[lefty][righty][op]:
        return Semcube[lefty][righty][op]
    if Semcube[lefty][righty][op] == "ERROR":
        print("Caracteres invalidos: No corresponden al mismo tipo de elemento \"%s\" y \"%s\""  %(righty, lefty))
        quit()
    print ("Caracteres invalidos: Elementos no son compatibles \"%s\" y \"%s\""  % (righty, lefty))
    quit()