import pandas as pd
import numpy as np

df=pd.DataFrame(data=np.arange(0,50).reshape(5,10), index=["Row 1","Row 2","Row 3","Row 4", "Row 5"])
print(df)
print("\n for head")
print(df.head(1))
print("\n for bottom")
print(df.tail(2))
