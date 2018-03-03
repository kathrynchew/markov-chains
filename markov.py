"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_path = file_path.split("/")
    file_contents = open(file_path[-1]).read()

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

### DYNAMIC N-GRAMS VERSION HERE ###
    # n_gram = tuple()
    length_of_n = int(sys.argv[2])

    try:
        for num in range(len(words)):
            n_gram = tuple(words[num:num+length_of_n])
            # if len(n_gram) < length_of_n:
            #     n_gram = n_gram + (words[num],)
            # print n_gram
            # else:
            if n_gram not in chains:
                chains[n_gram] = [words[num + length_of_n]]
            else:
                chains[n_gram].append(words[num + length_of_n])
    except:
        chains[tuple(words[0-length_of_n:])] = None

    # print chains

    # except:
    #     for num in range(len(words)):
    #         if len(n_gram) < length_of_n:
    #             n_gram = (words)


### STATIC BI-GRAMS VERSION HERE ###
    # try:
    #     for num in range(len(words)):
    #         if (words[num], words[num + 1]) not in chains:
    #             chains[(words[num], words[num + 1])] = [words[num + 2]]
    #         else:
    #             chains[(words[num], words[num + 1])].append(words[num + 2])
    # except:
    #     chains[(words[-2], words[-1])] = None

    return chains


def make_text(chains):
    """Return text from chains."""
    length_of_n = int(sys.argv[2])

    words = []

    link = choice(chains.keys())
    words.extend(list(link))
    print link

    while chains[link]:
        new_link = choice(chains[link])
        words.append(new_link)
        link = tuple(words[0 - length_of_n:])
        # link = (words[-2], words[-1])

    return " ".join(words)


# input_path = "green-eggs.txt"
input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
