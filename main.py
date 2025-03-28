"""
Implement a program that : 
- Prompts the user for input (random music key / string of keys). Can be on a random string or all at once (Menu)
- List of naturals and accidentals OR one list for naturals, one for sharps, one for flats
- Accidentals are all there, even the same ones, but don't follow themselves (e.g. : G# and Ab, which are the
same, don't follow themselves)
- Maybe one natural and one accidental for the list, with changing order
- Need to implement menu and submenu to abstract all the conditions in main and the calling of other functions
"""
import random

def main() :
    
    print("Hello and welcome to Music Companion !\n"\
          "Press Ctrl + C to quit the program. Have fun practising ! :D")
    
    while True : 
        try :   
            choice = int(input("Choose an option :\n"  \
                        "1 for a random list of naturals / flats / sharps\n" \
                        "2 for a random list of all notes altogether\n"
                        ))
            if choice == 1 :
                choice2 = int(input("Choose an option :\n"
                "1 for Naturals\n"
                "2 for Flats\n"
                "3 for Sharps\n"))
                if choice2 == 1 :
                    selected_notes, number = notes_selection(choice2)
                    print(rand_list(selected_notes, number))
                elif choice2 == 2 :
                    selected_notes, number = notes_selection(choice2)
                    print(rand_list(selected_notes, number))
                elif choice2 == 3 :
                    selected_notes, number = notes_selection(choice2) 
                    print(rand_list(selected_notes, number))
                else : 
                    print("I didn't understand your request. Can you repeat, please ?")
            elif choice == 2 : 
                print(rand_all())
            else :
                print("Enter a valid selection number, please.\n")

        except ValueError : 
            print("What's that ? I didn't understand your request. Can you repeat, please ?\n")
        except KeyboardInterrupt :
            print("\nQuitting the program...\n"\
                "Goodbye ! :D")
            break
    


# def string_menu() :
#     choice = int(input("Choose between :\n"   \
#                 "1 for doing an exercise on a specific string\n"   \
#                 "2 for doing an exercise on all the strings\n"))
#     if choice == 1 : 
#         one_string = True
#     elif choice == 2 :
#         one_string = False
#     else : 
#         print("Enter a valid selection number, please.\n")
#     return one_string



# def list_menu() :
#     choice = int(input("Choose between :\n"   \
#         "1 for a random list of Naturals, Flats or Sharps\n"   \
#         "2 for a random list of all notes altogether\n"))
#     if choice == 1 :
#         choice = int(input("Choose between :\n"   \
#         "1 for Naturals\n"  \
#         "2 for Flats\n"  \
#         "3 for Sharps\n"))
#         return choice
#     elif choice == 2 :
#         return print(rand_all())
#     else :
#         print("Enter a valid selection number, please.\n")



def notes_selection(choice2):
    """
    Choose a list of notes between Naturals, Flats or Sharps;  
    Then return the list of notes and its length as an integer
    """
    naturals = ["A","B","C","D","E","F","G"]
    flats = ["Ab","Bb","Db","Eb","Gb"]
    sharps = ["A#","C#","D#","F#","G#"]

    if choice2 == 1 :
        return naturals, 7
    elif choice2 == 2 : 
        return flats, 5
    else :
        return sharps, 5    



def rand_list(selected_notes, number) :
    """ Gives a random list of naturals OR sharps OR flats  
    'number' is used to dynamically adapt the length of the list, as there are 7 naturals, 5 sharps and 5 flats
    """

    random_notes = []

    while len(random_notes) < number :
        index = random.randint(0,len(selected_notes)-1) # Getting index of random note from naturals
        if selected_notes[index] in random_notes : # If the note is already in the list, keep generating
            continue
        else :
            random_notes.append(selected_notes[index])

    return random_notes



def rand_all():
    """
    Gives a string of all notes combined  
    TO DO : Need to make sure the same notes don't follow themselves  
    Break the problem :
    A number between 0 and 16 is generated (i.e : 3 / Bb)
    Program check if random_notes is empty
    if true, add note
    if false :
    check if the last entry - new rand < 2
    if true : continue
    else add number
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
        # elif len(random_notes) != 0 and last_index != None and index - last_index < 2 :
        #     continue
        else :
            random_notes.append(notes[index]) # Add the whole note to the list (not just 1st character)
            # last_index = index
            
    return random_notes



def check_same_notes(notes_list) :
    """
    Check wheter or not the list contains two same notes following each other  
    NOT WORKING COMPLETELY
    """

    same_notes = [
        "F#, Gb", "Gb, F#"
        "G#, Ab", "Ab, G#"
        "A#, Bb", "Bb, A#"
        "C#, Db", "Db, C#"
        "D#, Eb", "Eb, D#"]




def notes_letter(notes_list):
    """
    Check whether or not the last two entries of the list are the same letters
    TO DO
    """
    
def rand_string() :
    """
    Selects a random string to play on.
    """

    strings = ["E","A","D","G","B","E"]

    index = random.randint(0, len(strings)-1)

    return strings[index]


main()