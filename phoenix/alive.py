from telethon import events
import phoenix.client
import time
client = phoenix.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.تحميل'))
async def alive(event):
		client = event.client
		me = await client.get_me()
		username = me.username
		img = await client.download_profile_photo(username)
		time.sleep(0.5)
		await event.respond(f"""**Foydalanuvchi:** @{username}
**FINALUSERBOT:** https://t.me/i0i0ii 

**Developer:** @I0I0II 
			
v.1.2.0

📥 التحميل 

$ `pkg update && pkg upgrade`

$ `apt update && apt upgrade`

$ `pkg install git`

$ `pkg install python`

$ `git clone https://github.com/1mrxe1/FINALUSERBOT`

$ `python setup.py`

$ `python main.py`""", file=img)
		await event.message.delete()
