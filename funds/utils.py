import csv
from datetime import datetime
import io

from api.serializers import FundSerializer


def process_fund_csv(file):
    """
    Reads and processes a CSV file containing Fund data.
    """

    decoded_file = io.TextIOWrapper(file.file, encoding="utf-8-sig")
    decoded_file.seek(0)

    reader = csv.DictReader(decoded_file)
    errors = []
    valid_funds = []

    for row in reader:
        fund_data = {
            "name": row["Name"].strip(),
            "strategy": row["Strategy"].strip().lower(),
            "aum": row.get("AUM (USD)", "").strip(),
            "inception_date": row.get("Inception Date", "").strip(),
        }

        # Convert AUM.
        try:
            fund_data["aum"] = int(fund_data["aum"].replace(",", "")) if fund_data["aum"].replace(",", "").isdigit() else None
        except ValueError:
            fund_data["aum"] = None
        
        # Convert Inception Date.
        try:
            fund_data["inception_date"] = datetime.strptime(fund_data["inception_date"], "%Y-%m-%d").date() if fund_data["inception_date"] else None
        except ValueError:
            fund_data["inception_date"] = None

        # Validate using serializer.
        serializer = FundSerializer(data=fund_data)
        if serializer.is_valid():
            valid_funds.append(serializer.validated_data)
        else:
            errors.append(f"Invalid row: {serializer.errors}")

    return valid_funds, errors
