import json as js
import shutil
f_name = "disk.json"
total, used, free = shutil.disk_usage('C:/Users/chere.DESKTOP-KAJEGIS')

disk = {
    "Total" :(total // (2**30)),
    "Used" : (used // (2**30)),
    "Free" : (free // (2**30))
}
with open(f_name, "w") as outfile:
    js.dump(disk, outfile)
with open(f_name, "r") as f:
    data = f.read()
dict_from_file = js.loads(data)
print(dict_from_file)