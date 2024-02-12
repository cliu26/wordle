from random import *
from Phyme import Phyme
import time
import sys

import subprocess
import sys

exwords = ["judge","strip","aside","bound","depth","candy","event","worse","aware",
        "shell","ranch","image","snake","aloud","dried","motor","chain","shirt","flour",
        "orbit","pound","curve","refer","tribe","tight","blind","slept","shade","claim",
        "theme","queen","fifth","seven","union","hence","straw","entry","issue","birth",
        "anger","brief","rhyme","glory","guard","fresh","trick","width","burst","route","uncle",
        "royal","forty","bread","opera","chose","owner","vapor","beats","tough","meter",
        "pride","grade","digit","badly","pilot","wound","lucky","prize","steep","slide",
        "arrow","solar","label","swing","truly","tense","split","raise","weigh","hotel",
        "skirt","nerve","grand","treat","honey","moist","legal","penny","crown","shock","novel","alarm",
        "trunk","error","porch","exist","marry","juice","goose","trust","fewer","favor","joint","eager",
        "blend","adult","index","flame","drill","trace","stuff","dirty","silly","hello","rifle","shine",
        "moral","shake","cycle","movie","slope","canal","thumb","shout","habit","reply","fever","crust",
        "swift","faint","civil","ghost","feast","blade","limit","dairy","worst","rapid","brick","beast",
        "shelf","print","crack","midst","coach","stiff","flood","verse","awake","rocky","march","fault",
        "proof","pause","arose","flash","mouse","tower","spare","shiny","alarm","sixth",
        "clerk","sunny","guest","inner","float","stuck","mercy","sweat","smart","upset",
        "rainy","sadly","fancy","unity","crash","craft","hatch","grace","admit","shift","pupil",
        "tiger","angel","cruel","drama","agent","vital","sword","blame","patch","bacon","chalk", 
        "cargo","vocal","crazy","arise","grave","witch","queer","cubic","paste","rural","chase",
        "ideal","beard","eagle","stamp","queen","mayor","cliff","phone","cheek","slice","slant",
        "yield","fleet","tooth","apron","organ","knock","noisy","cheer","twist","hiden","comma",
        "jelly","humor","steal","waist","reign","noble","cheap","dense","salad","shark"
        "grasp","blast","polar","fungi","pearl","frost","diver","phase","alert","coral",
        "focus","naked","puppy","jumps","spoil","quart","spark","vivid","steer","spray",
        "decay","urban","grant","minus","bride","wreck","stare","hobby","thief","crude",
        "flute","rader","skull","argue","scent","panel","fairy","olive","prism","cable",
        "peach","draft","charm","brake","delay","fetch","array","harsh","camel","naval",
        "purse","rigid","crawl","toast","sauce","basin","wrist","fluid","brand","stalk",
        "robot","sheer","grief","bloom","fiber","armor","algae","ditch","lemon","chill",
        "drunk","slain","panic","crisp","ledge","swamp","clung","liver","guage","breed",
        "stool","gross","diary","belly","trend","flask","stake","actor","haste","scope",
        "essay","thump","bliss","clown","roast","tidal","chant","dough","swore","lover",
        "cocoa","punch","award","drain","nylon","lunar","pulse","flown","elbow","fatal",
        "usage","swear","scare","relax","react","valid","robin","ramen","ozone","peace",
        "photo","sushi","spoon","trade","vague","zebra","video","upper","rebel","fight",
        "flake","drown","along","amber","viola","awful","cream","quick","round","scowl"
       ]


