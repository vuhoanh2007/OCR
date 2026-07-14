import numpy as np

class YOLODetector:
    def __init__(self):
        # Mocking YOLOv11 initialization
        self.ready = True
        
    def detect_cccd(self, image: np.ndarray):
        # Mock detection returning full image and dummy box
        h, w = image.shape[:2]
        return image, [0, 0, w, h]
