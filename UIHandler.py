########## DECODE FUNCTIONS ##########
class Decoder:
    def askForCode():
        return input("Please input code.")
    def askForKey():
        return input("Please input key.")
    def isCodeValid(code):
        if code.isnum():
            return True
        else:
            return False
    def userDecodeStyle():
        print('''How do you want to have the code decoded?
        1 = Each letter's number is associated with the first letter of a word in the key
        2 = Each letter's number is associated with a charactor in the key''')
        answer = input()
        if answer == "1" or answer == "2":
            return answer
