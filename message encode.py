import tkinter as tk

# Define a substitution key (mapping)
substitution_key = {
    ' ': ' ',
    'a': 'w',
    'b': 'g',
    'c': 'h',
    'd': 'x',
    'e': 'i',
    'f': 'y',
    'g': 'j',
    'h': 'k',
    'i': 'l',
    'j': 'm',
    'k': 'z',
    'l': 'n',
    'm': 'o',
    'n': 'p',
    'o': 'q',
    'p': 'r',
    'q': 'a',
    'r': 'b',
    's': 't',
    't': 's',
    'u': 'c',
    'v': 'd',
    'w': 'u',
    'x': 'e',
    'y': 'f',
    'z': 'v',
}

# Function to encode a message
def encode(message):
    encoded_message = []
    for char in message:
        if char in substitution_key:
            encoded_message.append(substitution_key[char])

    return ''.join(encoded_message)

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

# Encode and display button
def encode_and_display_message():
    message = input_entry.get()
    encoded_message = encode(message)

    # Display both original and encoded messages in the text box
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Original Message:\n{}\n\nEncoded Message:\n{}".format(message, encoded_message))

encode_button = tk.Button(root, text="Encode and Display", command=encode_and_display_message)
encode_button.pack()

root.mainloop()
