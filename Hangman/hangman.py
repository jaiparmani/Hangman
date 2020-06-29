from random import choice
import random
from Words import listOfWords
class mainLogic:
    def get_word():

        return random.choice(listOfWords)
    def main():
        # print(obj.get_word())
        word = obj.get_word()
        guessedWord=[]
        notGuessed = list(word)
        for i in word:
            guessedWord+='_'
        turns = 1
        answeredCorrectly = False
        while(turns<=10 and (not(answeredCorrectly))):
            print("Word:", end='')
            for i in guessedWord:
                print(i, end='')

            a = input("\nGuess a letter:")
            flag = False
            for i in range(len(notGuessed)):
                if(a == notGuessed[i]):
                    guessedWord[i] = a
                    notGuessed[i] = '*'
                    flag = True
                    break
            if('_' not in guessedWord):
                answeredCorrectly = True
            if(not flag):
                print('Turn wasted. Left Attempts:', (10-turns))

            turns+=1
        if(answeredCorrectly):
            print("Well Done! The word was '", word,"'")
        else:
            print("Try Again Later!")
        global wannaPlay
        wannaPlay = int(input("Enter 1 to play again else 0."))




global wannaPlay
wannaPlay = 1
obj = mainLogic
if __name__ == '__main__':
    print("Welcome to hangman")
    print(' __')
    print('|  |')
    print('|  o')
    print('|  |')
    print('|  /\\')
    print('|')


    while(wannaPlay):
        obj.main()
