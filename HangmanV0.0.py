import random


class FlavorText:
    
    def __init__(self, collection):
        self.collection = list(collection)

    def __str__(self):
        return f"Here is a list with the options for the flavor text: {self.collection}."
    
    def random_item_from_collection(self):
        return random.choice(self.collection)
    
    def __len__(self):
        return len(self.collection)

class Guess:
    
    def __init__(self, tries, collection):
        self.tries = tries
        self.selected_word = collection.random_item_from_collection()
        self.representation = "X" * len(self.selected_word)
        print(welcome.random_item_from_collection())
        print(self.representation)
        
    def is_guess_previous_guess(self):
        if self.guess in self.previous_guess:
            self.tries -= 1
            print(f"Come on, mate, you've already tried that! There goes one of your guesses, you've got {self.tries} remaining...\n")
            return True
        
    def is_guess_full_correct_guess(self):
        if self.guess == self.selected_word:
            return True
        else:
            return False
        
    def is_word_complete(self):
        if self.representation == self.selected_word:
            print("I guess we're done here...")
            return True
        
    def is_guess_too_long(self):
        if self.is_guess_full_correct_guess() is False and len(self.guess) != 1:
            self.tries -= 1
            print(f"Either guess the full word correctly, or take it one letter at a time, buddy. You have {self.tries} guesses remaining!\n")
            return True
    
    def is_guess_alphabetic(self):
        if not self.guess.isalpha():
            self.tries -= 1
            print(f"Come on, buddy... just what are you trying to pull? You have {self.tries} guesses remaining!\n")
            return True
        
    def validate(self, guess):
        self.guess = guess.lower()
        if self.is_guess_previous_guess():
            return False
        elif self.is_guess_too_long():
            return False
        elif self.is_guess_alphabetic():
            return False
        else:
            return True
        
    def react_to_wrong_guess(self):
        self.tries -= 1
        self.previous_guess.append(self.guess)
        print(fail_insults.random_item_from_collection(), f"You have {self.tries} guesses remaining!\n")
        print(self.representation)
        
    def react_to_correct_guess(self):
        self.previous_guess.append(self.guess)
        for i, character in enumerate(self.selected_word):
            if character == self.guess:
                self.representation = self.representation[:i] + self.guess + self.representation[i+1:]
        
    def run_game(self):
        self.previous_guess = []
        while self.tries > 0:
            self.guess = input(guess_prompts.random_item_from_collection())
            
            if self.validate(self.guess):               
                if self.is_guess_full_correct_guess():
                    print("You got it all in one! How could you do this to me???\n")
                    break
                
                elif self.guess not in self.selected_word:
                    self.react_to_wrong_guess()                   
                elif self.guess in self.selected_word:
                    self.react_to_correct_guess()
                    if self.is_word_complete():
                        break
                    print(success_insults.random_item_from_collection(), self.representation, "\n")
                    continue
            
            else:
                continue
       
        if self.tries == 0:
            print(final_insults.random_item_from_collection(), f"The word was {self.selected_word}!")    


fail_insults = FlavorText(["Wroooong! You suck!", "Wow, just, wow...", "Andrew, is that you?", "Hint: the word is in English. Do you speak it??? DOES HE LOOK LIKE A BI... sorry, sorry..."])
success_insults = FlavorText(["GG", "You got one! Damn you!!!", "Even a broken clock...", "Well, color me impressed...", "OK, OK, but don't get cocky on me now."])
final_insults = FlavorText(["Well, it seems you failed. Should I have made a tutorial or something?", "Oooooh, I'm so sorry, I didn't know you were illiterate!", "Wow... words fail me... as they have obviously failed you.", "I mean... should I bother insulting you, can you even read this?", "We're done here, STOP STARING AT ME!!!"])
guess_prompts = FlavorText(["Make your guess, foolish mortal: ", "Come on, try something: ", "Gimme a letter: ", "Just press one of the buttons in front of you, meatbag: ", "Please insert letter: "])
welcome = FlavorText(["Hey there! Welcome!", "How you doin'?", "What are you looking at, weirdo? Oh yeah, the game...", "So glad to see you here!"])

word_options = ["TV", "games", "alcoholism", "Lovecraft", "classical", "miscellaneous"]
words_TV = FlavorText(["janitor", "rat", "cheese", "archer", "tactical", "turtleneck"])
words_games = FlavorText(["tequila", "sunset", "disco", "dancer"])
words_alcoholism = FlavorText(["tequila", "gin", "whisky", "rum", "vodka"])
words_lovecraft = FlavorText(["mariner", "lighthouse", "insanity", "innsmouth"])
words_classical = FlavorText(["column", "oedipus", "literary", "logos", "pathos", "xenophon"])
words_miscellaneous = FlavorText(["peach", "laxative", "difficulty", "msspelled"])

word_type = input(f"What type of word do you want? Select from the following list: {word_options} ")
game_running = True

while game_running == True:
    if word_type in word_options:
        
        if word_type == "TV":
            user_guess = Guess(5, words_TV)
            user_guess.run_game()
            game_running = False
            
        elif word_type == "games":
            user_guess = Guess(5, words_games)
            user_guess.run_game()
            game_running = False
        
        elif word_type == "alcoholism":
            user_guess = Guess(5, words_alcoholism)
            user_guess.run_game()
            game_running = False
            
        elif word_type == "Lovecraft":
            user_guess = Guess(5, words_lovecraft)
            user_guess.run_game()
            game_running = False
            
        elif word_type == "classical":
            user_guess = Guess(5, words_classical)
            user_guess.run_game()
            game_running = False
            
        elif word_type == "miscellaneous":
            user_guess = Guess(5, words_miscellaneous)
            user_guess.run_game()
            game_running = False
            
    else:
        print("\nSorry, that's not a valid type")
        word_type = input(f"What type of word do you want? Select from the following list: {word_options} ")