

class Skill:
    def __init__(self,name,stat_used,value,prof=False,exp=False):
        self.name = name
        self.stat_used = stat_used
        self.base = value   # Base is used just for stat mod without including proficiency
        self.value = value  # Value includes proficiency if skill is proficient
        self.prof = False
        self.exp = False

    def set_prof(self,is_prof,prof_val=2):
        # Sets whether a skill is proficient or not
        # Proficiency value assumed = 2 for level one characters 
        if is_prof == True:
            self.value = self.base + prof_val
            self.prof = True
        else:
            self.value = self.base
            self.prof = False
    
    def set_exp(self,is_exp,prof_val=2):
        # Sets whether a skill has expertise or not
        # Proficiency value assumed = 2 for level one characters 
        if is_exp == True:
            self.value = self.base + (prof_val * 2)
            self.exp = True
        else:   # TODO is there a better way to do this logic?
            self.exp = False
            if self.prof == True:
                self.set_prof(True)
            else:
                self.value = self.base
                
    def __repr__(self):
        return (f"Skill: {self.name}, uses {self.stat_used}, Val: {self.value},Prof: {self.prof}")
