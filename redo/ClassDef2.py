import random
from charClasses import CharClass,ClassList
from charSpecies import CharSpecies,SpeciesList 
from charBacks import CharBack,BackList
from find_checks import fill_skill_check,fill_save_check
from Stats import Stats
from SkillList import SkillList
from Feature import Features

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
        self.speed = self.char_species.speed

        # Derived from stats
        self.prof_bonus = 2
        self.save_checks = []
        self.set_stats(random_stats)
        self.set_hp()

        self.skill_prof = []
        self.tool_prof = []
        self.weapon_prof = []
        self.armor_prof = []
        self.set_proficiencies()
        self.skill_list = SkillList(self.stats,self.skill_prof)
        self.armor_class = 10

        self.features = self.set_features()
        
    
    def __repr__(self) -> str:
        return (f"Name: {self.player_name}\nChar: {self.char_name}\nClass: {self.char_class.name}\nSpecies: {self.char_species.name}\nBack: {self.char_back.name}\nSTATS: \n{self.stats}")

    def set_stats(self, random_stats):
        ''' 
        Sets character stats and saving throws
        '''
        rolls=[]

        # Roll for stats if requested
        if (random_stats == "True"):
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
        
        # Update saving throws
        for stat in self.char_class.saving_throws:
            self.stats.update_save(stat,self.prof_bonus,False)
            fill_save_check(stat,self.save_checks)
        
        return
    
    def set_hp(self):
        '''
        Sets character HP
        '''
        # Set baseline HP from CON mod + class
        self.max_hp = self.char_class.hit_die + self.stats.CON.mod
        # Check species hp bonuses

        # Check class hp bonuses

        self.current_hp = self.max_hp
        return
    
    def set_proficiencies(self):
        '''
        Sets character proficiencies: skills, tools, armor, weapons
        '''
        skills_to_pick = 0
        sources = [self.char_back,self.char_species,self.char_class]
        # Add weapon, armor, and tool prof from background, species, and class
        # Add skill proficiencies from only background and species. 
        # Class skill proficiencies are added later
        for source in sources:
            for p in source.armor_prof:
                self.armor_prof.append(p)
            for p in source.weapon_prof:
                self.weapon_prof.append(p)
            for p in source.tool_prof:
                self.tool_prof.append(p)
            if source != self.char_class:
                for p in source.skill_prof:
                    self.skill_prof.append(p)


        skills_to_pick += self.char_species.skill_count
        skills_to_pick += self.char_class.skill_count   
        available_skills = [skill for skill in self.char_class.skill_prof if skill not in self.skill_prof]
        
        # Select Class Skills
        # TODO We will use text prompt here, but need to find a dif way to handle this for other projects
        while skills_to_pick >0:
            for i in range(len(available_skills)):
                print(f"{i+1}: {available_skills[i]}")
            pick = input("Select a skill: ")
            if pick== '' or int(pick)<1 or int(pick)> len(available_skills):   # TODO string protection
                continue
            self.skill_prof.append(available_skills[int(pick)-1])
            available_skills.remove(available_skills[int(pick)-1])
            skills_to_pick -= 1

            
        self.skill_prof.sort()
        self.weapon_prof.sort()
        self.armor_prof.sort()
        self.tool_prof.sort()
        # self.printProfs()
        return
    
    def printProfs(self):
        # Print all proficiencies 
        print("\nWeapon Profs:")
        for p in self.weapon_prof:
            print(p)
        print("\nArmor Profs:")
        for p in self.armor_prof:
            print(p)
        print("\nTool Profs:")
        for p in self.tool_prof:
            print(p)
        print("\nSkill Profs:")
        for p in self.skill_prof:
            print(p,",")
        print("-----------------")

    def add_feature(self,feature_list,new_feature):
        feature_list.append(new_feature)
        for mod in new_feature.mods:
            mod(self)

    def set_features(self):
        feature_list = []
        self.add_feature(feature_list,self.char_back.feature)
        for f in self.char_class.features:
            self.add_feature(feature_list,f)
        for f in self.char_species.features:
            self.add_feature(feature_list,f)

        return feature_list
