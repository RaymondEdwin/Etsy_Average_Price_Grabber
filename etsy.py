import requests as req
from bs4 import BeautifulSoup as bs
import time
def Price_info():
  x=1
  Url=str(input("Term of interest: "))
  No=int(input("How many pages(12 results per page grabbed): "))
  Url=(Url.replace(" ","+"))
  Query=("https://www.etsy.com/uk/search?q="+Url+"&page="+str(x))
  print(Query)
  price_list=str()
  Title_list=str()
  for i in range (0,No):
    
    useragentid = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
   }
    r=req.get(Query,headers=useragentid)
    statusCode=r.status_code
    if r.status_code == 200:
        print("Grabbed page, "+str(x))
    else:
        print("Bad Headers")
    soup=bs(r.content,"html.parser")
    x=x+1
    boup=(soup.prettify())
    Info_on_price=str((soup.find_all("span","currency-value")))
    price_list=price_list+Info_on_price
    Info_on_title=str(soup.find_all("h3","""wt-mb-xs-0 wt-text-truncate wt-text-caption v2-listing-card__title"""))
    Title_list=Title_list+Info_on_title


  price_list=str(price_list)
  price_list=price_list.replace("""[<span class="currency-value">""","")
  price_list=price_list.replace("""</span>, <span class="currency-value">""","--")
  price_list=price_list.replace("""</span>]""","")
  price_list=price_list.split("--")
    # Close the file
  lenggth=(len(price_list))
  print(lenggth," data points")
  cleaning=int(0)
  length_of_lists=len(price_list)
  count1=0
  cleanedlists=[]
  uncleaned_lists=[]
  for i in range (length_of_lists):
    place=str(price_list[count1]).count(".")
    if place ==1:
      gong=(price_list[count1])
      cleanedlists.append(float(price_list[count1]))
      count1=count1+1
    else:
      count1=count1+1
  print(cleanedlists)
  average=sum(cleanedlists)/len(cleanedlists)
  print( "\n Average price is, £",average)


Price_info()