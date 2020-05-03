from collections import defaultdict
from dataclasses import dataclass
import re
from typing import Dict, List

from hanzitools.data import cedict_path


@dataclass
class CedictEntry:
    simplified: str
    traditional: str
    pinyin: str
    meaning: str


class Cedict:
    def __init__(self):
        self._simplified_to_entry: Dict[str, List[CedictEntry]] = defaultdict(list)
        self._traditional_to_entry: Dict[str, List[CedictEntry]] = defaultdict(list)

        with cedict_path().open() as f:
            for line in f:
                line = line.strip()

                # Strip header
                if line.startswith("#"):
                    continue

                # The format is
                # Traditional Simplified [pinyin] /English/
                matches = re.match(r"(.+) (.+) \[(.+)\] /(.+)/", line)
                traditional = matches.group(1)
                simplified = matches.group(2)
                pinyin = matches.group(3)
                meaning = matches.group(4)

                entry = CedictEntry(simplified=simplified, traditional=traditional, pinyin=pinyin, meaning=meaning)

                self._traditional_to_entry[traditional].append(entry)
                self._simplified_to_entry[simplified].append(entry)

    def lookup_traditional(self, cn: str) -> List[CedictEntry]:
        """ Looks up the Cedict entry for the given Chinese word in traditional characters.

        Args:
            cn (str): The word to look up.

        Returns:
            Optional[CedictEntry]: The entry for `word` if found else `None`
        """
        return self._traditional_to_entry.get(cn, [])

    def lookup_simplified(self, cn: str) -> List[CedictEntry]:
        """ Looks up the Cedict entry for the given Chinese word in simplified characters.

        Args:
            cn (str): The word to look up.

        Returns:
            Optional[HeisigEntry]: The entry for `word` if found else `None`
        """
        return self._simplified_to_entry.get(cn, [])
