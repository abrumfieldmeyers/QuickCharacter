from Feature import Features

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
        languages=["Draconic"],
        features= [
            Features("Draconic Ancestry: Gold",
                     "You can use your action to exhale destructive energy. It deals fire damage in a 15 foot cone. When you use your breath weapon, all creatures in the area must make a CON saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 fire damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. After using your breath weapon, you cannot use it again until you complete a short or long rest.",
                     "species",
                     [] # TODO - add fire breath weapon
                     ),
            Features("Damage Resistance",
                     'You have resistance to the damage type associated with your ancestry (fire).',
                     'species'),
        ]
    ),
    'Dwarf': CharSpecies(
        name='Dwarf',
        speed=25,
        languages=["Dwarvish"],
        stat_mod={'CON':2, 'WIS':1},
        tool_prof=['smith\'s Tools'],
        weapon_prof=['Battleaxe', 'Hand Axe', 'Light Hammer', 'Warhammer'],
        features=[
            Features("Darkvision",
                     "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
                     "species"),
            Features("Dwarven Resilience",
                     "You have advantage on saving throws against poison, and you have resistance against poison damage.",
                     "species"
                     ),
            Features("Stonecunning",
                     "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.",
                     "species"),
            Features("Dwarven Toughness",
                     "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.",
                     "species",
                     [] # TODO - increase HP by 1
                     ),
        ]
    ),
    'Elf': CharSpecies(
        name='Elf',
        languages=["Elven"],
        skill_prof=['Perception'],
        stat_mod={'DEX':2, 'INT':1},
        speed= 35, # from Wood Elf
        features=[
            Features("Darkvision",
                     "Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
                     "species"),
            Features("Fey Ancestry",
                     "You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
                     "species"),
            Features("Trance",
                     'Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is "trance." While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.',
                     "species"),
            Features("Mask of the Wild",
                     "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.",
                     "species"),
        ]
    ),
    'Gnome': CharSpecies(
        name='Gnome',
        size="Small",
        languages=["Gnomish"],
        speed=25,
        stat_mod={'INT':2, 'DEX':1},
        features= [
            Features("Darkvision",
                     "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
                     "species"),
            Features("Gnome Cunning",
                     "You have advantage on all Intelligence, Wisdom, and Charisma saves against magic.",
                     "species"),
            Features("Speak with Small Beasts",
                     "Through sound and gestures, you may communicate simple ideas with Small or smaller beasts",
                     "species"),
            Features("Natural Illusionist",
                     "You know the Minor Illusion cantrip. Intelligence is your spellcasting modifier for it",
                     "species",
                     [] # TODO add Minor Illusion cantrip
                     )
        ]
    ),
    'Half-Elf': CharSpecies(
        name='Half-Elf',
        languages=["Elven"],
        stat_mod={'CHA':2, 'WIS':1, 'INT':1},
        skill_count=2,
        speed=35,   # from Fleet of Foot feature
        features= [
            Features("Darkvision",
                     "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
                     "species"),
            Features("Fleet of Foot",
                     "Your base walking speed increases to 35 feet",
                     "species",
                     [] # TODO ensure that base speed = 35. Hard coded above, but we should double check
            ),
            Features("Fey Ancestry",
                     "You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
                     "species")
        ]
    ),
    'Half-Orc': CharSpecies(
        name='Half-Orc',
        languages=["Orc"],
        stat_mod={'STR':2, 'CON':1},
        skill_prof=['Intimidation'],
        features=[
            Features("Relentless Endurance",
                     "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.",
                      "species"),
            Features("Darkvision",
                     "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
                     "species"),
            Features("Savage Attacks",
                     "When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit.",
                     "species"),
        ]
    ),
    'Halfling': CharSpecies(
        name='Halfling',
        languages=["Halfling"],
        stat_mod={'DEX':2,"CHA":1},
        speed=25,
        size="Small",
        features=[
            Features("Lucky",
                     "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die. You must use the new result, even if it is a 1.",
                     "species"),
            Features("Brave",
                     "You have advantage on saving throws against being frightened.",
                     "species"),
            Features("Nimble",
                     "You can move through the space of any creature that is of a size larger than yours",
                     "species"),
            Features("Naturally Stealthy",
                     "You can attempt to hide even when you are only obscured by a creature that is at least one size larger than you",
                     "species")
        ]
    ),
    'Human': CharSpecies(
        name='Human',
        stat_mod={'STR':1, 'DEX': 1, 'CON':1, 'INT':1, 'WIS':1, 'CHA':1},
    ),
    'Tiefling': CharSpecies(
        name='Tiefling',
        stat_mod={'CHA':2, "INT":1},
        languages=["Infernal"],
        features=[
            Features("Darkvision",
                     "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
                     "species"),
            Features("Hellish Resistance",
                     "You have resistance to fire damage.",
                     "species"),
            Features("Infernal Legacy",
                     "You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Hellish Rebuke spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.",
                     "species",
                     []) # TODO - add Thaumaturgy cantrip to spells
        ]
    ),
    


},