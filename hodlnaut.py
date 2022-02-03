"""
Converts a Holdnaut Export to a TaxBit file
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
input_sheet = pd.read_csv(file_path,names=['Date and Time','Delete1','Delete2','Received Quantity'],\
engine='pyarrow',skiprows=1)
print(input_sheet)

#determine the currency type
token_name = input_sheet.iat[0,-1].split(' ')[1]

#remove the bad columns and insert blank columns and the hodlnaut column
df = df.drop(['Delete1','Delete2'], axis=1)

df.insert(2,"Received Currency",token_name,False)
df.insert(3,"Receiving Destination",'Hodlnaut',False)
df.insert(4,"Fee",'',False)
df.insert(5,"Fee Currency",'',False)
df.insert(6,"Exchange Transaction ID",'',False)
df.insert(7,"Blockchain Transaction Hash",'',False)

## insert  the between columns
df.insert(1,"Sending Source",'',False)
df.insert(1,"Sent Currency",'',False)
df.insert(1,"Sent Quantity",'',False)
df.insert(1,"Transaction Type",'Income',False)


#format the date time
df["Date and Time"] = df["Date and Time"].dt.strftime("%Y-%m-%dT%I:%M:%S")

# strip the token
df["Received Quantity"] = df["Received Quantity"].str.replace(' '+token_name,'')
print(df)
#save out
df.to_csv("hn_taxbit.csv", index=False)
