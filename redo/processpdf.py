from PyPDF2 import PdfReader, PdfWriter
from find_checks import get_skill_check
# from weaponlist import weaponlist

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
                        "ClassLevel": str(character.char_class.name) + " 1", 
                        "CharacterName": character.char_name,
                        "Background": character.char_back.name,
                        "Race " : character.char_species.name,
                        "HPMax": character.max_hp,
                        "HPCurrent": character.current_hp,
                        "Speed": character.speed,
                        "Initiative": character.stats.DEX.mod,
                        "ProfBonus": character.prof_bonus,

                        # Character Stats & Saves
                        "STR": character.stats.STR.value,
                        "STRmod": character.stats.STR.mod,
                        "ST Strength": character.stats.STR.save_mod,
                        "DEX": character.stats.DEX.value,
                        "DEXmod ": character.stats.DEX.mod,
                        "ST Dexterity": character.stats.DEX.save_mod,
                        "CON": character.stats.CON.value,
                        "CONmod": character.stats.CON.mod ,
                        "ST Constitution": character.stats.CON.save_mod,
                        "INT": character.stats.INT.value,
                        "INTmod": character.stats.INT.mod ,
                        "ST Intelligence": character.stats.INT.save_mod,
                        "WIS": character.stats.WIS.value,
                        "WISmod": character.stats.WIS.mod,
                        "ST Wisdom": character.stats.WIS.save_mod,
                        "CHA": character.stats.CHA.value,
                        "CHamod": character.stats.CHA.mod,
                        "ST Charisma": character.stats.CHA.save_mod,

                        # Armor Class
                        "AC" : int(character.armor_class),
                        # Hit Die
                        "HDTotal" : "1d"+str(character.char_class.hit_die),
                        "HD" : "1",

                        "Passive": 10 + int(character.skill_list.Perception.value)


                        }
                    
    )

    # Process all proficiency scores
    for s in vars(character.skill_list):
        if s == "proficient_skills" or s == "expertise_skills":
            continue
        # Check box for proficient/expertise skills
        skl = getattr(character.skill_list,s)
        if skl.prof == True or skl.exp == True:
            num = get_skill_check(s)
            writer.update_page_form_field_values(writer.pages[0], {f"Check Box {num}":"/Yes"})
        
        # Minor processing to account for weirdly named PDF fields
        if s == "AnimalHandling":
            s = "Animal"
        elif s == "Deception":
            s = "Deception "
        elif s == "History":
            s = "History "
        elif s == "Investigation":
            s = "Investigation "
        elif s == "Perception":
            s = "Perception "
        elif s == "SleightOfHand":
            s = "SleightofHand"
        elif s == "Stealth":
            s = "Stealth "
        writer.update_page_form_field_values(
            writer.pages[0], {s: skl.value}
        )
    
    # Process checkboxes for stat saves
    for num in character.save_checks:
        writer.update_page_form_field_values(writer.pages[0], {f"Check Box {num}":"/Yes"})

    # # Process equipment
    # equipmentlist = ""
    # gold = 0
    # for item, quantity in character.equipment.items():
    #     if item == 'Gold':
    #         gold += int(quantity)
    #     else:
    #         equipmentlist += f"{item}\t\tx{quantity}\n"
    # writer.update_page_form_field_values(
    #                 writer.pages[0], 
    #                 {"Equipment": equipmentlist, 
    #                     "GP": gold}  
    #             )

    # # Process weapons
    # for i in range(len(character.weapons)):
    #     # Add first weapon
    #     if i == 0:
    #         writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn Name":character.weapons[i]}
    #         )
    #         # Add attack bonus
    #         if weaponlist[character.weapons[i]][0] == "STR":
    #             writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn1 AtkBonus": str(character.stats["STRmod"] + 2), "Wpn1 Damage":weaponlist[character.weapons[i]][1] + "+" + str(character.stats["STRmod"])}
    #         )
    #         elif weaponlist[character.weapons[i]][0] == "DEX":
    #             writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn1 AtkBonus": str(character.stats["DEXmod"] + 2), "Wpn1 Damage":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["DEXmod"])}
    #         )
    #         elif weaponlist[character.weapons[i]][0] == "VERS":
    #             writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn1 AtkBonus": "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"])  + 2), "Wpn1 Damage":weaponlist[character.weapons[i]][1]+ "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"]))}
    #         )
            
    #     if i == 1:
    #         writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn Name 2":character.weapons[i]}
    #         )
    #         # Add attack bonus
    #         if weaponlist[character.weapons[i]][0] == "STR":
    #             writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn2 AtkBonus ":"+" +  str(character.stats["STRmod"] + 2), "Wpn2 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["STRmod"])}
    #         )
            
    #         elif weaponlist[character.weapons[i]][0] == "DEX":
    #             writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn2 AtkBonus ": "+" + str(character.stats["DEXmod"] + 2), "Wpn2 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["DEXmod"])}
    #         )
    #         elif weaponlist[character.weapons[i]][0] == "VERS":
    #             writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn2 AtkBonus ": "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"])  + 2), "Wpn2 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"]))}
    #         )
    #     if i == 2:
    #         writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn Name 3":character.weapons[i]}
    #         )
    #         # Add attack bonus
    #         if weaponlist[character.weapons[i]][0] == "STR":
    #             writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn3 AtkBonus  ":"+" +  str(character.stats["STRmod"] + 2), "Wpn3 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["STRmod"])}
    #         )
            
    #         elif weaponlist[character.weapons[i]][0] == "DEX":
    #             writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn3 AtkBonus  ": "+" + str(character.stats["DEXmod"] + 2), "Wpn3 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(character.stats["DEXmod"])}
    #         )
    #         elif weaponlist[character.weapons[i]][0] == "VERS":
    #             writer.update_page_form_field_values(
    #                 writer.pages[0],{"Wpn3 AtkBonus  ": "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"])  + 2), "Wpn3 Damage ":weaponlist[character.weapons[i]][1]+ "+" + str(max(character.stats["STRmod"],character.stats["DEXmod"]))}
    #         )
        
            



    # write "output" to PyPDF2-output.pdf
    with open(f"./Sheets/{character.char_name}_Level_1.pdf", "wb") as output_stream:
        writer.write(output_stream)
    return
# process('h')