from tkinter import *
import backgrounddicts
import heritage
import charclasses
from ClassDefinition import Character
from processpdf import process

root = Tk()
root.title('Generate Your Character')
#root.iconbitmap("c:/testicon.ico")
root.geometry('600x500')


# Function to get data from entries

def result():
    # First Confirm that all info is in place
    try:
        new_char = Character(character_name.get(),  player_name.get(), char_class.get(),
                                             background.get(), h.get(), stats.get())
        # print(new_char)
    except KeyError:
        return

    # Within this frame, func for selecting proficiencies
    # func to save profs
    def save_prof():
        if len(lb.curselection()) > new_char.class_skill_number:
            pass
        else:
            for i in lb.curselection():
                new_char.skill_proficiencies.append(charclasses.classes[new_char.charclass]['skill proficiencies'][i])
            # print(new_char)
            process(new_char)
            skillframe.destroy()

    # Build frame for choosing proficiencies
    skillframe = LabelFrame(root, text=f'Choose up to {new_char.class_skill_number} proficiencies', padx=5, pady=10)
    skillframe.grid(row=9, column=0)

    # Listbox for applicable profs
    profs = [p for p in charclasses.classes[new_char.charclass]['skill proficiencies'] if p not in new_char.skill_proficiencies]
    profs_var = StringVar(value=profs)
    lb = Listbox(skillframe, listvariable=profs_var, selectmode='multiple')
    lb.grid(row=1, column=0)

    # Create button for saving profs
    save_btn = Button(skillframe, text=f'Save your character', bg='light green', command=save_prof)
    save_btn.grid(row=1, column=2)


# General info to gather
# Text box for player name
player_name = Entry(root, width=50, borderwidth=10)
player_name.insert(0, 'Player Name:')
player_name.grid(row=0, column=0, columnspan=2)

# Text box for character name
character_name = Entry(root, width=50, borderwidth=10)
character_name.insert(0, 'Character Name:')
character_name.grid(row=1, column=0, columnspan=2)

# Dropdown for Heritage
heritage_label = Label(root, text='Heritage').grid(row=2, column=0)
h = StringVar()
h.set('Heritage')
heritage_drop = OptionMenu(root, h, *heritage.heritages).grid(row=2, column=1)

# Dropdown for background
background_label = Label(root, text='Background').grid(row=3, column=0)
background = StringVar()
background.set('Backgrounds')
background_drop = OptionMenu(root, background, *backgrounddicts.bgds).grid(row=3, column=1)


# Dropdown for Class
class_label = Label(root, text='Class').grid(row=4, column=0)
char_class = StringVar()
char_class.set('Classes')
class_drop = OptionMenu(root, char_class, *charclasses.classes).grid(row=4, column=1)

# Selector for stat choice
# stat_frame = LabelFrame(root, text="Stat generation").grid(row=6, column=0)
stat_label = Label(root, text="Select one stat generation method:").grid(row=5, column=0)
stats = StringVar()
s1 = Radiobutton(root, variable=stats, text="Recommended", value="Recommended" ).grid(row=6, column=0)
s2 = Radiobutton(root, variable=stats, text="Random", value="Random" ).grid(row=7, column=0)


# Button for gathering results
result_btn = Button(root, text='Next', command=result, bg='yellow').grid(row=8, column=0, columnspan=2)

# Create event Loop:
# when running a program, it's always looping. when mouse move,input,key input, notices difference in loop
root.mainloop()
