import numpy as np
from sklearn.linear_model import LinearRegression

# flat sizes in square feet
X = np.array([[500], [1000], [1500], [2000], [2500]])
# corresponding house prices in dollars
y= np.array([50, 100, 150, 200, 250])
# Create a linear regression model
model = LinearRegression()
# Fit the model to the data
model.fit(X,y)
# Predict the price of a house with a size of 1200 square feet
predicted_price = model.predict([[1200]])

print(f"The predicted price of a house with a size of 1200 square feet is: {predicted_price[0]} dollars.")