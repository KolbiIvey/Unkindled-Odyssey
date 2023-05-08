from django.db import models
from django.contrib.auth.models import User


STARTING_CLASS = (
    ('K', 'Knight'),
    ('M', 'Mercenary'),
    ('W', 'Warrior'),
    ('H', 'Herald'),
    ('T', 'Thief'),
    ('A', 'Assassin'),
    ('S', 'Sorcerer'),
    ('P', 'Pyromancer'),
    ('C', 'Cleric'),
    ('D', 'Deprived'),
)


STARTING_ATTRIBUTES = {
    'K': {'VIG': 16, 'ATT': 10, 'END': 12, 'VIT': 15, 'STR': 13, 'DEX': 12, 'INT': 9, 'FTH': 9, 'LCK': 7},
    'M': {'VIG': 11, 'ATT': 12, 'END': 11, 'VIT': 10, 'STR': 10, 'DEX': 16, 'INT': 10, 'FTH': 8, 'LCK': 9},
    'W': {'VIG': 14, 'ATT': 6, 'END': 16, 'VIT': 15, 'STR': 16, 'DEX': 9, 'INT': 7, 'FTH': 9, 'LCK': 11},
    'H': {'VIG': 12, 'ATT': 10, 'END': 9, 'VIT': 12, 'STR': 12, 'DEX': 11, 'INT': 8, 'FTH': 13, 'LCK': 11},
    'T': {'VIG': 10, 'ATT': 11, 'END': 10, 'VIT': 9, 'STR': 9, 'DEX': 14, 'INT': 10, 'FTH': 8, 'LCK': 14},
    'A': {'VIG': 10, 'ATT': 14, 'END': 11, 'VIT': 10, 'STR': 10, 'DEX': 14, 'INT': 11, 'FTH': 9, 'LCK': 10},
    'S': {'VIG': 9, 'ATT': 16, 'END': 9, 'VIT': 7, 'STR': 7, 'DEX': 12, 'INT': 16, 'FTH': 7, 'LCK': 12},
    'P': {'VIG': 8, 'ATT': 12, 'END': 14, 'VIT': 8, 'STR': 12, 'DEX': 9, 'INT': 14, 'FTH': 14, 'LCK': 7},
    'C': {'VIG': 10, 'ATT': 14, 'END': 9, 'VIT': 10, 'STR': 12, 'DEX': 8, 'INT': 7, 'FTH': 16, 'LCK': 13},
    'D': {'VIG': 10, 'ATT': 10, 'END': 10, 'VIT': 10, 'STR': 10, 'DEX': 10, 'INT': 10, 'FTH': 10, 'LCK': 10}
}


class Character(models.Model):
    name = models.CharField(max_length=100)
    starting_class = models.CharField(
        max_length=1,
        choices=STARTING_CLASS,
        default=[0][0]
    )
    level = models.IntegerField()
    story = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def starting_attributes(self):
        return STARTING_ATTRIBUTES[self.starting_class]
