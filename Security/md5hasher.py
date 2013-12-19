import os
import md5
import sys

fsize = os.path.getsize(sys.argv[1])
bytesRead = 0


fh = open(sys.argv[1],"rb")

m = md5.new()
while True:
    buffer = fh.read(1024*1024)

    if len(buffer) == 0:
        break

    bytesRead += len(buffer)

    m.update(buffer)
    p = (float(bytesRead)/fsize) * 100
    sys.stderr.write("%3.2f%%\r" % p)
    sys.stderr.flush()

fh.close()

print m.hexdigest()