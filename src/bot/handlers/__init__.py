from aiogram import Router

from src.bot.handlers import messages, callbacks, inlines, errors


def get_routers() -> list[Router]:
	## MESSAGES ##
	msg = [
		# MAIN #
		messages.routers.msg,
		
		# ADMIN #
		messages.routers.admin_msg,
	]
	
	## CALLBACKS ##
	cb = [
		# MAIN #
		# callbacks.routers.cb,
		
		# ADMIN #
		# callbacks.routers.admin_cb,
	]
	
	## INLINES ##
	inl = [
		# MAIN #
		# inlines.routers.inl,
	]
	
	## ERRORS ##
	err = [
		# MAIN #
		# errors.routers.err,
	]
	return msg + cb + inl + err
