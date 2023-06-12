import tkinter as tk
from tkinter import filedialog
import nltk
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    tokens = word_tokenize(text)
    fdist = FreqDist(tokens)

    data = {'Word': [], 'Frequency': []}
    for word, frequency in fdist.most_common():
        data['Word'].append(word)
        data['Frequency'].append(frequency)
    df = pd.DataFrame(data)

    plt.figure(figsize=(10, 6))
    plt.plot(df['Word'], df['Frequency'])
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.title('Word Frequency Distribution')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        process_file(file_path)


# Create the main Tkinter window
root = tk.Tk()

# Create a label and a button in the main window
label = tk.Label(root, text="Drag and drop a text file here")
label.pack(pady=20)
button = tk.Button(root, text="Browse", command=browse_file)
button.pack()

# Run the Tkinter event loop
root.mainloop()
