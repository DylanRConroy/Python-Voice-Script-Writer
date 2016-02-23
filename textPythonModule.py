indent = 0

def camelCase(words):
    name = words[0]
    for i in range(1,len(words)):
    while(i < len(words)):
        upper = words[

def makeDefine(line):
    keyword = line.split(' ')
    nonKeyword = keyword[1:len(keyword)]
    defineLine = "def "
    
    return "blah"
##    i = 1
##    cur = []
##    originalname = ""
##    while (i < len(words)):
##        originalname = originalname = words[i]
##        cur.append(words[i])
##        i+=1
##    funName = camelCase(cur)
##    output.write("def "+ funName+"():")
##    functions[funName] = originalname
##    indent+=1
##    return indent

def makePrint(output, words, indent, variables):
    addIndent(output,indent)
    output.write("print(")
    i = 1
    while(i < len(words)):
        if(words[i] in variables.keys()):
            output.write(words[i])
        elif(i == len(words)-1):
            output.write("'"+words[i]+"'")
        else:
            output.write("'"+words[i]+" '+")
        i+=1
    output.write(")")
    return indent

def variable(output, words, indent, variables):
    addIndent(output, indent)
    i = 1
    cur = []
    originalname = ""
    while (words[i] != "equals"):
        originalname = originalname = words[i]
        cur.append(words[i])
        i+=1
    varName = camelCase(cur)
    variables[varName] = originalname
    output.write(varName)
    output.write(" = ")
    if (words[i+1] == "integer" or words[i+1] == "int" or words[i+1] == float):
        output.write(words[i+2])
    elif (words[i+1] == "array"):
        output.write("[]")
    elif (words[i+1] == "string"):
        output.write("'")
        while (i+2 < len(words)):
            if(i+2 == len(words)-1):
                output.write(words[i+2])
            else:
                output.write(words[i+2]+" ")
            i+=1
        output.write("'")
    return indent

def makeWhile(output, words, indent, variables):
    addIndent(output, indent)
    output.write(words[0]+" (")
    i = 1
    while (i < len(words)):
        if(words[i] in variables.keys()):
            output.write(words[i])
        elif(words[i] == "equals"):
            output.write(" == ")
        elif(words[i] == "is"):
            pass
        elif(words[i] == "greater"):
            output.write(" >")
            i+=2
            if (words[i] == "or"):
                output.write("= ")
                i+=2
            else:
                output.write(" ")
        elif (words[i] == "less"):
            output.write(" <")
            i+=2
            if (words[i] == "or"):
                output.write("= ")
                i+=2
            else:
                output.write(" ")
        elif(words[i] == "string"):
            i+=1
            output.write("'")
            while(i < len(words)):
                if(i == len(words)-1):
                    output.write(words[i])
                else:
                    output.write(words[i]+" ")
                i+=1
            output.write("'")
        else:
            output.write(words[i])
        i+=1
    output.write("):")
    indent+=1
    return indent

def makeFor(output, words, indent, variables):
    addIndent(output, indent)
    output.write(words[0]+" ")
    i = 1
    while (i < len(words)):
        # found = False
        # for item in variables.values():
        #     if(words[i] in item and found == False):
        #         output.write(item)
        #         found == True
        if(words[i] in variables.keys()):
            output.write(words[i])
        elif(words[i] == "in"):
            output.write(" "+words[i]+ " ")
        elif (words[i] == "range"):
            output.write(words[i]+" ")
            i +=1
            output.write("("+words[i])
            i+=1
            if(words[i] == "to"):
                i+=1
                output.write(" , "+words[i])
            output.write(")")
        elif(words[i] == "equals"):
            output.write(" == ")
        elif(words[i] == "is"):
            pass
        elif(words[i] == "greater"):
            output.write(" >")
            i+=2
            if (words[i] == "or"):
                output.write("= ")
                i+=2
            else:
                i -=1
                output.write(" ")
        elif (words[i] == "less"):
            output.write(" <")
            i+=2
            if (words[i] == "or"):
                output.write("= ")
                i+=2
            else:
                output.write(" ")
                i-=1
        elif(words[i] == "string"):
            i+=1
            output.write("'")
            while(i < len(words)):
                if(i == len(words)-1):
                    output.write(words[i])
                else:
                    output.write(words[i]+" ")
                i+=1
            output.write("'")
        else:
            output.write(words[i])
        i+=1
    output.write(":")
    indent+=1
    return indent

def makeIfElse(output, words, indent, variables):
    addIndent(output, indent)
    output.write(words[0]+" ")
    i = 1
    while (i < len(words)):
        if(words[i] in variables.keys()):
            output.write(words[i])
        elif(words[i] == "in"):
            output.write(" "+words[i]+ " ")
        elif (words[i] == "range"):
            output.write(words[i]+" ")
            i +=1
            output.write("("+words[i])
            i+=1
            if(words[i] == "to"):
                i+=1
                output.write(" , "+words[i])
            output.write(")")
        elif(words[i] == "equals"):
            output.write(" == ")
        elif(words[i] == "is"):
            pass
        elif(words[i] == "greater"):
            output.write(" >")
            i+=2
            if (words[i] == "or"):
                output.write("= ")
                i+=2
            else:
                i -=1
                output.write(" ")
        elif (words[i] == "less"):
            output.write(" <")
            i+=2
            if (words[i] == "or"):
                output.write("= ")
                i+=2
            else:
                output.write(" ")
                i-=1
        elif(words[i] == "string"):
            i+=1
            output.write("'")
            while(i < len(words)):
                if(i == len(words)-1):
                    output.write(words[i])
                else:
                    output.write(words[i]+" ")
                i+=1
            output.write("'")
        else:
            output.write(words[i])
        i+=1
    output.write(":")
    indent+=1
    return indent

def endFun(output, words, indent):
    if(words[1] == "loop"):
        indent -= 1
    elif(words[1] == "define"):
        indent = 0
    elif(words[1] == "if"):
        indent -=1
    elif(words[1] =="elif"):
        indent -=1
    elif(words[1] =="else"):
        indent -=1
    return indent

def addIndent(output,indent):
    while(indent > 0):
        output.write("\t")
        indent-=1;

def keywordChoose(line):
    keyword = line.split(' ')[0]
    pythonLine = ""
    for i in range(indent):
        pythonLine += "\t"
    if keyword == "define":
        pythonLine = makeDefine(line)
    return pythonLine
    
def textPython():
    text = open("input.txt",'r').read()
    outFile = open("output.py", 'w')
    lines = text.split("next line")
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    for line in lines:
        pythonLine = keywordChoose(line)
        outFile.write(pythonLine + "\n")

    outFile.write("main()")
    outFile.close()
    
##    for word in words:
##        if words[0] == "define" or words[0] == "def":
##            indent = define(output, words, indent, functions)
##        elif words[0] == "print":
##            indent = makePrint(output, words, indent, variables)
##
##        elif words[0] == "variable" or words[0] == "var":
##            indent = variable(output, words,indent,variables)
##
##
##        elif(words[0] == "while"):
##            indent = makeWhile(output, words, indent,variables)
##
##        elif(words[0] == "for"):
##            indent = makeFor(output, words, indent, variables)
##
##        elif(words[0] == "end"):
##            indent = endFun(output, words, indent)
##
##        elif(words[0] == "run"):
##            addIndent(output, indent)
##            outFile.write(words[1]+"()")
##
##        elif(words[0] == "increase" or words[0] == "decrease"):
##            addIndent(output, indent)
##            if(words[1] in variables.keys()):
##                output.write(words[1])
##            if(words[0] == "increase"):
##                output.write(" += ")
##            else:
##                output.write(" -= ")
##            outFile.write(words[3])
##
##        elif(words[0] == "if" or words[0] == "elif" or words[0] == "else"):
##            indent = makeIfElse(output, words, indent, variables)
##
##
##        output.write("\n")
##    outFile.write("\n")
    
