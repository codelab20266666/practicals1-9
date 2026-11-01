# LP3 Practicals - Computer Vision, Deep Learning and Pygame

A collection of lab practicals covering OpenCV image processing, deep neural
networks with TensorFlow/Keras, and simple Pygame games.

| File | Practical | Topic |
|------|-----------|-------|
| `practical_02_image_processing.py` | 2 | Resize, crop, grayscale, threshold, contours, blob detection (OpenCV) |
| `practical_03_image_annotation.py` | 3 | Drawing lines, shapes and text on an image (OpenCV) |
| `practical_04_housing_regression.py` | 4 | California housing price prediction (Keras regression) |
| `practical_05_digit_recognition.py` | 5 | Handwritten digit classification (Keras DNN, scikit-learn digits) |
| `practical_06_fashion_mnist_cnn.py` | 6 | Fashion MNIST image classification (CNN) |
| `practical_08_obstacle_game.py` | 8 | Obstacle and coin game (Pygame) |
| `practical_09_jumping_game.py` | 9 | Jumping game with coins, obstacles and a win state (Pygame) |

## Setup

Python 3.9 - 3.12 is recommended (TensorFlow support for the newest Python
versions can lag behind).

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

## Running

```bash
python practical_02_image_processing.py   # needs sample.jpg in the same folder
python practical_03_image_annotation.py
python practical_04_housing_regression.py # downloads dataset on first run
python practical_05_digit_recognition.py
python practical_06_fashion_mnist_cnn.py  # downloads dataset on first run
python practical_08_obstacle_game.py
python practical_09_jumping_game.py
```

Notes:
- **Practical 2** reads `sample.jpg` from the script's folder. Add any image
  with that name. Output images are saved next to the script.
- **Practicals 4 and 6** download their datasets the first time they run, so
  an internet connection is needed once.
- **Practicals 8 and 9** controls: Left/Right arrows to move, Space to jump,
  `R` to restart after game over (or after winning in Practical 9).
- Image and plot windows stay open until you press a key (OpenCV) or close the
  window (Matplotlib).
