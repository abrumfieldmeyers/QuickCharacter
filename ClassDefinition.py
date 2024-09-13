import random
import charbackgrounds
import charclasses
from find_checks import fill_save_check, fill_skill_check, check_map
import charspecies
from weaponlist import weaponlist


class Character:
    def __init__(self, char_name, player_name, char_class, char_back, char_heritage, stats):
        self.char_name = char_name
        self.player_name = player_name
        self.heritage = char_heritage
        self.charclass = char_class
        self.background = char_back
        self.speed = 30
        self.ProfBonus = 2
        self.class_skill_number = charclasses.classes[char_class]['skill number']
        self.heritage_skill_number = 0
        self.skill_proficiencies = []
        self.tool_proficiencies = []
        self.weapon_proficiencies = []
        self.armor_proficiencies = []
        self.save_checkboxes = []            # Used for checking proficiencies
        self.skill_checkboxes = []
        self.set_proficiencies()
        self.stats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.saves = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.roll_stats(stats)
        self.saving_throws()
        self.set_hp()
        # self.abilities = []
        # self.abilities.append(self.background['feature'])
        self.armor = []
        self.armorclass = 0
        self.get_armor()
        self.weapons = []
        self.get_weapons()
        self.equipment = {}
        self.get_equipment()
        

    def __repr__(self):

        # Create strings for proficiencies
        prof_str = ', '.join(self.skill_proficiencies)
        tool_str = ', '.join(self.tool_proficiencies)
        armor_str = ', '.join(self.armor_proficiencies)
        weapon_str = ', '.join(self.weapon_proficiencies)
        stats_str = ', '.join(self.stats)

        # Return description of character
        
        return f'Your name is {self.player_name} \nYour character is {self.char_name}, ' \
               f'the {self.heritage} {self.charclass} ' \
               f'\nYour background is {self.background}\n' \
               f'Skills:\t {prof_str}\n' \
               f'Tools:\t{tool_str}\nArmor:\t{armor_str}\nWeapons:\t{weapon_str}\n' \
               f'Strength: {self.stats["STR"]} Dexterity: {self.stats["DEX"]} \nConstitution: {self.stats["CON"]} Intelligence: {self.stats["INT"]} \nWisdom: {self.stats["WIS"]} Charisma: {self.stats["CHA"]}'

    def set_hp(self):
        self.max_hp = self.stats["CONmod"] + charclasses.classes[self.charclass]['hit_die']

    def saving_throws(self):
        # Update saving throws based on class choice
        for stat in self.saves:
            # save = stat mod. If save is in class saves, += 2.
            if stat in charclasses.classes[self.charclass]['saving_throws']:
                self.saves[stat] = 2 + self.stats[stat+'mod']
                # Add the appropriate checkbox to list to check off.
                fill_save_check(stat, self.save_checkboxes)
            else:
                self.saves[stat] = self.stats[stat+ 'mod']
        
        
    def set_proficiencies(self):
        # Look at background, class, heritage for tool/armor/weapon profs
        count = 0   # Used to skip adding class skills twice
        for source in [charclasses.classes[self.charclass], charbackgrounds.bgds[self.background],
                       charspecies.heritages[self.heritage]]:
            if len(source['skill proficiencies']) != 0:
                # count = 0 when we're looking at class skills, need to skip
                if count != 0:
                    for item in source['skill proficiencies']:
                        self.skill_proficiencies.append(item)
                        # Add appropriate checkbox for each proficient skill
                        fill_skill_check(item, self.skill_checkboxes)
            if len(source['tool proficiencies']) != 0:
                for item in source['tool proficiencies']:
                    self.tool_proficiencies.append(item)

            if len(source['armor proficiencies']) != 0:
                for item in source['armor proficiencies']:
                    self.armor_proficiencies.append(item)

            if len(source['weapon proficiencies']) != 0:
                for item in source['weapon proficiencies']:
                    self.weapon_proficiencies.append(item)
            count += 1

        # Sort each prof list
        self.skill_proficiencies.sort()
        self.tool_proficiencies.sort()
        self.armor_proficiencies.sort()
        self.weapon_proficiencies.sort()

        # Update skill number
        try:
            self.class_skill_number += charspecies.heritages[self.heritage]['skill number']
        except KeyError:
            pass

    def get_equipment(self):
        # check background for any equipment
        
        for item, quantity in charbackgrounds.bgds[self.background]['equipment'].items():
            self.equipment[item] = quantity
        for item, quantity in charclasses.classes[self.charclass]['equipment'].items():
            self.equipment[item] = quantity
        for item in self.armor:
            self.equipment[item] = 1
       
        print(self.equipment)

    def get_weapons(self):
        # Store weapons in self
        if len(charclasses.classes[self.charclass]['weapons']) != 0:
            for item in charclasses.classes[self.charclass]['weapons']:
                self.weapons.append(item)
            
    def get_armor(self):
        # Check class for any armor provided
        armors = {
            'Leather Armor': 11,
            "Studded Leather Armor": 12,
            "Hide": 12,
            "Chain Shirt": 13,
            "Scale Mail": 14,
            "Breastplate": 14,
            "Half Plate": 15,
            "Chain Mail": 16,
            "Shield": 2 
        }

        # Add equipped armor to Armor Class
        if len(charclasses.classes[self.charclass]['armor']) != 0:
            for item in charclasses.classes[self.charclass]['armor']:
                self.armorclass += armors[item]
                self.armor.append(item)
            self.armorclass += self.stats["DEXmod"]
        if self.charclass == "Monk":
            self.armorclass = max(self.armorclass, (10 + self.stats["DEXmod"] + self.stats["WISmod"]))
        if self.charclass == "Barbarian":
            self.armorclass = max(self.armorclass, (10 + self.stats["DEXmod"] + self.stats["CONmod"]))

    def roll_stats(self, stats):
        # uses random to roll for stats
        if stats == 'Random':
            # Roll for stats randomly
            
            saved_rolls = []
            for i in range(6):
                roll = []
                while len(roll)<4:
                    roll.append(random.randint(1,6))
                roll.remove(min(roll))
                saved_rolls.append(sum(roll))
            print("Rolls: " + str(saved_rolls))
            
            # assign rolls to stats
            for key, value in self.stats.items():
                
                temp = random.choice(saved_rolls)
                self.stats[key] = temp 
                saved_rolls.remove(temp)


        else:
            print("RECOMMENDED ROLLS!")
            
            # print(backgrounddicts.bgds[self.background])
            self.stats['STR'] = charclasses.classes[self.charclass]['stat_rec'][0]
            self.stats['DEX'] = charclasses.classes[self.charclass]['stat_rec'][1]
            self.stats['CON'] = charclasses.classes[self.charclass]['stat_rec'][2]
            self.stats['INT'] = charclasses.classes[self.charclass]['stat_rec'][3]
            self.stats['WIS'] = charclasses.classes[self.charclass]['stat_rec'][4]
            self.stats['CHA'] = charclasses.classes[self.charclass]['stat_rec'][5]

            

            print('Your character\'s stats are: \nSTR: ' + str(self.stats['STR']) + '\nDEX: ' + str(self.stats['DEX']) +
              '\nCON: ' + str(self.stats['CON']) + '\nINT: ' + str(self.stats['INT']) + '\nWIS: '
              + str(self.stats['WIS']) + '\nCHA: ' +str(self.stats['CHA']) )
        
        # Add heritage bonuses to stats
        for key, value in charspecies.heritages[self.heritage]['stat_bonus'].items():
            self.stats[key] += value

        # Convert Stats to stat modifiers
        self.stats["STRmod"] = (self.stats["STR"] - 10) // 2
        self.stats["DEXmod"] = (self.stats["DEX"] - 10) // 2
        self.stats["CONmod"] = (self.stats["CON"] - 10) // 2
        self.stats["INTmod"] = (self.stats["INT"] - 10) // 2
        self.stats["WISmod"] = (self.stats["WIS"] - 10) // 2
        self.stats["CHAmod"] = (self.stats["CHA"] - 10) // 2





if __name__ == '__main__':
    jeff=Character('Rognar the Blue','Jeffery Stork', 'Bard','Acolyte', 'Human',"Recommended")
    print(jeff)
