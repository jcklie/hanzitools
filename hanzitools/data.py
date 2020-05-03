from pathlib import Path

PATH_ROOT: Path = Path(__file__).resolve().parents[1]
PATH_DATA: Path = PATH_ROOT / "data"


def heisig_path() -> Path:
    return PATH_DATA / "rsh.xml"


def cedict_path() -> Path:
    return PATH_DATA / "cedict_ts.u8"
