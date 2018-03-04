""" Generate Markov Text by Blending Multiple TV and/or Play Scripts """
# import markov
import sys


def find_character_names(script_text):
    """ Take script text, generate set of character names, return names """
    dramatis_personae = [name.strip(':') for name in script_text.split() if len(name) > 3 and name.isupper() and name[0] != "["]

    return set(dramatis_personae)


def find_location_names(script_text):
    """ Take script text, generate set of location names, return locations """
    locations = [place for place in script_text.split() if place[0] == "[" and place[-1] == "]"]

    return set(locations)


def open_and_read_script():
    """ Opens script file, returns string with full text """

    script_text = open(sys.argv[1]).read()

    return script_text


script_text = open_and_read_script()
print find_character_names(script_text)
print find_location_names(script_text)
