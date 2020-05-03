import unittest

from hanzitools import Heisig


class HeisigTests(unittest.TestCase):
    def setUp(self):
        self.heisig = Heisig()

    def test_lookup_existing_number(self):
        result = self.heisig.lookup_number(1755)

        self.assertEqual(result.keyword, "poplar")
        self.assertEqual(result.number, 1755)
        self.assertEqual(result.character, "杨")
        self.assertEqual(result.parts, ["tree", "piglets"])

    def test_lookup_absent_number(self):
        result = self.heisig.lookup_number(4321)

        self.assertIsNone(result)

    def test_lookup_existing_keyword(self):
        result = self.heisig.lookup_keyword("ocean")

        self.assertEqual(result.keyword, "ocean")
        self.assertEqual(result.number, 530)
        self.assertEqual(result.character, "洋")
        self.assertEqual(result.parts, ["water", "sheep"])

    def test_lookup_absent_keyword(self):
        result = self.heisig.lookup_keyword("reindeer")

        self.assertIsNone(result)

    def test_lookup_existing_character(self):
        result = self.heisig.lookup_character("约")

        self.assertEqual(result.keyword, "make an appointment")
        self.assertEqual(result.number, 1090)
        self.assertEqual(result.character, "约")
        self.assertEqual(result.parts, ["thread", "ladle"])

    def test_lookup_absent_character(self):
        result = self.heisig.lookup_character("馕")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
