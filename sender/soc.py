from telethon.sync import TelegramClient ,connection
import time
from sender.SendMessage import Chat

payam = Chat()

api_id = 2364290
api_hash = '41ea2ad0e9b099f728c6ee1c974b3bf3'
phone = '+989367438410'


client = TelegramClient(
    phone, api_id, api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=('Charles.FrEe-------------------------LoL.soft98---ir.tk.', 443, 'dd8a688e49b2cad1299445f0c23a6a581d')
)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
j=0
while 1:
    print(str(j)+'-'+'+989309655163')
    j += 1
    payam.send('+989309655163',client)
    time.sleep(100)