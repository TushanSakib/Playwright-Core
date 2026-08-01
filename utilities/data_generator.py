import uuid

class DataGenerator:
    @staticmethod
    def first_name():
        return "Auto"

    @staticmethod
    def middle_name():
        return "QA"

    @staticmethod
    def last_name():
        return str(uuid.uuid4())[:6]