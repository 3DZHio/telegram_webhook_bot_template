from aiogram import Router

from src.bot.handlers import messages, callbacks, inlines, errors


def get_routers() -> list[Router]:
	return [
		### MESSAGES ###
		## MAIN ##
		messages.routers.msg,
		## ADMIN ##
		messages.routers.admin_msg,
		
		### CALLBACKS ###
		## MAIN ##
		# callbacks.routers.cb,
		## ADMIN ##
		# callbacks.routers.admin_cb,
		
		### INLINES ###
		# inlines.routers.inl,
		
		### ERRORS ###
		# errors.routers.err,
	]
