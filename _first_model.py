import pandas as pd
import kaggle as kg


path = 'datasets/train.csv'

data = pd.read_csv(path)

print(data.describe())

avg_lot_size = 10517
newest_home_age = 14