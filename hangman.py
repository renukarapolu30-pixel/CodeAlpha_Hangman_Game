import random

words = ["python", "computer", "mountain", "laptop", "library"]

word = random.choice(words)

display = ['_'] * len(word)

attempts = 6

while attempts > 0 and '_' in display:

    letter = input("Enter a letter: ")

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
    else:
        attempts -= 1
        print("Wrong guess!")
    
    print(" ".join(display))
    print("Attempts left:", attempts)

if '_' not in display:
    print("YOU WON! ^_^")
    print("The word was:", word)
else:
    print("YOU LOST! >_<")
    print("The word was:", word)
