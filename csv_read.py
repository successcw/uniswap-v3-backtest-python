import pandas as pd
import GraphBacktest

df = pd.read_csv('eth.csv', parse_dates=['日期'])

def calc_average():
    selected_rows = df[(df['日期'] <= '2023-10-08') & (df['日期'] >= '2023-09-08')]

    print(selected_rows)

    # 将带有K和M的数值转换为常规数字
    numeric_values = []

    for value in selected_rows['交易量']:
        if 'K' in value:
            numeric_value = float(value.replace('K', '')) * 1000
        elif 'M' in value:
            numeric_value = float(value.replace('M', '')) * 1000000
        else:
            numeric_value = float(value)
        
        numeric_values.append(numeric_value)

    # 计算平均值
    average = sum(numeric_values) / len(numeric_values)

    # 打印平均值
    print("平均值：", average)

def calc_each_month():
    for i,row in df.iterrows():
        if df['日期'].iloc[i].day == 1:
            #print(df['日期'].iloc[i].strftime('%Y-%m-%d'))
            print(df['收盘'].iloc[i])
            float_value = float(df['收盘'].iloc[i].replace(',', ''))
            #print("{:.3f}".format(1000/float_value))


def show_unix_timestamp():
    for i,row in df.iterrows():
        if df['日期'].iloc[i].day == 1:
            print(int(df['日期'].iloc[i].timestamp()))

def get_gql():
    Adress = "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640" # ETH USDC Ethereum
    network = 1
    startfrom = 1622505600 #2021-6-1
    dpd = GraphBacktest.graph(network,Adress,startfrom)
    #print(dpd)
    datetime = pd.to_datetime(dpd['periodStartUnix'], unit='s')
    dpd.insert(loc=dpd.columns.get_loc('liquidity'), column='datetime', value=datetime)
    dpd.to_csv('gql.csv', index=False)

#calc_each_month()
#show_unix_timestamp()
get_gql()
