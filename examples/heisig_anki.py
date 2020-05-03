import csv
import pypinyin
from hanzitools import Heisig, Cedict


def create_deck():
    heisig = Heisig()
    cedict = Cedict()

    fieldnames = ["Id", "Number", "Keyword", "Simplified", "Traditional", "Pinyin", "Alias", "Parts"]

    with open("anki_heisig.csv", "w", newline="") as f:
        writer = csv.writer(f)

        last_number = None
        primitive_count = 0

        i = 1
        for entry in heisig:
            if not entry.is_primitive:
                number = entry.number
                keyword = entry.keyword
                simplified = entry.character

                dict_entries = cedict.lookup_simplified(simplified)
                traditional = dict_entries[0].traditional if len(dict_entries) else ""

                pinyin = pypinyin.pinyin(entry.character)[0][0]
                tags = []

                last_number = entry.number
                primitive_count = 0

            else:
                number = f"{last_number + 1}{chr(ord('a') + primitive_count)}"
                keyword = entry.keyword
                simplified = entry.character
                traditional = ""
                pinyin = ""
                tags = []

                primitive_count += 1

            parts = []
            for part in entry.parts:
                part_entry = heisig.lookup_keyword(part)
                if part_entry is None:
                    part_entry = heisig.lookup_alias(part)
                parts.append(f"{part} {part_entry.character if part_entry is not None else ''}")

            row = (
                i,
                number,
                keyword,
                simplified,
                traditional,
                pinyin,
                "\n".join(entry.also_known_as),
                "\n".join(parts),
            )

            writer.writerow(row)
            i += 1


if __name__ == "__main__":
    create_deck()
