import random


class Flavor_Text:
    def __init__(self, collection):
        self.options = list(collection)

    def __str__(self):
        return f"Here is a list with the options for the {self} flavor text: {self.options}."
    
    
# randomizálás method?

def random_item_from_collection(collection):
    return collection[random.randrange(len(collection))]


fail_insults = Flavor_Text(["Wroooong! You suck!", "Wow, just, wow...", "Andrew, is that you?", "Hint: the word is in English. Do you speak it??? DOES HE LOOK LIKE A BI... sorry, sorry..."])
success_insults = Flavor_Text(["GG", "You got one! Damn you!!!", "Even a broken clock...", "Well, color me impressed...", "OK, OK, but don't get cocky on me now."])
final_insults = Flavor_Text(["Well, it seems you failed. Should I have made a tutorial or something?", "Oooooh, I'm so sorry, I didn't know you were illiterate!", "Wow... words fail me... as they have obviously failed you.", "I mean... should I bother insulting you, can you even read this?", "We're done here, STOP STARING AT ME!!!"])
guess_prompts = Flavor_Text(["Make your guess, foolish mortal: ", "Come on, try something: ", "Gimme a letter: ", "Just press one of the buttons in front of you, meatbag: ", "Please insert letter: "])
print(guess_prompts)

words = ["tequila", "sunset", "disco", "dancer", "column", "mariner", "lighthouse", "insanity", "janitor", "rat", "cheese", "peach", "laxative", "archer", "tactical", "turtleneck", "oedipus", "literary", "difficulty", "msspelled", "xenophon"]
# welcome = ["Hey there! Welcome!", "How you doin'?", "What are you looking at, weirdo? Oh yeah, the game...", "So glad to see you here!"]
# fail_insults = ["Wroooong! You suck!", "Wow, just, wow...", "Andrew, is that you?", "Hint: the word is in English. Do you speak it??? DOES HE LOOK LIKE A BI... sorry, sorry..."]
# success_insults = ["GG", "You got one! Damn you!!!", "Even a broken clock...", "Well, color me impressed...", "OK, OK, but don't get cocky on me now."]
# final_insults = ["Well, it seems you failed. Should I have made a tutorial or something?", "Oooooh, I'm so sorry, I didn't know you were illiterate!", "Wow... words fail me... as they have obviously failed you.", "I mean... should I bother insulting you, can you even read this?", "We're done here, STOP STARING AT ME!!!"]
# guess_prompts = ["Make your guess, foolish mortal: ", "Come on, try something: ", "Gimme a letter: ", "Just press one of the buttons in front of you, meatbag: ", "Please insert letter: "]
# previous_guess = []
# selected_word = random_item_from_collection(words)
# representation = "X" * len(selected_word)
# tries = 8


# print(random_item_from_collection(welcome))
# print(representation)

# while tries > 0:
    
#     guess = input(random_item_from_collection(guess_prompts))
#     guess = guess.lower()
    
#     already_tried_that = guess in previous_guess
#     if already_tried_that:
#         tries -= 1
#         print(f"Come on, mate, you've already tried that! There goes one of your guesses, you've got {tries} remaining...")
#         continue
    
#     previous_guess.append(guess)
#     not_single_letter_nor_solve = guess != selected_word and len(guess) != 1
#     not_letter = not guess.isalpha()
#     full_correct_guess = guess == selected_word
#     wrong_guess = guess not in selected_word
#     if not_single_letter_nor_solve:
#         tries -= 1
#         print(f"Either guess the full word correctly, or take it one letter at a time, buddy. You have {tries} guesses remaining!")  
#     elif not_letter:
#         tries -= 1
#         print(f"Come on, buddy... just what are you trying to pull? You have {tries} guesses remaining!")
#     elif full_correct_guess:
#         print("You got it all in one! How could you do this to me???")
#         break
#     elif wrong_guess:
#         tries -= 1
#         print(random_item_from_collection(fail_insults), f"You have {tries} guesses remaining!")

#     elif guess in selected_word:
#         for i, word in enumerate(selected_word):
#             if selected_word[i] == guess:
#                 representation = representation[:i] + guess + representation[i+1:]
#         if representation == selected_word:
#             print("I guess we're done here...")
#             break
#         print(random_item_from_collection(success_insults), representation)
        
# if tries == 0:
#     print(random_item_from_collection(final_insults), f"The word was {selected_word}!")