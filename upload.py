import kagglehub
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
# kagglehub.login()

# Replace with path to directory containing model files.
LOCAL_MODEL_DIR = 'first_model_ml.py'

MODEL_SLUG = 'first_model_ml' # Replace with model slug.

# Learn more about naming model variations at
# https://www.kaggle.com/docs/models#name-model.
VARIATION_SLUG = '0.1' # Replace with variation slug.

kagglehub.model_upload(
  handle = f"avegatorres/{MODEL_SLUG}/keras/{VARIATION_SLUG}",
  local_model_dir = LOCAL_MODEL_DIR,
  version_notes = 'Update 2024-10-31')