import jieba

from hanzitools.cedict import Cedict


def pinyinify(text: str) -> str:
    cedict = Cedict()
    result = []

    for s in jieba.cut(text):
        entries = cedict.lookup_simplified(s)
        if len(entries):
            result.append(entries[0].pinyin.replace(" ", ""))
        else:
            result.append(s)

    return " ".join(result)
