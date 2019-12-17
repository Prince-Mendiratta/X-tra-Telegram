"""
DISCLAIMER:- 
	import disclaimer
	I am Not Responsible If this Software Causes you Any Kind Of Trouble.
	Use it on Your Own Risk.
	If You Blame me for Any Damage Caused by it. I will Laugh at you.
USAGE:-
	.rep = Reply To a User's message with ChatBot
	.autochat = //As a reply to user's Message. Add User in Auto-Chat List
	.stopchat = //As a reply to user's Message. Remove User from Auto-Chat List.
	.learnstart = Add Chat in Learning Chats List.
	.learnstop = Remove Chat from Learning Chats List.
	.listDB = Output Currently Stored Auto-Chat/Learning-Chat ID Data.
Credits:-
	@Zero_Cool7870 (Me)	

"""
from chatterbot import ChatBot 
from chatterbot.conversation import Statement
from telethon import events
import asyncio
import os
from uniborg.util import admin_cmd
import logging
logging.basicConfig(level=logging.INFO)


#Initialise Stuff
logic_adapters = [
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.SpecificResponseAdapter'
    ]
MONGO_URI= Config.MONGO_URI
try:	
	bot= ChatBot('Bot', #Prepare Bot
		 	storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
	    	database_uri=MONGO_URI,
	    	logic_adapters=logic_adapters
		)   
except Exception as e:
	logging.error(str(e))

#Some variables	  
current_msgs = {}
db = mongo_client['test']
auto_chat = db.auto_chat
learn_chat = db.learn_chat



@borg.on(admin_cmd(pattern="listDB", allow_sudo=True))
async def list_db(event):
	if event.fwd_from:
		return
	await event.edit("Processing...")	
	if MONGO_URI is None:
		await event.edit("Critical Error: Add Your MongoDB connection String in Env vars.")
		return
	autos = auto_chat.find({})
	learns = learn_chat.find({})
	msg = "**Data in Your DB:**\n__AutoChat:__\n"

	for i in autos:
		msg += "User: `"+str(i['user'])+"`\nChat: `"+str(i['id'])+"`\n"
	msg += "__LearnChats:__\n"
	for i in learns:
		msg += "Chat: `"+str(i['chat_id'])+"`\n"
	await event.edit(msg)		




@borg.on(admin_cmd(pattern="rep", allow_sudo=True))
async def chat_bot(event):
	if event.fwd_from:
		return
	if MONGO_URI is None:
		await event.edit("Critical Error: Add Your MongoDB connection String in Env vars.")	   
		return
	text = await event.get_reply_message()
	msg = str(text.message)
	reply = bot.get_response(msg)
	print(reply)
	await event.edit("**Jas's Bot:\n"+str(reply)+"**")

@borg.on(admin_cmd(pattern="autochat", allow_sudo=True))
async def chat_bot(event):
	if event.fwd_from:
		return  
	if MONGO_URI is None:
		await event.edit("Critical Error: Add Your MongoDB connection String in Env vars.")	
		return
	if not event.from_id:
		await event.edit("Reply To Someone's Message To add User in AutoChats..")
		return	
	reply_msg = await event.get_reply_message()	
	chats = auto_chat.find({})
	for c in chats:
		if event.chat_id == c['id'] and reply_msg.from_id == c['user']:
			await event.edit("This User is Already in Auto-Chat List.")
			await asyncio.sleep(1)
			await event.delete()
			return 
	auto_chat.insert_one({'id':event.chat_id,'user':reply_msg.from_id})
	await event.edit("Autochat mode turned on For User: "+str(reply_msg.from_id))
	await asyncio.sleep(1)
	await event.delete()

@borg.on(admin_cmd(pattern="stopchat", allow_sudo=True))
async def chat_bot(event):
	if event.fwd_from:
		return  
	if MONGO_URI is None:
		await event.edit("Critical Error: Add Your MongoDB connection String in Env vars.")	
		return
	if not event.from_id:
		await event.edit("Reply To Someone's Message To Remove User in AutoChats..")
		return		
	reply_msg = await event.get_reply_message()	
	auto_chat.delete_one({'id':event.chat_id,'user':reply_msg.from_id})
	await event.edit("Autochat mode turned off For User: "+str(reply_msg.from_id))	
	await asyncio.sleep(1)
	await event.delete()



@borg.on(admin_cmd(pattern="learnstart ?(.*)", allow_sudo=True))
async def learn_start(event):
	if event.fwd_from:
		return
	chat = event.pattern_match.group(1)
	if MONGO_URI is None:
		await event.edit("Critical Error: Add Your MongoDB connection String in Env vars.")	
		return
	chats = learn_chat.find({})	
	if chat:
		try:
			for c in chats:
				if int(chat) == c['chat_id']:
					await event.edit("This Chat is Already in Learning Chats.")
					return
			learn_chat.insert_one({'chat_id':int(chat)})
			await event.edit("ChatBot Auto learning started for Chat: "+chat)	
		except Exception as e:
			await event.edit("Error:\n{}".format(str(e)))		 
	else:	 
		chat = event.chat_id
		for c in chats:
			if int(chat) == c['chat_id']:
				await event.edit("This Chat is Already in Learning Chats.")
				return
		learn_chat.insert_one({'chat_id':chat})
		await event.edit("ChatBot Auto learning started for Chat: "+str(chat))	
	await asyncio.sleep(1)
	await event.delete()

@borg.on(admin_cmd(pattern="learnstop ?(.*)", allow_sudo=True))
async def learn_stop(event):
	if event.fwd_from:
		return
	chat = event.pattern_match.group(1)
	if MONGO_URI is None:
		await event.edit("Critical Error: Add Your MongoDB connection String in Env vars.")	
		return
	if chat:
		try:
			learn_chat.delete_one({'chat_id':int(chat)})
			await event.edit("ChatBot Auto learning stopped for Chat: "+chat)	
		except Exception as e:
			await event.edit("Error:\n{}".format(str(e)))		 
	else:	 
		chat = event.chat_id
		learn_chat.delete_one({'chat_id':chat})
		await event.edit("ChatBot Auto learning stopped for Chat: "+str(chat))	
	await asyncio.sleep(1)
	await event.delete()

#ChatBot Event Handler
@borg.on(events.NewMessage())      
async def chat_bot_update(event):			
	if MONGO_URI is None:
		return
	auto_chats = auto_chat.find({})
	learn_chats = learn_chat.find({})
	if not event.media:
		for ch in auto_chats:
			if event.chat_id == ch['id'] and event.from_id == ch['user']:  
				msg = str(event.text)
				reply = bot.get_response(msg)
				logging.info(reply)
				await event.reply("**Jas's Bot:\n"+str(reply)+"**")
	if not event.text:
		return
	for cht in learn_chats:		
		if event.chat_id == cht['chat_id']:	
			msg_id = event.id	
			current_msgs.update({event.text:msg_id})
			logging.info(event.text+":"+str(msg_id))
			if event.reply_to_msg_id:
				reply_msg = await event.get_reply_message()	
				try:
					for msg,mid in current_msgs.copy().items():
						if mid == event.id:	
							correct_response = Statement(str(msg))
							bot.learn_response(previous_statement=reply_msg.text,statement=correct_response)
							logging.info('Response added to bot!')
							current_msgs.pop(msg)
				except Exception as e:
					logging.error(str(e))
					pass	
			else:
				return 
						
