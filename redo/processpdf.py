from PyPDF2 import PdfReader, PdfWriter
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
                        "Initiative": character.stats.DEXMod,
                        "ProfBonus": character.prof_bonus,

                        # Character Stats & Saves
                        "STR": character.stats.STR,
                        "STRmod": int(character.stats.STRMod),
                        "ST Strength": int(character.stats.STRSave),
                        "DEX": int(character.stats.DEX),
                        "DEXmod ": int(character.stats.DEXMod),
                        "ST Dexterity": int(character.stats.DEXSave),
                        "CON": int(character.stats.CON),
                        "CONmod": int(character.stats.CONMod) ,
                        "ST Constitution": int(character.stats.CONSave),
                        "INT": int(character.stats.INT),
                        "INTmod": int(character.stats.INTMod) ,
                        "ST Intelligence": int(character.stats.INTSave),
                        "WIS": int(character.stats.WIS),
                        "WISmod": int(character.stats.WISMod) ,
                        "ST Wisdom": int(character.stats.WISSave),
                        "CHA": int(character.stats.CHA),
                        "CHamod": int(character.stats.CHAMod) ,
                        "ST Charisma": int(character.stats.CHASave),

                        # Armor Class
                        "AC" : int(character.armor_class)
                        }
                    
    )

    # Process all proficiency scores
    # for i in range(len(skill_list)):
    #     for skill in skill_list[i]:
    #         if skill in character.skill_proficiencies:
    #             writer.update_page_form_field_values(
    #                 writer.pages[0], {skill: character.stats[statlist[i]+'mod'] + 2}
    #             )
    #         else:
    #             writer.update_page_form_field_values(
    #                 writer.pages[0], {skill: character.stats[statlist[i]+'mod']}
    #             )
    # # Process checkboxes for skills
    # for num in character.skill_checkboxes:
    #     writer.update_page_form_field_values(writer.pages[0], {f"Check Box {num}":"/Yes"})

    # # Process checkboxes for stat saves
    # for num in character.save_checkboxes:
    #     writer.update_page_form_field_values(writer.pages[0], {f"Check Box {num}":"/Yes"})

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