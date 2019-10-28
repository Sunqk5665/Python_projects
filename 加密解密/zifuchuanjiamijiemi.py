# 字符串加密解密
def crypt(source, key):
    from itertools import cycle
    result = ''
    temp = cycle(key)
    for ch in source:
        result = result + chr(ord(ch) ^ ord(next(temp)))  # 异或结构实现加密解密
    return result


source = 'shangdong Institute of Business and Technology'
key = 'Dong Fuguo'

print('Before Encrypted:' + source)

encrypted = crypt(source, key)
print('After Encrypted:' + encrypted)
decrypted = crypt(encrypted, key)
print('After Decrypted:' + decrypted)