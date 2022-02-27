from sys import argv
print(argv)

variables = []
var_dict= {}

def isoperator(i):
    return True if i == '*' or i == '/' or i =='+' or i == '-' else False

def isquote(c):
    return True if "'" in c or '"' in c else False

def isbracket(c):
    return True if c == '(' or c == ')' else False

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def devide(a, b):
    return a / b

def mult(a, b):
    return a * b

def arithmetic(el, t):
    if '*' in el:
        ind = el.index('*')
        if ind != 0 and ind != len(el) - 1:
            if el[ind-1][0] == el[ind+1][0] == 'int' or el[ind-1][0] == el[ind+1][0] == 'float':
                el[ind - 1][1] *= el[ind + 1][1]
                el.pop(ind)
                el.pop(ind)
            elif el[ind-1][0] == 'int' and el[ind+1][0] == 'str' or el[ind-1][0] == 'str' and el[ind+1][0] == 'int':
                if el[ind-1][0] == 'int':
                    el[ind + 1][1] = mult(el[ind-1][1], el[ind+1][1])
                    el.pop(ind-1)
                    el.pop(ind-1)
                else:
                    el[ind - 1][1] = mult(el[ind-1][1], el[ind+1][1])
                    el.pop(ind)
                    el.pop(ind)
            else:
                print('TypeError')
                t = False
    elif '/' in el:
        ind = el.index('/')
        if ind != 0 and ind != len(el) - 1:
            if el[ind-1][0] == el[ind+1][0] == 'int' or el[ind-1][0] == el[ind+1][0] == 'float':
                el[ind - 1][1] /= el[ind + 1][1]
                el.pop(ind)
                el.pop(ind)
            else:
                print('TypeError')
                t = False
    elif '+' in el:
        ind = el.index('+')
        if ind == 0:
            el.pop(ind)
        elif ind == len(el):
            print('Arithmetic Syntax Error')
            t = False
        elif el[ind-1][0] == el[ind+1][0] == 'int' or el[ind-1][0] == el[ind+1][0] == 'float':
            el[ind - 1][1] += el[ind + 1][1]
            el.pop(ind)
            el.pop(ind)
        elif el[ind-1][0] == 'float' and el[ind+1][0] == 'int':
            el[ind - 1][1] += el[ind + 1][1]
            el.pop(ind)
            el.pop(ind)
        elif el[ind-1][0] == 'int' and el[ind+1][0] == 'float':
            el[ind + 1][1] = mult(el[ind-1][1], el[ind+1][1])
            el.pop(ind-1)
            el.pop(ind-1)
        elif el[ind-1][0] == el[ind+1][0] == 'str':
            el[ind - 1][1] += el[ind + 1][1]
            el.pop(ind)
            el.pop(ind)
        else:
            print('TypeError')
            t = False
                
    elif '-' in el:
        ind = el.index('-')
        if ind == 0:
            el[ind + 1][1] = -1 * el[ind + 1][1]
        elif ind == len(el):
            print('TypeError')
            t = False
        elif el[ind-1][0] == el[ind+1][0] == 'int' or el[ind-1][0] == el[ind+1][0] == 'float':
            el[ind - 1][1] -= el[ind + 1][1]
            el.pop(ind)
            el.pop(ind)
        else:
            print('TypeError')
            t = False
    return el, t
