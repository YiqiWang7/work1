def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Convert the text to uppercase for case-insensitive translation
    text = text.upper()

    # Translate each character and separate words with a forward slash
    translated = []
    for word in text.split():
        translated.append(' '.join(morse_code_dict[char] for char in word if char in morse_code_dict))

    return ' / '.join(translated)

# Adding user input functionality
user_input = input("Enter text to translate into Morse code: ")
print(morse_translator(user_input))
