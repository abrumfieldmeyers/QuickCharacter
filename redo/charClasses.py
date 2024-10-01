from Feature import Features

class CharClass:
    def __init__(self, name, hit_die, saving_throws, skill_count, skill_prof, tool_prof,
                 weapon_prof, armor_prof, stat_recs, weapons, armor, equipment, features):
        self.name = name
        self.hit_die = hit_die
        self.saving_throws = saving_throws
        self.skill_count = skill_count
        self.skill_prof = skill_prof
        self.tool_prof = tool_prof
        self.weapon_prof = weapon_prof
        self.armor_prof = armor_prof
        self.stat_recs = stat_recs
        self.weapons = weapons
        self.armor = armor
        self.equipment = equipment
        self.features = features

ClassList = {
    'Artificer': CharClass('Artificer',
                           8,
                           ['CON', 'INT'],
                           2,
                           ['Arcana', 'History', 'Investigation', 'Medicine', 'Perception ', 'Sleight of Hand'],
                           ["Thieves' Tools", "Tinker's Tools", "One type of artisan's tools of your choice"],
                           ['Simple Weapons'],
                           ['Light Armor', 'Medium Armor', 'Shields'],
                           [8,12,14,15,13,10],
                           ["Dagger", "Light Crossbow"],
                           ["Studded Leather Armor"],
                           {"Thieves tools": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50},
                           [
                               Features("Magical Tinkering",
                                        'At 1st level, you\'ve learned how to invest a spark of magic into mundane objects. To use this ability, you must have thieves\' tools or artisan\'s tools in hand. You then touch a Tiny nonmagical object as an action and give it one of the following magical properties of your choice: '
                                        'The object sheds bright light in a 5-foot radius and dim light for an additional 5 feet.'
                                        'Whenever tapped by a creature, the object emits a recorded message that can be heard up to 10 feet away. You utter the message when you bestow this property on the object, and the recording can be no more than 6 seconds long.'
                                        'The object continuously emits your choice of an odor or a nonverbal sound (wind, waves, chirping, or the like). The chosen phenomenon is perceivable up to 10 feet away.'
                                        'A static visual effect appears on one of the object\'s surfaces. This effect can be a picture, up to 25 words of text, lines and shapes, or a mixture of these elements, as you like.'
                                        'The chosen property lasts indefinitely. As an action, you can touch the object and end the property early.'
                                        'You can bestow magic on multiple objects, touching one object each time you use this feature, though a single object can only bear one property at a time. The maximum number of objects you can affect with this feature at one time is equal to your Intelligence modifier (minimum of one object). If you try to exceed your maximum, the oldest property immediately ends, and then the new property applies.',
                                        "class"),
                                Features("Ritual Casting",
                                         "You can cast an artificer spell as a ritual if that spell has the ritual tag and you have the spell prepared.",
                                         "class")
                           ]
    ),
    'Barbarian': CharClass('Barbarian',
                           12,
                           ['CON', 'STR'],
                           2,
                           ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception ', 'Survival'],
                           [],
                           ['Simple Weapons', 'Martial Weapons'],
                           ['Light Armor', 'Medium Armor', 'Shields'],
                           [15,13,14,8,10,12],
                           ["Greataxe", "Handaxe", "Javelin"],
                           [],
                           {"Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50},
                           [
                               Features("Rage",
                                        'In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.\n'

                                        'While raging, you gain the following benefits if you aren\'t wearing heavy armor:\n'
                                        'You have advantage on Strength checks and Strength saving throws.'
                                        'When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.'
                                        'You have resistance to bludgeoning, piercing, and slashing damage.'
                                        'If you are able to cast spells, you can\'t cast them or concentrate on them while raging.\n'
                                        'Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven\'t attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.\n'
                                        'Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again.',
                                        "class"),
                                Features("Unarmored Defense",
                                         "While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.",
                                         "class",
                                         [] # TODO - AC = 10 + DEX + CON
                                         )
                           ]
    ),
    'Bard': CharClass('Bard',
                           8,
                           ['DEX', 'CHA'],
                           3,
                           ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception ', 'History', 'Insight',
                                'Intimidation', 'Investigation', 'Medicine', 'Nature', 'Perception ', 'Performance',
                                'Persuasion', 'Religion', 'Sleight of Hand', 'Stealth ', 'Survival'],
                           ['Musical Instrument', 'Musical Instrument', 'Musical Instrument'],
                           ['Simple Weapons', 'Hand Crossbows', 'Longsword', 'Rapier', 'Shortsword'],
                           ['Light Armor'],
                           [8,14,13,12,10,15],
                           ["Rapier", "Dagger"],
                           ["Leather Armor"],
                           {"Lute": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} ,
                           [
                               Features("Bardic Inspiration",
                                        'You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6.'
                                        'Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time.'
                                        'You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.'
                                        'Your Bardic Inspiration die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level.',
                                        "class")
                           ]
    ),
    'Cleric': CharClass('Cleric',
                           8,
                           ['WIS', 'CHA'],
                           2,
                           ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion'],
                           [],
                           ['Simple Weapons'],
                           ['Light Armor', 'Medium Armor', 'Shields'],
                           [13,8,14,10,15,12],
                           ["Warhammer", "Light Crossbow"],
                           ["Scale Mail", "Shield"],
                           {"Shield":1, "Holy Symbol":1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} ,
                           []
    ),
    'Druid': CharClass('Druid',
                           8,
                           ['WIS', 'INT'],
                           2,
                           ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception ', 'Religion','Survival'],
                           ['Herbalism kit'],
                           ['Club', 'Dagger', 'Darts', 'Javelins', 'Maces', 'Quarterstaff', 'Scimitars', 'Sickles','Slings', 'Spears'],
                           ['Light Armor', 'Medium Armor', 'Shields', 'No armor or shields made of metal'],
                           [8,13,14,10,15,12],
                           ["Scimitar"],
                           ["Leather Armor", "Shield"],
                           {"Druidic Focus": 1, "Shield":1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} ,
                           [
                               Features("Druidic",
                                        'You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message\'s presence with a successful DC 15 Wisdom (Perception) check but can\'t decipher it without magic.',
                                        "class",
                                        []      # TODO - add Druidic Language
                                        )
                           ]
    ),
    'Fighter': CharClass('Fighter',
                           10,
                           ['CON', 'STR'],
                           2,
                           ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation','Perception ', 'Survival'],
                           [],
                           ['Simple Weapons', 'Martial Weapons'],
                           ['All Armor', 'Shields'],
                           [15,13,14,12,10,8],
                           ["Longsword", "Handaxe", "Light Crossbow"],
                           ["Chain Mail", "Shield"],
                           {"Shield":1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50} ,
                           [
                               # TODO - allow selection of fighting style
                               Features("Fighting Style: Interception",
                                        "When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by 1d10 + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.",
                                        "class"),   
                                Features("Second Wind",
                                         'You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level.'
                                         'Once you use this feature, you must finish a short or long rest before you can use it again.',
                                         "class"),
                           ]
    ),
    'Monk': CharClass('Monk',
                           8,
                           ['DEX', 'STR'],
                           2,
                           ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation','Perception ', 'Survival'],
                           ["One type of Artisan's tools or one musical instrument"],
                           ['Simple Weapons', 'Shortsword'],
                           [],
                           [8,15,13,10,14,12],
                           ["Unarmed", "Shortsword", "Darts"],
                           [],
                           {"Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50},
                           [
                               Features("Martial Arts",
                                        'At 1st level, your practice of martial arts gives you mastery of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don\'t have the two-handed or heavy property.'
                                        'You gain the following benefits while you are unarmed or wielding only monk weapons and you aren\'t wearing armor or wielding a shield:\n'
                                        'You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons.'
                                        'You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table.'
                                        'When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven\'t already taken a bonus action this turn.'
                                        'Certain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon on the Weapons page.',
                                        "class",
                                        [] # TODO - add unarmed attack to weapons
                               ),
                               Features("Unarmored Defense",
                                        "Beginning at 1st level, while you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.",
                                        "class",
                                        [] # TODO - AC = 10 + WIS + DEX
                                        ),
                           ]
    ),
    'Paladin': CharClass('Paladin',
                           10,
                           ['CHA', 'WIS'],
                           2,
                           ['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'],
                           [],
                           ['Simple Weapons', 'Martial Weapons'],
                           ['All armor', 'Shields'],
                           [15,8,13,10,12,14],
                           ["Greatsword", "Javelin"],
                           ["Chain Mail"],
                           {"Holy Symbol": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50},
                           [
                               Features("Divine Sense",
                                        'The presence of strong evil registers on your senses like a noxious odor, and powerful good rings like heavenly music in your ears. As an action, you can open your awareness to detect such forces. Until the end of your next turn, you know the location of any celestial, fiend, or undead within 60 feet of you that is not behind total cover. You know the type (celestial, fiend, or undead) of any being whose presence you sense, but not its identity (the vampire Count Strahd von Zarovich, for instance). Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the Hallow spell.'
                                        'You can use this feature a number of times equal to 1 + your Charisma modifier. When you finish a long rest, you regain all expended uses.',
                                        "class"
                               ),
                               Features("Lay On Hands",
                                        'Your blessed touch can heal wounds. You have a pool of healing power that replenishes when you take a long rest. With that pool, you can restore a total number of hit points equal to your paladin level x 5.'
                                        'As an action, you can touch a creature and draw power from the pool to restore a number of hit points to that creature, up to the maximum amount remaining in your pool.'
                                        'Alternatively, you can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Lay on Hands, expending hit points separately for each one.'
                                        'This feature has no effect on undead and constructs.',
                                        "class"
                               ),
                           ]
    ),
    'Ranger': CharClass('Ranger',
                           10,
                           ['DEX', 'STR'],
                           3,
                           ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception ', 'Stealth ', 'Survival'],
                           [],
                           ['Simple Weapons', 'Martial Weapons'],
                           ['Light Armor', 'Medium Armor', 'Shields'],
                           [10,15,13,8,14,12],
                           ["Shortsword", "Longbow"],
                           ["Scale Mail"],
                           {"Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50},
                           [
                               Features("Favored Enemy",
                                        'Beginning at 1st level, you have significant experience studying, tracking, hunting, and even talking to a certain type of enemy.'
                                        'Choose a type of favored enemy: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can select two races of humanoid (such as gnolls and orcs) as favored enemies.'
                                        'You have advantage on Wisdom (Survival) checks to track your favored enemies, as well as on Intelligence checks to recall information about them.'
                                        'When you gain this feature, you also learn one language of your choice that is spoken by your favored enemies, if they speak one at all.'
                                        'You choose one additional favored enemy, as well as an associated language, at 6th and 14th level. As you gain levels, your choices should reflect the types of monsters you have encountered on your adventures.',
                                        "class"),
                                Features("Natural Explorer",
                                         'At 1st level, you are particularly familiar with one type of natural environment and are adept at traveling and surviving in such regions. Choose one type of favored terrain: arctic, coast, desert, forest, grassland, mountain, swamp, or the Underdark. When you make an Intelligence or Wisdom check related to your favored terrain, your proficiency bonus is doubled if you are using a skill that you’re proficient in.'
                                         'While traveling for an hour or more in your favored terrain, you gain the following benefits:\n'
                                         'Difficult terrain doesn\'t slow your group\'s travel.'
                                         'Your group can\'t become lost except by magical means.'
                                         'Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger.'
                                         'If you are traveling alone, you can move stealthily at a normal pace.'
                                         'When you forage, you find twice as much food as you normally would.'
                                         'While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.'
                                         'You choose additional favored terrain types at 6th and 10th level.',
                                         "class"),
                           ]
    ),
    'Rogue': CharClass('Rogue',
                           8,
                           ['DEX', 'INT'],
                           4,
                           ['Acrobatics', 'Deception ', 'Insight', 'Intimidation', 'Investigation', 'Perception ', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth '],
                           ["Thieves' Tools"],
                           ['Simple Weapons', 'Hand Crossbows', 'Longswords', 'Rapiers', 'Shortswords'],
                           ['Light Armor'],
                           [8,15,12,14,10,13],
                           ["Rapier", "Dagger", "Shortbow"],
                           ["Leather Armor"],
                           {"Thieves tools": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50},
                           [
                               Features("Expertise",
                                        'At 1st level, choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves\' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.'
                                        'At 6th level, you can choose two more of your proficiencies (in skills or with thieves\' tools) to gain this benefit.',
                                        "class",
                                        [] # TODO - select two skills for expertise
                               ),
                               Features("Sneak Attack",
                                        'Beginning at 1st level, you know how to strike subtly and exploit a foe\'s distraction. Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon.'
                                        'You don\'t need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn\'t incapacitated, and you don\'t have disadvantage on the attack roll.'
                                        'The amount of the extra damage increases as you gain levels in this class, as shown in the Sneak Attack column of the Rogue table.',
                                        "class"
                                        ),
                                Features("Thieves' Cant",
                                         'During your rogue training you learned thieves\' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves\' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly.'
                                         'In addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves\' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run.',
                                         "class",
                                         []     # TODO - add Thieves' Cant to languages
                                )
                           ]
    ),
    'Sorcerer': CharClass('Sorcerer',
                           6,
                           ['CON', 'CHA'],
                           2,
                           ['Arcana', 'Deception ', 'Insight', 'Intimidation', 'Persuasion', 'Religion'],
                           [],
                           ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows'],
                           [],
                           [8,13,14,10,12,15],
                           ["Light Crossbow", "Dagger"],
                           [],
                           {"Arcane Focus": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50},
                           [
                               # TODO - allow selection for sorcerous origns
                               Features("Sorcerous Origin: Storm Sorcery: Wind Speaker",
                                        "The arcane magic you command is infused with elemental air. You can speak, read, and write Primordial. Knowing this language allows you to understand and be understood by those who speak its dialects: Aquan, Auran, Ignan, and Terran.",
                                        "class",
                                        [] # TODO - add primordial to languages
                                        ),
                                Features("Sorcerous Origin: Storm Sorcery: Tempestuous Magic",
                                         'Starting at 1st level, you can use a bonus action on your turn to cause whirling gusts of elemental air to briefly surround you, immediately before or after you cast a spell of 1st level or higher. Doing so allows you to fly up to 10 feet without provoking opportunity attacks.',
                                         "class")
                           ]
    ),
    'Warlock': CharClass('Warlock',
                           8,
                           ['WIS', 'CHA'],
                           2,
                           ['Arcana', 'Deception ', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion'],
                           [],
                           ['Simple Weapons'],
                           ['Light Armor'],
                           [10, 12,14,13,8,15],
                           ["Light Crossbow", "Dagger"],
                           ["Leather Armor"],
                           {"Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50},
                           [
                               Features("Patron: The Fiend: Dark One's Blessing",
                                        'Starting at 1st level, when you reduce a hostile creature to 0 hit points, you gain temporary hit points equal to your Charisma modifier + your warlock level (minimum of 1).'
                                        'class'),
                                # Features(None,None,None,[]) # TODO - add spells to spell list
                                    
                           ]
    ),
    'Wizard': CharClass('Wizard',
                           6,
                           ['WIS', 'INT'],
                           2,
                           ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion'],
                           [],
                           ['Daggers', 'Darts', 'Slings', 'Quarterstaffs', 'Light Crossbows'],
                           [],
                           [8,14,13,15,10,12],
                           ["Dagger"],
                           [],
                           {"Arcane Focus": 1, "Spellbook": 1, "Backpack": 1, "Crowbar": 1, "Hammer": 1, "Pitons": 10, "Torches": 10, "Tinderbox": 1, "Waterskin": 1, "Hemp Rope": 50},
                           [
                               Features("Arcane Recovery",
                                        'You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher.',
                                        "class")
                           ]
    ),

    }
