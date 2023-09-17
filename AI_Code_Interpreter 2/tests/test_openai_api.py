import unittest
from app.utils.openai_api import OpenAIAPI

class TestOpenAIAPI(unittest.TestCase):
    def setUp(self):
        self.openai_api = OpenAIAPI()

    def test_generate_code(self):
        code = self.openai_api.generate_code("Python")
        self.assertIsInstance(code, str)
        self.assertNotEqual(code, "")

    def test_analyze_code(self):
        code = "def add(a, b):\n    return a + b"
        analysis = self.openai_api.analyze_code(code)
        self.assertIsInstance(analysis, dict)
        self.assertIn("complexity", analysis)
        self.assertIn("errors", analysis)
        self.assertIn("warnings", analysis)

if __name__ == '__main__':
    unittest.main()