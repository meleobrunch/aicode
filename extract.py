import pandas as pd
# header를 추가해준다 이걸로 완전한 파일을 얻었다
df = pd.read_csv('FirDay.csv', header=None,sep='|', names=['price', 'quantity', 'type', 'timestamp'])
df.to_csv('2023-04-29-exchange-market-orderbook.csv',sep='|', index=False,header=True)

sec_df = pd.read_csv('SecDay.csv', header=None,sep='|', names=['price', 'quantity', 'type', 'timestamp'])
sec_df.to_csv('2023-04-30-exchange-market-orderbook.csv',sep='|', index=False,header=True)
