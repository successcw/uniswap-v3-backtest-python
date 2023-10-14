from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import pandas as pd
import time


def graph(network,Adress,fromdate):

    if network == 1:

        sample_transport=RequestsHTTPTransport(
        url='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3',
        verify=True,
        retries=5,
        )
        client = Client(
        transport=sample_transport
        )


    elif network == 2:
       
        sample_transport=RequestsHTTPTransport(
        url='https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-arbitrum-one',
        verify=True,
        retries=5,
        )
        client = Client(
        transport=sample_transport
        )

    elif network == 3:
        sample_transport=RequestsHTTPTransport(
        url='https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-optimism-dev',
        verify=True,
        retries=5,
        )
        client = Client(
        transport=sample_transport
        )
    print(fromdate)

    query = gql('''
    query ($fromdate: Int!)
    {
    poolHourDatas(where:{pool:"'''+str(Adress)+'''",periodStartUnix_gt:$fromdate},orderBy:periodStartUnix,orderDirection:asc,first:1000)
    {
    periodStartUnix
    liquidity
    high
    low
    pool{
        
        totalValueLockedUSD
        totalValueLockedToken1
        totalValueLockedToken0
        token0
            {decimals
            }
        token1
            {decimals
            }
        }
    close
    feeGrowthGlobal0X128
    feeGrowthGlobal1X128
    }
 
    }
    ''')

    first_run = True
    print("time", time.time())
    while fromdate < time.time():
        print(fromdate)
        print(pd.to_datetime(fromdate,unit='s'))
        params = {
        "fromdate": fromdate
        }
        response = client.execute(query,variable_values=params)
        dpd = pd.json_normalize(response['poolHourDatas'])
        dpd = dpd.astype(float)
        if first_run:
            df = dpd
            first_run = False
        else:
            df = pd.concat([df,dpd], ignore_index=True)
        #print(dpd)
        fromdate = fromdate + 1000*3600

    return df

