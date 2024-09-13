
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
        self.STRMod = self.STR - 10 //2
        self.STRSave = self.STRMod
        self.DEXMod = self.DEX - 10 //2
        self.DEXSave = self.DEXMod
        self.CONMod = self.CON - 10 //2
        self.CONSave = self.CONMod
        self.INTMod = self.INT - 10 //2
        self.INTSave = self.INTMod
        self.WISMod = self.WIS - 10 //2
        self.WISSave = self.WISMod
        self.CHAMod = self.CHA - 10 //2
        self.CHASave = self.CHAMod


    def update_stat(self,stat_str,val,replace):
        if (replace == True):
            setattr(self,stat_str,val)
        else:
            stat_to_change = getattr(self,stat_str)
            setattr(self,stat_str,str(val + stat_to_change))
        return

    def update_save(self,stat_str,val,replace):
        # make sure we're updating the saving throw, not the main stat
        statMod = getattr(self,stat_str + "Mod")
        statSave = getattr(self,stat_str + "Save")

        if (replace == True):
            setattr(self,statSave,val)
        else:
            stat_to_change = getattr(self,stat_str)
            setattr(self,statSave,str(val + statMod))
        return

    def __repr__(self):
        return (f"STR: {self.STR}\nDEX: {self.DEX}\nCON: {self.CON}\nINT: {self.INT}\nWIS: {self.WIS}\nCHA: {self.CHA}\n")