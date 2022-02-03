"""
Converts a PolkaDot staking extract to a TaxBit file
"""
import pandas as pd
import  tkinter as tk
from tkinter import filedialog

# should support any given input for TaxBit

# ui for picking file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# bring in sheet
#FILE = "polkadot.csv"
df = pd.read_csv(file_path,names=['Blockchain Transaction Hash','Date and Time','Received Quantity'],\
engine='pyarrow',skiprows=1)
print(df)

df.insert(2,"Receiving Currency",'DOT',False)
df.insert(2,"Receiving Destination",'Polkadot Wallet',False)
df.insert(3,"Fee",'',False)
df.insert(4,"Fee Currency",'',False)
df.insert(5,"Exchange Transaction ID",'',False)

## insert  the between columns
df.insert(1,"Sending Source",'',False)
df.insert(1,"Sent Currency",'',False)
df.insert(1,"Sent Quantity",'',False)
df.insert(1,"Transaction Type",'Income',False)

# change the order
df = df.reindex(columns=['Date and Time','Transaction Type','Sent Quantity','Sent Currency',
'Sending Source','Received Quantity',"Received Currency",'Receiving Destination','Fee','Fee Currency',
'Exchange Transaction ID','Blockchain Transaction Hash'])
print(df)
#save out
df.to_csv("polkadot_taxbit.csv", index=False)
