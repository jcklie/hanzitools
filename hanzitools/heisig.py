from collections import OrderedDict
from dataclasses import dataclass, field
import re
import xml.etree.ElementTree as ET
from typing import List, Optional, Dict, Iterator

from hanzitools.data import heisig_path


@dataclass
class HeisigEntry:
    character: str
    keyword: str
    is_primitive: bool
    number: Optional[int] = field(default=None)
    also_known_as: List[str] = field(default_factory=list)
    parts: List[str] = field(default_factory=list)


class Heisig:
    """ A class used to work with Heisig's 'Remembering Simplified Hanzi: How Not to Forget the
    Meaning and Writing of Chinese Characters'.
    """

    def __init__(self):
        self._number_to_entry: Dict[int, HeisigEntry] = OrderedDict()
        self._keyword_to_entry: Dict[str, HeisigEntry] = OrderedDict()
        self._character_to_entry: Dict[str, HeisigEntry] = OrderedDict()
        self._alias_to_entry: Dict[str, HeisigEntry] = OrderedDict()

        with heisig_path().open() as f:
            tree = ET.parse(f)
            root = tree.getroot()

        for frame in root.findall(".//frame"):
            number = frame.get("number")
            character = frame.get("character")
            keyword = frame.get("keyword")
            typ = frame.get("{http://www.w3.org/2001/XMLSchema-instance}type")
            is_primitive = typ == "primitive"

            if is_primitive:
                keyword = f"p. {keyword}"

            entry = HeisigEntry(character=character, keyword=keyword, is_primitive=is_primitive)

            # Number can be optional for primitives like `丶` or `丨`
            if number is not None:
                number = int(number)
                entry.number = number

            # Parts
            for cite in frame.findall(".//cite"):
                entry.parts.append(re.sub(r"\s+", " ", cite.text).strip())

            # Self references
            for pself in frame.findall(".//pself"):
                alias = re.sub(r"\s+", " ", pself.text).strip()
                entry.also_known_as.append(alias)

            assert keyword not in self._keyword_to_entry, (entry, self._keyword_to_entry[keyword])
            self._keyword_to_entry[keyword] = entry

            assert character not in self._character_to_entry
            self._character_to_entry[character] = entry

            if number is not None:
                assert number not in self._number_to_entry
                self._number_to_entry[number] = entry

            for alias in entry.also_known_as:
                if alias in self._alias_to_entry and self._alias_to_entry[alias].keyword != keyword:
                    raise RuntimeError(f"Duplicate alias: [{alias}]")

                self._alias_to_entry[alias] = entry

    def lookup_number(self, number: int) -> Optional[HeisigEntry]:
        """ Looks up the Heisig entry for the given number.

        Args:
            number (int): The Heisig number to look up.

        Returns:
            Optional[HeisigEntry]: The entry for the Heisig number if found else `None`
        """
        return self._number_to_entry.get(number, None)

    def lookup_keyword(self, keyword: str) -> Optional[HeisigEntry]:
        """ Looks up the Heisig entry for the given keyword.

        Args:
            keyword (str): The Heisig keyword to look up.

        Returns:
            Optional[HeisigEntry]: The entry for the Heisig keyword if found else `None`
        """
        return self._keyword_to_entry.get(keyword, None)

    def lookup_character(self, character: str) -> Optional[HeisigEntry]:
        """ Looks up the Heisig entry for the given Hanzi.

        Args:
            character (str): The Hanzi to look up.

        Returns:
            Optional[HeisigEntry]: The entry for the Hanzi if found else `None`
        """
        return self._character_to_entry.get(character, None)

    def lookup_alias(self, alias: str) -> Optional[HeisigEntry]:
        return self._alias_to_entry.get(alias, None)

    def __iter__(self):
        """ Iterate over all Heisig entries sorted increasingly by the Heisig number.

        Returns:
            Iterator[HeisigEntry]: Iterator over all Heisig entries sorted by number
        """
        return iter(self._keyword_to_entry.values())
