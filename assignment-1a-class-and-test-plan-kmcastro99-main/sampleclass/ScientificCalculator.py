# ScientificCalculator.py
#
# Author: Karla Castro
# Email: kmcastro@uwaterloo.ca
# Student ID: 20745522
# Date: October 8th, 2023
# This code contains the ScientificCalculator class with its accessor, mutator methods and functionality methods
# The methods are currently a stub type; thus, they all return "None #: Stub"

import numpy as np
import unittest
import numpy as np

class ScientificCalculator:
    """
    ScientificCalculator

    class representing a scientific calculator, the brands avilable in the market,
    the name and prices per name, and a list of functionalities/operations that can be performed.
    """
    def __init__(self, brand_name, models, functionalities):
        """
        Constructor
        Parameters:
            brand_name: string representing the brand of the calculator.
            models: dictionary (string -> float) mapping calculator models per brand to their price.
            functionalities: list of strings with all the available functionalities/operations of the calculator.
            state: string representing if a calculator is working or damaged.
        """
        self.brand_name = brand_name
        self.models = models
        self.functionalities = functionalities
        self.state = None

    # Accessor Methods

    def get_brand_name(self):
        """
        get_brand_name()

        Accessor Method for the name of the calculator brand (brand_name)
        """
        return None #TODO: Stub
    
    def get_price(self, calculator_model):
        """
        get_price()

        Accessor Method for the price of the calculator based on its model.

        Parameters:
            calculator_model: to find the price of the calculator based on its model.

        Returns:
            float or None: The price of the calculator as a float or None if the model is not in the dictionary.

        """
        return None #TODO: Stub

    def get_functionalities(self):
        """
        get_functionalities()

        Accessor Method for a list of operations/functionalities that can be performed with the calculator.
        """
        return None #TODO: Stub
    
    def set_state(self, new_state):
        # Mutator Methods
        """
        set_state()

        Method for changing the current state of a calculator (working/damaged).
        Sets the state after running the functionality tests.

        Parameters:
            new_state: the new state of the calculator.
        
        Returns:
            true: if the state was changed.
            false: otherwise.
        """
        return None #TODO: Stub
    
    def get_state(self):
        # Accessor method
        """
        get_state()

        Accessor Method for the state of the calculator.
        """
        return None #TODO: Stub
    
    def add_models(self, model_name, model_price):
        """
        add_models()

        Method for adding an existing calculator model from the models offered.
        
        Parameters:
            model_name: the name of the new models as a string.
            model_price: the price of the new model as a float.

        Returns:
            true: if the model has been added.
            false: otherwise.
        """
        return None #TODO: Stub

    def change_model_price(self, model_name, new_price):
        """
        change_model_price()

        Method for changing an existing model with a new price.

        Parameters:
            model_name: the name of the models that will be changed (string type).
            new_price: the new price of the model.
        
        Returns:
            true: if the price has been changed.
            false: otherwise.
        """
        return None #TODO: Stub

    def basic_math_operation(x, y, operation_type):
        """
        basic_math_operation()

        Performs mathematical operations on the input values given an operation_type.
        The input values are real numbers.

        Parameters:
            x: A number representing the first input value (float type).
            y: A number representing the second input value (float type).
            operation_type: The operation type to be performed (string type).
                            - Multiplication
                            - Division
                            - Power
        
        Returns:
            result: A value representing the result of the mathematical operation (float type)

        Raises:
            ValueError: If an operation is impossible to perform due to an inappropriate value.
        """
        return None #TODO: Stub
    
    def matrix_operation(matrix_1, matrix_2, operation_type):
        """
        matrix_operation()

        Performs matrix operations on the input matrices given an operation_type.
        Matrices need to be 2x2 or bigger size

        Parameters:
            matrix_1: First matrix of array type (np.ndarray).
            matrix_2: Second matrix of array type (np.ndarray).
            operation_type: The operation type to be performed (string type).
                            - Multiplication 
                            - Determinant
                            - Eigenvalues
        
        Returns:
            result: The result of the matrix operation as array type (np.ndarray)

        Raises:
            ValueError: If an invalid operation type is given.
            LinAlgError: If a linalg function cannot be executed.
        """
        return None #TODO: Stub