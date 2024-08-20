from aiogram import Router

from src.bot.handlers import messages, callbacks, inlines, errors


def get_routers() -> list[Router]:
    # MESSAGES
    msg = [
        messages.routers.msg,
    ]
    # CALLBACKS
    cb = [
        # callbacks.routers.cb,
    ]
    # INLINES
    inl = [
        # inlines.routers.inl,
    ]
    # ERRORS
    err = [
        # errors.routers.err,
    ]
    # EXTRA
    extra = [
        messages.routers.admin_msg,
        # callbacks.routers.admin_cb,
        # inlines.routers.admin_inl,
    ]
    return msg + cb + inl + err + extra
