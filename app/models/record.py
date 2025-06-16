"""
record.py
Author: Inigo Abuel
Course: CST8002 – Programming Language Research Project
Professor: [Stanley Pieda]
Due Date: June 15, 2025
"""

# app/models/record.py
class Record:
    def __init__(self, region, function, origin, product, date_sampled,
                 type_of_test, component, result, unit, plan_code):
        self.region = region
        self.function = function
        self.origin = origin
        self.product = product
        self.date_sampled = date_sampled
        self.type_of_test = type_of_test
        self.component = component
        self.result = result
        self.unit = unit
        self.plan_code = plan_code
