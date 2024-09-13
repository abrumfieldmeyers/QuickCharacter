
class Stats():
    def __init__(self,*args):
        if isinstance(args[0],list):
            self.STR=args[0][0]
            self.DEX=args[0][1]
            self.CON=args[0][2]
            self.INT=args[0][3]
            self.WIS=args[0][4]
            self.CHA=args[0][5]
        else:
            self.STR=args[0]
            self.DEX=args[1]
            self.CON=args[2]
            self.INT=args[3]
            self.WIS=args[4]
            self.CHA=args[5]
        self.set_stat_mods()

    def set_stat_mods(self):
        # Derive modifier and saving throw from base stats
        self.STRMod = self.stat_to_mod(self.STR) 
        self.STRSave = self.STRMod
        self.DEXMod = self.stat_to_mod(self.DEX) 
        self.DEXSave = self.DEXMod
        self.CONMod = self.stat_to_mod(self.CON) 
        self.CONSave = self.CONMod
        self.INTMod = self.stat_to_mod(self.INT) 
        self.INTSave = self.INTMod
        self.WISMod = self.stat_to_mod(self.WIS) 
        self.WISSave = self.WISMod
        self.CHAMod = self.stat_to_mod(self.CHA) 
        self.CHASave = self.CHAMod


    def stat_to_mod(self,stat):
        # Helper function to get mod value from base stat
        return (stat - 10)//2

    def update_stat(self,stat_str,val,replace):
        # Updates or replaces base stat value
        stat_to_change = getattr(self,stat_str)
        if (replace == True):   # TODO - Is this ever used?
            setattr(self,stat_str,val)
        else:
            setattr(self,stat_str,str(val + stat_to_change))

        # update associated stat mod
        setattr(self,stat_str+"Mod",self.stat_to_mod(int(getattr(self,stat_str))))
        return

    def update_save(self,stat_str,val,replace):
        # Update exsting save
        stat_mod = getattr(self,stat_str +"Mod")
        
        if (replace == True):
            setattr(self,stat_str+"Save",str(val))
        else:
            setattr(self,stat_str+"Save",str(stat_mod+val))

        return

    def printMods(self):
        print("Modifiers:")
        print(f"STR: {self.STRMod}\nDEX: {self.DEXMod}\nCON: {self.CONMod}\nINT: {self.INTMod}\nWIS: {self.WISMod}\nCHA: {self.CHAMod}\n")
        print("Stats")
        print(f"STR: {self.STR}\nDEX: {self.DEX}\nCON: {self.CON}\nINT: {self.INT}\nWIS: {self.WIS}\nCHA: {self.CHA}\n")
        print("Saves")
        print(f"STR: {self.STRSave}\nDEX: {self.DEXSave}\nCON: {self.CONSave}\nINT: {self.INTSave}\nWIS: {self.WISSave}\nCHA: {self.CHASave}\n")
    
    def __repr__(self):
        return (f"STR: {self.STR}\nDEX: {self.DEX}\nCON: {self.CON}\nINT: {self.INT}\nWIS: {self.WIS}\nCHA: {self.CHA}\n")