import sys
import os
import datetime

path=sys.argv[1]
with open(path) as f:
    print("size:"+str(os.path.getsize(path))+"byte")
    print("updated_at:"+str(datetime.datetime.fromtimestamp(os.path.getmtime(path))))
    print("created_at:"+str(datetime.datetime.fromtimestamp(os.path.getctime(path))))
    print(f.read())
