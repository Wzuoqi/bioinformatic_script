import os

path = "."
fileList = os.listdir(path)

for i in fileList:
    if i.endswith(".fna"):
        name_list = i.split("_")
        new_name = "GCA_"+i.split("_")[1]+".fa"
        os.rename(i,new_name)
    else:
        continue