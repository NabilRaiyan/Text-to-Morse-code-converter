import customtkinter
import tkinter

window = customtkinter.CTk()
window.title("Text to Morse code converter")
window.geometry('430x620')

window.configure(bg='cyan')
window.configure(padx=20, pady=20)

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', ' ': '/', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ',': '--..--'}


# Function to cipher the text

def cipher():
    show_converted_message.delete('1.0', 'end')

    text = message_box.get("0.0", "end").upper()
    stripped_text = text.rstrip("\n")
    converted_text = ''
    try:
        for char in stripped_text:
            if char != ' ':
                converted_text += MORSE_CODE_DICT[char] + ' '
            else:
                converted_text += '/ '
        show_converted_message.insert('end', converted_text)
    except:
        converted_text += 'Please enter a valid text {A-Z, a-z, 0-9, (, ), /, ?, ",", .}'
        show_converted_message.insert('end', converted_text)


# Function to decipher the morse code
def decipher():
    show_converted_message.delete('1.0', 'end')

    text = message_box.get("0.0", "end").upper()
    stripped_text = text.rstrip("\n")
    converted_text = ''

    morse_list = stripped_text.split()

    for char in morse_list:

        for key, value in MORSE_CODE_DICT.items():
            if char == value:
                converted_text = key

        show_converted_message.insert('end', converted_text)


# Morse code converter Gui
# Text input by user
text_input = customtkinter.CTkLabel(text='Enter message', text_font=("Courier", 15, 'bold'))
text_input.grid(column=0, row=0, padx=50, pady=10)

message_box = tkinter.Text(master=window, width=45, height=10)
message_box.grid(row=1, column=0, padx=20, pady=10)

# Text to Morse code converter button
cipher_button = customtkinter.CTkButton(text='Cipher', text_font=("Courier", 15, 'bold'), border_width=2,
                                        corner_radius=8, bg_color='cyan', fg_color='cyan', hover_color='white',
                                        command=cipher)
cipher_button.grid(column=0, row=2, padx=50, pady=20)

decipher_button = customtkinter.CTkButton(text='Decipher', text_font=("Courier", 15, 'bold'), border_width=2,
                                          corner_radius=8, bg_color='cyan', fg_color='cyan', hover_color='white',
                                          command=decipher)
decipher_button.grid(column=0, row=3, padx=50, pady=20)

# Show conversion after converted to morse code
message_label = customtkinter.CTkLabel(text='Converted Message', text_font=("Courier", 15, 'bold'))
message_label.grid(column=0, row=4, padx=50, pady=10)

show_converted_message = tkinter.Text(master=window, width=45, height=10)
show_converted_message.grid(column=0, row=5)

window.mainloop()
