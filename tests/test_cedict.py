import unittest

from hanzitools import Cedict


class CedictTests(unittest.TestCase):
    def setUp(self):
        self.cedict = Cedict()

    def test_lookup_simplified_when_query_in_dictionary(self):
        result = self.cedict.lookup_simplified("约")

        self.assertEqual(len(result), 2)

        yao = result[0]
        self.assertEqual(yao.simplified, "约")
        self.assertEqual(yao.traditional, "約")
        self.assertEqual(yao.pinyin, "yao1")
        self.assertEqual(yao.meaning, "to weigh in a balance or on a scale")

        yue = result[1]
        self.assertEqual(yue.simplified, "约")
        self.assertEqual(yue.traditional, "約")
        self.assertEqual(yue.pinyin, "yue1")
        self.assertEqual(
            yue.meaning,
            "to make an appointment/to invite/approximately/pact/treaty/to economize/to restrict/to reduce (a fraction)/concise",
        )

    def test_lookup_simplified_when_query_not_in_dictionary(self):
        result = self.cedict.lookup_simplified("Rentier")

        self.assertEqual(len(result), 0)

    def test_lookup_traditional_when_query_in_dictionary(self):
        result = self.cedict.lookup_traditional("翰")
        self.assertEqual(len(result), 2)

        han1 = result[0]
        self.assertEqual(han1.simplified, "翰")
        self.assertEqual(han1.traditional, "翰")
        self.assertEqual(han1.pinyin, "Han4")
        self.assertEqual(han1.meaning, "surname Han")

        han2 = result[1]
        self.assertEqual(han2.simplified, "翰")
        self.assertEqual(han2.traditional, "翰")
        self.assertEqual(han2.pinyin, "han4")
        self.assertEqual(han2.meaning, "writing brush/writing/pen")

    def test_lookup_traditional_when_query_not_in_dictionary(self):
        result = self.cedict.lookup_traditional("Rentier")

        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()
