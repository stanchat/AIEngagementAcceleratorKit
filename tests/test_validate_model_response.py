# test_validate_model_response.py

import unittest
from helpers.validate_model_response import validate_response

class TestValidateModelResponse(unittest.TestCase):
    def test_valid_response(self):
        result = validate_response("AI will transform industries and workflows.")
        self.assertTrue(result)

    def test_short_response(self):
        result = validate_response("Hi.")
        self.assertFalse(result)

    def test_error_in_response(self):
        result = validate_response("Error: something went wrong.")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
