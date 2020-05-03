# hanzitools

This is a Python package to work with Chinese characters, also calle Hanzi (汉字). Currently
implemented is the following:

- Dictionary lookup via [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cedict)
- Working with [Remembering Simplified Hanzi](https://uhpress.hawaii.edu/title/remembering-simplified-hanzi-1-how-not-to-forget-the-meaning-and-writing-of-chinese-characters/)

## Heisig

````python
from hanzitools import Heisig

heisig = Heisig()

# Look up by number
heisig.lookup_number(1755)      # Entry(character='杨', keyword='poplar', number=1755, also_known_as=[], parts=['tree', 'piglets'])

# Look up by keyword
heisig.lookup_keyword("ocean")  # Entry(character='洋', keyword='ocean', number=530, also_known_as=[], parts=['water', 'sheep'])

# Look up by character
heisig.lookup_character("力")   # HeisigEntry(character='力', keyword='power', is_primitive=False, number=732, also_known_as=['muscle', 'power'], parts=[])
````

## CC-CEDICT

```python
from hanzitools import Cedict

cedict = Cedict()

cedict.lookup_simplified("约")
cedict.lookup_traditional("翰")  
```

## Pinyin

Translate Chinese characters to pinyin. This is currently very basic. For a better library, 
maybe use [mozillazg/python-pinyin](https://github.com/mozillazg/python-pinyin).

```python
from hanzitools import pinyinify

pinyinify("转换汉字为拼音。")
pinyinify("你好！你今天吃饭了没？")
```

## Acknowledgements

The Heisig data is owned by *J. W. Heisig & T. W. Richardson, Honolulu: University of Hawai’i Press*.
We use the repository from [rouseabout/heisig](https://github.com/rouseabout/heisig) which provides
a XML database of the Heisig data (MIT License). We use the [CC-CEDICT](https://cc-cedict.org/wiki/start#cc-cedict_home)
as our go-to dictionary ([CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)). 

