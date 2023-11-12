"""
Description: Enumerations to keep track of valid mortgage rates 
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: {Student Name}
Date: {Date}
Usage: The enumerations and list in this file may be used when working 
with mortgages to ensure only valid rates, frequencies and amortization 
periods are used.
"""


from enum import Enum

VALID_AMORTIZATION = [5, 10, 15, 20, 25, 30] 

class MortgageRates(Enum):
    """
    An enumeration containing the different valid mortgage rates.

    Values:
    FIXED_5: 
    FIXED_3:
    FIXED_1:
    VARIABLE_5
    VARIABLE_3:
    VARIABLE_1:
 
    """
    FIXED_5 = 0.0500
    FIXED_3 = 0.0579
    FIXED_1 = 0.0589
    VARIABLE_5 = 0.0650
    VARIABLE_3 = 0.0660
    VARIABLE_1 = 0.0679

class MortgageFrequency(Enum):
    """
    An enumeration containing the different mortgage payment frequencies.

    Values:
    MONTHLY: Payment frequency of monthly payments.
    BI_WEEKLY: Payment frequency of bi weekly payments.
    WEEKLY: Payment frequency of weekly payments.
       
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52


