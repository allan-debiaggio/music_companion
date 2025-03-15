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
    
    print("Hello and welcome to the Music Companion !\n"\
          "Press Ctrl + C to quit the program. Have fun practising ! :D")
    
    while True : 
        try :
            user = int(input("Choose an option :\n"  \
                        "1 for a random list of naturals / sharps / flats\n" \
                        "2 for a random list of all notes altogether\n"
                        ))
            if user == 1 :
                print(rand_list())
            elif user == 2 : 
                print(rand_all())
        except ValueError : 
            print("What's that ? I didn't understand your request. Can you repeat, please ?\n")
        except KeyboardInterrupt :
            print("\nQuitting the program...\n"\
             "Goodbye ! :D")
            break



def rand_list() :
    """ Function where you can get separated list of naturals / sharps / flats """
    
    naturals = ["A","B","C","D","E","F","G"]
    sharps = ["A#","C#","D#","F#","G#"]
    flats = ["Ab","Bb","Db","Eb","Gb"]
    random_notes = []

    while len(random_notes) < 7 :
        index = random.randint(0,len(naturals)-1) # Getting index of random note from naturals
        if naturals[index] in random_notes : # If the note is already in the list, keep generating
            continue
        else :
            random_notes += (naturals[index])

    return random_notes



def rand_all():
    """
    Function where you can get a string of all notes combined  
    TO DO : Need to make sure the same notes don't follow themselves  
    Idea : Create a list where to put same notes,  
    If combo in list then throw another rand,  
    Elif same letter in note that follows, throw another rand
    """

    notes = [
        "Ab","A","A#",
        "Bb","B",
        "C","C#",
        "Db","D","D#",
        "Eb","E",
        "F","F#",
        "Gb","G","G#"]

    random_notes = []

    while len(random_notes) < 17 :
        index = random.randint(0, len(notes)-1)

        if notes[index] in random_notes :
            continue
        elif check_same_notes(random_notes) :
            continue
        else :
            random_notes.append(notes[index]) # Add the whole note to the list (not just 1st character)
    return random_notes



def check_same_notes(notes_list) :
    """
    Function to check wheter or not the list contains two same notes following each other  
    NOT WORKING COMPLETELY
    """

    same_notes = [
        "F#, Gb", "Gb, F#"
        "G#, Ab", "Ab, G#"
        "A#, Bb", "Bb, A#"
        "C#, Db", "Db, C#"
        "D#, Eb", "Eb, D#"]
    
    if same_notes in notes_list :
        return True
    else :
        return False


main()