from app import create_app
from app.services import record_service

app = create_app()

if __name__ == '__main__':
    record_service.load_csv("dataset/2013-14_coumarin_in_dried_beverage_mixes_breads_baking_mixes.csv")
    app.run(debug=True)
