import configparser
import os

from app.infrastructure.config.models import (
    AppConfig,
    Config,
    DatabaseConfig,
)


DEFAULT_CONFIG_PATH: str = "./config/local.ini"


def load_config(path: str | None = None) -> Config:
    if path is None:
        path = os.getenv("CONFIG_PATH", DEFAULT_CONFIG_PATH)

    parser = configparser.ConfigParser()
    parser.read(path)

    application_data, database_data = parser["application"], parser["database"]

    application_config = AppConfig(
        debug=application_data.getboolean("debug"),
        major_version=application_data.getint("major_version"),
        minor_version=application_data.getint("minor_version"),
        patch_version=application_data.getint("patch_version"),
    )
    database_config = DatabaseConfig(
        host=database_data.get("host"),
        port=database_data.getint("port"),
        database=database_data.get("database"),
        user=database_data.get("user"),
        password=database_data.get("password"),
        echo=database_data.getboolean("echo"),
    )

    return Config(application_config, database_config)