AI_wordlist = ["judge","strip","aside","bound","depth","candy","event","worse","aware",
        "shell","ranch","image","snake","aloud","dried","motor","chain","shirt","flour",
        "orbit","pound","curve","refer","tribe","tight","blind","slept","shade","claim",
        "theme","queen","fifth","seven","union","hence","straw","entry","issue","birth",
        "anger","brief","rhyme","glory","guard","fresh","trick","width","burst","route","uncle",
        "royal","forty","bread","opera","chose","owner","vapor","beats","tough","meter",
        "pride","grade","digit","badly","pilot","wound","lucky","prize","steep","slide",
        "arrow","solar","label","swing","truly","tense","split","raise","weigh","hotel",
        "skirt","nerve","grand","treat","honey","moist","legal","penny","crown","shock","novel","alarm",
        "trunk","error","porch","exist","marry","juice","goose","trust","fewer","favor","joint","eager",
        "blend","adult","index","flame","drill","trace","stuff","dirty","silly","hello","rifle","shine",
        "moral","shake","cycle","movie","slope","canal","thumb","shout","habit","reply","fever","crust",
        "swift","faint","civil","ghost","feast","blade","limit","dairy","worst","rapid","brick","beast",
        "shelf","print","crack","midst","coach","stiff","flood","verse","awake","rocky","march","fault",
        "proof","pause","arose","flash","mouse","tower","spare","shiny","alarm","sixth",
        "clerk","sunny","guest","inner","float","stuck","mercy","sweat","smart","upset",
        "rainy","sadly","fancy","unity","crash","craft","hatch","grace","admit","shift","pupil",
        "tiger","angel","cruel","drama","agent","vital","sword","blame","patch","bacon","chalk", 
        "cargo","vocal","crazy","arise","grave","witch","queer","cubic","paste","rural","chase",
        "ideal","beard","eagle","stamp","queen","mayor","cliff","phone","cheek","slice","slant",
        "yield","fleet","tooth","apron","organ","knock","noisy","cheer","twist","hiden","comma",
        "jelly","humor","steal","waist","reign","noble","cheap","dense","salad","shark"
        "grasp","blast","polar","fungi","pearl","frost","diver","phase","alert","coral",
        "focus","naked","puppy","jumps","spoil","quart","spark","vivid","steer","spray",
        "decay","urban","grant","minus","bride","wreck","stare","hobby","thief","crude",
        "flute","rader","skull","argue","scent","panel","fairy","olive","prism","cable",
        "peach","draft","charm","brake","delay","fetch","array","harsh","camel","naval",
        "purse","rigid","crawl","toast","sauce","basin","wrist","fluid","brand","stalk",
        "robot","sheer","grief","bloom","fiber","armor","algae","ditch","lemon","chill",
        "drunk","slain","panic","crisp","ledge","swamp","clung","liver","guage","breed",
        "stool","gross","diary","belly","trend","flask","stake","actor","haste","scope",
        "essay","thump","bliss","clown","roast","tidal","chant","dough","swore","lover",
        "cocoa","punch","award","drain","nylon","lunar","pulse","flown","elbow","fatal",
        "usage","swear","scare","relax","react","valid","robin","ramen","ozone","peace",
        "photo","sushi","spoon","trade","vague","zebra","video","upper","rebel","fight",
        "flake","drown","along","amber","viola","awful","cream","quick","round","scowl"
       ]


