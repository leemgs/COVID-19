from __future__ import print_function
import numpy as np
import sys
import tensorflow as tf
from Models.Model import GenerateModel
from Utils.utilities import get_data, print_result
np.set_printoptions(suppress=True,formatter={'float_kind':'{:f}'.format})

if __name__=='__main__':
    filename_path=sys.argv[1]
    #filename_path='Demo.jpeg'
    img = get_data(filename_path)

    model = GenerateModel().prelim_model()
    prediction = model.predict(img)
    print_result(prediction)