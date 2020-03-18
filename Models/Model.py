import tensorflow as tf
from tensorflow.keras.models import model_from_json

class GenerateModel:
    """
        For Getting the Model Architecture and Loading the Weights
    """

    def __init__(self, random_state=9):
        self.random_state = random_state

    def prelim_model(self):
        model_structure = 'Models/Model-18-3.json'
        model_weights = 'Models/Model-18-3.h5'

        with open(model_structure, 'r') as f:
            model = model_from_json(f.read())
        model.load_weights(model_weights)
        return model
