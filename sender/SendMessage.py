from telethon import errors
import time
class Chat:
    def send(self,target_user,client):

        async def main():

            try:
                try:
                    try:



                            # me = await client.get_me()
                            text1 = "عاقلان نقطه ی پرگار وجودند ولی\n عشق داند که در این دایره سرگردانند"

                            text = "🔴🔴🔴🔴🔴\nهیدرولیک ثامن\n\nتامین کننده تمام قطعات هیدرولیک\nاز جمله:\n✅ شیر بلین آلمان\n✅ موتور غوطه ور\n✅ پمپ اسکرو\n✅ رابچر ولو\n✅ هیتر\nو...\n🌸🌸🌸🌸🌸🌸\nهیدرولیک ثامن\nتولید کننده جک و پاور یونیت های بالابری و اسانسوری\n\nبا بهترین قیمت و کیفیت بالا\n🏷کیفیت واقعی رو از ما بخواهید\n☎️جهت ارتباط:\n02125917397\n۰۹۱۲۹۳۳۵۰۷۷\n۰۹۱۹۶۵۵۳۷۱۳"
                            await client.send_message(target_user, text)

                    except errors.TakeoutInitDelayError as e:
                        print('3')
                        print('Must wait', e.seconds, 'before takeout')
                        time.sleep(e.seconds)
                except errors.FloodWaitError as e:
                    print('Have to sleep', e.seconds, 'seconds becuase FloodWait')
                    time.sleep(e.seconds)
            except errors.PeerFloodError as e:
                print('Have to sleep becuase PeerFlood')
                time.sleep(1800)



        with client:
            client.loop.run_until_complete(main())


    def send_group(self,target_user,client):

        async def main():

            try:
                try:
                    try:
                        try:
                            cap = "📍مشخصات هیدرولیک ثامن📍\n#آسانسور #هیتر #جک #پاوریونیت\n#شیر_برقی_بلین\n☎️جهت ارتباط:\n02125917397\n۰۹۱۲۹۳۳۵۰۷۷\n۰۹۱۹۶۵۵۳۷۱۳"
                            await client.send_file(target_user, 'photo_2021-02-26_19-34-15.jpg', caption=cap)

                        except errors.FloodWaitError as e:
                            print('Have to sleep', e.seconds, 'seconds becuase FloodWait')
                            time.sleep(e.seconds)
                    except errors.ChannelPrivateError as e:
                        print('ChannelPrivateError')
                except errors.SlowModeWaitError as e:
                    print('Have to sleep', e.seconds, 'seconds becuase SlowMode')
                    time.sleep(e.seconds)
            except errors.PeerFloodError as e:
                print('Have to sleep becuase PeerFlood')
                time.sleep(60)


        with client:
            client.loop.run_until_complete(main())