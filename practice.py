from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.amazon.in/Victorinox-Maverick-Large-Blue-43/dp/B09MJYYQZ7/ref=sr_1_8?pf_rd_i=2563504031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=3847c7f8-31ab-4ba4-824f-833f979d5d48&pf_rd_r=NV0DZRSMXV9JTQ97GXTK&pf_rd_s=merchandised-search-1&pf_rd_t=30901&qid=1658418709&s=apparel&sr=1-8"
# url = "https://www.amazon.in/Apple-MME73HN-A-AirPods-3rd-Generation/dp/B09JRDN6PL/ref=sr_1_1?crid=3PVCSGJIIVVBQ&keywords=air+podspro+apple&qid=1658414582&s=electronics&sprefix=air+pods%2Celectronics%2C353&sr=1-1"
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
#     "Accept-Language":"en",
# }

# r=requests.get(url,headers=headers)

# soup = BeautifulSoup(r.text,'lxml')

# # print(soup.prettify())

# name = soup.select_one(selector='#productTitle').getText()
# name=name.strip()
# # print(name)

# price = soup.select_one(selector='.a-offscreen').getText()
# price=float(price[1:])
# # print(price)

def get_link_data(url):
    headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language":"en",
}
    r=requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'lxml')

    name = soup.select_one(selector='#productTitle').getText()
    name=name.strip()

    price = soup.select_one(selector='.a-offscreen').getText()
    price=price.replace(",","")
    price=float(price[1:])

    return name,price

print(get_link_data(url))
