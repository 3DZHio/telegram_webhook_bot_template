from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from redis.asyncio import Redis

from src.bot.handlers import get_routers
from src.bot.utils.logs import setup_logger
from src.config import settings
from src.database.core import db


async def on_startup(bot: Bot) -> None:
    await db.connect()
    await bot.set_webhook(url=settings.webhook_url, drop_pending_updates=settings.pending_updates,
                          secret_token=settings.WEBHOOK_SECRET.get_secret_value())


async def on_shutdown(bot: Bot) -> None:
    await db.disconnect()
    await bot.delete_webhook()


def main() -> None:
    setup_logger(level=settings.LOG_LEVEL)
    bot = Bot(
        token=settings.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(
        storage=RedisStorage(redis=Redis.from_url(url=settings.storage_dsn))
    )
    dp.include_routers(*get_routers())
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp, bot=bot, secret_token=settings.WEBHOOK_SECRET.get_secret_value()
    )
    webhook_requests_handler.register(
        app, path=f"/{settings.WEBHOOK_PATH.get_secret_value()}"
    )
    setup_application(app, dp, bot=bot)
    web.run_app(
        app,
        host=settings.WEBHOOK_HOST.get_secret_value(),
        port=int(settings.WEBHOOK_PORT.get_secret_value()),
    )


if __name__ == "__main__":
    main()
