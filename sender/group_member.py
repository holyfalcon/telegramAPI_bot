from telethon.sync import TelegramClient , connection
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from sender.SendMessage import Chat



payam = Chat()
api_id = 3614966
api_hash = '5e7f994e5d0585260342f59b862b1251'
phone = '+989059034729'

client = TelegramClient(
    phone, api_id, api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=('Charles.FrEe-------------------------LoL.soft98---ir.tk.', 443, 'dd8a688e49b2cad1299445f0c23a6a581d')
)

client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))

chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue


print('Choose a group to get members, from:')
i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i += 1

g_index = input("Enter a Number: ")
target_group = groups[int(g_index)]

print('Fetching Members...')

all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)
j = 0
for user in all_participants:
    if user.username:
        print(str(j) +"_"+ user.username)
        j +=1
        # payam.send(user.username,client)
