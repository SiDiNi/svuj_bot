from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    bot_token: str
    admin_ids: list[int]


# @dataclass
# class Database:
#     host: str
#     port: int
#     name_db: str
#     name_user: str
#     password: str
#
#     @property
#     def database_url(self) -> str:
#         return f"postgresql+asyncpg://{self.name_user}:{self.password}@{self.host}:{self.port}/{self.name_db}"


@dataclass
class Config:
    bot: TgBot
    # db: Database


def load_config(data: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(data)

    return Config(
        bot=TgBot(
            bot_token=env("BOT_TOKEN"), admin_ids=list(map(int, env.list("ADMIN_IDS")))
        ),
        # db=Database(
        #     host=env("DB_HOST"),
        #     port=env("DB_PORT"),
        #     name_db=env("DB_NAME"),
        #     name_user=env("DB_USER"),
        #     password=env("DB_PASSWORD"),
        # ),
    )


config = load_config()
