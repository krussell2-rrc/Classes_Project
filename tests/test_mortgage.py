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
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        with self.assertRaises(ValueError) as context:
            target.loan_amount = 0

        # Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_rate_invalid_input(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        with self.assertRaises(ValueError) as context:
            target.rate = "MortgageRate.FIXED_2"
        # Assert
        self.assertEqual(str(context.exception), "Rate provided is invalid.")

    def test_frequency_invalid_input(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        with self.assertRaises(ValueError) as context:
            target.frequency = "MortgageFrequency.DAILY"

        # Assert
        self.assertEqual(str(context.exception), "Frequency provided is invalid.")

    def test_amortization_invalid_input(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        with self.assertRaises(ValueError) as context:
            target.amortization = 12

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
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        with self.assertRaises(ValueError) as context:
            target.loan_amount = -50
        
        # Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_loan_amount_mutator_zero_value(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        with self.assertRaises(ValueError) as context:
            target.loan_amount = 0

        # Assert
        self.assertEqual(str(context.exception), "Loan Amount must be positive.")

    def test_loan_amount_valid_accessor(self):
        # Arrange
        loan_amount = 1000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        actual = target._loan_amount

        # Assert
        expected = 1000
        self.assertEqual(expected,actual)

    # rate accessor/mutator tests

    def test_rate_valid_accessor(self):
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

    def test_rate_invalid_mutator(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        with self.assertRaises(ValueError) as context:
            target.rate = "MortgageRate.FIXED_2"

        # Assert
        self.assertEqual(str(context.exception), "Rate provided is invalid.")

    # frequency accessor/mutator tests

    def test_frequency_valid_accessor(self):
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

    def test_frequency_invalid_mutator(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        with self.assertRaises(ValueError) as context:
            target.frequency = "MortgageFrequency.DAILY"

        # Assert
        self.assertEqual(str(context.exception), "Frequency provided is invalid.")

    # amortization accessor/mutator tests

    def test_amortization_valid_accessor(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        actual = target._amortization

        # Assert
        expected = 15
        self.assertEqual(expected,actual)

    def test_amortization_invalid_mutator(self):
        # Arrange
        loan_amount = 5000
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 15

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        with self.assertRaises(ValueError) as context:
            target.amortization = 37

        # Assert
        self.assertEqual(str(context.exception), "Amortization provided is invalid.")

    # calculate_payment tests

    def test_calculate_payment_valid(self):
        # Arrange
        loan_amount = 682912.45
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.MONTHLY
        amortization = 30

        target = Mortgage(loan_amount, rate, frequency, amortization)
        
        # Act
        calculated_payment = target.calculate_payment()

        # Assert
        self.assertAlmostEqual(calculated_payment, 4046.23, places=2)

    def test_calculate_payment_new_loan_amount(self):
        # Arrange
        loan_amount = 2000.12
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.MONTHLY
        amortization = 30

        target = Mortgage(loan_amount, rate, frequency, amortization)
        
        # Act
        calculated_payment = target.calculate_payment()

        # Assert
        self.assertAlmostEqual(calculated_payment, 11.85, places=2)

    def test_calculate_payment_new_rate(self):
        # Arrange
        loan_amount = 682912.45  
        rate = MortgageRate.FIXED_5
        frequency = MortgageFrequency.MONTHLY
        amortization = 30

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        calculated_payment = target.calculate_payment()

        # Assert
        self.assertAlmostEqual(calculated_payment, 3666.02, places=2)

    def test_calculate_payment_new_frequency(self):
        # Arrange
        loan_amount = 682912.45  
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.BI_WEEKLY
        amortization = 30

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        calculated_payment = target.calculate_payment()

        # Assert
        self.assertAlmostEqual(calculated_payment, 3427.18, places=2)

    def test_calculate_payment_new_amortization(self):
        # Arrange
        loan_amount = 682912.45  
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.MONTHLY
        amortization = 5

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        calculated_payment = target.calculate_payment()

        # Assert
        self.assertAlmostEqual(calculated_payment, 13167.71, places=2)

    # __str__ tests

    def test_str_monthly_payment(self):
        # Arranges
        loan_amount = 682912.45  
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.MONTHLY
        amortization = 30

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        result = str(target)

        # Assert
        expected = "Mortgage Amount: $682,912.45\nRate: 5.89%\nAmortization: 30\nFrequency: Monthly -- Calculated Payment: $4,046.23"
        self.assertEqual(expected, result)

    def test_str_biweekly_payment(self):
        # Arrange
        loan_amount = 682912.45  
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.BI_WEEKLY
        amortization = 30

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        result = str(target)

        # Assert
        expected = "Mortgage Amount: $682,912.45\nRate: 5.89%\nAmortization: 30\nFrequency: Bi_weekly -- Calculated Payment: $3,427.18"
        self.assertEqual(expected, result)

    def test_str_weekly_payment(self):
        # Arrange
        loan_amount = 682912.45  
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.WEEKLY
        amortization = 30

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        result = str(target)

        # Assert
        expected = "Mortgage Amount: $682,912.45\nRate: 5.89%\nAmortization: 30\nFrequency: Weekly -- Calculated Payment: $3,353.58"
        self.assertEqual(expected, result)

    # repr test

    def test_repr_valid(self):
        # Arrange
        loan_amount = 682912.45  
        rate = MortgageRate.FIXED_1
        frequency = MortgageFrequency.WEEKLY
        amortization = 30

        target = Mortgage(loan_amount, rate, frequency, amortization)

        # Act
        result = repr(target)

        # Assert
        expected = "[682912.45, 0.0589, 30, 52]"
        self.assertEqual(expected,result)










    



        

    




    

