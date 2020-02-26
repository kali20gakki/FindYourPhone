import requests,re
import aiohttp,asyncio,time,json
from requests.packages import urllib3
urllib3.disable_warnings()

url = ''

head = {
}

data = {
}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=head) as resp:
            r = await resp.text()
            print(r)
            if re.search("0\"\}", r):
                print('未注册')
            elif re.search('6\"\}', r):
                print('已注册')
            



loop = asyncio.get_event_loop()
loop.run_until_complete(main())


# r = requests.get(url, params=data,headers={}, verify=False)
# print(r.text)