api_id = 2364290
api_hash = '41ea2ad0e9b099f728c6ee1c974b3bf3'
phone = '+989367438410'

token = '1644184309:AAFmp328u6xH8GsT9j3FujtW12mEQnGrlJk'



api_id = 3614966
api_hash = '5e7f994e5d0585260342f59b862b1251'
phone = '+989059034729'


api_id = 3025057
api_hash = 'b3a776308c52ac92732b4f441a762306'
phone = '+989382247683'




# Traceback (most recent call last):
#   File "C:/Users/Shahin/PycharmProjects/inf_gp_bot/sender/Send_To_Member.py", line 29, in <module>
#     payam.send(mem,client)
#   File "C:\Users\Shahin\PycharmProjects\inf_gp_bot\sender\SendMessage.py", line 27, in send
#     client.loop.run_until_complete(main())
#   File "C:\Users\Shahin\AppData\Local\Programs\Python\Python37\lib\asyncio\base_events.py", line 587, in run_until_complete
#     return future.result()
#   File "C:\Users\Shahin\PycharmProjects\inf_gp_bot\sender\SendMessage.py", line 15, in main
#     await client.send_message(target_user, text)
#   File "C:\Users\Shahin\AppData\Local\Programs\Python\Python37\lib\site-packages\telethon\client\messages.py", line 798, in send_message
#     result = await self(request)
#   File "C:\Users\Shahin\AppData\Local\Programs\Python\Python37\lib\site-packages\telethon\client\users.py", line 30, in __call__
#     return await self._call(self._sender, request, ordered=ordered)
#   File "C:\Users\Shahin\AppData\Local\Programs\Python\Python37\lib\site-packages\telethon\client\users.py", line 79, in _call
#     result = await future
# telethon.errors.rpcerrorlist.PeerFloodError: Too many requests (caused by SendMessageRequest)