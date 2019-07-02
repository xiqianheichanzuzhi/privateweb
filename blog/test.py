import hashlib

a = 'chenchong'

m2 = hashlib.md5()
m2.update(a.encode())
print(m2.hexdigest())
print(a)