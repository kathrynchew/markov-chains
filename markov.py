"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_files():
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_path = sys.argv[1]
    file_path = file_path.split("/")
    file_contents = open(file_path[-1]).read()

    if sys.argv[3]:
        file_path2 = sys.argv[3].split("/")
        file_contents2 = open(file_path2[-1]).read()
        file_contents = file_contents + " " + file_contents2

    return file_contents


def make_chains(text_string):
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

    words = text_string.split()

    length_of_n = int(sys.argv[2])  # Take user inputted value of n, makes usable

    try:    # In all cases where there is not an IndexError, run this loop
        for num in range(len(words)):
            n_gram = tuple(words[num:num+length_of_n])
            # Tuple value is a slice of words list, starting at for loop item,
            # ending at loop item + inputted value of n, to ensure correct n-gram length

            if n_gram not in chains:
                chains[n_gram] = [words[num + length_of_n]]
            else:
                chains[n_gram].append(words[num + length_of_n])
    except:  # If IndexError (string @ end of text not long enough), do this
        chains[tuple(words[0-length_of_n:])] = None
             # Make a tuple of the last n items in words list, add it to chains
             # as key, set the value to None (this will be break condition)

    return chains


def make_start_sentences(chains):
    """ Return list of all markov chains that start with a capital letter """

    start_sentences = [key for key in chains.items() if key[0].istitle()]

    return start_sentences


def make_text(chains, start_sentences):
    """Return text from chains."""
    length_of_n = int(sys.argv[2])

    words = []

    link = choice(start_sentences)
    words.extend(list(link))

    while chains[link]:
        new_link = choice(chains[link])
        words.append(new_link)
        link = tuple(words[0 - length_of_n:])

    return " ".join(words)


# input_path = "green-eggs.txt"
# input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_files()

# Get a Markov chain
chains = make_chains(input_text)
start_sentences = make_start_sentences(chains)

# Produce random text
random_text = make_text(chains, start_sentences)

print random_text
