import unittest
from app.utils import analysis

class TestAnalysis(unittest.TestCase):
    def test_analyze_directory(self):
        directory_path = "/path/to/directory"
        result = analysis.analyze_directory(directory_path)
        self.assertEqual(result, "Analysis completed successfully")

if __name__ == '__main__':
    unittest.main()