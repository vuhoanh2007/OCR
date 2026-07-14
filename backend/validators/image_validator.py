import cv2
import numpy as np

class ImageValidator:
    @staticmethod
    def validate(image: np.ndarray) -> tuple[bool, str]:
        if image is None or image.size == 0:
            return False, "Invalid image data"
            
        h, w = image.shape[:2]
        if h < 300 or w < 400:
            return False, "Image too small, minimum 400x300 required"

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur_val = cv2.Laplacian(gray, cv2.CV_64F).var()
        if blur_val < 50:
            return False, f"Image is too blurry (score: {blur_val:.2f})"

        brightness = np.mean(gray)
        if brightness < 40:
            return False, "Image is too dark"
        if brightness > 220:
            return False, "Image is overexposed"

        return True, "Valid"
