import requests, aiohttp, asyncio
import logging, sys, re
from lxml import etree
from config import data_list
from requests.packages import urllib3
urllib3.disable_warnings()

logging.basicConfig(stream=sys.stderr, format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)

class Spider:
    def __init__(self, phone_num, data_list):
        self.phone = phone_num
        self.data_list = data_list
    

    def __get_area(self):
        if self.__check_phone_aviable():
            url = 'https://shouji.supfree.net/fish.asp?cat=' + self.phone
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
            }
            r = requests.get(url=url, headers=headers)
            if r.encoding == 'ISO-8859-1':
                encodings = requests.utils.get_encodings_from_content(r.text)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = r.apparent_encoding
                encode_content = r.content.decode(encoding, 'replace')

            
            html = etree.HTML(encode_content)
            area = html.xpath("//*[@id='content']/div/div[2]/div[3]/p[1]/text()")[0]
            num = html.xpath("//*[@id='content']/div/div[2]/div[3]/p[2]/a/text()")[0]
            sim_type = html.xpath("//*[@id='content']/div/div[2]/div[3]/p[3]/text()")[0]
            in_sim = html.xpath("//*[@id='content']/div/div[2]/div[3]/p[5]/a/text()")[0]
            stand = html.xpath("//*[@id='content']/div/div[2]/div[3]/p[6]/a[1]/text()")[0]
            
            logging.info('归属地: %s'%area)
            logging.info('号码段: %s'%num)
            logging.info('卡类型: %s'%sim_type)
            logging.info('内置卡: %s'%in_sim)
            logging.info('标  准: %s'%stand)

            return True
        else:
            return False


    def __check_phone_aviable(self):
        # 联通 130，131，132，155，156，185，186，145，176
        if re.match(r'^13[0,1,2]\d{8}$',self.phone) or \
           re.match(r'^15[5,6]\d{8}$',self.phone) or \
           re.match(r'^18[5,6]\d{8}$',self.phone) or \
           re.match(r'^145\d{8}$',self.phone) or \
           re.match(r'^176\d{8}$',self.phone):
            logging.info('手机号: %s 联通'%self.phone)
            return True
        # 移动 134, 135 , 136, 137, 138, 139, 147, 150, 151,
        # 152, 157, 158, 159, 178, 182, 183, 184, 187, 188
        elif re.match(r'^13[4,5,6,7,8,9]\d{8}$',self.phone) or \
             re.match(r'^147\d{8}|178\d{8}$',self.phone) or \
             re.match(r'^15[0,1,2,7,8,9]\d{8}$',self.phone) or \
             re.match(r'^18[2,3,4,7,8]\d{8}$',self.phone):
            logging.info('手机号: %s 移动'%self.phone)
            return True
        # 电信 133,153,189
        elif re.match(r'^133\d{8}$',self.phone) or \
             re.match(r'^153\d{8}$',self.phone) or \
             re.match(r'^189\d{8}$',self.phone):
            logging.info('手机号: %s 电信'%self.phone)
            return True
        else:
            logging.error('手机号: %s 非法'%self.phone)
            return False
    

    async def __check_register(self, data_dict):
        data_dict['payload'][data_dict.get('phone_parameter')] += self.phone

        async with aiohttp.ClientSession() as session:
            if data_dict.get('type') == 'POST':
                async with session.post(url=data_dict.get('url'), 
                                        data=data_dict.get('payload'), 
                                        headers=data_dict.get('headers')) as resp:
                    r = await resp.text()

            elif data_dict.get('type') == 'GET':
                if data_dict.get('verify'):
                    async with session.get(url=data_dict.get('url'), 
                                            params=data_dict.get('payload'), 
                                            headers=data_dict.get('headers')) as resp:
                        r = await resp.text()
                else:
                    r = requests.get(url=data_dict.get('url'),
                                     params=data_dict.get('payload'),
                                     verify=False)
                    r = r.text

            if re.search(data_dict.get('unused_text'), r):
                logging.info("手机号: %s -- [X] %s"%(self.phone, data_dict.get('name')))
            elif re.search(data_dict.get('used_text'), r):
                logging.info("手机号: %s -- [√] %s"%(self.phone, data_dict.get('name')))
            else:
                logging.error('查询 %s 错误'%data_dict.get('name'))
    

    def run(self):
        if self.__get_area():
            tasks = [asyncio.ensure_future(self.__check_register(data_dict)) for data_dict in self.data_list]
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.wait(tasks))





if __name__ == '__main__':
    phone = input('输入手机号: ')
    s = Spider(phone, data_list)
    s.run()