# from importlib.metadata import files
import pandas as pd

f = open("pandas1.txt", "r")
x=f.read()
val=x.split("LOAD")
# print(val)

tableName=val[0]
###Table Name
# print("table name:",tableName)
val.pop(0)

## Field names seperate
newlist=val[0].split("\n\n ")
field=newlist[0].strip("LOAD \n\n")
x=field.split(',')
# print(x)
x1=len(x)



#location seperate
newlist1=newlist[-1].split("\n ")
y=newlist1[0]
## Path Source
# print("PATH of Source:",newlist1[0])
tb=[]
ps=[]
for i in range (x1):
  ps.append(y)
  tb.append(tableName)
# print(tb)
# print(ps)


data = {
  "field name": x,
    #######
  # "field type": ["x"],
  # #######
  "path of source": ps,
  # #######
  "table name": tb,
}

# #load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 