"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    with open(file_path) as long_string:
        text_string = long_string.read()
    return text_string


def make_chains(text_string, number_words):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    text_list = text_string.split()


    for i in range(len(text_list)-number_words):
        word_combo = tuple(text_list[i:i+number_words])
        chains[word_combo] = chains.get(word_combo, []) + [text_list[i+number_words]]
        # if word_combo in chains.keys():
        #     chains[word_combo].append(text_list[i+2])
        # else:
        #     chains[word_combo] = [text_list[i+2]]

    return chains


def make_text(chains, number_words):
    """Return text from chains."""


    # from tuple / link key
    # randomly pick an item from its list of values
    # adds last two words of the k-v pair as new current key..do until the key doesn't exist
    current_key = choice(chains.keys())
    words = list(current_key)

    # print "this is the current key", current_key
    # print "these are the words:", words
    
    while current_key in chains.keys():
        last_word = choice(chains[current_key])
        words.append(last_word)
        current_key = tuple(words[-number_words:])          
    return " ".join(words)


input_path = sys.argv[1]
number_words = 4

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, number_words)

print chains

# Produce random text
random_text = make_text(chains, number_words)

print random_text
