class CharBack:
    def __init__(self, name, skill_prof=[], tool_prof=[], weapon_prof=[], armor_prof=[], languages=[], weapons=[], armor=[], equipment={}, feature=[]):
        self.name = name
        self.skill_prof = skill_prof
        self.tool_prof = tool_prof
        self.weapon_prof = weapon_prof
        self.armor_prof = armor_prof
        self.weapons = weapons
        self.armor = armor
        self.equipment = equipment
        self.languages = languages
        self.feature = feature

BackList = {
    "Acolyte": CharBack(
        "Acolyte",
        skill_prof=['Insight', 'Religion'],
        languages=["Any","Any"],
        equipment={
            'Holy symbol': 1,
            'Prayer book or prayer wheel': 1,
            'Sticks of incense': 5,
            'Vestments': 1,
            'Common Clothes': 1,
            'Gold': 15
        },
        feature='Shelter of the Faithful: As an acolyte, you command the respect of those who share your faith, and '
                   'you can perform the religious ceremonies of your deity. You and your adventuring companions can '
                   'expect to receive free healing and care at a temple, shrine, or other established presence of your '
                   'faith, though you must provide any material components needed for spells. Those who share your '
                   'religion will support you (but only you) at a modest lifestyle. \nYou might also have ties to a '
                   'specific temple dedicated to your chosen deity or pantheon, and you have a residence there. This '
                   'could be the temple where you used to serve, if you remain on good terms with it, or a temple '
                   'where you have found a new home. While near your temple, you can call upon the priests for '
                   'assistance, provided the assistance you ask for is not hazardous and you remain in good standing '
                   'with your temple.'
    ),

    "Charlatan": CharBack(
        "Charlatan",
        skill_prof=['Deception', 'Sleight of Hand'],
        tool_prof=['Forgery Kit', 'Disguise Kit'],
        equipment={
            'Fine Clothes': 1,
            'Disguise Kit': 1,
            'Tools of your trade': 1,
            'Gold': 15
        },
        feature='False Identity: You have created a second identity that includes documentation, established '
                   'acquaintances, and disguises that allow you to assume that persona. Additionally, you can forge '
                   'documents including official papers and personal letters, as long as you have seen an example of '
                   'the kind of document or the handwriting you are trying to copy.',
    ),

    "Criminal": CharBack(
        "Criminal",
        skill_prof=['Deception', 'Stealth'],
        tool_prof=['Thieves Tools', 'One Gaming Set'],
        equipment={
            'Crowbar': 1,
            'Dark Common Clothes with a hood': 1,
            'Gold': 15
        },
        feature='Criminal Contact: You have a reliable and trustworthy contact who acts as your liaison to a network'
                   ' of other criminals. You know how to get messages to and from your contact, even over great '
                   'distances; specifically, you know the local messengers, corrupt caravan masters, and seedy sailors '
                   'who can deliver messages for you.',
    ),

    "Entertainer": CharBack(
        "Entertainer",
        skill_prof=['Acrobatics', 'Performance'],
        tool_prof=['Disguise Kit', 'One Musical Instrument'],
        equipment={
            'Musical Instrument': 1,
            'Favor of an admirer ': 1,
            'Costume': 1,
            'Gold': 15
        },
        feature='By Popular Demand: You can always find a place to perform, usually in an inn or tavern but possibly'
                   ' with a circus, at a theater, or even in a noble\'s court. At such a place, you receive free '
                   'lodging and food of a modest or comfortable standard (depending on the quality of the '
                   'establishment), as long as you perform each night. In addition, your performance makes you '
                   'something of a local figure. When strangers recognize you in a town where you have performed, they '
                   'typically take a liking to you.',
    ),

    "Folk Hero": CharBack(
        "Folk Hero",
        skill_prof=['Animal Handling', 'Survival'],
        tool_prof=['Artisans Tools', 'Vehicles (land)'],
        equipment={
            'Artisans Tools': 1,
            'Shovel': 1,
            'Iron Pot': 1,
            'Common Clothes': 1,
            'Gold': 10
        },
        feature='Rustic Hospitality: Since you come from the ranks of the common folk, you fit in among them with '
                   'ease. You can find a place to hide, rest, or recuperate among other commoners, unless you have '
                   'shown yourself to be a danger to them. They will shield you from the law or anyone else searching '
                   'for you, though they will not risk their lives for you.',
    ),

    "Gladiator": CharBack(
        "Gladiator",
        skill_prof=['Acrobatics', 'Performance'],
        tool_prof=['Disguise Kit', 'Musical Instrument'],
        equipment={
            'Unusual Weapon': 1,
            'Favor of an admirer ': 1,
            'Costume': 1,
            'Gold': 15
        },
        feature='By Popular Demand: You can always find a place to perform, usually in an inn or tavern but possibly'
                   ' with a circus, at a theater, or even in a noble\'s court. At such a place, you receive free '
                   'lodging and food of a modest or comfortable standard (depending on the quality of the '
                   'establishment), as long as you perform each night. In addition, your performance makes you '
                   'something of a local figure. When strangers recognize you in a town where you have performed, they '
                   'typically take a liking to you. Using your By Popular Demand feature, you can find a place to '
                   'perform in any place that features combat for entertainment-perhaps a gladiatorial arena or secret '
                   'pit fighting club. ',
    ),

    "Guild Artisan": CharBack(
        "Guild Artisan",
        skill_prof=['Insight', 'Persuasion'],
        tool_prof=['Artisans Tools'],
        languages=["Any"],
        equipment={
            'Artisans Tools': 1,
            'Letter of Introduction from your guild': 1,
            'Traveller\'s clothes': 1,
            'Gold': 15
        },
        feature='Guild Membership: As an established and respected member of a guild, you can rely on certain '
                   'benefits that membership provides. Your fellow guild members will provide you with lodging and food'
                   ' if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a '
                   'central place to meet other members of your profession, which can be a good place to meet potential'
                   ' patrons, allies, or hirelings. \nGuilds often wield tremendous political power. If you are accused'
                   ' of a crime, your guild will support you if a good case can be made for your innocence or the crime'
                   ' is justifiable. You can also gain access to powerful political figures through the guild, if you '
                   'are a member in good standing. Such connections might require the donation of money or magic items '
                   'to the guild\'s coffers. You must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues '
                   'to remain in the guild\'s good graces.'
    ),

    "Guild Merchant": CharBack(
        "Guild Merchant",
        skill_prof=['Insight', 'Persuasion'],
        tool_prof=['Navigator\'s Tools'],
        languages=["Any"],
        equipment={
            'Mule': 1,
            'Cart': 1,
            'Letter of Introduction from your guild': 1,
            'Traveller\'s clothes': 1,
            'Gold': 15
        },
        feature='Guild Membership: As an established and respected member of a guild, you can rely on certain '
                   'benefits that membership provides. Your fellow guild members will provide you with lodging and food'
                   ' if necessary, and pay for your funeral if needed. In some cities and towns, a guildhall offers a '
                   'central place to meet other members of your profession, which can be a good place to meet potential'
                   ' patrons, allies, or hirelings. \nGuilds often wield tremendous political power. If you are accused'
                   ' of a crime, your guild will support you if a good case can be made for your innocence or the crime'
                   ' is justifiable. You can also gain access to powerful political figures through the guild, if you '
                   'are a member in good standing. Such connections might require the donation of money or magic items '
                   'to the guild\'s coffers.'
                   'You must pay dues of 5 gp per month to the guild. If you miss payments, you must make up back dues '
                   'to remain in the guild\'s good graces.',
    ),

    "Hermit": CharBack(
        "Hermit",
        skill_prof=['Medicine', 'Religion'],
        tool_prof=['Herbalism Kit'],
        languages=["Any"],
        equipment={
            'Scroll case stuffed with notes': 1,
            'Winter Blanket': 1,
            'Common clothes': 1,
            'Herbalism Kit': 1,
            'Gold': 5
        },
        feature='Discovery: The quiet seclusion of your extended hermitage gave you access to a unique and powerful '
                   'discovery. The exact nature of this revelation depends on the nature of your seclusion. It might '
                   'be '
                   'a great truth about the cosmos, the deities, the powerful beings of the outer planes, '
                   'or the forces '
                   'of nature. It could be a site that no one else has ever seen. You might have uncovered a fact that '
                   'has long been forgotten, or unearthed some relic of the past that could rewrite history. It might '
                   'be information that would be damaging to the people who or consigned you to exile, and hence the '
                   'reason for your return to society.',
    ),

    "Knight": CharBack(
        "Knight",
        skill_prof=['History', 'Persuasion'],
        tool_prof=['One Gaming Set'],
        languages=["Any"],
        equipment={
            'Signet Ring': 1,
            'Scroll of Pedigree': 1,
            'Fine clothes': 1,
            'Gold': 25
        },
        feature='Retainers: You have the service of three retainers loyal to your family. These retainers can be '
                   'attendants or messengers, and one might be a majordomo. Your retainers are commoners who can '
                   'perform mundane tasks for you, but they do not fight for you, will not follow you into obviously '
                   'dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused.',
    ),

    "Noble": CharBack(
        "Noble",
        skill_prof=['History', 'Persuasion'],
        tool_prof=['One Gaming Set'],
        languages=["Any"],
        equipment={
            'Signet Ring': 1,
            'Scroll of Pedigree': 1,
            'Fine clothes': 1,
            'Gold': 25
        },
        feature='Retainers: You have the service of three retainers loyal to your family. These retainers can be '
                   'attendants or messengers, and one might be a majordomo. Your retainers are commoners who can '
                   'perform mundane tasks for you, but they do not fight for you, will not follow you into obviously '
                   'dangerous areas (such as dungeons), and will leave if they are frequently endangered or abused.',
    ),

    "Outlander": CharBack(
        "Outlander",
        skill_prof=['Athletics', 'Survival'],
        tool_prof=['One Musical Instrument'],
        languages=["Any"],
        equipment={
            'Staff': 1,
            'Hunting Trap': 1,
            'Trophy from an animal you killed': 1,
            'Traveller\'s clothes': 1,
            'Gold': 10
        },
        feature='Wanderer: You have an excellent memory for maps and geography, and you can always recall the '
                   'general layout of terrain, settlements, and other features around you. In addition, you can find food and '
                   'fresh water for yourself and up to five other people each day, provided that the land offers '
                   'berries, small game, water, and so forth.',
    ),

    "Sage": CharBack(
        "Sage",
        skill_prof=['Arcana', 'History'],
        languages=["Any","Any"],
        equipment={
            'Bottle of Ink': 1,
            'Quill': 1,
            'Small knife': 1,
            'Letter from a dead colleague': 1,
            'Common clothes': 1,
            'Gold': 10
        },
        feature='Researcher: When you attempt to learn or recall a piece of lore, if you do not know that '
                   'information, you often know where and from whom you can obtain it. Usually, this information comes '
                   'from a library, scriptorium, university, or a sage or other learned person or creature. Your DM '
                   'might rule that the knowledge you seek is secreted away in an almost inaccessible place, or that '
                   'it simply cannot be found. Unearthing the deepest secrets of the multiverse can require an adventure '
                   'or even a whole campaign.',
    ),

    "Sailor": CharBack(
        "Sailor",
        skill_prof=['Athletics', 'Perception'],
        tool_prof=['Navigator\'s Tools', 'Vehicles (water)'],
        equipment={
            'Silk Rope, feet': 50,
            'Lucky Charm': 1,
            'Common clothes': 1,
            'Gold': 10
        },
        weapons=["Club"],
        feature='Ship\'s Passage: When you need to, you can secure free passage on a sailing ship for yourself and'
                   ' your adventuring companions. You might sail on the ship you served on, or another ship you have '
                   'good relations with (perhaps one captained by a former crewmate). Because you\'re calling in a '
                   'favor, you can\'t be certain of a schedule or route that will meet your every need. Your DM will '
                   'determine how long it takes to get where you need to go. In return for your free passage, you and '
                   'your companions are expected to assist the crew during the voyage.',
    ),

    "Soldier": CharBack(
        "Soldier",
        skill_prof=['Athletics', 'Intimidation'],
        tool_prof=['One Gaming Set', 'Vehicles (land)'],
        equipment={
            'Insignia of Rank': 1,
            'Trophy taken from a fallen enemy': 1,
            'Gaming Set': 1,
            'Common clothes': 1,
            'Gold': 10
        },
        feature='Military Rank: You have a military rank from your career as a soldier. Soldiers loyal to your '
                   'former'
                   ' military organization still recognize your authority and influence, and they defer to you if they'
                   ' are of a lower rank. You can invoke your rank to exert influence over other soldiers and '
                   'requisition simple equipment or horses for temporary use. You can also usually gain access to '
                   'friendly military encampments and fortresses where your rank is recognized.',
    ),

    "Urchin": CharBack(
        "Urchin",
        skill_prof=['Stealth', 'Sleight of Hand'],
        tool_prof=['Disguise Kit', 'Thieves Tools'],
        equipment={
            'Map of the city you grew up in': 1,
            'Token to remember your parents by': 1,
            'Common clothes': 1,
            'Gold': 10
        },
        weapons=["Dagger"],
        feature='City Secrets: You know the secret patterns and flow to cities and can find passages through the '
                   'urban sprawl that others would miss. When you are not in combat, you (and companions you lead) can '
                   'travel between any two locations in the city twice as fast as your speed would normally allow.',
    ),


}
