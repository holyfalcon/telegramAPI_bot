from telethon.sync import TelegramClient , connection
from sender.SendMessage import Chat
from sender.get_members import Member
from sender.read_csv import Read

member = Member()
read = Read()
payam = Chat()

members = []

api_id = 3600066
api_hash = '5e7f9****1251'
phone = '+98905***29'


proxy = 'gamsteel.ir.modirafzar.ir.iranspider.com.monitorict.org.amitistour.net.ebrahimsoltani.ir.joveyn.ir.pichab.ir.meiranian.ir.sotsotak.com.barekatstore.com.honarfa.ir.dibikala.com.rahearman.ir.azaliagroup.ir.sobhekavir.com.nejatrayaneh.ir.times-strait.co.in.'
client = TelegramClient(
    phone, api_id, api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=(proxy, 443, 'ddda411655b684fe87abf58ec2235e2816')
)

client.connect()

# member.get_member(client)
file = member.get_file()
members = read.read_member(file)
j = 1
for mem in members:
    payam.send(mem,client)
    print(str(j) + '_message SEND to => '+mem)
    j +=1