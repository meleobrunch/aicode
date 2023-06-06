import pandas as pd

from calMid import cal_mid_price
from calBookI import live_cal_book_i_v1
from calBookD import live_cal_book_d_v1
from calBookD import get_diff_count_units

i=0
j=0
com=0
para=[0.2,5,1]
para2=[0.1,5,1]
val={'_flag': 0,'prevBidQty': 0,'prevAskQty': 0,'prevBidTop': 0,'prevAskTop': 0,
     'bidSideCount': 0,'askSideCount': 0,'bidSideAdd': 0,'bidSideDelete': 0,'askSideAdd': 0,'askSideDelete': 0,'bidSideTrade': 0,
     'askSideTrade': 0,'bidSideFlip': 0,'askSideFlip': 0}
#None을 쓰면 안되는게 일단 정수형이여 하니까 None은 연산이 안돼 0으로 넣자 일단

conse=pd.DataFrame(columns=['book-delta-v1-0.1-5-1','book-delta-v1-0.2-5-1','book-imbalance-0.1-5-1','book-imbalance-0.2-5-1','mid_price','timestamp'])
df = pd.read_csv('2023-05-10-upbit-BTC-book.csv')
tra = pd.read_csv('2023-05-10-upbit-BTC-trade.csv')

#다음 코드가 작동하는 것은 timestamp의 개수가 동일하기 때문이다 중복을 제외하면

    #bid, ask값 가져오기
for start in range(0, len(df)-29,30):
    bid = df[start:start+15] 
    ask = df[start+15:start+30]
    #이건 10줄을 꺼내는 방식 10줄 = 1줄혹은 2줄?????? 
    
    
    #diff거래내역 받아오기  
        

    if(i==len(tra)-1):
        dar= tra[i:i+1]
        
    else:
        if (tra.loc[i, 'timestamp'] == tra.loc[i+1, 'timestamp']):
        
            dar=tra[i:i+2]
            i+=2
       
        else:
            dar= tra[i:i+1]
        i+=1
        #중요한게 tra[i:i+1]은 한줄 tra[i]는 열을 가져오려하는 거다 두줄이라면 알잖아 tra[i:i+2]
    #dar에 임시 저장했고 매순간 초기화되며 될거다 
    
        
    
    
    #매순간 오더북을 불러오면서 거래내역의 diff값을 1개혹은 2개 혹은 0개인 값을 불러와야 한다. 0개는 문제가 되지 않는다 없으면 없다고 알려주니 최소 1개는 준다 
    # 
    # 중요한 건 중복 데이터를 어떻게 처리하는 가 이것이 문제다 groupby는 동시에 처리되지 않는다

    result=cal_mid_price(bid,ask,None) # midprice와 timestamp를 구했다 result[0]와 result[1]이다
    
    #para의 ratio,interval은 임의의 값을 주면 되는가?
    result2=live_cal_book_i_v1(para,bid,ask,None,None,result[0]) #bookimbalance ratio 0.2 interval 5
    result2_1=live_cal_book_i_v1(para2,bid,ask,None,None,result[0]) #ratio 0.1 interval 5
   
    result3=live_cal_book_d_v1(para,bid,ask,get_diff_count_units(dar),val,result)#bookD ratio 0.2 interval 5
    result3_1=live_cal_book_d_v1(para2,bid,ask,get_diff_count_units(dar),val,result)# ratio 0.1 interval 5
    conse.loc[j]=[result3_1,result3,result2_1,result2,result[0],result[1]] #conse에 써주기
    j+=1

print(conse) 
conse.to_csv('2023-05-10-upbit-btc-feature.csv',sep='|', index=False,header=True) #완료~~~
    