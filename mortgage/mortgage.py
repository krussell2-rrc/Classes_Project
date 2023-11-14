"""
Description: A class meant to manage Mortgage options.
Author: Kareem Russell
Date: November 12, 2023
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""

from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class Mortgage:
    def __init__(self, loan_amount: float, rate: MortgageRate, frequency: MortgageFrequency, amortization: int):

        """
        This class will create an instance of the Mortgage class to manage mortgage records
        and calculate payments.

        Args:
            loan_amount (float): The amount of mortgage loan.
            rate (MortgageRate): The annual interest rate.
            frequency (MortgageFrequency): The number of payments per year.
            amortization (int): The number of years to repay the mortgage loan.

        Raises:

        """
        self._loan_amount = loan_amount
        self._rate = rate
        self._frequency = frequency
        self._amortization = amortization

    @property
    def loan_amount(self) -> float:
        """
        float: Gets and sets the amount of the mortgage loan.

        Raises: 
            ValueError: Raised if the incoming loan amount value is zero or negative.
        """
        return self._loan_amount
    
    @property
    def rate(self) -> MortgageRate:
        """
        MortgageRate: Gets and sets the annual interest rate.

        Raises: 
            ValueError: Raised if the incoming rate value is not an instance of the MortgageRate enum.
        """
        return self._rate

    @property
    def frequency(self) -> MortgageFrequency:
        """   
        MortgageFrequency: Gets and sets the number of payments per year.

        Raises:
            ValueError: Raised if the incoming frequency value is not an instance of the MortgageFrequency enum.    
        """
        return self._frequency
    
    @property
    def amortization(self) -> int:
        """
        amortization (int): Gets and sets number of years.

        Raises:
            ValueError: Raised if the incoming amortization value is not found in the VALID_AMORTIZATION list.               
        """
        return self._amortization
    
    @loan_amount.setter
    def loan_amount(self, loan_amount: float) -> None:    
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        
        self._loan_amount = loan_amount
           
    @rate.setter
    def rate(self, rate: MortgageRate) -> None:
        if not isinstance(rate, MortgageRate):
            raise ValueError("Rate provided is invalid.")
            
        self._rate = rate
        
    @frequency.setter
    def frequency(self, frequency: MortgageFrequency) -> None:
        if not isinstance (frequency, MortgageFrequency):
            raise ValueError("Frequency provided is invalid.")
        
        self._frequency = frequency
        
    @amortization.setter
    def amortization(self, amortization: int) -> None:
        if not amortization in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")

        self._amortization = amortization

    def calculate_payment(self) -> float:
        if self.loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        
        monthly_interest_rate = self.rate.value / 12 
        number_of_payments = self.amortization * self.frequency.value

        calculated_payment = (self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / (((1 + monthly_interest_rate) ** number_of_payments) - 1))

        calculated_payment = round(calculated_payment, 2)
        return calculated_payment
    

        


        

    

    
        
        


        
    