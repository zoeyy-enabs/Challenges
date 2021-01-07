#  from Alice
qa = Point(4726, 6287)
# Shared secret exchange 
ss = qa * 6534
print(ss)
shared_secret = 1791
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'
