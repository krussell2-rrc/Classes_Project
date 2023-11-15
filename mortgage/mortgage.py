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
            amortization (int): The number of years in which the loan must be repaid.

        Raises:
        """
        self._loan_amount = loan_amount
        self._rate = rate
        self._frequency = frequency
        self._amortization = amortization

    @property
    def loan_amount(self) -> float:
        """
        float: Gets the amount of the mortgage loan.

        Raises: 
            ValueError: Raised if the incoming loan amount value is zero or negative.
        """
        return self._loan_amount
    
    @property
    def rate(self) -> MortgageRate:
        """
        MortgageRate: Gets the annual interest rate.

        Raises: 
            ValueError: Raised if the incoming rate value is not an instance of the MortgageRate enum.
        """
        return self._rate

    @property
    def frequency(self) -> MortgageFrequency:
        """   
        MortgageFrequency: Gets the number of payments per year.

        Raises:
            ValueError: Raised if the incoming frequency value is not an instance of the MortgageFrequency enum.    
        """
        return self._frequency
    
    @property
    def amortization(self) -> int:
        """
        amortization (int): Gets the number of years in which the loan must be paid.

        Raises:
            ValueError: Raised if the incoming amortization value is not found in the VALID_AMORTIZATION list.               
        """
        return self._amortization
    
    @loan_amount.setter
    def loan_amount(self, loan_amount: float) -> None:
        """
        Sets the amount of the mortgage loan.

        Args:
            loan_amount (float): The amount of the mortgage loan.

        Raises: 
            ValueError: Raised if the incoming loan amount value is zero or negative.
        """    
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        
        self._loan_amount = loan_amount
           
    @rate.setter
    def rate(self, rate: MortgageRate) -> None:
        """
        Sets the annual interest rate.

        Args:
            rate (MortgageRate): The annual interest rate.

        Raises: 
            ValueError: Raised if the incoming rate value is not an instance of the MortgageRate enum.
        """
        if not isinstance(rate, MortgageRate):
            raise ValueError("Rate provided is invalid.")
            
        self._rate = rate
        
    @frequency.setter
    def frequency(self, frequency: MortgageFrequency) -> None:
        """   
        Sets the number of payments per year.

        Args: 
            frequency (MortgageFrequency): The number of payments per year.

        Raises:
            ValueError: Raised if the incoming frequency value is not an instance of the MortgageFrequency enum.    
        """
        if not isinstance (frequency, MortgageFrequency):
            raise ValueError("Frequency provided is invalid.")
        
        self._frequency = frequency
        
    @amortization.setter
    def amortization(self, amortization: int) -> None:
        """
        Sets number of years in which the loan must be paid.

        Args: 
            amortization (int): The number of years in which the loan must be repaid.

        Raises:
            ValueError: Raised if the incoming amortization value is not found in the VALID_AMORTIZATION list.               
        """
        if not amortization in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")

        self._amortization = amortization

    def calculate_payment(self) -> float:
        """
        Calculates and returns the mortgage payment amount based on the loan amount, 
        annual interest rate, payment frequency and amortization.

        Returns:
            float: The mortgage payment amount.

        Raises:
            ValueError: Raised if the incoming loan amount value is zero or negative.        
        """        
        if self.loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        
        monthly_interest_rate = self.rate.value / 12 
        number_of_payments = self.amortization * self.frequency.value

        calculated_payment = (self.loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments / (((1 + monthly_interest_rate) ** number_of_payments) - 1))

        calculated_payment = round(calculated_payment, 2)
        return calculated_payment
    
    def __str__(self):
        """String representation of Mortgage object.
        """
        return f"Mortgage Amount: ${self._loan_amount:,.2f}\nRate: {self._rate.value * 100}%\nAmortization: {self._amortization}\nFrequency: {self._frequency.name.capitalize()} -- Calculated Payment: ${self.calculate_payment():,.2f}"

    def __repr__(self):
        """Representation of Mortgage object.
        """
        return f"[{self.loan_amount}, {self._rate.value}, {self._amortization}, {self._frequency.value}]"

    

        


        

    

    
        
        


        
    