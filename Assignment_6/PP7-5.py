
def main():
    filename = input("Please input your file name: ")
    ins = open(filename, "r")
    lines = 0
    words = 0
    characters = 0
    for line in ins:
        lines += 1
        lineList = line.split(" ")
        words += len(lineList)
        for c in line:
            if str(c).isalpha():
                characters += 1
    
    print(f"Lines: {lines}\nWords: {words}\nCharacters: {characters}")

main()