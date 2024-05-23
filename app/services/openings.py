import csv

from app.schemas.opening import Opening


def load_openings() -> list[Opening]:
    with open("data/openings.tsv") as f:
        csv_reader = csv.DictReader(f, delimiter="\t")
        return [Opening.model_validate(row) for row in csv_reader]
