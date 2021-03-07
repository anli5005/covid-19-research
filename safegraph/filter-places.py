import pandas as pd

print("key,type")
places = pd.read_csv("places.csv", index_col=0, names=["","bb","code","key"])
for index, row in places.iterrows():
    code = str(row["code"])
    if code.startswith("721"):
        print("%s,0" % row["key"])
    elif code.startswith("722"):
        print("%s,1" % row["key"])
    elif code.startswith("44") or code.startswith("45"):
        print("%s,2" % row["key"])
    elif code.startswith("8121"):
        print("%s,3" % row["key"])
    elif code.startswith("71394"):
        print("%s,4" % row["key"])
    elif code.startswith("62"):
        print("%s,5" % row["key"])
