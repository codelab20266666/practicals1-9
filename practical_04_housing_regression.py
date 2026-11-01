"""Practical No. 4 - Housing price prediction with a deep neural network.

Uses the California housing dataset (downloaded automatically by
scikit-learn the first time) and a small Keras regression model.
"""
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Step 1: Load the housing dataset
data = fetch_california_housing()
X = data.data
y = data.target

print("Dataset loaded successfully")
print("Total records:", X.shape[0])
print("Number of features:", X.shape[1])

# Step 2: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 3: Normalize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 4: Build the deep neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1),
])

# Step 5: Compile the model
model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"],
)

# Step 6: Train the model
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=1,
)

# Step 7: Evaluate the model
loss, mae = model.evaluate(X_test, y_test, verbose=0)
print("\nModel Evaluation")
print("Test Mean Squared Error:", round(loss, 4))
print("Test Mean Absolute Error:", round(mae, 4))

# Step 8: Predict house prices (target is in units of $100,000)
predictions = model.predict(X_test[:5], verbose=0)
print("\nActual vs Predicted House Values")
for actual, predicted in zip(y_test[:5], predictions.flatten()):
    print(
        f"Actual: ${actual * 100000:.2f}, "
        f"Predicted: ${predicted * 100000:.2f}"
    )

# Step 9: Plot training and validation loss
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Neural Network - Housing Price Prediction")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")
plt.legend()
plt.tight_layout()
plt.show()