def install(package):
    """ 
    Takes in package as a string, installs the package for hint to work.
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


class Wordle:


    def __init__(self, width, height):
        """Construct objects of type Wordle, 
        with the given width and height which are int."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]
    
    def __repr__(self):
        """This method returns a string representation
           for an object of type Wordle.
        """
        s = ""
           # The string to return
        for row in range(0, self.height):
            s += ' | ' + " "
            for col in range(0, self.width):
                s += self.data[row][col] + " " + ' | ' + " "
            s += '\n'


        return s       # The board is complete; return it

    def guessWord(self, answer):
        """
        This function allows the user to guess a word and puts the word into the 
        wordle board  
        
        """
        word = input("Please guess a word: ")

        hints = 1

        if word == "hint" and hints == 1:
                self.rhymeHint(answer, hints)
                word = input("Please guess a word: ")
                hints -= 1

        while len(word) != 5:
            word = input("Please enter a five letter word: ")

        for row in range(self.height):
            if self.data[row][0] == " ":
                for col in range(5):
                    self.data[row][col] = word[col]
                return word
    
    def checkWordAI(self, answer, row, guess):
        """
            Takes in two strings and int, checks AI word in humanvai
        """

        for i in range(len(guess)):
            if row > 5:
                return
            if guess[i] == answer[i]:
                self.data[row][i+6] = "\033[1;32m" + guess[i] + "\033[0m"
            elif guess[i] in answer:
                self.data[row][i+6] = "\033[1;33m" + guess[i] + "\033[0m"
            else:
                 self.data[row][i+6] = guess[i] 

    def checkWord(self, answer, row, guess):
        """ 
        Takes in the guess and answer which are strings and the next available row to
        put the word in(int) and returns if a letter is in the word or if a letter
        is in the word and it is in the right position
        """
        for i in range(len(guess)):
            if row > 5:
                return
            if guess[i] == answer[i]:
                self.data[row][i] = "\033[1;32m" + guess[i] + "\033[0m"
            elif guess[i] in answer:
                self.data[row][i] = "\033[1;33m" + guess[i] + "\033[0m"
            else:
                 self.data[row][i] = guess[i] 

    # AI Functions

    def rhymeHint(self, answer, numHints):
        """ This is a help function for human player when they do not know what to guess.
            It will give a word that rhymes with the answer. Takes in string answer and
            int numHints.  
        """
        install("Phyme")
        
        if numHints <= 0:
            return "You have no hints!"
        ph = Phyme()
        mydict = ph.get_perfect_rhymes(answer)
        x = len(mydict)
        #listofrhymes = []

        if x == 0:
            print("The word starts with " + answer[0] + " and ends with " + answer[-1])
            return

        items_list = [i for i in mydict.values()]

        hint = items_list[0][0]

        if hint == answer:
            print("The word starts with " + answer[0] + " and ends with " + answer[-1])
            return

        print("The answer rhymes with: " + hint)
        numHints -= 1
        print("You have " + str(numHints) + " hints left.")
        return 

        
    def rightPlaceList(self, guess, answer):
        """  
        Takes in strings of guess and answer, returns a list of letters that are
        in the correct position
        """

        rightPlace = []

        for i in range(len(guess)):
            if guess[i] == answer[i]:
                rightPlace.append([guess[i], i])
        
        return rightPlace
            
    def inWordList(self, guess, answer):
        """
        Takes in strings guess and answer, returns a list of letters that are
        in the answer word but not in the right place
        
        """

        inWord = []
        for i in range(len(guess)):
            if guess[i] in answer and (guess != answer):
                inWord.append(guess[i])
    
        newlist = []

        for i in inWord:
            if i not in newlist:
                newlist.append(i)

        return newlist
    
    def aiFirstWord(self):
        """ This function helps AI generate the first word by choosing words that has vowels in it.
            It will generate a list of possible words.
        """
        possibilities = []
        for i in range(len(exwords)):
            if "a" in exwords[i] and "e" in exwords[i]:
                possibilities.append(exwords[i])
        
        return choice(possibilities)

    def remAll(self, lc, item):
        """
                Takes in a list and item, removes all instances of item in list
        
        """

        answer = []
        for i in lc:
            if i != item:
                answer.append(i)
        return answer

    
    def aiGuess(self, d, rightPlace, inWord):
        """
        takes in dictionary of words, and lists with correct position words and 
        words in answer, returns a guess
        
        """
        z = 0
        x = 0
        y = 0
        possibleGuesses = []
        finalPossibleGuesses = []
        inWordL = []

        for i in range(len(rightPlace)):
            if rightPlace[i][0] in inWord:
                self.remAll(inWord, rightPlace[i][0])

        if self.data[0][0] == "":
            return self.aiFirstWord()

        if len(inWord) == 0:
            return choice(d)
        
        if len(rightPlace) == 0:
            for i in range(len(AI_wordlist)):
                for j in range(len(inWord)):
                    if inWord[j] in AI_wordlist[i]:
                        z += 1
                if z == len(inWord):
                    inWordL.append(AI_wordlist[i])
            if len(inWordL) > 0:
                return choice(inWordL)
            else:
                return choice(d)

        
        for i in range(len(d)):
            x = 0
            for j in range(len(rightPlace)):
                if (d[i])[(rightPlace[j][1])] == rightPlace[j][0]:
                    x += 1
            if x == len(rightPlace):
                possibleGuesses.append(d[i])

        for i in range(len(possibleGuesses)):
            y = 0
            for j in range(len(inWord)):
                if inWord[j] in possibleGuesses[i]:
                    y += 1
            if y == len(inWord):
                finalPossibleGuesses.append(possibleGuesses[i]) 
        
        return choice(finalPossibleGuesses)

    def canGuess(self):
        """ 
        Returns true if the user has guesses left and false otherwise
        """
        if self.data[5][0] == " ":
            return True
        else:
            return False
    
        
    def clearBoard(self):
        """ 
        Clears the board
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.data[row][col] != " ":
                    self.data[row][col] = " "


    def saveBoard(self, filname):
        """
        Saves the previously played board into a file
        """

        f = open('file', "w")  # Open file for writing
        for i in range(self.height):
            for j in range(self.width):
                print(self.data[i][j], file = f, end='')
            print(file = f)
        f.close()
        print("File saved.")


    def loadBoard(self, filename):
        """
        Takes in file and returns the board that was saved
        
        """

        f = open('file', "r")  # Open file for reading
        with open('file', 'r') as f:
            print(f.read())
        f.close()
        print(" File loaded. ")

    def hostGame(self, words):
        """ 
        Hosts a game of Wordle, takes in list of words

        """
        hints = 1

        print("Instructions: this is a word guessing game where the answer is a 5 letter word.")
        print("\n")
        print("You have one hint, use it wisely. Type hint in place of your guess to use!")
        print("Disclaimer: Phyme will be installed if you use a hint. ")
        print('     W O R D L E' )    
        print("\n" + "\n")

        row = 0
        answer = choice(words)
        repeat = "y"

        while True:
            
            if self.canGuess() == True:
                guess = input("Please guess a word: ")

                if guess == "hint":
                    self.rhymeHint(answer, hints)
                    guess = input("Please guess a word: ")

                while len(guess) != 5:
                    guess = input("Please enter a 5 letter word: ")

                if answer == guess:
                    self.checkWord(answer, row, guess)
                    print(self)
                    print("You have guessed the word!")
                    prevboard = input("Save this board?[y/n] ")
                    if prevboard == "y":
                        self.saveBoard("file")
                    self.clearBoard()
                    repeat = input("Would you like to play again?[y/n] ")
                    if repeat == "y":
                        # self.introduction()
                        starter()
                    elif repeat == "n":
                        g = input("Do you have a saved board?[y/n] ")
                        if g == "y":
                            s = input("Would you like to see it?[y/n] " )
                            if s == "y":
                                self.loadBoard("file")
                        print("See you next time <3")
                    return
                
                else:
                    self.checkWord(answer, row, guess) 
                    print(self)
            
            row += 1

            if self.canGuess() == False:
                print("You're out of guesses")
                print("The answer is " + answer)
                prevboard = input("Save this board?[y/n] ")
                if prevboard == "y":
                    self.saveBoard("file")
                self.clearBoard()            
                print("\n") 
                repeat = input("Would you like to play again?[y/n]? ")
                if repeat == "y":
                    #self.introduction()
                    starter()
                elif repeat == "n":
                    g = input("Do you have a saved board?[y/n] ")
                    if g == "y":
                        s = input("Would you like to see it?[y/n] " )
                        if s == "y":
                            self.loadBoard("file")
                    print("See you next time <3")
                    break
                return
    
    def hostGameAI(self, AI_wordlist):
        """ 
        Hosts a game of Wordle. AI should be able to randomly choose a word from the AI wordlist and check if it gets the word.
        """
        print("Instructions: this is a word guessing game where the answer is a 5 letter word.")
        print("\n")
        print('     W O R D L E' )    
        print("\n" + "\n")

        row = 0
        answer = choice(exwords)
        prevGuess = ""
        guessList = []
        c = 0
    
        while True:
            if self.canGuess() == True:
                
                rightPlaceList = self.rightPlaceList(prevGuess, answer)
                inWordList = self.inWordList(prevGuess, answer)
                guess = self.aiGuess(AI_wordlist, rightPlaceList, inWordList)

                if answer != guess:
                    guessList.append(guess)
                
                while guess in guessList:
                    guess = self.aiGuess(AI_wordlist, rightPlaceList, inWordList)
                    c += 1
                    if c > 100:
                        break

                if answer == guess:
                    self.checkWord(answer, row, guess) 
                    print(self)
                    print("You have guessed the word!")
                    self.clearBoard()
                    print("See you next time <3")
                    return
                else:
                    self.checkWord(answer, row, guess) 
                    print(self)
                    
            row += 1

            prevGuess = guess
                

            if self.canGuess() == False:
                print("You're out of guesses")
                print("The answer is " + answer)
                self.clearBoard()            
                print("\n") 
                print("See you next time <3")
                return
    
   
    def humanvAI(self, exwords, AI_wordlist):
        """ 
        Hosts a game of Wordle between human player and AI.
        It will need to reference from both answer wordlist and AI wordlist
        """

        print("Instructions: this is a word guessing game where the answer is a 5 letter word.")
        print("You have one hint, use it wisely. Type hint in place of your guess to use!")
        print("Disclaimer: Phyme will be installed if you use a hint. ")
        print("\n")
        print('     W O R D L E' )    
        print("\n" + "\n")

        row = 0
        answer = choice(exwords)
        repeat = "y"
        prevGuess = ""
        guessList = []
        c = 0
        

        # Human make a move            
        while "true": 
            if row < 6:
                HPguess = self.guessWord(answer)

                while len(HPguess) != 5:
                    HPguess = input("Please enter a 5 letter word: ")
                
                self.checkWord(answer,row,HPguess)
                print(self)
                print("AI will guess now . . . ")
                time.sleep(3)

                
            # ai make a move
                rightPlaceList = self.rightPlaceList(prevGuess, answer)
                inWordList = self.inWordList(prevGuess, answer)
                AIguess = self.aiGuess(AI_wordlist, rightPlaceList, inWordList)

                if answer != AIguess:
                    guessList.append(AIguess)
                
                while AIguess in guessList:
                    AIguess = self.aiGuess(AI_wordlist, rightPlaceList, inWordList)
                    c += 1
                    if c > 100:
                        break

                self.checkWordAI(answer,row,AIguess)
                print(self)

                prevGuess = AIguess
                
            # If the human player guess the word
                if answer == HPguess and answer != AIguess:
                    print("The answer is " + HPguess)
                    print("You are a super genius! WOOHOOO! Congrats on guessing the word! ")
                    prevboard = input("Save this board?[y/n] ")
                    if prevboard == "y":
                        self.saveBoard("file")
                    self.clearBoard()
                    repeat = input("Would you like to play again?[y/n]? ")
                    if repeat == "y":
                        #self.introduction()
                        starter()
                    elif repeat == "n":
                        g = input("Do you have a saved board?[y/n] ")
                        if g == "y":
                            s = input("Would you like to see it?[y/n] " )
                            if s == "y":
                                self.loadBoard("file")
                        print("See you next time <3")
                        return
                    return
                                
            # If the AI guess the word    
                if answer == AIguess and answer != HPguess:
                    self.checkWordAI(answer,row,AIguess)
                    self.checkWord(answer,row,HPguess)
                    print("The answer is " + AIguess)
                    print("Oops, AI just got the answer! ")
                    prevboard = input("Save this board?[y/n] ")
                    if prevboard == "y":
                        self.saveBoard("file")
                    self.clearBoard()
                    repeat = input("Would you like to play again?[y/n]? ")
                    if repeat == "y":
                        #self.introduction()
                        starter()
                    elif repeat == "n":
                        g = input("Do you have a saved board?[y/n] ")
                        if g == "y":
                            s = input("Would you like to see it?[y/n] " )
                            if s == "y":
                                self.loadBoard("file")
                        print("See you next time <3")
                        break
                    return
                                
            # If none of them guess the word
                if answer != AIguess and answer != HPguess:
                    self.checkWordAI(answer,row,AIguess)
                    self.checkWord(answer,row,HPguess)
                    print ("Your Answer " + HPguess + " and AI's answer " + AIguess + " are both not right. ")

        # Trying to repeat and loop
            row += 1

            if row >= 6 or (AIguess == answer and HPguess == answer):
                print("Result of human vs AI : TIE")
                print("The answer is " + answer)
                prevboard = input("Save this board?[y/n] ")
                if prevboard == "y":
                    self.saveBoard("file")
                self.clearBoard()            
                print("\n") 
                repeat = input("Would you like to play again?[y/n]? ")
                if repeat == "y":
                    #self.introduction()
                    starter()
                elif repeat == "n":
                    g = input("Do you have a saved board?[y/n] ")
                    if g == "y":
                        s = input("Would you like to see it?[y/n] " )
                        if s == "y":
                            self.loadBoard("file")
                    print("See you next time <3")
                    break
                return
            

def starter():
        """ This is a conversational AI, it will interact with player and 
        jump to specific choices.
        """

        print("Hello there! Nice to meet you! My name is: Wordleboo ʕ •ᴥ•ʔ")
        username = input("What's your name? ")

        print("Dear",str(username), ", Nice to meet you!")
        firstquestion = input("Do you need an introduction to this game or should we head over?[intro/start] ")

        if firstquestion in ["introduction", "I need an introduction","intro", "y", "yes", "Yes"]:
            print("Wordle is a word guessing game. You will have 6 opportunities to guess a five-letter-word. You can play with an AI or on your own. It's not hard. You will figure it out...")
            print("Let's start the game now.\n")
            StartorQuit = input("Y/N? ")
            if StartorQuit in ["Y","Yes","Yeah","yes","y"]:
                print("Welcome to Wordle! \n")
                print("Please choose which mode you would like to play in: \n")
                print(" 1 [Human Player] ")
                print(" 2 [AI Player] ")
                print(" 3 [Human vs AI] ")
                choice = input("Type the number of your choice: ")
                introduction(choice)
        else:
            print("Welcome to Wordle! \n")
            print("Please choose which mode you would like to play in: \n")
            print(" 1 [Human Player] ")
            print(" 2 [AI Player] ")
            print(" 3 [Human vs AI] ")
            print("\n")
            choice = input("Type the number of your choice: ")
            introduction(choice)

def introduction(choice):
        """
        Introduces the game and offers choice that player chose to play
        
        """
        if choice == "1":
            w = Wordle(5,6)
            w.hostGame(exwords)
        elif choice == "2":
            w = Wordle(5,6)
            w.hostGameAI(AI_wordlist)
        else:
            w = Wordle(11,6)
            w.humanvAI(exwords,AI_wordlist)
        return
        
starter()