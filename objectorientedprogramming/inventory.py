import unittest


class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = []
        self.total = 0

    def add_item(self, name, price, quantity):
        if (self.total + quantity) <= self.max_capacity:
            for item in self.items:
                if item[0] == name:
                    return False
            self.items.append([name, price, quantity])
            self.total += quantity
            return True
        return False
            

    def delete_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.total -= item[2]
                self.items.remove(item)
                return True
        return False

    def get_items_in_price_range(self, min_price, max_price):
        items_copy = []
        for item in self.items:
            if min_price <= item[1] <= max_price:
               items_copy.append(item[0])
        
        return items_copy

    def get_most_stocked_item(self):
        if len(self.items) == 0:
            return None
        
        def get_item_value(item):
            return item[2]
        
        return sorted(self.items, reverse=True, key=get_item_value)[0][0]
        


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        inventory = Inventory(0)
        self.assertFalse(inventory.add_item("Chocolate", 4.99, 1))

    def test_case_2(self):
        inventory = Inventory(3)
        self.assertFalse(inventory.add_item("Chocolate", 4.99, 4))

    def test_case_3(self):
        inventory = Inventory(3)
        self.assertTrue(inventory.add_item("Chocolate", 4.99, 1))
        self.assertTrue(inventory.add_item("Butter", 4.99, 1))
        self.assertFalse(inventory.add_item("Butter", 4.99, 1))
        self.assertFalse(inventory.add_item("Bread", 4.99, 2))

    def test_case_4(self):
        inventory = Inventory(4)
        self.assertTrue(inventory.add_item("Chocolate", 4.99, 1))
        self.assertTrue(inventory.add_item("Butter", 4.99, 1))
        self.assertTrue(inventory.add_item("Bread", 4.99, 2))
        self.assertEqual("Bread", inventory.get_most_stocked_item())

    def test_case_5(self):
        inventory = Inventory(4)
        self.assertTrue(inventory.add_item("Chocolate", 4.99, 4))
        self.assertTrue(inventory.delete_item("Chocolate"))
        self.assertFalse(inventory.delete_item("Chocolate"))
        self.assertFalse(inventory.delete_item("Bread"))
        self.assertTrue(inventory.add_item("Chocolate", 4.99, 2))
        self.assertTrue(inventory.add_item("Bread", 4.99, 2))
        self.assertIn(inventory.get_most_stocked_item(), ("Chocolate", "Bread"))

    def test_case_6(self):
        inventory = Inventory(5)
        self.assertIsNone(inventory.get_most_stocked_item())
        self.assertEqual([], inventory.get_items_in_price_range(1, 10))

    def test_case_7(self):
        inventory = Inventory(5)
        self.assertTrue(inventory.add_item("Chocolate", 4.99, 1))
        self.assertTrue(inventory.add_item("Bread", 3.99, 1))
        self.assertTrue(inventory.add_item("Milk", 5.99, 3))
        self.assertEqual(
            sorted(["Chocolate", "Milk", "Bread"]),
            sorted(inventory.get_items_in_price_range(1, 10)),
        )

    def test_case_8(self):
        max_capacity = 4
        inventory = Inventory(max_capacity)
        self.assertEqual(inventory.add_item("Chocolate", 4.99, 1), True)
        self.assertEqual(inventory.add_item("Cereal", 6.99, 1), True)
        self.assertEqual(inventory.add_item("Milk", 3.99, 2), True)
        self.assertEqual(inventory.add_item("Butter", 2.99, 1), False)
        self.assertEqual(inventory.delete_item("Bread"), False)
        self.assertEqual(inventory.delete_item("Cereal"), True)
        self.assertEqual(inventory.get_items_in_price_range(4.50, 6.50), ["Chocolate"])


if __name__ == "__main__":
    unittest.main()
