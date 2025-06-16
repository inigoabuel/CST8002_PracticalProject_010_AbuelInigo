# Practical Project 2 – Coumarin Dataset Flask App

**Course:** CST8002 – Programming Language Research Project  
**Author:** Inigo Abuel  
**Professor:** Stanley Pieda  
**Due Date:** June 15, 2025  

---

## 🧠 Project Overview

This Flask MVC application loads the **2013–14 Coumarin Dataset** and displays it in a user-friendly web interface. The project supports:
- Viewing data (100 rows max)
- Saving filtered records to a new CSV using UUID filenames
- Unit testing via `unittest`

---

## 📁 Project Structure

practical_project2/
│
├── app/
│ ├── models/record.py # Record class
│ ├── services/record_service.py # Data logic
│ ├── views/routes.py # Flask routes
│ └── templates/index.html # HTML UI
│
├── dataset/ # Contains original + exported CSVs
├── tests/ # Unit tests
│ └── test_record.py
├── run.py # Flask entry point
├── requirements.txt
└── README.md
