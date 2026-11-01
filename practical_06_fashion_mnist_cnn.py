"""Practical No. 6 - Image classification with a CNN on Fashion MNIST."""
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models

# Step 1: Load the Fashion MNIST dataset
print("Loading Fashion MNIST dataset...")
(X_train, y_train), (X_test, y_test) = (
    tf.keras.datasets.fashion_mnist.load_data()
)

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

print("Dataset loaded successfully!")
print("Training images:", X_train.shape[0])
print("Testing images:", X_test.shape[0])

# Step 2: Normalize image pixel values
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# Step 3: Reshape images for CNN
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

# Step 4: Build the CNN model
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(10, activation="softmax"),
])

# Step 5: Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)

print("\nCNN Model Summary:")
model.summary()

# Step 6: Train the model
print("\nTraining the CNN model...")
history = model.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1,
    verbose=1,
)

# Step 7: Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print("\nModel Evaluation")
print("Test Loss:", round(test_loss, 4))
print("Test Accuracy:", round(test_accuracy * 100, 2), "%")

# Step 8: Predict images
predictions = model.predict(X_test[:10], verbose=0)
predicted_labels = np.argmax(predictions, axis=1)

# Step 9: Display sample images and predictions
plt.figure(figsize=(14, 7))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_test[i].reshape(28, 28), cmap="gray")

    actual_name = class_names[y_test[i]]
    predicted_name = class_names[predicted_labels[i]]
    color = "green" if y_test[i] == predicted_labels[i] else "red"

    plt.title(
        f"Actual: {actual_name}\nPredicted: {predicted_name}",
        color=color,
        fontsize=9,
    )
    plt.axis("off")

plt.suptitle("Fashion MNIST CNN Image Classification")
plt.tight_layout()
plt.show()

# Step 10: Plot training and validation accuracy
plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("CNN Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
