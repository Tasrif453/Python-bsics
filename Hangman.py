import random as rd


def hangman1():
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========
          ''')


def hangman2():
    print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
          ''')


def hangman3():
    print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
          ''')


def hangman4():
    print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
          ''')


def hangman5():
    print('''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
          ''')


def hangman6():
    print('''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
          ''')


def hangman7():
    print('''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
          ''')


# Map remaining lives to figure
fig = {
    6: hangman1,
    5: hangman2,
    4: hangman3,
    3: hangman4,
    2: hangman5,
    1: hangman6,
    0: hangman7
}

# Word list
words = ['apple', 'banana', 'orange', 'grapes', 'mango',
         'pineapple', 'strawberry', 'watermelon', 'peach', 'cherry']
word = rd.choice(words)
hidden = ["_"] * len(word)
life = 6

print("Welcome to Hangman!")
fig[life]()
print(" ".join(hidden))

while life > 0 and "_" in hidden:
    guess = input("Enter your guess: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden[i] = guess
                word = word[:i] + "_" + word[i+1:]
                break
        print("✅ Correct!", " ".join(hidden))
    else:
        life -= 1
        print(f"❌ Wrong! '{guess}' is not in the word.")
    fig[life]()
    print(
        f"**************************** {life}/6 LIVES LEFT ****************************")

if "_" not in hidden:
    print(f"🎉 Congrats! You guessed the word '{hidden}' correctly!")
else:
    fig[0]()
    print(f"😢 You lose! The word was '{"".join(hidden)}'.")
