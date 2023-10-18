import tkinter as tk

# Define a decode key (mapping)
decode_key = {
    ' ': ' ',
    'w': 'a',
    'g': 'b',
    'h': 'c',
    'x': 'd',
    'i': 'e',
    'y': 'f',
    'j': 'g',
    'k': 'h',
    'l': 'i',
    'm': 'j',
    'z': 'k',
    'n': 'l',
    'o': 'm',
    'p': 'n',
    'q': 'o',
    'r': 'p',
    'a': 'q',
    'b': 'r',
    't': 's',
    's': 't',
    'c': 'u',
    'd': 'v',
    'u': 'w',
    'e': 'x',
    'f': 'y',
    'v': 'z',
}

# Function to encode a message
def decode(message):
    decoded_message = []
    for char in message:
        if char in decode_key:
            decoded_message.append(decode_key[char])

    return ''.join(decoded_message)

# Create a Tkinter application
root = tk.Tk()
root.title("Encode Message")

# Entry widget for input
input_label = tk.Label(root, text="Enter your word:")
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

# Text widget to display results
result_text = tk.Text(root, height=5, width=40)
result_text.pack()

# Decode and display button
def decode_and_display_message():
    message = input_entry.get()
    decoded_message = decode(message)

    # Display both original and decoded messages in the text box
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Original Message:\n{}\n\nDecoded Message:\n{}".format(message, decoded_message))

encode_button = tk.Button(root, text="Decode and Display", command=decode_and_display_message)
encode_button.pack()

root.mainloop()
