import random


def Random_Item_From_Collection(collection):
    return collection[random.randrange(len(collection))]


def Already_Tried_That(player_guess):
    if player_guess in previous_guess:
        return True
    else:
        return False
    

def Not_Single_Letter_Nor_Solve(guess, selected_word):
    if guess != selected_word and len(guess) != 1:
        return True
    else:
        return False
    
    
def Not_A_Letter(player_guess):
    if player_guess.isalpha():
        return False
    else:
        return True
    
    
def Full_Correct_Guess(player_guess):
    if player_guess == selected_word:
        return True
    else:
        return False
    

def Wrong_Guess(player_guess):
    if player_guess not in selected_word:
       return True
    else:
       return False


words = ["tequila", "sunset", "disco", "dancer", "column", "mariner", "lighthouse", "insanity", "janitor", "rat", "cheese", "peach", "laxative", "archer", "tactical", "turtleneck", "oedipus", "literary", "difficulty", "msspelled", "xenophon"]
welcome = ["Hey there! Welcome!", "How you doin'?", "What are you looking at, weirdo? Oh yeah, the game...", "So glad to see you here!"]
fail_insults = ["Wroooong! You suck!", "Wow, just, wow...", "Andrew, is that you?", "Hint: the word is in English. Do you speak it??? DOES HE LOOK LIKE A BI... sorry, sorry..."]
success_insults = ["GG", "You got one! Damn you!!!", "Even a broken clock...", "Well, color me impressed...", "OK, OK, but don't get cocky on me now."]
final_insults = ["Well, it seems you failed. Should I have made a tutorial or something?", "Oooooh, I'm so sorry, I didn't know you were illiterate!", "Wow... words fail me... as they have obviously failed you.", "I mean... should I bother insulting you, can you even read this?", "We're done here, STOP STARING AT ME!!!"]
guess_prompts = ["Make your guess, foolish mortal: ", "Come on, try something: ", "Gimme a letter: ", "Just press one of the buttons in front of you, meatbag: ", "Please insert letter: "]
previous_guess = []
selected_word = Random_Item_From_Collection(words)
representation = "X"*len(selected_word)
print(Random_Item_From_Collection(welcome))
print(representation)


tries = 8
while tries > 0:
    guess = input(Random_Item_From_Collection(guess_prompts))
    guess = guess.lower()
    if Already_Tried_That(guess):
        tries -= 1
        print(f"Come on, mate, you've already tried that! There goes one of your guesses, you've got {tries} remaining...")
    else:
        previous_guess.append(guess)
        if Not_Single_Letter_Nor_Solve(guess, selected_word):
            tries -= 1
            print(f"Either guess the full word correctly, or take it one letter at a time, buddy. You have {tries} guesses remaining!")  
        elif Not_A_Letter(guess):
            tries -= 1
            print(f"Come on, buddy... just what are you trying to pull? You have {tries} guesses remaining!")
        elif Full_Correct_Guess(guess):
            print("You got it all in one! How could you do this to me???")
            break
        elif Wrong_Guess(guess):
            tries -= 1
            print(Random_Item_From_Collection(fail_insults), f"You have {tries} guesses remaining!")
        elif guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == guess:
                    representation = representation[:i] + guess + representation[i+1:]
            if representation == selected_word:
                print("I guess we're done here...")
                break   
            print(Random_Item_From_Collection(success_insults), representation)
if tries == 0:
    print(Random_Item_From_Collection(final_insults), f"The word was {selected_word}!")