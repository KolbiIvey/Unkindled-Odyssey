<div align="center">

# ![home page](/main_app/static/home.png)

# Unkindled-Odyssey

### Built by: **[Kolbi Ivey](https://www.linkedin.com/in/kolbi-ivey-15b5631a8/)**

### Link to deployed app: **[Unkindled-Odyssey](https://unkindledodyssey.herokuapp.com/)**


# Technologies Used:
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![Maintainer](https://img.shields.io/badge/Maintainer-Kolbi-blue)
![Ask](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)

![Django](https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)


![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Heroku badge](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)





 [Trello](https://trello.com/b/EblsAQBN/unkindled-odyssey)

 [Wireframe/ERD](https://whimsical.com/CPw5Uo9ix1XHVb9P3erB16)



## My Favorite Code Snipit:
The Charcter Modl for my project is by far my favorite bit of code. It was the very first thing I worked on.
```
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

STARTING_WEAPONS = (
    ('S', 'Straight Sword'),
    ('K', 'Katana'),
    ('G', 'Greatsword'),
    ('A', 'Axe'),
    ('C', 'Curved Sword'),
    ('D', 'Dagger'),
    ('H', 'Halberd'),
    ('B', 'Bow'),
    ('W', 'Whip'),
    ('T', 'Talisman'),
    ('Ss', 'Sorcerer\'s Staff'),
)

STARTING_GIFT = (
    ('E', 'Ember'),
    ('L', 'Life Ring'),
    ('Y', 'Young White Branch'),
    ('D', 'Divine Blessing'),
    ('H', 'Human Pine Resin'),
)


class Character(models.Model):
    name = models.CharField(max_length=100)
    starting_class = models.CharField(
        max_length=1,
        choices=STARTING_CLASS,
        default=[0][0]
    )
    starting_weapon = models.CharField(
        max_length=100,
        choices=STARTING_WEAPONS,
        default=STARTING_WEAPONS[0][0]
    )
    starting_gift = models.CharField(
        max_length=1,
        choices=STARTING_GIFT,
        default=STARTING_GIFT[0][0]
    )

    level = models.IntegerField()
    story = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
