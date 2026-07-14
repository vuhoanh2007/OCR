import numpy as np
from paddleocr import PaddleOCR

class CCCDRecognizer:
    def __init__(self):
        # Disable logging for cleaner output
        self.ocr = PaddleOCR(use_angle_cls=True, lang='vi', show_log=False)
        
    def recognize_text(self, image: np.ndarray) -> list:
        result = self.ocr.ocr(image, cls=True)
        if not result or not result[0]:
            return []
        
        extracted = []
        for line in result[0]:
            text = line[1][0]
            confidence = line[1][1]
            extracted.append((text, confidence))
        return extracted
