# test_ScientificCalculator
#
# Author: Karla Castro
# Email: kmcastro@uwaterloo.ca
# Student ID: 20745522
# Date: October 8th, 2023
#
# these are the unit tests for ScientificCalculator Class

import unittest
import numpy as np

from ScientificCalculator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):
    def test_constructor_typical1(self):
        """
         Input: ("casio", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: instance of a ScientificCalculator with all variables above
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator("Casio", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(casio.get_brand_name(), "casio")
        self.assertEquals(casio.get_price("FX-991"), 48.69)
        self.assertEquals(casio.get_price("FX-300"), 21.99)
        self.assertEquals(casio.get_price("FX-9750"), 64.99)
        self.assertAlmostEquals(casio.get_functionalities(), ("math operations", "matrix operations", "roots finding operations"))
    
    def test_constructor_typical2(self):
        """
         Input: ("Texas Instruments", {"TI-30XS MultiView":52.3, "TI-36X Pro":32.9, "TI-30Xa":42.1}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: instance of a ScientificCalculator with all variables above
        """

        # create ScientificCalculator instance
        texas_inst = ScientificCalculator("Texas Instruments", {"TI-30XS MultiView":52.3, "TI-36X Pro":32.9, "TI-30Xa":42.1}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(texas_inst.get_brand_name(), "Texas Instruments")
        self.assertEquals(texas_inst.get_price("TI-30XS MultiView"), 52.3)
        self.assertEquals(texas_inst.get_price("TI-36X Pro"), 32.9)
        self.assertEquals(texas_inst.get_price("TI-30Xa"), 42.1)
        self.assertAlmostEquals(texas_inst.get_functionalities(), ("math operations", "matrix operations", "roots finding operations"))
    
    def test_constructor_unusual(self):
        """
         Input: ('42', {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: instance of a ScientificCalculator with all variables above. Unusual case where name is a number
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator("42", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(casio.get_brand_name(), "42")
        self.assertEquals(casio.get_price("FX-991"), 48.69)
        self.assertEquals(casio.get_price("FX-300"), 21.99)
        self.assertEquals(casio.get_price("FX-9750"), 64.99)
        self.assertAlmostEquals(casio.get_functionalities(), ("math operations", "matrix operations", "roots finding operations"))
    
    def test_constructor_error(self):
        """
         Input: ("casio", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: Type error where a string was given for the price instead of the number, and a number was given as the name
        """

        with self.assertRaises(TypeError):
            casio = ScientificCalculator(34, {"FX-991":48.69, "FX-300":"21.99", "FX-9750":64.99},"math operations")

    def test_get_brand_name_typical(self):
        """
         Input: ("casio", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: return "casio" as a string
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(casio.get_brand_name(), "casio")

    def test_get_brand_name_unusual(self):
        """
         Input: (('c'+'asio'), {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output:  return "casio" as one string not with the + signs
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator(('c'+'asio'+ ' '+ 'models 1'), {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(casio.get_brand_name(), 'casio')

    def test_get_price_typical(self):
        """
         Input: ("casio", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: return the price given a specific model
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-991":48.69, "FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(casio.get_price("FX-991"), 48.69)

    def test_get_price_unusual(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: None since asking for price of unknown model
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(casio.get_price("FX-991"), None)

    def test_get_functionalities_typical(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: list containing the functionalities ("math operations", "matrix operations", "roots finding operations")
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(casio.get_functionalities(), ("math operations", "matrix operations", "roots finding operations"))

    def test_get_functionalities_unusual(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations"))
         Expected output: list containing one string with one functionality ("math operations")
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations"))
        #check post conditions
        self.assertEquals(casio.get_functionalities(), ("math operations"))
    
    def test_get_state_typical(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: "working"
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(casio.get_state(), "working")

    def test_get_state_unusual(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: None
        """

        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        #check post conditions
        self.assertEquals(casio.get_state(), None)

    def test_set_state_typical(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Input: new_state variable contains a value
         Expected output: True for a modified state
        """
        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        new_state = casio.get_state()
        #check post conditions
        self.assertEquals(casio.set_state(new_state), True)

    def test_set_state_unusual(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Input: new_state variable is empty []
         Expected output: False if the state was not modified
        """
        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        new_state = casio.get_state()
        #check post conditions
        self.assertEquals(casio.set_state(new_state), False)
    
    def test_set_state_error(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Input: new_state variable is None
         Expected output: Raise type error
        """
        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        new_state = casio.get_state()

        with self.assertRaises(TypeError):
            casio.set_state(None)

    def test_add_models_typical(self):
        """
        Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        Input: model_name variable, model_price
        Expected output: True if the model and price were added
        """
        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        model_name = "FX-500"
        model_price = 23.99
        #check post conditions
        self.assertEquals(casio.add_models(model_name, model_price), True)

    def test_add_models_unusual(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Input: model_name variable, model_price
         Expected output: Return false if model already exists
        """
        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        model_name = "FX-300"
        model_price = 21.99
        #check post conditions
        self.assertEquals(casio.add_models(model_name, model_price), False)
    
    def test_add_models_error(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Input: model_name variable, model_price
         Expected output: Type error
        """
        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        model_name = "FX-500"
        model_price = -23.99
        model_price_2 = "23.99"
        #check post conditions
        with self.assertRaises(TypeError):
            casio.add_models(model_name, model_price)
            casio.add_models(model_name, model_price_2)
    
    def test_change_model_price_typical(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Input: model_name, new_price
         Expected output: True when the new_price is changed
        """
        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        model_name = "FX-300"
        new_price = 25.61
        #check post conditions
        self.assertEquals(casio.change_model_price(model_name, new_price), True)
    
    def test_change_model_price_unusual(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Input: model_name, new_price = old price
         Expected output: False since new_price equals old price
        """
        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        model_name = "FX-300"
        new_price = 21.99
        #check post conditions
        self.assertEquals(casio.change_model_price(model_name, new_price), False)

    def test_change_model_price_error(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Input: model_name, new_price = "32"
         Expected output: Type error since new price has a string type
        """
        # create ScientificCalculator instance
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        model_name = "FX-300"
        new_price = "32"
        #check post conditions
        with self.assertRaises(TypeError):
            casio.add_models(model_name, new_price)

    def test_basic_math_operation_multiplication_typical(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: result of the multiplication
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        result = casio.basic_math_operation(4, 2, 'multiplication')
        self.assertEquals(result, 8.0)

    def test_basic_math_operation_multiplication_unusual1(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: result of the multiplication =0 since one number was zero
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        result = casio.basic_math_operation(0, 2, 'multiplication')
        self.assertEquals(result, 0)

    def test_basic_math_operation_multiplication_unusual2(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: result of the multiplication is negative since one number was negative
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        result = casio.basic_math_operation(-4, 2, 'multiplication')
        self.assertEquals(result, -8.0)

    def test_basic_math_operation_multiplication_error(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: raise type error since one number was given as a string
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        with self.assertRaises(TypeError):
            casio.basic_math_operation("4", 2, 'multiplication')

    def test_basic_math_operation_division_typical(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: result of the division
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        result = casio.basic_math_operation(4, 2, 'division')
        self.assertEquals(result, 2.0)
        
    def test_basic_math_operation_division_unusual1(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: result of the division is a negative number since value given was negative
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        result = casio.basic_math_operation(-4, 2, 'division')
        self.assertEquals(result, -2)

    def test_basic_math_operation_division_unusual2(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: result of the division is 0 since the numerator was zero
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        result = casio.basic_math_operation(0, 2, 'division')
        self.assertEquals(result, 0)

    def test_basic_math_operation_division_error(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: raise ZeroDivisionError
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        with self.assertRaises(ZeroDivisionError):
            casio.basic_math_operation(4, 0, 'division')

    def test_basic_math_operation_power_typical(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: result of the finding the exponent
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        result = casio.basic_math_operation(4, 2, 'power')
        self.assertEquals(result, 16.0)
        
    def test_basic_math_operation_power_unusual1(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: result of finding the exponent of negative value to an even power
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        result = casio.basic_math_operation(-4, 2, 'power')
        self.assertEquals(result, 16)

    def test_basic_math_operation_power_unusual2(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: result of finding the exponent of negative value to an odd power
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        result = casio.basic_math_operation(-4, 3, 'power')
        self.assertEquals(result, -64)

    def test_basic_math_operation_power_error(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         Expected output: raise TypeError for using a string as the power value
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        with self.assertRaises(TypeError):
            casio.basic_math_operation(4, "2", 'power')

    def test_matrix_operation_mutiplication_typical(self):
        """
        2x2 matrices
        Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        casio.matrix_opperation(matrix1, matrix2, operation_type) for matrices 2x2 or higher size
        Expected output: array with the matrix multiplication result
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        matrix_1 = np.array([[1, 2], [3, 4]])
        matrix_2 = np.array([[5, 6], [7, 8]])
        result = casio.matrix_operation(matrix_1, matrix_2, 'multiplication')
        self.assertEquals(result,np.array([[19, 22], [43, 50]]) )

    def test_matrix_operation_mutiplication_unusual(self):
        """
        1x1 matrices
        Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        casio.matrix_opperation(matrix1, matrix2, operation_type) for matrices 1x1
        Expected output: integer with the dot product
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        matrix_1 = np.array([2, 3])
        matrix_2 = np.array([2, 4])
        result = casio.matrix_operation(matrix_1, matrix_2, 'multiplication')
        self.assertEquals(result, 16 )

    def test_matrix_operation_mutiplication_error(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         casio.matrix_opperation(matrix1, matrix2, operation_type) for matrices 2x2 or higher size
         Expected output: raise Value Error for incompatible matrices
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        matrix_1 = np.array([[1, 2], [3, 4]])
        matrix_2 = np.array([[5, 6, 7], [8, 9, 10]])
        with self.assertRaises(ValueError):
            casio.matrix_operation(matrix_1, matrix_2, 'multiplication')
    
    def test_matrix_operation_determinant_typical(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         casio.matrix_opperation(matrix1, matrix2 = None, determinant)
         Expected output: result with determinant value (float) for a 2x2 matrix
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        matrix_1 = np.array([[2, 3], [1, 4]])
        result = casio.matrix_operation(matrix_1, None, 'determinant')
        self.assertEquals(result, 5.0 )
    
    def test_matrix_operation_determinant_unusual(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         casio.matrix_opperation(matrix1, matrix2 = None, determinant)
         Expected output: result with determinant value (float) (with a 3x3 matrix)
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        matrix_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        result = casio.matrix_operation(matrix_1, None, 'determinant')
        self.assertEquals(result, 0 )
    
    def test_matrix_operation_determinant_error(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         casio.matrix_opperation(matrix1, matrix2 = None, determinant)
         Expected output: raise ValueError for non-square matrices
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        matrix_1 = np.array([[1, 3, 5], [4, 5, 6]])
        with self.assertRaises(ValueError):
            casio.matrix_operation(matrix_1, None, 'determinant')

    def test_matrix_operation_eigenvalues_typical(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         casio.matrix_opperation(matrix1, matrix2 = None, eigenvalues)
         Expected output: result with eigenvalues and eigenvectors of a typical square matrix
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        matrix_1 = np.array([[4, 2], [2, 3]])
        result1, result2 = casio.matrix_operation(matrix_1, None, 'eigenvalues')
        self.assertEquals(result1, np.array([5.366, 1.634]), rtol=1e-3)
        self.assertEquals(result2, np.array([[0.914, -0.707], [0.407, 0.707]]), rtol=1e-3)

    def test_matrix_operation_eigenvalues_unusual(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         casio.matrix_opperation(matrix1, matrix2 = None, eigenvalues)
         Expected output: ValueError for non-square matrices
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        matrix_1 = np.array([[4, 2, 1], [7, 8, 9]]) #non-square matrix
        with self.assertRaises(ValueError):
            result1, resul2 = casio.matrix_operation(matrix_1, None, 'eigenvalues')
    
    def test_matrix_operation_eigenvalues_error(self):
        """
         Input: ("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
         casio.matrix_opperation(matrix1, matrix2 = None, eigenvalues)
         Expected output: raise TypeError for invalid matrices
        """
        casio = ScientificCalculator("casio", {"FX-300":21.99, "FX-9750":64.99}, ("math operations", "matrix operations", "roots finding operations"))
        matrix_1 =  [[4, 2], [2, 3]] #invalid matrix
        with self.assertRaises(TypeError):
            result1, resul2 = casio.matrix_operation(matrix_1, None, 'eigenvalues')
            
unittest.main()