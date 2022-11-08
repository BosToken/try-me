from Crypto.Util.number import *
from secret import *

def enkripsi(flag, e, q):
    cipherText = (flag ** e) % q
    return long_to_bytes(cipherText)

def maybeYouNeedSomeLeak(p, q, d, n):
    leak = pow(p, d, (n % ((p * q) ** 2)))
    return long_to_bytes(leak)

flag = bytes_to_long(secret)
e = 0x10001
p = getPrime(516)
q = getPrime(516)
n = p * q 
phi = (p - 1) * (q - 1)
d = inverse(e , phi)

print("Cipher = ", enkripsi(flag, e, q), "\nn = ", long_to_bytes(n), "\nLeak = ", maybeYouNeedSomeLeak(p, q, d, n))