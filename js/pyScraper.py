import sys
import json
import requests
from requests.exceptions import ConnectionError

import scrapeScout as scout
import scrapeMobileDE as mobile

headersDE = {
    'Host': 'www.mobile.de',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': 'sorting_e=""; show_qs_e=vhc%3Acar%2Cms1%3A25200_14_; _abck=A29FBBA04447D66FAF82AC5E995225EA~0~YAAQRggQAq2L9o2AAQAA3grAmAdeTWunTIqhlCsbISDOjoi8bFEfSzyl+WxbYc5DglHzL/Ckor43VXIKLZJaJOg/aVTvIuEW5d044z5vSRj4tfoWnquJQvQMfFVDDoZBjfRjGGi1fCFv3m3NAPQ/uHGFhp0t/gBnEIL0D/VF+UqEzsdPXCISCLBhL+HSSSyjRa+JwTLWnj5gzjQqoFa6v7VQYiW8I4YDVATfv3oNV+8WY67dsWih4GkDaYlgQfhpg3TFrNHEr4qlktl9kedOjR63MxWqSrrX0hJrEUaWYKuWzquODayDPw8FEhLhkaxM1tLGT33qfXSwKALFbStSwmHD3P9k//1d0yOLycEWvLbgLqBszPl2hDces7BrIzy4Izt4pJI7wM2qhhvnIMugJtxmr6UYSx0=~-1~-1~-1; bm_sz=521F24D458DC92A597605A8599F764C2~YAAQp+oWArq/1HOAAQAALixUmA/2dtKD0sEKJFQNeQatNCx5J3PzSjICeDXEvZa9XPL3ibOpbwRmjzZzZpuldKdgH5p57sg23lrAFOOCQngPqAEfPLLaliyk/LSC3EhKolqnU6kKG3fCTxRwuSfWs/mVVLbhM9MRXeJW3IB/M6i66Fy0DVLCa9Ebu5plR0x0uIuKnVGZWSIMPbh73iSNSsUO1u7JlqRqtLMiZxruYxp4EdNM5g2cdXgYZCcpn/asBptlAGvm/GjnHIpp1E9rZNIGKVGYc6ncSz2UGylcfPVVuw==~3225650~4342321; vi=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjaWQiOiJiNDVmOGJmMC1mZDZiLTRiNTAtOWU0MC1hYmRjZDQ4MDY0ZDkiLCJpYXQiOjE2NTE4MjMwOTl9.i1Mo5x_AgHrcrUY43_Wmerj_KGovLBojbvoghnbnsLg; mobile.LOCALE=de; optimizelyEndUserId=oeu1651823096569r0.5312481568497365; visited=1; mdeConsentDataGoogle=1; mdeConsentData=CPYkDPWPYkDPWEyAHADECMCgAP_AAELAAAYgIsNd_X__bX9n-_7__ft0eY1f9_r3_-QzjhfNs-8F3L_W_L0X_2E7NF36tq4KuR4ku3bBIQNtHMnUTUmxaolVrzHsak2cpyNKJ7LkknsZe2dYGH9Pn9lD-YKZ7_5___f53z___9_-39z3_9f___d__-__-vjf_599n_v9fV_____________-_______8C84A4ACgAQAA0ACKAEwALYC8wCQkBAABYAFQAMgAcABEADIAHgARAAngBVAGGAP0BIgDJAGTgMuDQBQAmABcAOqAkQBk4iAIAEwA6oCRAGTioAgATAAuAKbAXmMgBABMAXmOgLAALAAqABkADgAIgAZAA8AB8AEQAJ4AVQAuABfADEAJgAYYA_QCLAJEAZIAycBlxCAUAAsADIAIgAmABVAC4AF8AMQCRAGTkoBgACwAMgAcABEADwAIgAVQAuABfADEAkQBk5SAmAAsACoAGQAOAAiABkADwAIgATwApABVAC-AGIAfoBFgEiAMkAZOAy4.YAAAAAAAD4AAAKcAAAAA; _ga=GA1.2.1824592379.1651823100; _gid=GA1.2.186741692.1651823100; _ga_2H40T2VTNP=GS1.1.1651828825.2.1.1651830167.0; ioam2018=0019f5046cda69a946274d1fd:1678434304777:1651823104777:.mobile.de:31:mobile:DE/ES/OB/S/P/D:noevent:1651830286721:sssfvb; iom_consent=0103ff03ff&1651823105397; _pubcid=c2cb941e-bb17-4ac5-b2e1-cebb14223731; cto_bundle=-ZMfdV9kMWFpbGZCWmhIejJZZVNjN2xPbjYzY21mZjdkVmQxU3p3OHdId2FlVW1HNGowWHp5RDAlMkJIRUNtTFJnT0EwUVhKd2h0JTJGS2FBakMlMkJlOGlYbVBlbTZuJTJCckwlMkJ4U1VlR2xGTVo0RXFXWXJ5Rk1FdTlXZkNseHV6U0hVS3pYYklYRU5xOWtxcHV2M1pxdGpWaWpSV2JmNWZnJTNEJTNE; cto_axid=x6mG858LHXc9na4WBHkYdsdWA_35tuiY; _clck=fsdy4i|1|f18|0; _clsk=6obze5|1651830164043|8|1|a.clarity.ms/collect; _uetsid=dfeb0740cd1011ec92ee71a685fb3d44; _uetvid=dfeb4d70cd1011ec942103db0d71c99a',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'trailers',
}


class SiteNotInDatabase(Exception):
    pass


class BadURL(Exception):
    pass


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        try:
            r = requests.get(url, headers=headersDE)
        except ConnectionError as e:
            raise(BadURL)
        if r:
            if 'mobile.de' in url:
                ans = mobile.main(r)
            elif 'autoscout.es' in url:
                ans = ''
            else:
                raise(SiteNotInDatabase)
            
            print(json.dumps(ans))
        else:
            raise(BadURL)

    except SiteNotInDatabase:
        print(json.dumps({'Response': 'Site Not Found'}))

    except BadURL:
        print(json.dumps({'Response': 'Bad URL'}))

    # except Exception:
    #     print(json.dumps({'Response': 'Unknown Error'}))
