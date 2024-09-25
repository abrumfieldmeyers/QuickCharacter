from Skill import Skill
from find_checks import get_skill_check

class SkillList:
    def __init__(self,stats,skill_profs):
        self.Acrobatics = Skill("Acrobatics","DEX",stats.DEX.mod)
        self.AnimalHandling = Skill("AnimalHandling","CHA",stats.CHA.mod)
        self.Arcana = Skill("Arcana","INT",stats.INT.mod)
        self.Athletics = Skill("Athletics","STR",stats.STR.mod)
        self.Deception = Skill("Deception","CHA",stats.CHA.mod)
        self.History = Skill("History","INT",stats.INT.mod)
        self.Insight = Skill("Insight","WIS",stats.WIS.mod)
        self.Intimidation = Skill("Intimidation","CHA",stats.CHA.mod)
        self.Investigation = Skill("Investigation","INT",stats.INT.mod)
        self.Medicine = Skill("Medicine","INT",stats.INT.mod)
        self.Nature = Skill("Nature","INT",stats.INT.mod)
        self.Perception = Skill("Perception","WIS",stats.WIS.mod)
        self.Performance = Skill("Performance","CHA",stats.CHA.mod)
        self.Persuasion = Skill("Persuasion","CHA",stats.CHA.mod)
        self.Religion = Skill("Religion","INT",stats.INT.mod)
        self.SleightofHand = Skill("SleightOfHand","DEX",stats.DEX.mod)
        self.Stealth = Skill("Stealth","DEX",stats.DEX.mod)
        self.Survival = Skill("Survivial","WIS",stats.WIS.mod)
        self.proficient_skills = {} # Tracks names and checkbox # of skills that are marked as proficient
        self.expertise_skills = {} # TODO Tracks names and checkbox # of skills that are marked as expertise
        self.set_proficient_skills(skill_profs)


    def set_proficient_skills(self,skill_profs):
        # skill_profs: list of names of skills that character is proficient in
        for skill in skill_profs:
            toUpdate = getattr(self,skill.replace(" ",""))  # Strip to avoid whitespace issues
            toUpdate.set_prof(True)
            self.proficient_skills[skill] = get_skill_check(skill)
        
    def __repr__(self):
        print(self.proficient_skills)
        return (f"{self.Acrobatics}\n{self.Athletics}\n{self.AnimalHandling}\n{self.Arcana}\n{self.Deception}\n{self.History}\n{self.Insight}\n{self.Intimidation}\n{self.Investigation}\n{self.Medicine}\n{self.Nature}\n{self.Perception}\n{self.Performance}\n{self.Persuasion}\n{self.Religion}\n{self.SleightOfHand}\n{self.Stealth}\n{self.Survival}\n")


    