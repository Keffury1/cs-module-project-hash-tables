import unittest

from hashtable import HashTable


class TestHashTable(unittest.TestCase):


    def test_hash_table_resize(self):
        ht = HashTable(8)

        ht.put("key-0", "val-0")
        ht.put("key-1", "val-1")
        ht.put("key-2", "val-2")
        ht.put("key-3", "val-3")
        ht.put("key-4", "val-4")
        ht.put("key-5", "val-5")
        ht.put("key-6", "val-6")
        ht.put("key-7", "val-7")
        ht.put("key-8", "val-8")
        ht.put("key-9", "val-9")

        ht.resize(1024)

        self.assertTrue(ht.get_num_slots() == 1024)

        return_value = ht.get("key-0")
        self.assertTrue(return_value == "val-0")
        return_value = ht.get("key-1")
        self.assertTrue(return_value == "val-1")
        return_value = ht.get("key-2")
        self.assertTrue(return_value == "val-2")
        return_value = ht.get("key-3")
        self.assertTrue(return_value == "val-3")
        return_value = ht.get("key-4")
        self.assertTrue(return_value == "val-4")
        return_value = ht.get("key-5")
        self.assertTrue(return_value == "val-5")
        return_value = ht.get("key-6")
        self.assertTrue(return_value == "val-6")
        return_value = ht.get("key-7")
        self.assertTrue(return_value == "val-7")
        return_value = ht.get("key-8")
        self.assertTrue(return_value == "val-8")
        return_value = ht.get("key-9")
        self.assertTrue(return_value == "val-9")


if __name__ == '__main__':
    unittest.main()
