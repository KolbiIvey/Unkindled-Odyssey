<div align="center">

# Unkindled-Odyssey

# ![home-page](/main_app/static/home-page.png)

## Description
Immerse yourself in the world of Dark Souls! Create a character with your name, starting class,
character level, and accompanying attributes, as well as watch a short story about your
newly created character and their struggles unfolds before your eyes. Welcome, to Unkindled Odyssey.

### Built by: **[Kolbi Ivey](https://www.linkedin.com/in/kolbi-ivey-15b5631a8/)**

### Link to deployed app: **[Unkindled-Odyssey](https://unkindledodyssey.herokuapp.com/)**


### Technologies Used:
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


## Additional Screenshots

#### Character Index Page
![index](/main_app/static/index-page.png)

#### Character Creation Form
![create](/main_app/static/create-form.png)

#### Character Detail Page Part 1
![detail-1](/main_app/static/detail-1.png)

#### Character Detail Page Part 2
![detail-2](/main_app/static/detail-2.png)


</div>

## My Favorite Code Snipit:
The Charcter Model for my project is by far my favorite bit of code. It was the very first thing I worked on.
```python
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

## Next Steps/Future User Stories
- AAU: I want to be able to comment on other user's stories and characters, and see comments on my own stories and characters.
- AAU: I want to be able to view other user's characters and their generated stories.
- AAU: I want to be able to search for characters by name, attributes, or other criteria.
- AAU: I want to be able to sort characters by various attributes, such as level, strength, or dexterity.
- AAU: I want to be able to save other users' characters to my profile.
- AAU: I want to be able to receive notifications when someone comments on one of my stories or characters.
- AAU: I want to be able to rate and review other users' characters and stories.