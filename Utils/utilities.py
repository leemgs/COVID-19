import numpy as np
import tensorflow as tf


def get_data(path):
    img = tf.keras.preprocessing.image.load_img(path, target_size=(256, 256))
    img = np.reshape(img, (256, 256, 3))
    img = img.astype('float32') / 255

    # Transforming PIL Image Object to Numpy Array
    img = np.expand_dims(img, axis=0)

    return img


def print_result(predictions):
    prediction_class = np.argmax(predictions, axis=1)

    if prediction_class == 0:
        print("The Person is Suffering from Pneumonia with a confidence of ", predictions[0][0] * 100)
    elif prediction_class == 1:
        print("The Person is Healthy with a confidence of ", predictions[0][1] * 100)
    else:
        print("The Person is COVID-19 Suspect with a confidence of ", predictions[0][2] * 100)