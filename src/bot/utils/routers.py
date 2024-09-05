from aiogram import Router

from src.bot.utils import filters

## MESSAGES ##
# MAIN #
msg = Router()
# ADMIN #
admin_msg = Router()
admin_msg.message.filter(filters.IsAdmin())

## CALLBACKS ##
# MAIN #
# cb = Router()
# ADMIN #
# admin_cb = Router()
# admin_cb.callback_query.filter(filters.IsAdmin())

## INLINES ##
# MAIN #
# inl = Router()

## ERRORS ##
# MAIN #
# err = Router()
