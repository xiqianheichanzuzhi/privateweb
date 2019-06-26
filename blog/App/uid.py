import uuid
SAFEHASH = [x for x in "0123456789-abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

def RandomPickName(name):
    namespace = uuid.NAMESPACE_URL
    row = str(uuid.uuid5(namespace,name)).replace('-', '')
    safe_code = ''
    for i in range(10):
        enbin = "%012d" % int(bin(int(row[i * 3] + row[i * 3 + 1] + row[i * 3 + 2], 16))[2:], 10)
        safe_code += (SAFEHASH[int(enbin[0:6], 2)] + SAFEHASH[int(enbin[6:12], 2)])
    return safe_code

