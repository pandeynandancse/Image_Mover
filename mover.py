import os
import shutil
import pandas as pd
# Move a file from the directory d1 to d2

print("=============================================================")
print("creating folders and strating copying")
train = pd.read_csv("train.csv")
i=0
for i in range(len(train)):
	path = f"./{train.iloc[i]['target']}"
	try:

		if ( not os.path.isfile(path)  ):
			os.mkdir(path)
	except:
		pass
	image = train.iloc[i]["Image"]
	#move,copy
	shutil.copy(f'./train/{image}', f"./{train.iloc[i]['target']}/")
if(i == len(train) - 1):
	print("*************************")
	print("Successfull")
else : 
	print("--------------------------------")
	print("Unsuccessful")