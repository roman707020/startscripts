from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait

stop = False
client = Client('startscripts', '26817926', '170e3ff3845374cf26f0566f7423056f')

client.start()
client.stop()

@client.on_message(filters.command('flood', prefixes='.') & filters.me)
def message_handler(client, message):
    global stop
    args = message.text.split(' ')
    if args[1] == 'stop':
        stop = True
        client.send_message(message.chat.id, 'spam stopped 🧨')
    i = int(args[1])
    while i >= 0:
        try:
            if(stop == True):
                i = 0
                stop = False
            client.send_message(message.chat.id, args[2])
            sleep(1/7)
        except FloodWait as e:
            sleep(e.x)
        i -= 1
        
@client.on_message(filters.command("giffsend", prefixes=".") & filters.me)
def sendgif(app, message):
	for _ in range(int(message.command[1])):
		sleep(0.01)
		app.send_document(message.chat.id, "https://tenor.com/ru/view/happy-llamas-gif-13768958")
		
client.run()