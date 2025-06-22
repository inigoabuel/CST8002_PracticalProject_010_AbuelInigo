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

CSV_HEADERS = [
    "Region - Région", "Function", "Origin", "Product",
    "Date Sampled \x96 Date d\x92échantillonage", "Type of Test",
    "Component", "Result - Résultat", "Unit - Unité", "Plan Code - Code du régime"
]

EXPORT_HEADERS = [
    "Region", "Function", "Origin", "Product", "DateSampled",
    "TypeOfTest", "Component", "Result", "Unit", "PlanCode"
]

def load_csv(filepath):
    """
    Load records from a CSV file into memory.

    Args:
        filepath (str): Path to the dataset CSV file.

    Returns:
        None
    """
    global records
    records.clear()

    with open(filepath, encoding='ISO-8859-1') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= 100:  # Optional performance limit
                break

            record = Record(
                row[CSV_HEADERS[0]],
                row[CSV_HEADERS[1]],
                row[CSV_HEADERS[2]],
                row[CSV_HEADERS[3]],
                row[CSV_HEADERS[4]],
                row[CSV_HEADERS[5]],
                row[CSV_HEADERS[6]],
                row[CSV_HEADERS[7]],
                row[CSV_HEADERS[8]],
                row[CSV_HEADERS[9]]
            )
            records.append(record)

def get_all_records():
    """
    Retrieve all loaded records.

    Returns:
        list: The in-memory list of Record objects.
    """
    return records

def save_all_records(filepath):
    """
    Save the current records to a specified CSV file.

    Args:
        filepath (str): Path to save the CSV file.

    Returns:
        None
    """
    with open(filepath, 'w', newline='', encoding='ISO-8859-1') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADERS)
        for r in records:
            writer.writerow([
                r.region, r.function, r.origin, r.product,
                r.date_sampled, r.type_of_test, r.component,
                r.result, r.unit, r.plan_code
            ])

def save_to_csv():
    """
    Save the current records to a new CSV file using a UUID filename.

    Returns:
        str: The generated filename used for saving.
    """
    filename = f"export_{uuid.uuid4()}.csv"
    full_path = f"dataset/{filename}"

    with open(full_path, 'w', newline='', encoding='ISO-8859-1') as f:
        writer = csv.writer(f)
        writer.writerow(EXPORT_HEADERS)
        for r in records:
            writer.writerow([
                r.region, r.function, r.origin, r.product,
                r.date_sampled, r.type_of_test, r.component,
                r.result, r.unit, r.plan_code
            ])
    return filename
