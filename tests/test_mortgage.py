"""
Description: A class used to test the Mortgage class.
Author: Kareem Russell
Date: November 12, 2023
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
import unittest
from unittest import TestCase
from unittest.mock import patch
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, MortgageFrequency, VALID_AMORTIZATION

class MortgageTests(unittest.TestCase):

    # __init__ tests
    
    def test_loan_amount_invalid_input(self):
        # Arrange
        mortgage_instance = Mortgage(50000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 15)
        invalid_loan_amount = -50.0

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage_instance.loan_amount = invalid_loan_amount

        # Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_rate_invalid_input(self):
        # Arrange
        mortgage_instance = Mortgage(100000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 15)
        invalid_rate = "FIXED_2"

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage_instance.rate = invalid_rate

        # Assert
        self.assertEqual(str(context.exception), "Rate provided is invalid.")

    def test_frequency_invalid_input(self):
        # Arrange
        mortgage_instance = Mortgage(100000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 15)
        invalid_frequency = "DAILY"

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage_instance.frequency = invalid_frequency

        # Assert
        self.assertEqual(str(context.exception), "Frequency provided is invalid.")

    def test_amortization_invalid_input(self):
        # Arrange
        mortgage_instance = Mortgage(100000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 15)
        invalid_amortization = 12

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage_instance.amortization = invalid_amortization

        # Assert
        self.assertEqual(str(context.exception), "Amortization provided is invalid.")

    def test_init_sets_valid_attributes(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        # Act
        target = Mortgage(loan_amount, rate, frequency, amortization)
        actual = target._loan_amount, target._rate, target._frequency, target._amortization

        # Assert
        expected = 5000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 15
        self.assertEqual(expected, actual)

    # loan_amount accessor/mutator tests

    def test_loan_amount_mutator_negative_value(self):
        # Arrange
        mortgage_instance = Mortgage(50000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 15)
        negative_loan_amount = -50

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage_instance.loan_amount = negative_loan_amount

        # Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_loan_amount_mutator_zero_value(self):
        # Arrange
        mortgage_instance = Mortgage(50000, MortgageRate.FIXED_5, MortgageFrequency.MONTHLY, 15)
        zero_loan_amount = 0

        # Act
        with self.assertRaises(ValueError) as context:
            mortgage_instance.loan_amount = zero_loan_amount

        # Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_loan_amount_mutator_positive_value(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        target._loan_amount = 1000
        actual = target.loan_amount

        # Assert
        expected = 1000
        self.assertEqual(expected,actual)

    # rate accessor/mutator tests

    def test_rate_accessor(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        actual = target._rate

        # Assert
        expected = MortgageRate.FIXED_5
        self.assertEqual(expected,actual)

    def test_rate_mutator(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        target._rate = MortgageRate.FIXED_3
        actual = target._rate

        # Assert
        expected = MortgageRate.FIXED_3
        self.assertEqual(expected,actual) 

    # frequency accessor/mutator tests

    def test_frequency_accessor(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        actual = target._frequency

        # Assert
        expected = MortgageFrequency.MONTHLY
        self.assertEqual(expected,actual)

    def test_frequency_mutator(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        target._frequency = MortgageFrequency.WEEKLY
        actual = target._frequency

        # Assert
        expected = MortgageFrequency.WEEKLY
        self.assertEqual(expected,actual)         


    


        

    




    

