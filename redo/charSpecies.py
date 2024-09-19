class CharSpecies:
    def __init__(self,name,speed=30,size="Medium",languages=[],skill_prof=[],weapon_prof=[],armor_prof=[],tool_prof=[],stat_mod={},skill_count=0,features=[]):
        self.name = name
        self.skill_prof = skill_prof
        self.weapon_prof = weapon_prof
        self.armor_prof = armor_prof
        self.tool_prof = tool_prof
        self.stat_mod = stat_mod
        self.skill_count = skill_count
        self.features = features
        self.size = size
        self.speed = speed
        self.languages = languages


SpeciesList = {
    'xx': CharSpecies(
        'xx',
        [],
        [],
        [],
        [],
        {'STR':2, 'CHA':1},
        []
    ),

    'Dragonborn': CharSpecies(
        name='Dragonborn',
        stat_mod={'STR':2, 'CHA':1},
        languages=["Draconic"]
    ),
    'Dwarf': CharSpecies(
        name='Dwarf',
        speed=25,
        languages=["Dwarvish"],
        stat_mod={'CON':2, 'WIS':1},
        tool_prof=['smith\'s Tools'],
        weapon_prof=['Battleaxe', 'Hand Axe', 'Light Hammer', 'Warhammer']
    ),
    'Elf': CharSpecies(
        name='Elf',
        languages=["Elven"],
        skill_prof=['Perception'],
        stat_mod={'DEX':2, 'INT':1},
    ),
    'Gnome': CharSpecies(
        name='Gnome',
        size="Small",
        languages=["Gnomish"],
        speed=25,
        stat_mod={'INT':2, 'DEX':1},
    ),
    'Half-Elf': CharSpecies(
        name='Half-Elf',
        languages=["Elven"],
        stat_mod={'CHA':2, 'WIS':1, 'INT':1},
        skill_count=2,
    ),
    'Half-Orc': CharSpecies(
        name='Half-Orc',
        languages=["Orc"],
        stat_mod={'STR':2, 'CON':1},
        skill_prof=['Intimidation'],
    ),
    'Halfling': CharSpecies(
        name='Halfling',
        languages=["Halfling"],
        stat_mod={'DEX':2,"CHA":1},
        speed=25,
        size="Small",
        skill_prof=['Intimidation'],
    ),
    'Human': CharSpecies(
        name='Human',
        stat_mod={'STR':1, 'DEX': 1, 'CON':1, 'INT':1, 'WIS':1, 'CHA':1},
    ),
    'Tiefling': CharSpecies(
        name='Tiefling',
        stat_mod={'CHA':2, "INT":1},
        languages=["Infernal"]
    ),
    


}