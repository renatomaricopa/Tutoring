import unittest
from sep_chain_ht import MyHashTable

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = MyHashTable()
        ht.insert(16, "cat")
        self.assertEqual(ht.size(), 1)

    def test_01b(self):
        ht = MyHashTable()
        ht.insert(16, "cat")
        self.assertEqual(ht.load_factor(), 1/11)

    def test_01c(self):
        ht = MyHashTable()
        ht.insert(16, "cat")
        self.assertAlmostEqual(ht.collisions(), 0)

    def test_01d(self):
        ht = MyHashTable()
        ht.insert(16, "cat")
        self.assertEqual(ht.get(16), (16, "cat"))

    def test_01e(self):
        ht = MyHashTable()
        ht.insert(16, "cat")
        self.assertEqual(ht.remove(16), (16, "cat"))
    
    def test_01f(self):
        ht = MyHashTable()
        ht.insert(16, "cat")
        self.assertEqual(ht.remove(20),"Lookup Error")

    def test_02(self):
        ht = MyHashTable(table_size=10)
        ht.insert(0, "a")
        self.assertEqual(ht.get(0), (0, "a"))
        ht.insert(0, "f")
        self.assertEqual(ht.get(0), (0, "f"))
        ht.insert(20, "g")
        self.assertEqual(ht.get(20), (20, "g"))
        ht.insert(100, "g")
        ht.insert(1, "q")
        ht.insert(2, "r")
        ht.insert(22, "s")
        ht.insert(3, "t")
        ht.insert(4, "u")
        ht.insert(5, "v")
        self.assertEqual(ht.collisions(), 3)

if __name__ == '__main__':
   unittest.main()
