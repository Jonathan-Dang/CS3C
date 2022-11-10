from sys import argv

def main():
    files = []
    word = ""
    for arg in argv[1:]:
        if arg.count('.') == 0 and len(word) == 0:
            word = arg
        elif arg.count('.') > 0:
            files.append(arg)
    
    openfiles = []
    try:
        if len(word) == 0 or word.isspace():
            raise SyntaxError("No target word input")
        
        for file in files:
            openfiles.append(open(file,"r"))
            
        for openFile in openfiles:
            for line in openFile:
                lineList = line.split(' ')
                if lineList.count(word) >= 1:
                    print(openFile.name + ": " + line, end = '')
    except Exception as e:
        if e == SyntaxError:
            usage()
        print ("Error: " + str(e))
        return
    finally:
        for openFile in openfiles:
            openFile.close()

def usage():
    print("Usage: py find.py {word} {List of inputs}")



main()
