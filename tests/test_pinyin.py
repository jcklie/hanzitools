import unittest

from hanzitools import pinyinify


class PinyinTests(unittest.TestCase):
    def test_pinyinify1(self):
        result = pinyinify("转换汉字为拼音。")

        self.assertEqual(result, "zhuan3huan4 han4zi4 wei2 pin1yin1 。")

    def test_pinyinify2(self):
        result = pinyinify("你好！你今天吃饭了没？")

        self.assertEqual(result, "ni3hao3 ！ ni3 jin1tian1 chi1fan4 le5 mei2 ？")


if __name__ == "__main__":
    unittest.main()
