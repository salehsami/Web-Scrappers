# import requests
# # r = requests.get('http://google.com')
# # we get 200 coz requests approve and we can access the website data
# # print(r.status_code)
# # print(r.request.headers)  # this is the headerthat is passed with the request
# # r = requests.get('https://www.amazon.com/Where-Crawdads-Sing-Delia-Owens/dp/0735219109/ref=zg_sccl_2/139-2375612-6019031?pd_rd_w=EIax8&content-id=amzn1.sym.193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_p=193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_r=4NCAZZTCZZ6NWPFYPNRN&pd_rd_wg=FvFQy&pd_rd_r=6649b81b-c338-4e53-8356-b39f4ed0ed56&pd_rd_i=0735219109&psc=1')
# # print(r.status_code) # it is 503 coz amazon thinks an automated service or a bot is accessing their resources so it blocks the request
# # print(r.text) # this wil show all the tags of the page but we couldn't crawl the page beacoz o the bot restrictions
# # but if we change the user agent than we can access it coz then it wont think about the bot
# # so
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
# r = requests.get('https://www.amazon.com/Where-Crawdads-Sing-Delia-Owens/dp/0735219109/ref=zg_sccl_2/139-2375612-6019031?pd_rd_w=EIax8&content-id=amzn1.sym.193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_p=193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_r=4NCAZZTCZZ6NWPFYPNRN&pd_rd_wg=FvFQy&pd_rd_r=6649b81b-c338-4e53-8356-b39f4ed0ed56&pd_rd_i=0735219109&psc=1', headers=headers)
# # know we can access it so thast it for the user agent we can get more user agents from the url mentioned in readme file
# print(r.status_code)

# know if we use this concept while runnig a program lets see what happens

import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Where-Crawdads-Sing-Delia-Owens/dp/0735219109/ref=zg_sccl_2/139-2375612-6019031?pd_rd_w=EIax8&content-id=amzn1.sym.193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_p=193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_r=4NCAZZTCZZ6NWPFYPNRN&pd_rd_wg=FvFQy&pd_rd_r=6649b81b-c338-4e53-8356-b39f4ed0ed56&pd_rd_i=0735219109&psc=1'


headerss = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}

r = requests.get(url, headers=headerss)

soup = BeautifulSoup(r.content, features="lxml")

title = soup.find('span', {'id': 'productTitle'}).text

print(title)
