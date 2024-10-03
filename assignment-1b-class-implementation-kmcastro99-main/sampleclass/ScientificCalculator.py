# ScientificCalculator.py
#
# Author: Karla Castro
# Email: kmcastro@uwaterloo.ca
# Student ID: 20745522
#
# This code contains the ScientificCalculator class with its accessor, mutator methods and functionality methods
# The methods are currently a stub type; thus, they all return "None #: Stub"

import numpy as np
import sys
from numpy.linalg import LinAlgError
import matplotlib.pyplot as plt

# Cretae class for custom error
class PriceTooHighError(Exception):
    """
    PriceTooHighError

    raise when a price above 100 is given for a model
    """
    pass

# Create Scientific Calculator Class
class ScientificCalculator:
    """
    ScientificCalculator

    class representing a scientific calculator, the brands avilable in the market,
    the name and prices per name, and a tuple of functionalities/operations that can be performed.
    """

    # Storage Analysis

    def __sizeof__(self):
        """
        __sizeof__()

        Sums up your various members to get the accurate size of the class instance
        """
        # Returm summation of sizes
        return sys.getsizeof(self._brand_name) + sys.getsizeof(self._models) + sys.getsizeof(self._functionalities) + sys.getsizeof(self._state)

    def __init__(self, brand_name, models, functionalities):
        """
        Constructor
        Parameters:
            brand_name: string representing the brand of the calculator.
            models: dictionary (string -> float) mapping calculator models per brand to their price.
            functionalities: tuple of strings with all the available functionalities/operations of the calculator.
            state: string representing if a calculator is working or damaged.
        """
        # Check if the brand_name is a string
        if type(brand_name) == str:
            # Assign brand_name to the instance variable
            self._brand_name = brand_name
        else:
            # Raise error when not a string type
            raise TypeError('brand_name expects a string type')
        
        # Check if models is a dictionary
        if type(models) == dict:
            self._models = models
        else:
            # Raise error when not a dictionary type
            raise TypeError('models expects a dictionary type')
        # Check if keys in dictionary are int or floats
        if not isinstance(models.get(list(models.keys())[1]), (int, float)):
                # Raise Error when not int or float
                raise TypeError('The price needs to be an int or float')
        # Check if functionalities type is tuple
        if type(functionalities) == tuple:
            # Check if elements in tuple are strings
            for i in range(len(functionalities)):
                if type(functionalities[i]) == str:
                    self._functionalities = functionalities
                else:
                    # Raise error when not a string type
                    raise TypeError('element in tuple should be a string type')
        else:
            raise TypeError('functionalities expects a tuple type')
        
        self._state = None
        
    # Accessor Methods

    def get_brand_name(self):
        """
        get_brand_name()

        Accessor Method for the name of the calculator brand (brand_name)
        """
        return self._brand_name
    
    def get_price(self, calculator_model):
        """
        get_price()

        Accessor Method for the price of the calculator based on its model.

        Parameters:
            calculator_model: to find the price of the calculator based on its model.

        Returns:
            float or None: The price of the calculator as a float or None if the model is not in the dictionary.

        """

        # Check that calculator_model exists in the dictionary
        if calculator_model in self._models:
            # Access the element based on the reference element
            price = self._models[calculator_model]
            return price
        else:
            return None

    def get_functionalities(self):
        """
        get_functionalities()

        Accessor Method for a tuple of operations/functionalities that can be performed with the calculator.
        """
        return self._functionalities
    
    def set_state(self):
        # Mutator Methods
        """
        set_state()

        Method for changing the current state of a calculator (working/damaged).
        Sets the state after running one functionality test (multiplication).

        Parameters:
            new_state: the new state of the calculator.
        
        Returns:
            true: if the state was changed.
            false: otherwise.
        """
        try:
            # Check multiplication functionality
            result = self.basic_math_operation(5, 2, 'multiplication')
            # If working set new_state to "working", if damaged set new_state to "damaged
            if result == 10:
                new_state = 'working'
                if new_state != self._state:
                    self._state = new_state
                    return True
                else: 
                    return False
            elif result == "10":
                new_state = 'damaged'
                if new_state != self._state:
                    self._state = new_state
                    return True
                else: 
                    return False
        except:
            return None
    
    def get_state(self):
        # Accessor method
        """
        get_state()

        Accessor Method for the state of the calculator.
        """
        # Call method to set_state and return the state
        ScientificCalculator.set_state(self)
        return self._state
    
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

        # Check if the model name is already in the models dictionary
        # In case there is a new model, update the dictionary with the new model
        if type(model_name) !=  str:
            raise TypeError('The model name needs to be an string')
        else:
            # Check if model_price is an int or float
            if not isinstance(model_price, (int, float)):
                raise TypeError('The new price needs to be an int or float')
            # Check if model_price is negative
            if model_price < 0:
                raise ValueError('The model price cannot be negative')
            # Check if model_price is higher than 100
            elif model_price > 100:
                raise PriceTooHighError('The model price cannot be higher than 100')
            else:
                if model_name in self._models:
                    return False
                else:
                    # Update dictionary with new model
                    self._models.update({model_name: model_price})
                    return True

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
        # Check if the model name is a string
        if type(model_name) !=  str:
            # Raise error if model_name is not a string
            raise TypeError('The model name needs to be an string')
        else:
            # Raise error if new_price is not an int or float
            if not isinstance(new_price, (int, float)):
                raise TypeError('The new price needs to be an int or float')
            # Raise error if new_price is negative
            if new_price <0:
                raise ValueError('The new price value cannot be negative')
            # Raise error if new_price is higher than 100
            elif new_price > 100:
                raise PriceTooHighError('The model price cannot be higher than 100')
            # Check if model_name is in the models dictionary
            if model_name in self._models:
                # Check if new_price is different from the current price
                if new_price != self._models[model_name]:
                    # Assign new_price to the model_name key (price)
                    self._models[model_name] = new_price
                    return True
                else:
                    return False

    def basic_math_operation(self, x, y, operation_type):
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
        # Raise error if x or y are not int or float
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both x and y must be real numbers (float or int).")

        # Raise error if operation_type is not supported
        if operation_type not in ["multiplication", "division", "power"]:
            raise ValueError("Invalid operation_type. Supported values are 'multiplication', 'division', and 'power'.")
        
        # To perform Multiplication
        if operation_type == 'multiplication':
            result = x * y

        # To perform division
        elif operation_type == "division":
            if y == 0:
                # Raise error when division by 0
                raise ZeroDivisionError
            result = x / y

        # To perform power operation
        elif operation_type == "power":
            result = x ** y

        return result
    
    def matrix_operation(self, matrix_1, matrix_2, operation_type):
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
        if matrix_2 is None:
            if not isinstance(matrix_1, np.ndarray):
                raise TypeError("Matrix_1 must be NumPy arrays.")
            if matrix_1.shape[0] < 2 or matrix_1.shape[1] < 2:
                raise ValueError("Matrix_1 should be at least 2x2 or bigger in size.")
            
        elif matrix_1 is None:
            if not isinstance(matrix_2, np.ndarray):
                raise TypeError("Matrix_2 must be NumPy arrays.")
            if matrix_2.shape[0] < 2 or matrix_2.shape[1] < 2:
                raise ValueError("Matrix_2 should be at least 2x2 or bigger in size.")
        
        if operation_type not in ["multiplication", "determinant", "eigenvalues"]:
            raise ValueError("Invalid operation_type. Supported values are 'Multiplication', 'Determinant', and 'Eigenvalues'.")

        if operation_type == "multiplication":
            try:
                result = np.dot(matrix_1, matrix_2)
                return result
            except ValueError:
                raise ValueError("Multiplication cannot be performed due to incompatible matrices")
            
        elif operation_type == "determinant":

            if matrix_2 is None:
                try:
                    if len(matrix_1.shape) != 2 or matrix_1.shape[0] != matrix_1.shape[1]:
                        raise ValueError("Matrix must be square to find its determinant")
                    else:
                        result = np.linalg.det(matrix_1)
                    return result
                except LinAlgError:
                    raise LinAlgError("The determinant could not be found.")
            elif matrix_1 is None:
                try:
                    if len(matrix_2.shape) != 2 or matrix_2.shape[0] != matrix_2.shape[1]:
                        raise ValueError("Matrix must be square to find its determinant")
                    else:
                        result = np.linalg.det(matrix_2)
                    return result
                except LinAlgError:
                    raise LinAlgError("The determinant could not be found.")
            
        elif operation_type == "eigenvalues":

            if matrix_2 is None:
                try:
                    eigenvalues, eigenvectors = np.linalg.eig(matrix_1) 
                    # Round to have better accuracy when testing
                    result_1 = np.round(eigenvalues,3)
                    result_2 = np.round(eigenvectors,3)
                    return result_1, result_2
                except LinAlgError:
                    raise LinAlgError("A linear algebra function could not be executed.")
            elif matrix_1 is None:
                try:
                    eigenvalues, eigenvectors = np.linalg.eig(matrix_2) 
                    # Round to have better accuracy when testing
                    result_1 = np.round(eigenvalues,3)
                    result_2 = np.round(eigenvectors,3)
                    return result_1, result_2
                except LinAlgError:
                    raise LinAlgError("A linear algebra function could not be executed.") 

