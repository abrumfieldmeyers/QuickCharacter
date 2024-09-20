from Stat import Stat

class Stats():
    def __init__(self,*args):
        if isinstance(args[0],list):
            print("LIST")
            self.STR=Stat("STR",args[0][0])
            self.DEX=Stat("DEX",args[0][1])
            self.CON=Stat("CON",args[0][2])
            self.INT=Stat("INT",args[0][3])
            self.WIS=Stat("WIS",args[0][4])
            self.CHA=Stat("CHA",args[0][5])
        else:
            print("OTHER")
            self.STR=Stat("STR",args[0])
            self.DEX=Stat("DEX",args[1])
            self.CON=Stat("CON",args[2])
            self.INT=Stat("INT",args[3])
            self.WIS=Stat("WIS",args[4])
            self.CHA=Stat("CHA",args[5])
        
    

    def update_stat(self,stat_str,val,replace):
        # Updates or replaces base stat value
        stat_to_change = getattr(self,stat_str)
        if (replace == True):   # TODO - Is this ever used?
            setattr(self,stat_str,Stat(stat_to_change.name,val))
        else:
            stat_to_change.update_val(val,False)
        return

    def update_save(self,stat_str,val,replace):
        # Update exsting save to be proficient
        stat_to_update = getattr(self,stat_str)
        if val != 0:
            stat_to_update.set_save_prof()
        else:
            stat_to_update.remove_save_prof()

        return

    def printMods(self):
        print("All Stat Info")
        self.STR.print_all()
        self.DEX.print_all()
        self.CON.print_all()
        self.INT.print_all()
        self.WIS.print_all()
        self.CHA.print_all()
         
           
    def __repr__(self):
        return f"{self.STR}\n{self.DEX}\n{self.CON}\n{self.INT}\n{self.WIS}\n{self.CHA}"