import random
import charbackgrounds
from charClasses import CharClass,ClassList
from charSpecies import CharSpecies,SpeciesList 
from charBacks import CharBack,BackList
from find_checks import fill_save_check, fill_skill_check, check_map

from weaponlist import weaponlist

class Character:

    def __init__(self, char_name, player_name, char_class, char_back, char_species, random_stats):
        '''
        char_name = String
        player_name = String
        char_class = String that exists within charclasses.py
        char_back = String that exists within charbackgrounds.py
        char_species = String that exists within charspecies.py
        random_stats
        '''
        self.char_name = char_name
        self.player_name = player_name
        self.char_class = ClassList[char_class]
        self.char_back = char_back
        self.char_species = SpeciesList[char_species]

        # Derived from stats
   
        self.set_stats(random_stats)
        self.set_hp()

        self.skill_prof = []
        self.tool_prof = []
        self.weapon_prof = []
        self.armor_prof = []
        self.set_proficiencies()
        self.armor_class = 10







    def set_stats(self, random_stats):
        ''' 
        Sets character stats and saving throws
        '''
        self.stats = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        self.saves = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}
        # Roll for stats if requested

        # use recommended stats if not

        # Add heritage bonuses to stats

        # save stat modifiers

        # Update saving throws
        return
    
    def set_hp(self):
        '''
        Sets character HP
        '''
        # Set baselin HP from CON mod + class
        self.max_hp = 10
        # Check species hp bonuses

        # Check class hp bonuses

        return
    
    def set_proficiencies(self):
        '''
        Sets character proficiencies: skills, tools, armor, weapons
        '''
        # Add all proficiencies from classes[self.char_class]
        # 
        # Add all proficiencies from species[self.char_species]
        # 
        # Add all proficiencies from backgrounds[self.char_background] 

        # Sort profs for readability

        # Update count for class skills not yet selected
        return
    
