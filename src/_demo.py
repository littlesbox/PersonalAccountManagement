import pandas as pd

a = {
    "col1":[1],
    "col2":[2],
    "col3":[3]
}

df = pd.DataFrame(a)

b={'1c':'1','2':'2','3':'3'}
for k,v in b.items():
    print(k,v)