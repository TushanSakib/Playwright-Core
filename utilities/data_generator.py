import uuid


class DataGenerator:

    @staticmethod
    def first_name():

        return "Automation"

    @staticmethod
    def middle_name():

        return "QA"

    @staticmethod
    def last_name():

        return f"User{uuid.uuid4().hex[:6]}"

    @staticmethod
    def nickname():
        return f"Nick{uuid.uuid4().hex[:4]}"

    @staticmethod
    def username():
        return (
            "user_"+
            uuid.uuid4().hex[:5]
        )

    @staticmethod
    def email():
        return(
            f"automation_ "
            f"{uuid.uuid4().hex[:5]}"
            f"@mail.com"
        )