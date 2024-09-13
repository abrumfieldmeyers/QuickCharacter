import random
from charClasses import CharClass,ClassList
from charSpecies import CharSpecies,SpeciesList 
from charBacks import CharBack,BackList
from Stats import Stats

class Character:

    def __init__(self, player_name, char_name, char_class, char_back, char_species, random_stats):
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
        self.char_back = BackList[char_back]
        self.char_species = SpeciesList[char_species]

        # Derived from stats
        self.prof_bonus = 2
        self.set_stats(random_stats)
        self.set_hp()

        self.skill_prof = []
        self.tool_prof = []
        self.weapon_prof = []
        self.armor_prof = []
        self.set_proficiencies()
        self.armor_class = 10
    
    def __repr__(self) -> str:
        return (f"Name: {self.player_name}\nChar: {self.char_name}\nClass: {self.char_class.title}\nSpecies: {self.char_species.name}\nBack: {self.char_back.title}\nSTATS: \n{self.stats}")

    def set_stats(self, random_stats):
        ''' 
        Sets character stats and saving throws
        '''
        rolls=[]

        # Roll for stats if requested
        if (random_stats == True):
            # roll 4d6, drop lowest for each stat
            for i in range(6):
                roll=random.sample(range(1,7),4)
                roll.remove(min(roll))
                rolls.append(sum(roll))
        # use recommended stats if not
        else:
            rolls = self.char_class.stat_recs

        self.stats = Stats(rolls)

        # Add species bonuses to stats
        if self.char_species.stat_mod != {}:
            for key,val in self.char_species.stat_mod.items():
                self.stats.update_stat(key,val,False)
        print("After update stat")
        self.stats.printMods()

        # Update saving throws
        for stat in self.char_class.saving_throws:
            self.stats.update_save(stat,self.prof_bonus,False)
        print("After update saves")
        self.stats.printMods()


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
    
