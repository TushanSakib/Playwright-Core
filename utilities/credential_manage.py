import json


class CredentialManager:

    FILE_PATH = (
        "config/credentials.json"
    )

    @classmethod
    def get_credentials(cls, role):

        with open(
            cls.FILE_PATH,
            "r",
            encoding="utf-8"
        ) as file:

            credentials = json.load(file)

        return credentials[role]