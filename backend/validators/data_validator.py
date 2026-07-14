import re
from datetime import datetime

class DataValidator:
    @staticmethod
    def validate_cccd_id(id_str: str) -> bool:
        return bool(re.fullmatch(r'\d{12}', id_str))

    @staticmethod
    def validate_date(date_str: str) -> bool:
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False
