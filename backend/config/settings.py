from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "CCCD OCR Service"
    VERSION: str = "1.0.0"
    MAX_FILE_SIZE_MB: int = 10
    ALLOWED_EXTENSIONS: set = {"jpg", "jpeg", "png"}
    TEMP_DIR: str = "/tmp/ocr_uploads"

settings = Settings()
