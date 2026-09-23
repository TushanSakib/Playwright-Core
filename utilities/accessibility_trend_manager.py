import json
import os
class AccessibilityTrendManager:
    FILE_PATH = (
        "reports/accessibility/"
        "history/trend.json"
    )

    @classmethod
    def save_trend(cls,data):
        if os.path.exists(cls.FILE_PATH):
            with open(cls.FILE_PATH, "r") as file:
                trends = json.load(file)
        else:
            trends = []

        trends.append(data)
        with open(cls.FILE_PATH,"w") as file:
            json.dump(trends,file,indent=4)