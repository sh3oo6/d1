from time import sleep;
import requests
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.sync import TelegramClient , functions , events
import asyncio
import random


id='5229914714'
token='6183317549:AAGB5jAoTSGSc0M0Y_8WR7kEa7oYbyjshM0'
numb_s ='1'
user='dex34bot'
led=TelegramClient('dex40', 2192036, '3b86a67fc4e14bd9dcfc2f593e75c841')
led.start()
led.send_message('me','ok')
uss='qwertyuioplkjhgfdsazxcvbnm1234567890'
rr='qwertyuioplkjhgfdsazxcvbnm'


@led.on(events.NewMessage(pattern=r'x', outgoing=True))
async def execute_script(event):
    await led.send_message('me','offf')
    x = 0
    while True:
        i=0
        while True:
            i += +1
            x += +1
            u = str(''.join((random.choice(uss) for i in range(2))))
            e = str(''.join((random.choice(rr) for i in range(1))))
            user = e + u + 'bot'
            if i == 100:
                sleep(1.4)
                break
            sleep(1)
            req = requests.get(f"https://t.me/{user}")
            if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
                p = requests.get(f"https://fragment.com/username/{user}").text
                sleep(0.7)
                if "On auction" in p or 'Available' in p:
                    pass
                elif 'Sold' in p:
                    pass
                else:
                    try:
                        take = await led(UpdateUsernameRequest(user))
                        if take:
                            exit()

                    except Exception:
                        pass
            else:
                await led.send_message('me',(f"NOOO : {user}" + ' ' + str(i) + " " + str(x)))

@led.on(events.NewMessage(outgoing=True, pattern="i"))
async def _(event, x):
    await led.send_message('me',x)



led.run_until_disconnected()
