"""
11 Str Save
18 - dex save
19 - con save
20 - int save
21 - wis save
22 - Cha save
23 - acro
24 - animal
25 - arcana
26 - athletics
27 - decep
28 - history
29 - insight
30 -intim
31 - invest
32 - med
33 - nature
34- percep
35 - perform
36- persuasion
37- religion
38 - sleight of hand
39 - stealth
40 -  survival
# 309 Spell stuff
# 3010 - 3083 
"""

check_map = {
    "STR":11,
    "DEX":18,
    "CON":19,
    "INT":20,
    "WIS":21,
    "CHA":22,
    "Acrobatics":23,
    "Animal Handling":24,
    "Arcana":25,
    "Athletics":26,
    "Deception":27,
    "History":28,
    "Insight":29,
    "Intimidation":30,
    "Investigation":31,
    "Medicine":32,
    "Nature": 33,
    "Perception":34,
    "Performance":35,
    "Persuasion":36,
    "Religion": 37,
    "Sleight of Hand": 38,
    "Stealth":39,
    "Survival":40
}

def fill_save_check(stat, lst):
    lst.append(check_map[stat])

def fill_skill_check(skill, lst):
    lst.append(check_map[skill])


# for i in range (11,41):
#     reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
#     writer = PdfWriter()

#     page = reader.pages[0]
#     fields = reader.get_fields()

#     writer.add_page(page)

#     writer.update_page_form_field_values(
#         writer.pages[0], {f"Check Box {i}":"/Yes"}
#     )

#     with open(f"./Checks/Checkbox_{i}.pdf", "wb") as output_stream:
#         writer.write(output_stream)
    