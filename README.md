# CCCD OCR Service

A production-ready standalone OCR service for Vietnamese Citizen Identity Cards (CCCD).
Built with FastAPI, PaddleOCR, YOLOv11 (Structure), and OpenCV.

## Pipeline Architecture
1. **Validation**: Quality checks (blur, brightness) using OpenCV Laplacian and intensity means.
2. **Preprocessing**: CLAHE Contrast stretching.
3. **Detection**: YOLOv11 bounding box detection for the ID card boundaries.
4. **Recognition**: PaddleOCR extracts fields accurately.
5. **Post-processing & Validation**: Cleaned up via Regex rules and parsed into JSON format.

## Run via Docker
```bash
docker-compose up --build
```

## API Documentation
Once running, visit `http://localhost:8000/docs` for Swagger UI.
