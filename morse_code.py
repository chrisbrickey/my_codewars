def decodeMorse(morseCode):
    stripped_code = morseCode.strip() #removes spaces before and after

    code_words = filter(None, stripped_code.split("   "))  # list of words (each still coded)

    code_letters = []

    for word in code_words:
        letter_string = word.split()
        code_letters.append(letter_string)   #code_letters is a list (word) of lists (letters that make up each word)

    english_words = []
    morse_code = {
        '.-...': '&',
        '--..--': ',',
        '....-': '4',
        '.....': '5',
        '...---...': 'SOS',
        '-...': 'B',
        '-..-': 'X',
        '.-.': 'R',
        '.--': 'W',
        '..---': '2',
        '.-': 'A',
        '..': 'I',
        '..-.': 'F',
        '.': 'E',
        '.-..': 'L',
        '...': 'S',
        '..-': 'U',
        '..--..': '?',
        '.----': '1',
        '-.-': 'K',
        '-..': 'D',
        '-....': '6',
        '-...-': '=',
        '---': 'O',
        '.--.': 'P',
        '.-.-.-': '.',
        '--': 'M',
        '-.': 'N',
        '....': 'H',
        '.----.': "'",
        '...-': 'V',
        '--...': '7',
        '-.-.-.': ';',
        '-....-': '-',
        '..--.-': '_',
        '-.--.-': ')',
        '-.-.--': '!',
        '--.': 'G',
        '--.-': 'Q',
        '--..': 'Z',
        '-..-.': '/',
        '.-.-.': '+',
        '-.-.': 'C',
        '---...': ':',
        '-.--': 'Y',
        '-': 'T',
        '.--.-.': '@',
        '...-..-': '$',
        '.---': 'J',
        '-----': '0',
        '----.': '9',
        '.-..-.': '"',
        '-.--.': '(',
        '---..': '8',
        '...--': '3'}
    morse_code[' '] = ' '

    for index, word in enumerate(code_letters):
        if index != (len(code_letters)) - 1:
            word.append(' ')

        for letter in word:
            english_letter = morse_code[letter]
            english_words.append(english_letter)

    english_string = "".join(english_words)
    return english_string
