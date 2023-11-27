from dataclasses import dataclass


@dataclass
class AppConfig:
    debug: bool
    major_version: int
    minor_version: int
    patch_version: int


@dataclass
class DatabaseConfig:
    host: str
    port: int
    database: str
    user: str
    password: str
    echo: bool

    # default values
    rdbms: str = "postgresql"
    connector: str = "psycopg"

    @property
    def full_url(self) -> str:
        return "{}+{}://{}:{}@{}:{}/{}".format(
            self.rdbms, self.connector,
            self.user, self.password,
            self.host, self.port, self.database
        )


@dataclass
class TestDatabaseConfig(DatabaseConfig):
    pass


@dataclass
class Config:
    app_config: AppConfig
    db_config: DatabaseConfig
    test_db_config: TestDatabaseConfig