t = True
f = open('test.ry', mode='r', encoding='utf-8')
for line in f:
    el = []
    key = line.split(" ")
    key[-1] = key[-1].replace('\n', '')
    print(key)
    if key[0] == 'var':
        if line.split()[1].isalpha():
            if line.split()[2] == '=':
                el = []
                for c in range(key.index('=') + 1, len(key)):
                    if key[c] == '':
                        continue
                    elif isbracket(key[c]):
                        el.append(key[c])
                    elif key[c].isdigit():
                        el.append(['int', int(key[c])])        
                    elif isoperator(key[c]):
                        el.append(key[c])
                    elif key[c].isalpha():
                        if key[c] in var_dict.keys():
                            el.append(var_dict[key[c]])
                        else:
                            t = False
                            break
                    
                    elif isquote(key[c]):
                        start = 0
                        end = 0
                        if key[c][0] == "'" or key[c][0] == '"':
                            k = False
                            for i in key[c][1:]:
                                if key[c][0] == "'":
                                    if i == "'":
                                        end = key[c][1:].index("'")
                                        k = True
                                        if key[c][-1] == i:
                                            break
                                        else:
                                            k = False
                                            t = False
                                            break
                                else:
                                    if i == '"':
                                        end = key[c][1:].index('"')
                                        k = True
                                        if key[c][-1] == i:
                                            break
                                        else:
                                            k = False
                                            t = False
                                            break
                            if k:
                                el.append(['str', key[c][start+1:end+1]])
                            else:
                                print("String Error")
                                t = False
                                break
                    elif float(key[c]):
                        el.append(['float', float(key[c])])
                    else:
                        print('Error 1')
                        t = False
                        break
             
    elif key == ['']:
        continue
    elif key[0] == 'rprint(':
        if '(' in line:
            start_brac = line.index('(')
            if ')' in line:
                end_brac = line.index(')')
                if "'" in line.split() or '"' in line.split():
                    if "'" in line.split():
                        if "'" in line[line.split().index("'")+1:]:
                            start = line.split().index("'")
                            end = line.split()[start+1:].index("'")
                            print(line.split()[start + 1: end])
                    elif '"' in line.split():
                        if '"' in line.split()[line.index('"')+1:]:
                            start = line.split().index('"')
                            end = line.split()[start+1:].index('"')
                            print(line.split()[start + 1: end])
                elif line[start_brac + 1: end_brac].isalpha():
                    if line[start_brac + 1: end_brac] in var_dict.keys():
                        print(var_dict[line[start_brac + 1: end_brac]][1])
                        continue
                    else:
                        print('KeyError')
                        t = False
                        break
                elif '*' in line or '/' in line or '+' in line or '-' in line:
                    for i in line[start_brac + 1: end_brac].split():
                        if i.isdigit():
                            el.append(['int', int(i)])        
                        elif isoperator(i):
                            el.append(i)
                        elif i.isalpha():
                            if i in var_dict.keys():
                                el.append(var_dict[i])
                            else:
                                t = False
                        elif isquote(i):
                            el.append(['str', i[1: len(i) - 1]])
                    el, t = arithmetic(el, t)
                    print(el[0][1])
    elif key[0] == 'rif':
        tif = False
        if '==' in key[1:]:
            cond1 = key[1: key.index('==')]
            cond2 = key[key.index('==')+1:]
            if len(cond1) >  1:
                cond_1, t = arithmetic(cond1, t)
            elif cond1.isdigit() or float(cond1):
                cond_1 = float(cond1)
            if len(cond2) > 1:
                cond_2, t = arithmetic(cond2, t)
            elif cond2.isdigit() or float(cond2):
                cond_2 = float(cond2)
            if cond1 == cond2:
                tif = True
        elif '>=' in key[1:]:
            cond1 = key[1: key.index('==')]
            cond2 = key[key.index('==')+1:]
            if len(cond1) >  1:
                cond_1, t = arithmetic(cond1, t)
            elif cond1.isdigit() or float(cond1):
                cond_1 = float(cond1)
            if len(cond2) > 1:
                cond_2, t = arithmetic(cond2, t)
            elif cond2.isdigit() or float(cond2):
                cond_2 = float(cond2)
            if cond1 >= cond2:
                tif = True

        elif '<=' in key[1:]:
            cond1 = key[1: key.index('==')]
            cond2 = key[key.index('==')+1:]
            if len(cond1) >  1:
                cond_1, t = arithmetic(cond1, t)
            elif cond1.isdigit() or float(cond1):
                cond_1 = float(cond1)
            if len(cond2) > 1:
                cond_2, t = arithmetic(cond2, t)
            elif cond2.isdigit() or float(cond2):
                cond_2 = float(cond2)
            if cond1 <= cond2:
                tif = True

        elif '!=' in key[1:]:
            cond1 = key[1: key.index('==')]
            cond2 = key[key.index('==')+1:]
            if len(cond1) >  1:
                cond_1, t = arithmetic(cond1, t)
            elif cond1.isdigit() or float(cond1):
                cond_1 = float(cond1)
            if len(cond2) > 1:
                cond_2, t = arithmetic(cond2, t)
            elif cond2.isdigit() or float(cond2):
                cond_2 = float(cond2)
            if cond1 != cond2:
                tif = True
    
        elif '>' in key[1:]:
            cond1 = key[1: key.index('==')]
            cond2 = key[key.index('==')+1:]
            if len(cond1) >  1:
                cond_1, t = arithmetic(cond1, t)
            elif cond1.isdigit() or float(cond1):
                cond_1 = float(cond1)
            if len(cond2) > 1:
                cond_2, t = arithmetic(cond2, t)
            elif cond2.isdigit() or float(cond2):
                cond_2 = float(cond2)
            if cond1 > cond2:
                tif = True

        elif '<' in key[1:]:
            cond1 = key[1: key.index('==')]
            cond2 = key[key.index('==')+1:]
            if len(cond1) >  1:
                cond_1, t = arithmetic(cond1, t)
            elif cond1.isdigit() or float(cond1):
                cond_1 = float(cond1)
            if len(cond2) > 1:
                cond_2, t = arithmetic(cond2, t)
            elif cond2.isdigit() or float(cond2):
                cond_2 = float(cond2)
            if cond1 < cond2:
                tif = True
    
    #elif tif:
    
        
    elif not t:
        break
    else:    
        print("Syntax Error")
        break

    if len(el) > 1:
        while len(el) > 1:
            if '*' in line or '/' in line or '+' in line or '-' in el:
                el, t = arithmetic(el, t)
        if key[0] == 'var':
            var_dict[line.split()[1]] = el[0]
    elif len(el) == 1:
        if key[0] == 'var':    
            var_dict[line.split()[1]] = el[0]
    if not t:
        break

print(var_dict)

