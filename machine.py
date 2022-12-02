import json
f = open('obj.json')
data = json.load(f)
mod= data['modules']
cons= data['constants']
quad = data['Quads']
memg = []
meml = []
memt = []
currt = []
mem = [[],[]]
def getval(add):
    ret = None
    if isinstance(add, str):
        return ret
    meg = memg
    mel = meml
    met = memt
    con = cons
    #meg.reverse()
    #mel.reverse()
    #met.reverse()
    if add >= 0 and add < 6000:
        for i in range(len(meg)):
            #print("get", memg[i])
            if add == meg[i][1]:
                #print("cond", memg[i])
                ret = meg[i][0]
                #print("ret", ret)
                return ret
    elif add >= 6000 and add < 12000:
        for i in range(len(mel)):
            if add == mel[i][1]:
                ret = mel[i][0]
                return ret
    elif add >= 12000 and add < 20000:
        for i in range(len(met)):
            if add == met[i][1]:
                ret = met[i][0]
                return ret
    elif add >= 20000 and add < 26000:
        for i in range(len(con)):
            if add == con[i][1]:
                #print(con[i])
                ret = con[i][0]
                return ret
    else:
        print("Error, la variable no tiene valor")
        quit()

#print(quad) 
def setval(val, add):
    global memg, meml, memt
    mg = len(memg)
    ml = len(meml)
    mt = len(memt)

    meg = memg
    mel = meml
    met = memt
    #print(meg)
    #print(mel)
    #print(met)

    #print(meg, mel, met)
    if add >= 0 and add < 6000:
       # print(memg)
        if memg :
            for i in range(mg):
                if add == meg[i][1]:
                    #print(memg)
                    temp = list(meg[i])
                    #print(meml[i])
                    #print(add, temp[0], val)
                    temp[0] = val
                    memg[i] = tuple(temp)
                    #print(memg[i])
                    return
            memg.append((val, add))
        else:
            memg.append((val, add))
    elif add >= 6000 and add < 12000:
        #print(meml)
        if meml :
            for i in range(ml):
                #print(mel)
                if add == mel[i][1]:
                    temp = list(meml[i])
                    #print(meml[i])
                    #print(add, temp[0], val)
                    temp[0] = val
                    meml[i] = tuple(temp)
                    #print(meml[i])
                    return
            meml.append((val, add))
        else:
            meml.append((val, add))
    elif add >= 12000 and add < 20000:
        if memt :
            #print(memt, 'for')
            for i in range(mt):
                #print(add, memt[i])
                if add == met[i][1]:
                    #print(memt[i], 'if')
                    temp = list(met[i])
                    #print(temp, 'temp')
                    #print(add, temp[0], val)
                    temp[0] = val
                    memt[i] = tuple(temp)
                    #print(memt[i], 'sum')
                    return
            memt.append((val, add))
        else:
            memt.append((val, add))
            #print(memt, 'No tuple')
            return

curr = [0]
dim = 0
def setmem(mem):
    global dim
    currt.append(mem)
    memg.append(memg.copy())
    meml.append(meml.copy())
    memg.append(memg.copy())
    dim +=1

def delmem():
    global dim
    currt.pop()
    memg.pop()
    meml.pop()
    memg.pop()
    dim -=1

#print(top)
while True:
    op = quad[curr[-1]][0]
    lop = quad[curr[-1]][1]
    rop = quad[curr[-1]][2]
    top = quad[curr[-1]][3]
    print(op, lop, rop, top)
    if op == 'GoToMain':
        curr[-1] = top
        #print(quad[curr])
    elif op == 'GoToF':
        if (getval(lop)):
            curr[-1] += 1
        else:
            curr[-1] = top
    elif op == 'GoTo':
        curr[-1] = top
    elif op == 'ERA' :
        #setmem(lop)
        curr[-1] += 1
    elif op == 'Param':
        val = getval(lop)
        #print(val)
        setval(val, top)
        curr[-1] += 1
    elif op == 'Gosub':
        curr[-1] += 1
        curr.append(top)
        #print(curr)
    elif op == 'Return':
        #print(op, lop, rop, top)
        val = getval(top)
        #print(val)
        setval(val, top)
        curr[-1] += 1
    elif op == 'EndModule':
        curr.pop()
    elif op == 'Print':
        val = getval(lop)
        #print("print", val)
        if val != None:
            #print("printval")
            print(val)
        else:
            #print("print lop")
            print(lop)
        curr[-1] += 1
    elif op == 'Read':
        res = input()
        if top >= 0 and top < 6000:
            res = int(res)
            setval(res, top)
        elif top >= 6000 and top < 12000:
            res = float(res)
        elif top >= 12000 and top < 20000:
            setval(res, top)
        curr[-1] += 1
    elif op == '=':
        val = getval(lop)
        #print(val)
        setval(val, top)
        curr[-1] += 1
    elif op == '+':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 + val2
        #print( val1, '+', val2, '=', val)
        add = top
        setval(val, add)
        curr[-1] += 1
    elif op == '-':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 - val2
        setval(val, top)
        curr[-1] += 1
    elif op == '*':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 * val2
        setval(val, top)
        curr[-1] += 1
    elif op == '/':
        val1 = getval(lop)
        val2 = getval(rop)
        if (val2 == 0):
            print("Error: Div 0 ")
            quit()
        else:
            val = val1 / val2
        #print(val1, val2, val)
        setval(val, top)
        curr[-1] += 1
    elif op == '|':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 or val2
        setval(val, top)
        curr[-1] += 1
    elif op == '&':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 and val2
        setval(val, top)
        curr[-1] += 1
    elif op == '>':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 > val2
        setval(val, top)
        curr[-1] += 1
    elif op == '<':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 < val2
        setval(val, top)
        curr[-1] += 1
    elif op == '>=':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 >= val2
        setval(val, top)
        curr[-1] += 1
    elif op == '<=':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 <= val2
        setval(val, top)
        curr[-1] += 1
    elif op == '==':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 == val2
        setval(val, top)
        curr[-1] += 1
    elif op == '!=':
        val1 = getval(lop)
        val2 = getval(rop)
        val = val1 != val2
        setval(val, top)
        curr[-1] += 1
    
    elif op == 'END':
        print("Fin del programa")
        break
    #print (memg)
    #print (meml)
    #print (memt)

