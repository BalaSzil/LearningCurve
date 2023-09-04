words = ["tequila", "sunset", "disco", "dancer", "column", "mariner", "lighthouse", "insanity", "janitor", "rat", "cheese", "peach", "laxative", "archer", "tactical", "turtleneck", "oedipus", "literary", "difficulty", "msspelled", "xenophon"]
welcome = ["Hey there! Welcome!", "How you doin'?", "What are you looking at, weirdo? Oh yeah, the game...", "So glad to see you here!"]
fail_insults = ["Wroooong! You suck!", "Wow, just, wow...", "Andrew, is that you?", "Hint: the word is in English. Do you speak it??? DOES HE LOOK LIKE A BI... sorry, sorry..."]
success_insults = ["You got one! Damn you!!!", "Even a broken clock...", "Well, color me impressed...", "OK, OK, but don't get cocky on me now."]
final_insults = ["Well, it seems you failed. Should I have made a tutorial or something?", "Oooooh, I'm so sorry, I didn't know you were illiterate!", "Wow... words fail me... as they have obviously failed you.", "I mean... should I bother insulting you, can you even read this?", "We're done here, STOP STARING AT ME!!!"]
guess_prompts = ["Make your guess, foolish mortal: ", "Come on, try something: ", "Gimme a letter: ", "Just press one of the buttons in front of you, meatbag: ", "Please insert letter: "]
banned = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "'", "+", "-", "*", "!", "%", "/", "=", "(", ")"]
import random
def randomize(factor):
    return factor[random.randrange(len(factor))]
prob = randomize(words)
representation = "X"*len (prob)
print(randomize(welcome))
print(representation)
tries = 8
while tries>0:
    if representation == prob:
        print("I guess we're done here...")
        break
    guess = input(randomize(guess_prompts))
    guess = guess.lower()
    if guess != prob and len(guess) != 1:
        tries -= 1
        print(f"Either guess the full word correctly, or take it one letter at a time, buddy. You have {tries} guesses remaining!")
    elif guess in banned:
        tries -= 1
        print(f"Come on, buddy... just what are you trying to pull? You have {tries} guesses remaining!")
    elif guess == prob:
        print("You got it all in one! How could you do this to me???")
        break
    elif guess not in prob:
        tries -= 1
        print(randomize(fail_insults), f"You have {tries} guesses remaining!")
    elif guess in prob:
        for i in range(len(prob)):
            if prob[i] == guess:
                representation = representation[:i] + guess + representation[i+1:]
        print(randomize(success_insults), representation)
if tries == 0:
    print(randomize(final_insults), f"The word was {prob}!" )