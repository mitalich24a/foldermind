from pathlib import Path

from app.models.local import LocalDocument
from app.readers.txt import TXTReader


def test_txt_reader_reads_file():
    path = Path("tests/data/hello.txt")

    document = LocalDocument(
        name=path.name,
        path=path,
        size=path.stat().st_size,
    )

    reader = TXTReader()

    content = reader.read(document)

    assert content == "Hello FolderMind!\n\n"