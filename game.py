"""
Lab 4_6. Finishing the main module for a game.
"""

class Room():
    """
    Room class.
    >>> Room("Kitchen").name
    """
    def __init__(self, name) -> None:
        self.name=name
        self.linkedrooms=[]
        self.character=None
        self.item=None
        self.description=None

    def set_description(self, descr):
        """
        Sets a description. Returns None
        """
        self.description=descr

    def get_details(self):
        """
        Prints details. Returns None.
        """
        print(self.description)
        for i in self.linkedrooms:
            print(f"The {i[0].name} room is {i[1]}")

    def link_room(self, room, direction):
        """
        Sets room links. Returns None.
        """
        self.linkedrooms.append([room, direction])

    def move(self, command):
        """
        Moves a player.
        """
        return [x[0] for x in self.linkedrooms if x[1]==command][0]

    def set_character(self, char):
        """
        Sets character. Returns None.
        """
        self.character = char

    def set_item(self, item):
        """
        Sets item. Returns None.
        """
        self.item = item

    def get_character(self):
        """
        Returns character
        """
        return self.character

    def get_item(self):
        """
        Returns item
        """
        return self.item


class Enemy():
    """
    Enemy class.
    >>> Enemy("Spider").name
    "Spider"
    """
    def __init__(self, name, descr) -> None:
        self.name = name
        self.description=descr
        self.hp=0
    
    def set_weakness(self, weak):
        """
        Sets weakness. Returns None
        """
        self.weakness=weak
    
    def set_conversation(self, conv):
        """
        Sets conv. Returns None
        """
        self.conversation=conv
    
    def talk(self):
        """
        Prints conv. Returns None
        """
        print(self.conversation)

    def fight(self, fight_with):
        """
        Returns True if player guessed with weapon choice. 
        Else returns False.
        """
        return fight_with == self.weakness
    
    def describe(self):
        """
        Prints name and description of a character in the room.
        Returns None
        """
        print(self.name+" is here!")
        print(self.description)
    
    def get_defeated(self):
        """
        Determines if an enemy is dead. Returns it's received damage.
        """
        self.hp+=1
        return self.hp


class Item():
    """
    Enemy class.
    >>> Enemy("Spider").name
    "Spider"
    """
    def __init__(self, name) -> None:
        self.name = name
    
    def set_description(self, descr):
        """
        Sets a description. Returns None
        """
        self.description=descr

    def describe(self):
        """
        Prints a description. Returns None
        """
        print(self.description)
    
    def get_name(self):
        """
        Returns a name.
        >>> Item("Hand").name
        'Hand'
        """
        return self.name
    