'''
Created on Jul 12, 2015

@author: hashtonmartyn
'''
from datetime import datetime
from pytz import timezone
NZ_TIME_ZONE = timezone("Pacific/Auckland")

class Day(object):
    """
    This is a base class, you must override the is_today method in each class that inherits
    from this. 
    """
    
    def __init__(self, URL, name):
        """
        :param URL: something to stick in the href for the user to click
        :param name: the name of the day eg "Mother's Day"
        """
        self._URL = URL
        self._name = name
        
    @property
    def name(self):
        """
        The name of the day eg 'Waitangi Day'
        """
        return self._name
    
    @property
    def URL(self):
        """
        The URL for the day eg "christmasday"
        """
        return self._URL
    
    def is_today(self, current_datetime):
        raise NotImplementedError("You must implement this in your child class")
    
class MothersDay(Day):
    """
    Happens on the second Sunday of May
    """
    
    def __init__(self):
        super(MothersDay, self).__init__("/{0}".format(self.__class__.__name__.lower()),
                                         "Mother's Day")
    
    def is_today(self, current_datetime=datetime.now(tz=NZ_TIME_ZONE)):
        if current_datetime.month == 5:
            date_calc = datetime(current_datetime.year,
                                 current_datetime.month,
                                 1)
            date_calc_sunday_delta = (7 - date_calc.isoweekday()) + 7
            if current_datetime.day == date_calc.day + date_calc_sunday_delta:
                return True
        return False
    
class Christmas(Day):
    """
    25th of December
    """
    
    def __init__(self):
        super(Christmas, self).__init__("/{0}".format(self.__class__.__name__.lower()),
                                         "Christmas Day")
    
    def is_today(self, current_datetime=datetime.now(tz=NZ_TIME_ZONE)):
        return current_datetime.month == 12 and current_datetime.day == 25
    
class Today(Day):
    """
    It's always today
    """
    
    def __init__(self):
        super(Today, self).__init__("/{0}".format(self.__class__.__name__.lower()),
                                         "Today")
    
    def is_today(self, current_datetime=datetime.now(tz=NZ_TIME_ZONE)):
        return True
    
    @property
    def name(self):
        return datetime.now(tz=NZ_TIME_ZONE).strftime("%A %d %B %Y")
    
class WaitangiDay(Day):
    """
    Happens on the 6th of Feb
    """
    
    def __init__(self):
        super(WaitangiDay, self).__init__("/{0}".format(self.__class__.__name__.lower()),
                                          "Waitangi Day")
        
    def is_today(self, current_datetime=datetime.now(tz=NZ_TIME_ZONE)):
        return current_datetime.month == 2 and current_datetime.day == 6
    
class FathersDay(Day):
    """
    Happens on the first Sunday of September
    """
    
    def __init__(self):
        super(FathersDay, self).__init__("/{0}".format(self.__class__.__name__.lower()),
                                         "Father's Day")
    
    def is_today(self, current_datetime=datetime.now(tz=NZ_TIME_ZONE)):
        if current_datetime.month == 9:
            date_calc = datetime(current_datetime.year,
                                 current_datetime.month,
                                 1)
            date_calc_sunday_delta = 7 - date_calc.isoweekday()
            if current_datetime.day == date_calc.day + date_calc_sunday_delta:
                return True
        return False
    
    
MOTHERS_DAY = MothersDay()
CHRISTMAS = Christmas()
TODAY = Today()
WAITANGI_DAY = WaitangiDay()
FATHERS_DAY = FathersDay()

DAYS = (TODAY,
        MOTHERS_DAY,
        FATHERS_DAY,
        WAITANGI_DAY,
        CHRISTMAS)    