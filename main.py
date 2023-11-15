"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: Kareem Russell
Date: November 14, 2023
"""

from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

try:
    with open ("data\\pixell_river_mortgages.txt","r") as input:
        print("**************************************************")
    
        for data in input:
            items = data.split(",")
            
            try:
                amount = float(items[0])
                rate = getattr(MortgageRate, items[1])
                amortization = int(items[2])
                frequency = getattr(MortgageFrequency, items[3])

                mortgage_object = Mortgage(amount, rate, frequency, amortization)
                print(mortgage_object)

            except ValueError as e:
                # This except block will catch Explicit exceptions: 
                # Those raised by the programmer in the Mortgage class.
                print(f"Data: {data.strip()} caused Exception: {e}")
            
            except Exception as e:
                # This except block will catch Implicit exceptions:  
                # Those raised through normal execution.
                print(f"Data: {data.strip()} caused Exception: {e}")
            finally:
                print("**************************************************")
except FileNotFoundError:
    print("File not found.")