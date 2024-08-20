from aiogram import Router

from src.bot.utils import filters

# MESSAGES
msg = Router()

# CALLBACKS
cb = Router()

# INLINES
inl = Router()

# ERRORS
err = Router()

# EXTRA
# Admin
admin_msg = Router()
admin_msg.message.filter(filters.IsAdmin())
# admin_cb = Router()
# admin_cb.message.filter(filters.IsAdmin())
# admin_inl = Router()
# admin_inl.message.filter(filters.IsAdmin())
