import kaggle as kg
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# path = 'datasets/melb_data.csv'
# data = pd.read_csv(path)

# y = data.Price
# features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# X = data[features]

# melbourne_model = DecisionTreeRegressor(random_state = 1)
# melbourne_model.fit(X,y)

# print("Making predictions for the following 5 houses:")
# print(X.head())
# print("The predictions are")
# print(melbourne_model.predict(X.head()))

path = 'datasets/train.csv'
data = pd.read_csv(path)
print(data.describe())

y = data.SalePrice
features = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']
X = data[features]

print(X.head())

model = DecisionTreeRegressor(random_state=1) 
model.fit(X, y)

print(model.predict(X))

print(data.head())