import yaml
from pathlib import Path


class ConfigReader:
    _config = None

    @classmethod
    def load_config(cls):
        if cls._config is None:
            config_path = Path("config/config.yaml")

            with open(config_path, "r", encoding="utf-8") as file:
                cls._config = yaml.safe_load(file)

        return cls._config

    @classmethod
    def get(cls, *keys):
        data = cls.load_config()

        for key in keys:
            data = data[key]

        return data