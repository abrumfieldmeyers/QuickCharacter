from PyPDF2 import PdfReader, PdfWriter
from weaponlist import weaponlist

skill_list_STR = ['Athletics' ]
skill_list_DEX = ['Acrobatics', 'SleightofHand', 'Stealth ']
skill_list_INT = [ 'Arcana', 'History ', 'Investigation ', 'Nature', 'Religion']
skill_list_WIS = [ 'Animal',  'Insight', 'Medicine', 'Perception ', 'Survival' ]
skill_list_CHA = [  'Deception ', 'Intimidation', 'Performance', 'Persuasion' ]
skill_list = [skill_list_STR, skill_list_DEX, skill_list_INT, skill_list_WIS, skill_list_CHA]
statlist = ['STR','DEX','INT','WIS','CHA']


def process(character):
    reader = PdfReader("5E_CharacterSheet_Fillable.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    fields = reader.get_fields()

    writer.add_page(page)

    writer.update_page_form_field_values(
        writer.pages[0], {
                        # General Attributes
                        "PlayerName": character.player_name, 
                        "ClassLevel": character.charclass + " 1", 
                        "CharacterName": character.char_name,
                        "Background": character.background,
                        "Race " : character.heritage,
                        "HPMax": character.max_hp,
                        "HPCurrent": character.max_hp,
                        "Speed": character.speed,
                        "Initiative": int(character.stats["DEXmod"]),
                        "ProfBonus": character.ProfBonus,

                        # Character Stats & Saves
                        "STR": int(character.stats["STR"]),
                        "STRmod": int(character.stats["STRmod"]),
                        "ST Strength": int(character.saves["STR"]),
                        "DEX": int(character.stats["DEX"]),
                        "DEXmod ": int(character.stats["DEXmod"]),
                        "ST Dexterity": int(character.saves["DEX"]),
                        "CON": int(character.stats["CON"]),
                        "CONmod": int(character.stats["CONmod"]) ,
                        "ST Constitution": int(character.saves["CON"]),
                        "INT": int(character.stats["INT"]),
                        "INTmod": int(character.stats["INTmod"]) ,
                        "ST Intelligence": int(character.saves["INT"]),
                        "WIS": int(character.stats["WIS"]),
                        "WISmod": int(character.stats["WISmod"]) ,
                        "ST Wisdom": int(character.saves["WIS"]),
                        "CHA": int(character.stats["CHA"]),
                        "CHamod": int(character.stats["CHAmod"]) ,
                        "ST Charisma": int(character.saves["CHA"]),

                        # Armor Class
                        "AC" : int(character.armorclass)
                        }
                    
    )

    # Process all proficiency scores
    for i in range(len(skill_list)):
        for skill in skill_list[i]:
            if skill in character.skill_proficiencies:
                writer.update_page_form_field_values(
                    writer.pages[0], {skill: character.stats[statlist[i]+'mod'] + 2}
                )
            else:
                writer.update_page_form_field_values(
                    writer.pages[0], {skill: character.stats[statlist[i]+'mod']}
                )
    # Process checkboxes for skills
    for num in character.skill_checkboxes:
        writer.update_page_form_field_values(writer.pages[0], {f"Check Box {num}":"/Yes"})

    # Process checkboxes for stat saves
    for num in character.save_checkboxes:
        writer.update_page_form_field_values(writer.pages[0], {f"Check Box {num}":"/Yes"})

    # Process equipment
    equipmentlist = ""
    gold = 0
    for item, quantity in character.equipment.items():
        if item == 'Gold':
            gold += int(quantity)
        else:
            equipmentlist += f"{item}\t\tx{quantity}\n"
    writer.update_page_form_field_values(
                    writer.pages[0], 
                    {"Equipment": equipmentlist, 
                        "GP": gold}  
                )

    # Process weapons
    for i in range(len(character.weapons)):
        # Add first weapon
        if i == 0:
            writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn Name":character.weapons[i]}
            )
            # Add attack bonus
            if weaponlist[character.weapons[i]][0] == "STR":
                writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn1 AtkBonus": str(character.stats["STRmod"] + 2), "Wpn1 Damage":weaponlist[character.weapons[i]][1] + "+" + str(character.stats["STRmod"])}
            )
            elif weaponlist[character.weapons[i]][0] == "DEX":
                writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn1 AtkBonus": str(character.stats["DEXmod"] + 2), "Wpn1 Damage":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["DEXmod"])}
            )
            elif weaponlist[character.weapons[i]][0] == "VERS":
                writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn1 AtkBonus": "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"])  + 2), "Wpn1 Damage":weaponlist[character.weapons[i]][1]+ "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"]))}
            )
            
        if i == 1:
            writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn Name 2":character.weapons[i]}
            )
            # Add attack bonus
            if weaponlist[character.weapons[i]][0] == "STR":
                writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn2 AtkBonus ":"+" +  str(character.stats["STRmod"] + 2), "Wpn2 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["STRmod"])}
            )
            
            elif weaponlist[character.weapons[i]][0] == "DEX":
                writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn2 AtkBonus ": "+" + str(character.stats["DEXmod"] + 2), "Wpn2 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["DEXmod"])}
            )
            elif weaponlist[character.weapons[i]][0] == "VERS":
                writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn2 AtkBonus ": "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"])  + 2), "Wpn2 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"]))}
            )
        if i == 2:
            writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn Name 3":character.weapons[i]}
            )
            # Add attack bonus
            if weaponlist[character.weapons[i]][0] == "STR":
                writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn3 AtkBonus  ":"+" +  str(character.stats["STRmod"] + 2), "Wpn3 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["STRmod"])}
            )
            
            elif weaponlist[character.weapons[i]][0] == "DEX":
                writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn3 AtkBonus  ": "+" + str(character.stats["DEXmod"] + 2), "Wpn3 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["DEXmod"])}
            )
            elif weaponlist[character.weapons[i]][0] == "VERS":
                writer.update_page_form_field_values(
                    writer.pages[0],{"Wpn3 AtkBonus  ": "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"])  + 2), "Wpn3 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"]))}
            )
        
            



    # write "output" to PyPDF2-output.pdf
    with open(f"./Sheets/{character.char_name}_Level_1.pdf", "wb") as output_stream:
        writer.write(output_stream)
    return
# process('h')