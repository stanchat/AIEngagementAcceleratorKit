# test_ai_model_wrapper.py

import os
import unittest
from helpers.ai_model_wrapper import AIModelWrapper

class TestAIModelWrapper(unittest.TestCase):
    def test_huggingface_generation(self):
        wrapper = AIModelWrapper(backend="huggingface")
        result = wrapper.generate("The future of AI is")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 10)

    def test_invalid_backend(self):
        with self.assertRaises(ValueError):
            AIModelWrapper(backend="unsupported")

if __name__ == "__main__":
    unittest.main()
