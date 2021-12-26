from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(255, 255, 0),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)
wolf = Actor(
    char="w",
    color=(255, 255, 255),
    name="Wolf",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=8, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=45),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
weak_healing_potion = Item(
    char="!",
    color=(204, 255, 204),
    name="Weak Healing Potion",
    consumable=consumable.HealingConsumable(amount=2),
)
healing_potion = Item(
    char="!",
    color=(102, 255, 178),
    name="Healing Potion",
    consumable=consumable.HealingConsumable(amount=5),
)
great_healing_potion = Item(
    char="!",
    color=(0, 255, 0),
    name="Great Healing Potion",
    consumable=consumable.HealingConsumable(amount=10),
)
lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

moon_prism_staff = Item(
    char="|",
    color=(0, 102, 204),
    name="Moon Prism Healing Staff",
    consumable=consumable.HealingConsumable(amount=30),
)

dagger = Item(
    char="/", 
    color=(0, 191, 255), 
    name="Dagger", 
    equippable=equippable.Dagger()
)

fire_sword = Item(
    char="/", 
    color=(255, 102, 102), 
    name="Sword w/Fire Enchantment", 
    equippable=equippable.FireSword()
)

sword = Item(
    char="/", 
    color=(0, 191, 255), 
    name="Sword", 
    equippable=equippable.Sword()
)

leather_armor = Item(
    char="[",
    color=(139, 69, 19),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)

chain_mail = Item(
    char="[", 
    color=(139, 69, 19), 
    name="Chain Mail", 
    equippable=equippable.ChainMail()
)
