import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_files('dansbecker/home-data-for-ml-course', path='datasets', unzip=True)
