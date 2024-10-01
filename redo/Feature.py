class Features:
    def __init__(self,name=None,text=None,source=None,mods=[]):
        self.name = name
        self.text = text
        self.source = source
        self.mods = mods


    def set(self,name,text,source):
        self.name = name
        self.text = text
        self.source = source
    
    def __repr__(self):
        return (f"{self.name}\n{self.text}")