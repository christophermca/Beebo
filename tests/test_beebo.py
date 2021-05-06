import unittest
from context import Beebo
from map_enviroment import create_map, set_item
_map = create_map(16, 16)


class Test_Beebo(unittest.TestCase):
    """
    Testing Beebo Initialization
    """

    def setUp(self):
        _map = create_map(16, 16)
        self.beebo = Beebo(_map)

    def tareDown(self):
        self.beebo = None

    def test_initializing_beebo(self):
        self.assertEqual(self.beebo.heartbeat, True)

    def test_beebo_power_off(self):
        self.beebo.off()
        self.assertEqual(self.beebo.heartbeat, False)


class Test_Beebo_Handling_Items(unittest.TestCase):
    """
    Testing Handle Items
    """

    def setUp(self):
        self.beebo = Beebo(_map)

    def tareDown(self):
        self.beebo = None

    def test_pick_up_item(self):
        self.beebo.pick_up_item('a')
        self.assertEqual(len(self.beebo.ctnr), 1)

    def test_pick_up_item_too_many(self):
        self.beebo.pick_up_item('a')
        with self.assertRaises(Exception):
            self.beebo.pick_up_item('b')

    def test_drop_item(self):
        self.beebo.pick_up_item('a')
        self.assertEqual(self.beebo.drop_item(), 'a')

    def test_drop_Nothing(self):
        with self.assertRaises(Exception):
            self.assertEqual(self.beebo.drop_item())


if __name__ == '__main__':
    unittest.main()
