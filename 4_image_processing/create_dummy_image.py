import os
from dotenv import load_dotenv
import cv2
import numpy as np
import matplotlib.pyplot as plt

load_dotenv()

ML_Summer_School_ID = os.getenv("ML_Summer_School_ID")
print("Your Sudent ID is: " + ML_Summer_School_ID)


# Create a dummy image
dummy_image = np.zeros((100, 150, 3), dtype=np.uint8)

print(type(dummy_image))
print(dummy_image.shape)
