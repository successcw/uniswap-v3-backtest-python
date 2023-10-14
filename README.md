# Usage
1. get all history of ETH/USDC 0.05 pull data from Graph
```PYTHON
python csv_read.py
```
This will generate file qgl.csv

2. LP caculation
For example, an LP is started on 2023-08-01 and ended on 2023-10-01, the current price is 1874 and targe value is 1000
```PYTHON
python Backtest.py '2023-08-01' '2023-10-01' 1874
```