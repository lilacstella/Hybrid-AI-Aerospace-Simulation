# -*- coding: utf-8 -*-
"""Python Script.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a0OT6EPNw2YInM0ULbJ3lPbIaEudRStk
"""

from google.colab import drive
drive.mount('/content/mnt')

"""[[7.0,0.87],[8.0, 0.95], [5.0, 0.5]]"""

alpha1, mach1 = input("Enter the first set of alpha and mach values: ").split(', ')
alpha2, mach2 = input("Enter the second set of alpha and mach values: ").split(', ')
import numpy as np
examples = np.array([[alpha1, mach1], [alpha2, mach2]], dtype=float)

import tensorflow as tf
model = tf.keras.models.load_model('mnt/My Drive/AI Project/CRM Convergence/model.h5')

model.predict(examples)