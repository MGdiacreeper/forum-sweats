from ..commandparser import Member

name = 'rigduel'
aliases = ['rigduels']
channels = None

rigged_duel_users = set()


async def run(message, member: Member = None):
	global rigged_duel_users
	if message.author.id != 856340031999311872: return  # only works for mat
	rigged_duel_users.add(member.id if member else message.author.id)
	await message.delete()
