# with this code you can tokenize words of screenplays (txt files) 
# this is not tested yet

import tkinter as tk
from tkinter import filedialog
import nltk
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import wordnet


def get_word_type(word):
    pos_tag = nltk.pos_tag([word])[0][1]
    word_type = wordnet.synsets(word, pos=get_wordnet_pos(pos_tag))
    if word_type:
        return word_type[0].pos()
    return None


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('P'):
        return wordnet.PRON
    else:
        return None


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    tokens = word_tokenize(text)
    fdist = FreqDist(tokens)

    data = {'Word': [], 'Frequency': [], 'Type': []}
    for word, frequency in fdist.most_common():
        word_type = get_word_type(word)
        if word_type:
            data['Word'].append(word)
            data['Frequency'].append(frequency)
            data['Type'].append(word_type)
    df = pd.DataFrame(data)

    plt.figure(figsize=(10, 6))
    plt.plot(df['Word'], df['Frequency'])
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.title('Word Frequency Distribution')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Save the plot as a PDF
    plt.savefig('word_frequency_plot.pdf')
    plt.close()

    # Save the DataFrame as a PDF
    df.to_csv('word_frequency_results.csv', index=False)

    print(df)


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
