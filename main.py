"""
Implement a program that : 
- Prompts the user for input (random music key / string of keys). Can be on a random string or all at once (Menu)
- List of naturals and accidentals OR one list for naturals, one for sharps, one for flats
- Accidentals are all there, even the same ones, but don't follow themselves (e.g. : G# and Ab, which are the
same, don't follow themselves)
- Maybe one natural and one accidental for the list, with changing order
"""
import random

def main() :
    print("Hello and welcome to the Music Companion !")
    # user = input("Choose an option")
    print(random_list())

def random_list() :
    naturals = ["A","B","C","D","E","F","G"]
    sharps = ["A#","C#","D#","F#","G#"]
    flats = ["Ab","Bb","Db","Eb","Gb"]
    random_notes = []
    while len(random_notes) < 7 :
        index = random.randint(0,len(naturals)-1)
        if naturals[index] in random_notes :
            continue
        else :
            random_notes += (naturals[index])
    return random_notes


main()