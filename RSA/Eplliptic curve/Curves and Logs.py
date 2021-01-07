# Point from Alice
qa = Point(815, 3190)
# Shared secret
ss = qa * 1829
from hashlib import sha1
print(sha1(str(ss.x).encode()).hexdigest())