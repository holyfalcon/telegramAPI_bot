
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

class Member:
    def __init__(self):
        self.file = 'members.csv'

    def get_file(self):
        return self.file


    def get_member(self,client):

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


        print('Choose a group to scrape members from:')
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

        with open(self.file, "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['R','username'])

            for user in all_participants:
                if user.username:
                    username= user.username
                else:
                    continue

                writer.writerow([j ,username])
                j +=1

        print('Members scraped successfully.')