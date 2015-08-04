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
    
    def _the_nth_day_in_the_month(self, n, iso_day, month, current_datetime):
        """
        For use when a day is the xth y in the month. Eg Labour Day is the 4th Monday of
        October.
        
        :param n: eg for Labour Day n would be 4
        :param iso_day: they day of the week from 1-7 where Monday is 1 and Sunday is 7
        :param month: month of the year from 1-12 where 1 is January and 12 is December
        :return: True if the current_datetime is the nth day in the month and False if not
        """
        if current_datetime.month == month:
            date_calc = datetime(current_datetime.year,
                                 current_datetime.month,
                                 1)
            
            first_occurence = (iso_day - date_calc.isoweekday())
            if iso_day < date_calc.isoweekday():
                first_occurence += 7                
            date_calc_sunday_delta = first_occurence  + ((n - 1) * 7)
            if current_datetime.day == date_calc.day + date_calc_sunday_delta:
                return True
        return False
    
class MothersDay(Day):
    """
    Happens on the second Sunday of May
    """
    
    def __init__(self):
        super(MothersDay, self).__init__("/{0}".format(self.__class__.__name__.lower()),
                                         "Mother's Day")
    
    def is_today(self, current_datetime=datetime.now(tz=NZ_TIME_ZONE)):
        return self._the_nth_day_in_the_month(2, 7, 5, current_datetime)
    
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
        return self._the_nth_day_in_the_month(1, 7, 9, current_datetime)
    
class LabourDay(Day):
    """
    Happens on October 26th
    """
    
    def __init__(self):
        super(LabourDay, self).__init__("/{0}".format(self.__class__.__name__.lower()),
                                         "Labour Day")
        
    def is_today(self, current_datetime=datetime.now(tz=NZ_TIME_ZONE)):
        return self._the_nth_day_in_the_month(4, 1, 10, current_datetime)
    
class QueensBirthday(Day):
    """
    Happens on the first Monday of June
    """
    
    def __init__(self):
        super(QueensBirthday, self).__init__("/{0}".format(self.__class__.__name__.lower()),
                                         "Queen's Birthday")
        
    def is_today(self, current_datetime=datetime.now(tz=NZ_TIME_ZONE)):
        return self._the_nth_day_in_the_month(1, 1, 6, current_datetime)
    
class NewYearsDay(Day):
    """
    1st of the 1st
    """
    def __init__(self):
        super(NewYearsDay, self).__init__("/{0}".format(self.__class__.__name__.lower()),
                                         "New Year's Day")
        
    def is_today(self, current_datetime=datetime.now(tz=NZ_TIME_ZONE)):
        return current_datetime.month == 1 and current_datetime.day == 1
    
    
MOTHERS_DAY = MothersDay()
CHRISTMAS = Christmas()
TODAY = Today()
WAITANGI_DAY = WaitangiDay()
FATHERS_DAY = FathersDay()
LABOUR_DAY = LabourDay()
QUEENS_BIRTHDAY = QueensBirthday()
NEW_YEARS_DAY = NewYearsDay()

DAYS = (TODAY,
        MOTHERS_DAY,
        FATHERS_DAY,
        WAITANGI_DAY,
        CHRISTMAS,
        LABOUR_DAY,
        QUEENS_BIRTHDAY,
        NEW_YEARS_DAY)    