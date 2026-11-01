"""Practical No. 5 - Handwritten digit recognition with a deep neural network.

Uses scikit-learn's built-in 8x8 digits dataset and a Keras classifier.
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Sequential

# Step 1: Load the handwritten digit dataset
digits = load_digits()
X = digits.data
y = digits.target

print("Dataset loaded successfully")
print("Total images:", len(X))
print("Number of features:", X.shape[1])
print("Number of classes:", len(np.unique(y)))

# Step 2: Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

# Keep an unscaled copy of the test images for display
X_test_raw = X_test.copy()

# Step 3: Normalize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 4: Build the deep neural network
model = Sequential([
    Input(shape=(64,)),
    Dense(128, activation="relu"),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax"),
])

# Step 5: Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
model.summary()

# Step 6: Train the model
print("\nTraining the model...")
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.1,
    verbose=1,
)

# Step 7: Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print("\nModel Evaluation")
print("Test Loss:", round(test_loss, 4))
print("Test Accuracy:", round(test_accuracy * 100, 2), "%")

# Step 8: Predict the test images
probabilities = model.predict(X_test, verbose=0)
predictions = np.argmax(probabilities, axis=1)

print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Step 9: Display sample images and predictions
plt.figure(figsize=(15, 7))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(
        X_test_raw[i].reshape(8, 8),
        cmap="gray",
        interpolation="nearest",
    )
    plt.title(
        f"Actual: {y_test[i]}\nPredicted: {predictions[i]}",
        fontsize=12,
    )
    plt.axis("off")

plt.suptitle(
    "Handwritten Digit Recognition Using Deep Neural Network",
    fontsize=15,
)
plt.tight_layout(pad=3.0)
plt.show()

# Step 10: Plot training accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nPractical 5 completed successfully!")
