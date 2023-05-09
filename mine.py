import requests
import pandas as pd
import time
import datetime

#우선 데이터를 모은다. 첫시행에만 헤더를 기록하게 하고 나머지는 데이터만 기록되게 하였다

i=0
while(1):
    try:
      res = requests.get('https://api.bithumb.com/public/orderbook/BTC_KRW/?count=5')
    except:
       print("exception occured")
 

    reso = res.json()

    fil = reso['data']



    bids = (pd.DataFrame(fil['bids'])).apply(pd.to_numeric,errors='ignore')
    bids.sort_values('price',ascending=False, inplace=True)
    bids['type']=0

    asks = (pd.DataFrame(fil['asks'])).apply(pd.to_numeric,errors='ignore')
    asks.sort_values('price',ascending=True, inplace=True)
    asks['type']=1
    asks.reset_index(inplace=True,drop=True)
    total=pd.concat([bids,asks])

    tim= datetime.datetime.now()
    req_time= tim.strftime('%Y-%m-%d %H:%M:%S')


    rowlist = {}
    total['timestamp'] = req_time
    print(total)
    if i==0:
      rowlist = total.to_csv('minering1.csv',index=False,header=True,mode='w',sep='|')
    else:
      rowlist = total.to_csv('minering1.csv',index=False,header=False,mode='a',sep='|')
      
    i+=1
    time.sleep(1)