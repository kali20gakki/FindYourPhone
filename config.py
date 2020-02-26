import time



data_list = [
    {
        'name':'简书',
        'url':'https://www.jianshu.com/users/register',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'手机号已经被使用',
        'unused_text':'验证码无效或已过期，请重新发送验证码',
        'phone_parameter':'user[mobile_number]',
        'headers':{
            'Cookie': r'_ga=GA1.2.474973489.1582110939; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221703debf89c2b7-001ea025eeea3a-6313f69-921600-1703debf89d3b2%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D8e8EJXFcUmUTLIqMc3IugYPgGWfgcqyRpYRnk1zJbJDgWRAe27JadkqXEj-ZDiyR%26ck%3D6260.2.10.346.314.198.318.2%26shh%3Dwww.baidu.com%26wd%3D%26eqid%3Df1c7ed810004d400000000065e54c78a%22%7D%2C%22%24device_id%22%3A%221703debf89c2b7-001ea025eeea3a-6313f69-921600-1703debf89d3b2%22%7D; locale=zh-CN; _gid=GA1.2.1861532545.1582614418; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1582197016,1582434345,1582434780,1582614418; _m7e_session_core=75cd5c190099f3268795149ab1d32889; read_mode=day; default_font=font2; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2Fcaptchas%2Fnew%3Ft%3D1582614867140-53b; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1582614934',
            'Referer': 'https://www.jianshu.com/sign_up',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        },
        'payload':{
            'utf8': r'%E2%9C%93',
            'authenticity_token':'eOXnQKWzuHKSrLZ5L9sSqAgpBxYvmMB93zaJfSuqARsAV939uN1OzbsKYFWAp+AsJGu3BH6PJaPI64zpFu+y0Q==',
            'user[nickname]': 'eOXnQKWzuH',
            'user[mobile_number_country_code]': 'CN',
            'user[mobile_number]': '',
            'oversea': 'false',
            'force_user_nonexist': 'true',
            'sms_code': '1111',
            'captcha[validation][challenge]': '1d70c63d6ce297a067b34888d6da832e',
            'captcha[validation][gt]': 'ec47641997d5292180681a247db3c92e',
            'captcha[validation][validate]':'',
            'captcha[validation][seccode]':'',
            'captcha[id]': '',
            'security_number': 'true',
            'user[password]':'ec47641997d5292180sdsd',
            'commit': '注册'
        }
    },
    {
        'name':'微博',
        'url':'https://weibo.com/signup/v5/formcheck',
        'type':'GET',
        'use_poxies':False,
        'verify': True,
        'used_text':'err',
        'unused_text':'ok',
        'phone_parameter':'value',
        'headers':{
            'Cookie': 'SUB=_2AkMpCZKFf8NxqwJRmP4WxW_maYtxzA3EieKfVWNeJRMxHRl-yT92qmg_tRB6Aom8aq5XID3SLyMrPOcheOlxQdA_Qqbu; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhWTYLy9pfa7WhWLYzYbEvE; login_sid_t=f831acca5db61d1da8e881375abb2e2e; cross_origin_proto=SSL; Ugrow-G0=589da022062e21d675f389ce54f2eae7; TC-V5-G0=4de7df00d4dc12eb0897c97413797808; WBStorage=42212210b087ca50|undefined; _s_tentry=passport.weibo.com; wb_view_log=1280*7201.5; appkey=; Apache=5439766794933.822.1582636473650; SINAGLOBAL=5439766794933.822.1582636473650; ULV=1582636473693:1:1:1:5439766794933.822.1582636473650:',
            'Referer': 'https://weibo.com/signup/signup.php',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        },
        'payload':{
            'type': 'mobilesea',
            'zone': '0086',
            'value': '',
            'from': '',
            '__rnd': '1582636504070'
        }
    },
    {
        'name':'知网',
        'url':'https://my.cnki.net/Register/Server.aspx',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'2',
        'unused_text':'0',
        'phone_parameter':'mobile', 
        'headers':{
            'Cookie': 'Ecp_ClientId=5200225223400688636; Ecp_IpLoginFail=20022514.204.170.150; ASP.NET_SessionId=zc53fq2gglbthyxqewrh1ws0; SID=020101',
            'Referer': 'https://my.cnki.net/Register/CommonRegister.aspx',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        },
        'payload':{
            'mobile': '',
            'temp': str(round(time.time())),
            'operatetype': '3',
        }      
    },
    {
        'name':'百度',
        'url':'https://passport.baidu.com/v2/?regphonecheck&phone=15846007767&isexchangeable=1',
        'type':'GET',
        'use_poxies':False,
        'verify': False,
        'used_text':'400001',
        'unused_text':'110000',
        'phone_parameter':'phone', 
        'headers':{},
        'payload':{
            "phone": '', 
            "isexchangeable": 1
        }
    },
    {
        'name':'前程无忧',
        'url':'https://login.51job.com/ajax/checkinfo.php',
        'type':'GET',
        'use_poxies':False,
        'verify': True,
        'used_text':'1',
        'unused_text':'0',
        'phone_parameter':'value', 
        'headers':{},
        'payload':{
            "value": '', 
            "nation":"CN",
            "type":"mobile"
        }
    },
    {
        'name':'360',
        'url':'https://login.360.cn',
        'type':'GET',
        'use_poxies':False,
        'verify': True,
        'used_text':'1',
        'unused_text':'0',
        'phone_parameter':'mobile', 
        'headers':{},
        'payload':{
            "m": "checkmobile", 
            "mobile": ''
        }       
    },
    {
        'name':'暴风影音',
        'url':'https://sso.baofeng.com/new/api/is_mobile_used',
        'type':'GET',
        'use_poxies':False,
        'verify': False,
        'used_text':'1}$',
        'unused_text':'0}$',
        'phone_parameter':'mobile', 
        'headers':{},
        'payload':{
            "appid": 8637,
            "sign": "32a4a7b48d4a1a12f445ac51e878cf2e5d9aa3c5",
            "mobile": ''
        }
    },
    {
        'name':'凯撒旅游网',
        'url':'http://my.caissa.com.cn/Registered/CheckPhone',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'0',
        'unused_text':'1',
        'phone_parameter':'phone', 
        'headers':{},
        'payload':{
            "hdurl": "http://caissa.com.cn/",
            "phone": ''
        }       
    },
    {
        'name':'凤凰网',
        'url':'https://id.ifeng.com/api/checkMobile',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'\:1\,',
        'unused_text':'\:0\,',
        'phone_parameter':'u', 
        'headers':{},
        'payload':{
            'u':''
        }       
    },
    {
        'name':'爱医医',
        'url':'https://account.iiyi.com/index/checkbind',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'400',
        'unused_text':'200',
        'phone_parameter':'bind', 
        'headers':{
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
        },
        'payload':{
           "bind": ''
        }       
    },
    {
        'name':'爱奇艺',
        'url':'https://passport.iqiyi.com/apis/user/check_account.action',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'true}$',
        'unused_text':'false}$',
        'phone_parameter':'account', 
        'headers':{
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "https://www.iqiyi.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.iqiyi.com/iframe/loginreg?ver=1&is_reg=1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9"
        },
        'payload':{
            "account":'', 
            "agenttype":1
        }       
    },
    {
        'name':'乐淘网',
        'url':'http://www.letao.com/ff80808157ffc1c2015800534d4c0000/checkPhone.do',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'true',
        'unused_text':'false',
        'phone_parameter':'phone', 
        'headers':{},
        'payload':{
           "phone": ''
        }
    },
    {
        'name':'猫扑网',
        'url':'http://passport.mop.com/ajax/mobileWasBound',
        'type':'GET',
        'use_poxies':False,
        'verify': True,
        'used_text':'\:1\,',
        'unused_text':'\:0\,',
        'phone_parameter':'mobile', 
        'headers':{},
        'payload':{
           'mobile': ''
        }
    },
    {
        'name':'牛客网',
        'url':'https://www.nowcoder.com/nccommon/register/check-phone-available',
        'type':'GET',
        'use_poxies':False,
        'verify': True,
        'used_text':'1}$',
        'unused_text':'0}$',
        'phone_parameter':'phone', 
        'headers':{},
        'payload':{
           'phone': '%2B86'
        }
    },
    {
        'name':'PPTV聚力',
        'url':'http://api.passport.pptv.com/checkRegister',
        'type':'GET',
        'use_poxies':False,
        'verify': True,
        'used_text':'6\"\}',
        'unused_text':'0\"\}',
        'phone_parameter':'loginid', 
        'headers':{
            "Host": "api.passport.pptv.com",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9"           
        },
        'payload':{
          "loginid": '', 
          "sceneFlag": "1", 
          "channel":"208000103005", 
          "format": "jsonp"
        }
    },
    {
        'name':'去哪儿',
        'url':'https://user.qunar.com/ajax/validator.jsp',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'11009',
        'unused_text':'21006',
        'phone_parameter':'method', 
        'headers':{},
        'payload':{
           "method":'' , 
           "prenum": "86"
        }
    },
    {
        'name':'人人网',
        'url':'http://reg.renren.com/AjaxRegisterAuth.do',
        'type':'POST',
        'use_poxies':False,
        'verify': True,
        'used_text':'不能注册',
        'unused_text':'OK',
        'phone_parameter':'value', 
        'headers':{},
        'payload':{
            "authType": "email",
            "stage":3,
            "value":'',
        }
    },
]
