def codeBeale(code, key):
    codeList = [""]
    codeList = []
    codeList = code.split(",")
    result = ""
    for i in codeList:
        result += key[int(i)-1]
    print(result)