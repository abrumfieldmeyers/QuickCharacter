# For creating character classes with basic starting equipment and abilities
# Each needs to contain class abilities, equipment, proficiency, saving throws
classes = {
    'Artificer': {
        'skill number': 2,
        'hit_die': 8,
        'saving_throws':['CON', 'INT'],
        'skill proficiencies': ['Arcana', 'History', 'Investigation', 'Medicine', 'Perception ', 'Sleight of Hand'],
        'tool proficiencies': ["Thieves' Tools", "Tinker's Tools", "One type of artisan's tools of your choice"],
        'weapon proficiencies': ['Simple Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec':[ 8,12,14,15,13,10],
        'weapons': ["Dagger", "Light Crossbow"],
        "armor":["Studded Leather Armor"],
        'equipment':{"Thieves tools": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 
 
    },
    'Barbarian': {
        'skill number': 2,
        'hit_die': 12,
        'saving_throws':['CON', 'STR'],
        'skill proficiencies': ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception ', 'Survival'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec': [15,13,14,8,10,12],
        'weapons': ["Greataxe", "Handaxe", "Javelin"],
        'armor': [],
        'equipment': {"Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 
    }    ,
    'Bard': {
        'hit_die':8,
        'skill number': 3,
        'saving_throws':['DEX', 'CHA'],
        'skill proficiencies': ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception ', 'History',
                                'Insight',
                                'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception ', 'Performance',
                                'Persuasion', 'Religion', 'Sleight of Hand', 'Stealth ', 'Survival'],
        'tool proficiencies': ['Musical Instrument', 'Musical Instrument', 'Musical Instrument'],
        'weapon proficiencies': ['Simple Weapons', 'Hand Crossbows', 'Longsword', 'Rapier', 'Shortsword'],
        'armor proficiencies': ['Light Armor'],
        'stat_rec': [8,14,13,12,10,15],
        'weapons': ["Rapier", "Dagger"],
        'armor': ["Leather Armor"],
        'equipment': {"Lute": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 


    },
    'Blood Hunter': {
        'hit_die': 10,
        'skill number': 3,
        'saving_throws':['DEX', 'INT'],
        'skill proficiencies': ['Athletics', 'Acrobatics', 'Arcana', 'History', 'Insight', 'Investigation', 'Religion',
                                'Survival'],
        'tool proficiencies': ["Alchemist's supplies"],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec' : [14,12,13,15,10,8],
        'weapons': ["Greataxe", "Light Crossbow"],
        'armor': ["Studded Leather Armor"],
        'equipment': {"Alchemist supplies": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 

    },
    'Cleric': {
        'skill number': 2,
        'hit_die': 8,
        'saving_throws':['WIS', 'CHA'],
        'skill proficiencies': ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec': [13,8,14,10,15,12],
        'weapons': ["Warhammer", "Light Crossbow"],
        'armor': ["Scale Mail", "Shield"],
        'equipment': {"Shield":1, "Holy Symbol":1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 
 
    },
    'Druid': {
        'skill number': 2,
        'hit_die': 8,
        'saving_throws':['WIS', 'INT'],
        'skill proficiencies': ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception ', 'Religion',
                                'Survival'],
        'tool proficiencies': ['Herbalism kit'],
        'weapon proficiencies': ['Club', 'Dagger', 'Darts', 'Javelins', 'Maces', 'Quarterstaff', 'Scimitars', 'Sickles',
                                 'Slings', 'Spears'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields', 'No armor or shields made of metal'],
        'stat_rec': [8,13,14,10,15,12],
        'weapons': ["Scimitar"],
        'armor': ["Leather Armor", "Shield"],
        'equipment': {"Druidic Focus": 1, "Shield":1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 
 
    },
    'Fighter': {
        'skill number': 2,
        'hit_die': 10,
        'saving_throws':['CON', 'STR'],
        'skill proficiencies': ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation',
                                'Perception ', 'Survival'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['All Armor', 'Shields'],
        'stat_rec': [15,13,14,12,10,8],
        'weapons': ["Longsword", "Handaxe", "Light Crossbow"],
        'armor': ["Chain Mail", "Shield"],
        'equipment': {"Shield":1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 

    },
    'Monk': {
        'skill number': 2,
        'hit_die': 8,
        'saving_throws':['DEX', 'STR'],
        'skill proficiencies': ['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth '],
        'tool proficiencies': ["One type of Artisan's tools or one musical instrument"],
        'weapon proficiencies': ['Simple Weapons', 'Shortsword'],
        'armor proficiencies': [],
        'stat_rec': [8,15,13,10,14,12],
        'weapons': ["Unarmed", "Shortsword", "Darts"],
        'armor': [],
        'equipment': {"Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 

    },
    'Paladin': {
        'skill number': 2,
        'hit_die': 10,
        'saving_throws':['CHA', 'WIS'],
        'skill proficiencies': ['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['All armor', 'Shields'],
        'stat_rec': [15,8,13,10,12,14],
        'weapons': ["Greatsword", "Javelin"],
        'armor': ["Chain Mail"],
        'equipment': {"Holy Symbol": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 

    },
    'Ranger': {
        'skill number': 3,
        'hit_die': 10,
        'saving_throws':['DEX', 'STR'],
        'skill proficiencies': ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception ',
                                'Stealth ', 'Survival'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons', 'Martial Weapons'],
        'armor proficiencies': ['Light Armor', 'Medium Armor', 'Shields'],
        'stat_rec': [10,15,13,8,14,12],
        'weapons': ["Shortsword", "Longbow"],
        'armor': ["Scale Mail"],
        'equipment': {"Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 

    },
    'Rogue': {
        'skill number': 4,
        'saving_throws':['DEX', 'INT'],
        'skill proficiencies': ['Acrobatics', 'Deception ', 'Insight', 'Intimidation', 'Investigation', 'Perception ',
                                'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth '],
        'tool proficiencies': ["Thieves' Tools"],
        'weapon proficiencies': ['Simple Weapons', 'Hand Crossbows', 'Longswords', 'Rapiers', 'Shortswords'],
        'armor proficiencies': ['Light Armor'],
        'hit_die': 8,
        'stat_rec': [8,15,12,14,10,13],
        'weapons': ["Rapier", "Dagger", "Shortbow"],
        'armor': ["Leather Armor"],
        'equipment': {"Thieves tools": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 

    },
    'Sorcerer': {
        'skill number': 2,
        'saving_throws':['CON', 'CHA'],
        'skill proficiencies': ['Arcana', 'Deception ', 'Insight', 'Intimidation', 'Persuasion', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows'],
        'armor proficiencies': [],
        'hit_die': 6,
        'stat_rec': [8,13,14,10,12,15],
        'weapons': ["Light Crossbow", "Dagger"],
        'armor': [],
        'equipment': {"Arcane Focus": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 

    },
    'Warlock': {
        'skill number': 2,
        'saving_throws':['CHA', 'WIS'],
        'skill proficiencies': ['Arcana', 'Deception ', 'History', 'Intimidation', 'Investigation', 'Nature',
                                'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Simple Weapons'],
        'armor proficiencies': ['Light Armor'],
        'hit_die': 8,
        'stat_rec': [10, 12,14,13,8,15],
        'weapons': ["Light Crossbow", "Dagger"],
        'armor': ["Leather Armor"],
        'equipment': {"Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 

    },
    'Wizard': {
        'skill number': 2,
        'saving_throws':['WIS', 'INT'],
        'skill proficiencies': ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion'],
        'tool proficiencies': [],
        'weapon proficiencies': ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows'],
        'armor proficiencies': [],
        'hit_die': 6,
        'stat_rec': [8,14,13,15,10,12],
        'weapons': ["Dagger"],
        'armor': [],
        'equipment': {"Arcane Focus": 1, "Spellbook": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} 

    }
}
