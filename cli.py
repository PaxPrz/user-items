import os
from dotenv import load_dotenv
import uvicorn

from alembic import command
from alembic.config import Config

from fire import Fire


_ = load_dotenv()


class AlembicCommand:

    def __init__(self):
        self.alembic_cfg = Config("alembic.ini")
        self.alembic_cfg.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))
        self.alembic_cfg.set_main_option("database_schema", os.environ.get("DATABASE_SCHEMA"))

    def heads(self, verbose: bool = False):
        """ Displays alembic heads """
        command.heads(self.alembic_cfg, verbose=verbose)

    def migrate(self, revision: str = "head", sql=False) -> None:
        """ upgrades the revisions """
        command.upgrade(self.alembic_cfg, revision=revision, sql=sql, tag=None)


class Command:
    def __init__(self):
        self.alembic = AlembicCommand()

    def serve(self, host: str = "127.0.0.1", port: int = 8080):
        uvicorn.run(
            "docker_test.app:app",
            host=host,
            port=port,
            log_level="info",
            reload=True,
        )


def main():
    Fire(Command)


if __name__ == "__main__":
    main()
