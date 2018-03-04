""" Generate Markov Text by Blending Multiple TV and/or Play Scripts """
# import markov
import sys


def find_character_names(script_text):
    """ Take script text, find character names, return names & frequency

    Any items matching formatting of names are added to a set (no duplicates)
    and also to a list (duplicates; tracks frequency of occurrence)

    Set of names & list of freqency are returned in a dictionary with collection
    titles ("names", "frequency") as keys & corresponding collections as values.
    """

    char_names = set()
    char_frequency = []

    for line in script_text:
        line = line.rstrip().split()
        try:
            if line[0].isupper() and line[0][-1] == ":":
                char_names.add(line[0].rstrip(":"))
                char_frequency.append(line[0].rstrip(":"))
            elif line[0].isupper() and line[1].isupper() and line[1][-1] == ":":
                char_names.add(line[0])
                char_frequency.append(line[0])
        except:
            continue

    return {
        "names": char_names,
        "frequency": char_frequency
        }


def find_location_names(script_text):
    """ Take script text, find location names, return locations & frequency

    Any items matching formatting of a location are added to a set (no
    duplicates) and also to a list (duplicates; tracks frequency of occurence)

    Set of locations & list of frequency are returned in a dictionary with
    collection titles ("names", "frequency") as keys & corresponding collections
    as values.
    """

    location_names = set()
    location_frequency = []

    for line in script_text:
        if line[0] == "[":
            location_names.add(line.rstrip())
            location_frequency.append(line.rstrip())

    return {
        "names": location_names,
        "frequency": location_frequency
        }


def collect_dialogue_by_speaker(characters, script_text):
    """ Takes characters dict & script text, returns dict of lines by speaker """
    dialogue_dict = {}

    for line in script_text:
        line = line.split()
        if len(line) < 1:
            pass
        else:
            if line[0].rstrip(":") in characters["names"]:
                if line[0].rstrip(":") not in dialogue_dict:
                    if line[1] == "[OC]:":
                        dialogue_dict[line[0].rstrip(":")] = [" ".join(line[2:])]
                    else:
                        dialogue_dict[line[0].rstrip(":")] = [" ".join(line[1:])]
                else:
                    if line[1] == "[OC]:":
                        dialogue_dict[line[0].rstrip(":")].append(" ".join(line[2:]))
                    else:
                        dialogue_dict[line[0].rstrip(":")].append(" ".join(line[1:]))

    return dialogue_dict


def open_and_read_script():
    """ Opens script file, returns list of all rows of text, closes file """

    script_text = [line for line in open(sys.argv[1])]
    return script_text


script_text = open_and_read_script()
characters = find_character_names(script_text)
locations = find_location_names(script_text)
dialogue_dict = collect_dialogue_by_speaker(characters, script_text)

print dialogue_dict
