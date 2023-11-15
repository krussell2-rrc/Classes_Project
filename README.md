# Assignment 6

## Description
Using classes and enums to determine mortgage payment options for clients.

## Author
Kareem Russell

## Assignment
Assignment 6: Defining and using classes.

pixell_lookup.py

- Created Enum MortgageRate to store and keep track of the different valid mortgage rates.

- Created Enum MortgageFrequency to store and keep track of the different valid mortgage payment frequencies.

mortgage.py

- Created mortgage class to manage mortgage records and calculate payments. 

- Created init method in mortgage class with arguments: loan_amount, rate, frequency, amortization.

- Created accessors and setters for each argument in the init method.

- Created function that calculates and returns the mortgage payment amount based on the loan amount, annual interest rate, payment frequency and amortization.

- Created str method that prints a string representation of the mortgage object.

- Created repr method that prints a representation of the mortgage object.

test_mortgage.py

- Created test cases to test the init method on its the functionality of raising exceptions and ability to set attributes when valid inputs are provided.

- Created test cases to test the functionality of the accessors and mutators of the arguments: loan_amount, rate, frequency and amortization.

- Created test cases to test the functionality of the calculate_payment function.

- Created test cases to test the functionality of the str method.

- Created test cases to test the functionality of the repr method.

main.py 

- Added import statements for the Mortgage class, MortgageRate and MortgageFrequency enumerations and VALID_AMORTIZATION list.

- Wrapped with open function with a try-except block to raise a FileNotFoundError exception.

- Instantiated and printed mortgage object using the values provided.

- Added getattr function to get the names of the attributes of the enumerations.

- Converted amortization value to an integer.
