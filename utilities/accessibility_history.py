import json
import os
from datetime import datetime

from tensorflow import timestamp


class AccessibilityHistory:
    @staticmethod
    def save_results(
            page_name,
            results
    ):
        folder = (
            f"reposts/accessibility/{page_name}"
        )

        os.mkdir(
            folder,
            exist_ok=True
        )
        timestamp = (
            datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )
        )

        file_path = (
            f"{folder}/"
            f"accessibility_{timestamp}.json"
        )

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                results,
                file,
                indent=4
            )
        return file_path
