class Stat():
    def __init__(self,name,value,save_prof=False):
        self.name = name
        self.value = value
        self.mod = self.stat_to_mod()
        self.save_prof = save_prof
        self.save_mod = self.mod

    def __repr__(self):
        return f"{self.name}: {self.value}"
    
    def print_all(self):
        print(f"{self.name}: {self.value}, MOD: {self.mod}, Save: {self.save_prof}/{self.save_mod}")
     
    def update_val(self,val,replace):
        # Update skill value and associated mods 
        if (replace == True):
            self.value = val
        else:
            self.value += val
        self.mod = self.stat_to_mod()
        if (self.save_prof == True):
            self.set_save_prof()
        else:
            self.save_mod = self.mod
    
    def stat_to_mod(self):
        # Helper function to set mod value from base stat
        return (self.value - 10)//2
    
    def set_save_prof(self,prof_bonus=2):
        # Updates save to include proficiency bonus, and save_prof to True
        # Default is 2 for Level 1 character
        self.save_prof = True
        self.save_mod = self.mod + prof_bonus

    def remove_save_prof(self):
        # Updates save to exclude proficiency bonus, and save_prof to False
        self.save_prof = False
        self.save_mod = self.mod
    