# Test Implementation

if __name__ == '__main__':

    # Create class 1 instance
    class_1_1 = ScientificCalculator("Casio", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
    # Class 1 modified
    class_1_2 = ScientificCalculator("Casio", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations"))
    
    # Create class 2 instance
    class_2_1 = ScientificCalculator("Texas Instruments", {"TI-30XS MultiView":52.3, "TI-36X Pro":32.9, "TI-30Xa":42.1}, ("math operations", "matrix operations"))
    # Class 2 modified
    class_2_2 = ScientificCalculator("Texas Instruments", {"TI-36X Pro":32.9, "TI-30Xa":42.1}, ("math operations", "matrix operations"))
    
    # Create class 3 instance
    class_3_1 = ScientificCalculator("Citizen Calc", {"CDC-100": 23.5, "CDC-80": 34.6, "ECC-210":10.544}, ("math operations", "roots finding operations", "roots finding operations"))
    # Class 3 modified
    class_3_2 = ScientificCalculator("Citizen", {"CDC-100": 23.5, "CDC-80": 34.6, "ECC-210":10.544}, ("math operations", "roots finding operations", "roots finding operations"))
    
    # ----------------------------------------------------------------------------------------------------------------------------
    # Simplified Memory Model
    # Extraxting values from dictionary to use in simplified memory model calculation
    
    # Class 1
    class_1_1_dict = class_1_1._models
    class_1_1_dict_flipped = {value: key for key, value in class_1_1_dict.items()}
    keys_c1_1 = []
    values_c1_1 = []
    for item in class_1_1_dict:
        new = (class_1_1_dict[item])
        values_c1_1.append(new)
    for item in class_1_1_dict_flipped:
        new = (class_1_1_dict_flipped[item])
        keys_c1_1.append(new)

    # Class 1 modified
    class_1_2_dict = class_1_2._models
    class_1_2_dict_flipped = {value: key for key, value in class_1_2_dict.items()}
    keys_c1_2 = []
    values_c1_2 = []
    for item in class_1_2_dict:
        new = (class_1_2_dict[item])
        values_c1_2.append(new)
    for item in class_1_2_dict_flipped:
        new = (class_1_2_dict_flipped[item])
        keys_c1_2.append(new)

    # Class 2
    class_2_1_dict = class_2_1._models
    class_2_1_dict_flipped = {value: key for key, value in class_2_1_dict.items()}
    keys_c2_1 = []
    values_c2_1 = []
    for item in class_2_1_dict:
        new = (class_2_1_dict[item])
        values_c2_1.append(new)
    for item in class_2_1_dict_flipped:
        new = (class_2_1_dict_flipped[item])
        keys_c2_1.append(new)

    # Class 2 Modified
    class_2_2_dict = class_2_2._models
    class_2_2_dict_flipped = {value: key for key, value in class_2_2_dict.items()}
    keys_c2_2 = []
    values_c2_2 = []
    for item in class_2_2_dict:
        new = (class_2_2_dict[item])
        values_c2_2.append(new)
    for item in class_2_2_dict_flipped:
        new = (class_2_2_dict_flipped[item])
        keys_c2_2.append(new)

    # Class 3
    class_3_1_dict = class_3_1._models
    class_3_1_dict_flipped = {value: key for key, value in class_3_1_dict.items()}
    keys_c3_1 = []
    values_c3_1 = []
    for item in class_3_1_dict:
        new = (class_3_1_dict[item])
        values_c3_1.append(new)
    for item in class_3_1_dict_flipped:
        new = (class_3_1_dict_flipped[item])
        keys_c3_1.append(new)

    # Class 3 Modified
    class_3_2_dict = class_3_2._models
    class_3_2_dict_flipped = {value: key for key, value in class_3_2_dict.items()}
    keys_c3_2 = []
    values_c3_2 = []
    for item in class_3_2_dict:
        new = (class_3_2_dict[item])
        values_c3_2.append(new)
    for item in class_3_2_dict_flipped:
        new = (class_3_2_dict_flipped[item])
        keys_c3_2.append(new)

    # Calculating the size of the classes

    # Class 1
    size_class_1_1 = 8 + 4*8 + len(class_1_1._brand_name) + 3*8 + len(keys_c1_1[0]) + len(keys_c1_1[1]) + len(keys_c1_1[2]) + 3*8 + 3*4 + 3*8 + len(class_1_1._functionalities[0]) + len(class_1_1._functionalities[1]) + len(class_1_1._functionalities[2]) + 4
    # Class 1 modified
    size_class_1_2 = 8 + 4*8 + len(class_1_2._brand_name) + 3*8 + len(keys_c1_2[0]) + len(keys_c1_2[1]) + len(keys_c1_2[2]) + 3*8 + 3*4 + 2*8 + len(class_1_2._functionalities[0]) + len(class_1_2._functionalities[1]) + 4
    # Class 2
    size_class_2_1 = 8 + 4*8 + len(class_2_1._brand_name) + 3*8 + len(keys_c2_1[0]) + len(keys_c2_1[1]) + len(keys_c2_1[2]) + 3*8 + 3*4 + 2*8 + len(class_2_1._functionalities[0]) + len(class_2_1._functionalities[1]) + 4
    # Class 2 modified
    size_class_2_2 = 8 + 4*8 + len(class_2_2._brand_name) + 2*8 + len(keys_c2_2[0]) + len(keys_c2_2[1]) + 2*8 + 2*4 + 2*8 + len(class_2_2._functionalities[0]) + len(class_2_2._functionalities[1]) + 4
    # Class 3
    size_class_3_1 = 8 + 4*8 + len(class_3_1._brand_name) + 3*8 + len(keys_c3_1[0]) + len(keys_c3_1[1]) + len(keys_c3_1[2]) + 3*8 + 3*4 + 3*8 + len(class_3_1._functionalities[0]) + len(class_3_1._functionalities[1]) + len(class_3_1._functionalities[2]) + 4
    # Class 3 modified
    size_class_3_2 = 8 + 4*8 + len(class_3_2._brand_name) + 3*8 + len(keys_c3_2[0]) + len(keys_c3_2[1]) + len(keys_c3_2[2]) + 3*8 + 3*4 + 3*8 + len(class_3_2._functionalities[0]) + len(class_3_2._functionalities[1]) + len(class_3_2._functionalities[2]) + 4

    # ----------------------------------------------------------------------------------------------------------------------------
    # Empirical Model
    # Calculating the size of the classes
    classSize1_1 = sys.getsizeof(class_1_1)
    classSize1_2 = sys.getsizeof(class_1_2)
    classSize2_1 = sys.getsizeof(class_2_1)
    classSize2_2 = sys.getsizeof(class_2_2)
    classSize3_1 = sys.getsizeof(class_3_1)
    classSize3_2 = sys.getsizeof(class_3_2)

    # Creating list containing values for plotting
    classes_list = ['Class 1', 'Class 1 Modified', 'Class 2', 'Class 2 Modified', 'Class 3', 'Class 3 Modified']
    classes_size_empirical = [classSize1_1, classSize1_2, classSize2_1, classSize2_2, classSize3_1, classSize3_2 ]
    classes_size_simplified = [size_class_1_1, size_class_1_2, size_class_2_1, size_class_2_2, size_class_3_1, size_class_3_2]

    # ----------------------------------------------------------------------------------------------------------------------------
    # Plots

    # Scatter Plot 
    plt.title(' Memory Size vs Class Type Empirical Model')
    plt.xlabel('Classes Type')
    plt.ylabel('Classes Size')
    plt.scatter(classes_list, classes_size_empirical, marker='*', color='blue')
    plt.show()

    plt.title(' Memory Size vs Class Type Simplified Model')
    plt.xlabel('Classes Type')
    plt.ylabel('Classes Size')
    plt.scatter(classes_list, classes_size_simplified, marker='*', color='red')
    plt.show()

    # Line graph
    plt.title(' Memory Size vs Class Type Empirical Model')
    plt.xlabel('Classes Type')
    plt.ylabel('Classes Size')
    plt.plot(classes_list, classes_size_empirical, marker='*', color='blue')
    plt.show()

    plt.title(' Memory Size vs Class Type Simplified Model')
    plt.xlabel('Classes Type')
    plt.ylabel('Classes Size')
    plt.plot(classes_list, classes_size_simplified, marker='*', color='red')
    plt.show()

    # ----------------------------------------------------------------------------------------------------------------------------
    # Print size for each class

    # Simplified Memory Model
    print('Simplified Memory Model')

    # Class 1
    print(f"The size of the first class instance is: {size_class_1_1}")
    print(f"The size of the first class instance (modified) is: {size_class_1_2}")

    # Class 2
    print(f"The size of the second class instance is: {size_class_2_1}")
    print(f"The size of the second class instance (modified) is: {size_class_2_2}")

    # Class 3
    print(f"The size of the third class instance is: {size_class_3_1}")
    print(f"The size of the thirs class instance (modified) is: {size_class_3_2}")


    # Empirical Model
    print('Empirical Model')

    # Class 1 
    print(f"The size of the first class instance is: {classSize1_1}")
    print(f"The size of the first class instance (modified) is: {classSize1_2}")

    # Class 2 
    print(f"The size of the second class instance is: {classSize2_1}")
    print(f"The size of the second class instance (modified) is: {classSize2_2}")

    # Class 3
    print(f"The size of the third class instance is: {classSize3_1}")
    print(f"The size of the third class instance (modified) is: {classSize3_2}")