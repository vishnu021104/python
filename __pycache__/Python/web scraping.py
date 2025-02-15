#import section
import requests
import pandas
from bs4 import BeautifulSoup



response=requests.get("https://www.flipkart.com/realme-c63-5g-charger-box-forest-green-128-gb/p/itm10b8f5cccfadd?pid=MOBH3DZQ3GCQEYUC&lid=LSTMOBH3DZQ3GCQEYUCLNXQPP&marketplace=FLIPKART&fm=productRecommendation%2Fsimilar&iid=R%3As%3Bp%3AMOBH3YKQT2HEAPAM%3Bl%3ALSTMOBH3YKQT2HEAPAMKGOCTP%3Bpt%3App%3Buid%3A921f53fc-6545-11ef-95c8-c14387bbff1d%3B.MOBH3DZQ3GCQEYUC&ppt=pp&ppn=pp&ssid=lt942s38xs0000001724853402001&otracker=pp_reco_Similar%2BProducts_1_36.productCard.PMU_HORIZONTAL_realme%2BC63%2B5G%2BCharger%2Bin%2Bthe%2BBox%2B%2528Forest%2BGreen%252C%2B128%2BGB%2529_MOBH3DZQ3GCQEYUC_productRecommendation%2Fsimilar_0&otracker1=pp_reco_PINNED_productRecommendation%2Fsimilar_Similar%2BProducts_GRID_productCard_cc_1_NA_view-all&cid=MOBH3DZQ3GCQEYUC")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('span',class_='_VU-ZEz')
name=[]
for i in names[0:5]:
    d=i.get_text()
    name.append(d)
print(name) 
  
 




