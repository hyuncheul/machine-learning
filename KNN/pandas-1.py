import numpy as np
import pandas as pd

values = [500, 800, 200]
index = ["메로나","누가바","빠삐코"]

s = pd.Series(values,index)


s.loc["바밤바"] = 400
s.iloc[3] = 600
s1 = s+100

저가 = pd.Series([10,200,200,400,600])
고가 = pd.Series([100,300,400,500,600])
제약조건 = (고가 - 저가)>= 100
#print(고가[제약조건])

종가 = pd.Series([93000,82400,99100,81000,72300],['05/14','05/15','05/16','05/17','05/18'])
제약조건2 = (80000<= 종가) & (종가 < 90000)
#print(종가[제약조건2].index)


index = ["비트코인","리플","이더리움"]
colum = ["시가","고가","저가","종가"]
data = [[980,990,920,930],[200,300,180,180],[300,500,300,400]]

result = pd.DataFrame(data, index, colum)
#print(result["시가"])
