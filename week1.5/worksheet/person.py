# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self,name,birth):
        """initialises a person with name and date of birth"""
        if type(name) != str:
            raise TypeError

        if name == "":
            raise ValueError

        if type(birth) != date:
            raise TypeError

        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here

    def initials(self):
        """returns uppercase initials of name"""
        nameInitials = ""
        for i in self.name.split():
            nameInitials = nameInitials + i[0].upper()
        return nameInitials

    def is_birthday(self):
        """checks if today is person's birthday"""
        dateToday = date.today()
        return(self.birth.month, self.birth.day) == (dateToday.month, dateToday.day)
