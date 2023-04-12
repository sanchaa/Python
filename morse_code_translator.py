# A Morse code encoder/decoder
# encryption & decryption

import time

MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"),
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)


def print_intro():
    # Welcome user to morse code program
    print("Welcome to Sanz\nThis program encodes and decodes Morse code.\n")


def get_input():
    # get user input
    while True:

        user_input = input("Do you want to encode (e) or decode(d)? ")
        if user_input != 'e' and user_input != 'd':
            print("Incorrect mode. Please type e or d!")
            time.sleep(2)
            continue
        else:
            message = input("What message would you like to encode/decode? ").upper()
            # user should write message # 
        break
    return user_input, message


def encode(message):
    # for loop as morse_code is tuple
    secret_word = ""
    for letter in message:
        if letter != " ":
            value = [i[0] for i in MORSE_CODE if (i[1] == letter)]
            secret_word = secret_word + value[0] + " "
        else:
            secret_word += " "
    return secret_word


def decode(message):
    decode_word = ' '
    words = message.split(' ')
    for w in words:
        letters = w.split('   ')
        for letter in letters:
            for i in range(0, len(MORSE_CODE)):
                if letter == MORSE_CODE[i][0]:
                    decode_word = decode_word + MORSE_CODE[i][1]
            decode_word = decode_word + ' '
        decode_word = decode_word.strip()
    return decode_word


# ---------- Challenge Functions (Optional) ----------


def process_lines(filename, mode):
    list_messages = []
    f = open(filename, 'r')
    for line in f:
        list_messages.append(line)
    print(list_messages)


def write_lines(lines):
    pass


def check_file_exists(filename):
    pass


"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encode (e) or decode (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encode/decode.
    • Encode/decode the message as appropriate and print the output.
    • Prompt the user whether they would like to encode/decode another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.

Hints:
    • Use the tuple MORSE_CODE above to convert between plain text/Morse code
    • You can make use of str.split() to generate a list of Morse words and characters
      by using the spaces between words and characters as a separator.
    • You will also find str.join() useful for constructing a string from a list of strings.
    • You should use a loop to keep the programming running if the user says that would like to
      encode/decode another message after the first.
    • Your program should handle both uppercase and lowercase inputs. You can make use of str.upper()
      and str.lower() to convert a message to that case.
    • Check the assessment specification for code examples.
"""


def main():
    print_intro()
    mode, message = get_input()
    if mode == 'e':
        print(encode(message))
    elif mode == 'd':
        print(decode(message))


# Program execution begins here
if __name__ == '__main__':
    main()
