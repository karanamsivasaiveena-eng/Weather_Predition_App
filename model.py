import numpy as np
from sklearn.linear_model import LinearRegression

# Simulated past temperature trend
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([25, 26, 27, 28, 29, 30])

model = LinearRegression()
model.fit(X, y)

def predict_temperature(current_temp):
    # Predict next day temperature based on trend
    next_day = model.predict([[7]])
    
    # Adjust with current temp
    predicted = (current_temp + next_day[0]) / 2
    
    return round(predicted, 2)