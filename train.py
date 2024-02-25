import tensorflow as tf
from sklearn.datasets import fetch_lfw_people
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# preprocess data
# ...

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50, 37, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(data.target_names.shape[0])
])

# Compile the model
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=10)

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)


for path in Path(folder).rglob('*'):
  # Skip all but files
  if not os.path.isfile(path): continue
