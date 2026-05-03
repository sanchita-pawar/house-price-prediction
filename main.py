import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data: size (sq ft) vs price
X = np.array([[500], [1000], [1500], [2000]])
y = np.array([10000, 20000, 30000, 40000])

model = LinearRegression()
model.fit(X, y)

size = int(input("Enter house size: "))
predicted_price = model.predict([[size]])

print(f"Predicted price: {predicted_price[0]}")
