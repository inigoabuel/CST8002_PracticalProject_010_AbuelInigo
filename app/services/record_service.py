"""
record_service.py
Author: Inigo Abuel
Course: CST8002 – Programming Language Research Project
Professor: Stanley Pieda
Due Date: June 15, 2025
"""

import csv
import uuid
from app.models.record import Record

# In-memory list to store Record objects
records = []

def load_csv(filepath):
    """
    Load records from a CSV file into memory.

    Args:
        filepath (str): Path to the dataset CSV file.

    Returns:
        None
    """
    global records
    records.clear()  # Clear any existing records to avoid duplicates

    with open(filepath, encoding='ISO-8859-1') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= 100:  # Limit to 100 records for performance
                break

            # Map CSV fields to the Record class
            record = Record(
                row["Region - Région"],
                row["Function"],
                row["Origin"],
                row["Product"],
                row["Date Sampled \x96 Date d\x92échantillonage"],
                row["Type of Test"],
                row["Component"],
                row["Result - Résultat"],
                row["Unit - Unité"],
                row["Plan Code - Code du régime"]
            )
            records.append(record)  # Add each record to the global list

def get_all():
    """
    Retrieve all loaded records.

    Returns:
        list: The in-memory list of Record objects.
    """
    return records

def save_to_csv():
    """
    Save the current records to a new CSV file using a UUID filename.

    Returns:
        str: The generated filename used for saving.
    """
    filename = f"export_{uuid.uuid4()}.csv"
    with open(f"dataset/{filename}", 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the header row
        writer.writerow(["Region", "Function", "Origin", "Product", "DateSampled",
                         "TypeOfTest", "Component", "Result", "Unit", "PlanCode"])

        # Write each record as a CSV row
        for r in records:
            writer.writerow([
                r.region, r.function, r.origin, r.product, r.date_sampled,
                r.type_of_test, r.component, r.result, r.unit, r.plan_code
            ])
    return filename
