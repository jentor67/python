from datetime import date
from datetime import timedelta

"""JohnAdamsRecord.py: """
"""  1.  Determine when John Adams became the oldest presidents"""
"""  2.  Determine when Ronald Reagan became the oldest president"""
"""  3.  Determine the length of time John Adams was the oldest president"""
__author__    = "John Major"
__copyright__ = "Copyright 2018, Jentor"

birthGeorgeWashington = date(1732, 2, 22)
deathGeorgeWashington = date(1799, 12, 14)
birthJohnAdams = date(1735, 10, 30)
deathJohnAdams = date(1826, 7, 4)
birthRonaldReagan = date(1911, 2, 6)

deltaGW = (deathGeorgeWashington - birthGeorgeWashington).days 

deltaJA = (deathJohnAdams - birthJohnAdams).days 

dateJAOldest = birthJohnAdams + timedelta(days=deltaGW) 
dateRROldest = birthRonaldReagan + timedelta(days=deltaJA) 

recordJA = (dateRROldest - dateJAOldest).days


print("George Washington was %1.2f years old when he died." % (deltaGW/365.25))
print("John Adams turned the same age on "+str(dateJAOldest))
print("When John Adams died he was %1.2f years old." % (deltaJA/365.25))
print("Ronald Reagan turned the same age as John Adams on his death on "+str(dateRROldest))
print("So John Adams held the record as the oldest Presdent for %1.2f years." % (recordJA/365.25))
