#TODO: Create a letter using starting_letter.txt
import random

with open("./input/Letters/starting_letter.txt", "r") as l:
    letter = l.read()
    with (open("./input/Names/invited_names.txt", "r") as m):
        data = m.readlines()
        for name in data:
            stripped_name = name.strip()
            a = letter.replace("[name]", stripped_name)
            with open(f"Output/ReadyToSend/letter_of_{stripped_name}.docx", "w") as w:
                w.write(a)



#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp