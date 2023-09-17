import unittest
from app.agents.agent1 import Agent1

class TestAgent1(unittest.TestCase):
    def setUp(self):
        self.agent = Agent1()

    def test_something(self):
        # Test case code here
        pass

    def test_another_thing(self):
        # Test case code here
        pass

if __name__ == '__main__':
    unittest.main()