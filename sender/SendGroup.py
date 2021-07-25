# coding=utf8
import asyncio
import time
from telethon import TelegramClient,connection
from datetime import datetime
from sender.SendMessage import Chat
from sender.read_csv import Read


payam = Chat()
read = Read()

api_id = 3614966
api_hash = '5e7f994e5d0585260342f59b862b1251'
phone = '+989059034729'
proxy = 'gamsteel.ir.modirafzar.ir.iranspider.com.monitorict.org.amitistour.net.ebrahimsoltani.ir.joveyn.ir.pichab.ir.meiranian.ir.sotsotak.com.barekatstore.com.honarfa.ir.dibikala.com.rahearman.ir.azaliagroup.ir.sobhekavir.com.nejatrayaneh.ir.times-strait.co.in.'
client = TelegramClient(
    phone, api_id, api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=(proxy, 443, 'ddda411655b684fe87abf58ec2235e2816')
)

groups = read.read_group('group.csv')

client.start()
print(client)
# time.sleep(14400)

j = 12
while j>0:
    print(str(j)+"-------------------------------------------------------------")
    for group in groups:
            payam.send_group(group, client)
            print("send to => " + group)
            time.sleep(2)

    now = datetime.now()
    print(now)
    time.sleep(3600)

    j -= 1
