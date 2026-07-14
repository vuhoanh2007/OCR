import cv2
import numpy as np

class ImageValidator:
    @staticmethod
    def validate(image: np.ndarray) -> tuple[bool, str]:
        if image is None or image.size == 0:
            return False, "Invalid image data"
            
        h, w = image.shape[:2]
        if h < 150 or w < 200:
            return False, "Image too small, minimum 200x150 required"

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur_val = cv2.Laplacian(gray, cv2.CV_64F).var()
        if blur_val < 15:
            return False, f"Image is too blurry (score: {blur_val:.2f})"

        brightness = np.mean(gray)
        if brightness < 20:
            return False, "Image is too dark"
        if brightness > 240:
            return False, "Image is overexposed"

        return True, "Valid"
