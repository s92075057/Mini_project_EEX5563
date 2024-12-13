import unittest
from memory_manager import MemoryManager

class TestMemoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = MemoryManager(100)

    def test_allocate_success(self):
        self.assertEqual(self.manager.allocate(10), 0)
        self.assertEqual(self.manager.allocate(20), 10)

    def test_allocate_failure(self):
        self.manager.allocate(100)
        self.assertEqual(self.manager.allocate(10), -1)

    def test_wrap_around(self):
        self.manager.allocate(90)
        self.assertEqual(self.manager.allocate(10), -1)
        self.manager.deallocate(0, 10)
        self.assertEqual(self.manager.allocate(10), 0)

    def test_deallocate(self):
        self.manager.allocate(10)
        self.manager.deallocate(0, 10)
        self.assertEqual(self.manager.allocate(10), 0)

if __name__ == "__main__":
    unittest.main()
