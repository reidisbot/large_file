pi = 3.14
try:
    stuff = open("pi.pi", "r").read()
except:
    pass
    open("pi.pi", "w").close()

import os
filepath = 'pi.pi'
import time
size  = os.path.getsize(filepath)
start = time.time()
while size < 537_000_000:
    with open("pi.pi", "w") as f:
        f.write(str(pi) + stuff + stuff)
    stuff = open("pi.pi", "r").read()
    size  = os.path.getsize(filepath)
    #print (size)
end = time.time()
print(end - start)
