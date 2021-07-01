import hashlib
import zlib
from Crypto.Hash import *

def banner():
   print("""
 _   _           _       _____       _            _       _      Made By Shaheer          
| | | |         | |     /  __ \     | |          | |     | |     Github: https://github.com/Shaheertura       
| |_| | __ _ ___| |__   | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
|  _  |/ _` / __| '_ \  | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| | | | (_| \__ \ | | | | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
\_| |_/\__,_|___/_| |_|  \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                        
                                                                        


      """)
banner()

text = input("Enter a String: ")
cop1 = text
def md2():
   print()
   h = MD2.new()
   h.update(text)
   print("MD2:",h.hexdigest())

def md4():
   h = MD4.new()
   h.update(text)
   print("MD4:",h.hexdigest())


def md5():
   hash_object = hashlib.md5(text.encode())
   hash = hash_object.hexdigest()
   print("MD5:",hash)

def sha1():
   encoded=text.encode()
   result = hashlib.sha1(encoded)
   print("SHA1:",result.hexdigest())

def sha224():
   encoded=text.encode()
   result = hashlib.sha224(encoded)
   print("SHA224:",result.hexdigest())

def sha256():
   encoded=text.encode()
   result = hashlib.sha256(encoded)
   print("SHA256:",result.hexdigest())

def sha384():
   encoded=text.encode()
   result = hashlib.sha384(encoded)
   print("SHA384:",result.hexdigest())

def sha512():
   encoded=text.encode()
   result = hashlib.sha512(encoded)
   print("SHA512:",result.hexdigest())

def ripemd160():
   encoded = text.encode()
   x = encoded
   x = hashlib.new('ripemd160')
   print("RIPEMD160:",x.hexdigest())

def crc32():
   encoded = text.encode()
   result = zlib.crc32(encoded)
   print("CRC32:",result)

def adler32():
   encoded = text.encode()
   result = zlib.adler32(encoded)
   print("ADLER32:",result)

def des():
   from passlib.hash import des_crypt
   hash = des_crypt.hash(text)
   print("DES Crypt:",hash)

def bsdicrypt():
   from passlib.hash import bsdi_crypt
   hash = bsdi_crypt.hash(text)
   print("BSDI Crypt:",hash)

def bigcrypt():
   from passlib.hash import bigcrypt
   hash = bigcrypt.hash(text)
   print("BIGCrypt:",hash)

def crypt16():
   from passlib.hash import crypt16
   hash = crypt16.hash(text)
   print("Crypt16:",hash)

def md5crypt():
    from passlib.hash import md5_crypt as mc
    hash = mc.hash(text)
    print ("MD5 Crypt:",hash)

def sha1crypt():
    from passlib.hash import sha1_crypt as mc
    hash = mc.hash(text)
    print("SHA-1 Crypt:",hash)

def sha256crypt():
    from passlib.hash import sha256_crypt as mc
    hash = mc.hash(text)
    print ("SHA-256 Crypt:",hash)

def sha512crypt():
    from passlib.hash import sha512_crypt as mc
    hash = mc.hash(text)
    print ("SHA-512 Crypt:",hash)

def sunmd5():
    from passlib.hash import sun_md5_crypt as mc
    hash = mc.hash(text)
    print("Sun MD5 Crypt:",hash)

def apachemd5crypt():
    from passlib.hash import apr_md5_crypt as mc
    hash = mc.hash(text)
    print("Apache's MD5 Crypt:",hash)

def phpass():
    from passlib.hash import phpass as mc
    hash = mc.hash(text)
    print("PHPass Portable Hash:",hash)

def ctapbkdf2sha1():
    from passlib.hash import cta_pbkdf2_sha1 as mc
    hash = mc.hash(text)
    print("Cryptacular's PBKDF2 Hash:",hash)

def dlitzpbkdf2sha1():
    from passlib.hash import dlitz_pbkdf2_sha1 as mc
    hash = mc.hash(text)
    print("Dwayne Litzenberger’s PBKDF2 Hash:",hash)

def apbkdf2sha1():
    from passlib.hash import cta_pbkdf2_sha1 as mc
    hash = mc.hash(text)
    print("Atlassian’s PBKDF2 Hash:",hash)

def scram():
    from passlib.hash import scram as mc
    hash = mc.hash(text)
    print("SCRAM Hash:",hash)

def bsdnthash():
    from passlib.hash import bsd_nthash as mc
    hash = mc.hash(text)
    print("FreeBSD  nthash:",hash)

def mysql323():
   from passlib.hash import mysql323
   hash=mysql323.hash(text)
   print("MySQL 3.2.3:",hash)

def mysql41():
   from passlib.hash import mysql41
   hash=mysql41.hash(text)
   print("MySQL 4.1:",hash)

def mssql2000():
    from passlib.hash import  mssql2000 as m20
    h = m20.hash(text)
    print("MSSQL 2000:",h)

def mssql2005():
    from passlib.hash import  mssql2005 as m25
    h = m25.hash(text)
    print("MSSQL 2005:",h)

def oracle11():
   from passlib.hash import  oracle11 as m25
   h = m25.hash(text)
   print ("Oracle 11g password Hash",h)

def lmhash():
    from passlib.hash import  lmhash as m25
    h = m25.hash(text)
    print ("LanManager Hash:",h)

def nthash():
    from passlib.hash import  nthash as m25
    h = m25.hash(text)
    print ("Windows NT-Hash:",h)

def cisco():
    from passlib.hash import  cisco_type7 as m25
    h = m25.hash(text)
    print ("Cisco Type 7 Hash:",h)

def djangopsha1():
    from passlib.hash import  django_pbkdf2_sha1  as m25
    h = m25.hash(text)
    print ("Django PBKDF2-HMAC-SHA1:",h)
def djangopsha256():
    from passlib.hash import  django_pbkdf2_sha256  as m25
    h = m25.hash(text)
    print("Django PBKDF2-HMAC-SHA256:",h)
def grubpsha512():
    from passlib.hash import  grub_pbkdf2_sha512  as m25
    h = m25.hash(text)
    print ("Grub's PBKDF2 Hash:",h)

def fshp():
    from passlib.hash import  fshp  as m25
    h = m25.hash(text)
    print("Fairly Secure Hashed Password:",h)




md2()
md4()
md5()
sha1()
sha224()
sha256()
sha384()
sha512()
ripemd160()
crc32()
adler32()
des()
bsdicrypt()
bigcrypt()
crypt16()
md5crypt()
sha1crypt()
sha256crypt()
sha512crypt()
sunmd5()
apachemd5crypt()
phpass()
ctapbkdf2sha1()
dlitzpbkdf2sha1()
apbkdf2sha1()
scram()
bsdnthash()
mysql323()
mysql41()
mssql2000()
mssql2005()
oracle11()
lmhash()
nthash()
cisco()
djangopsha1()
djangopsha256()
grubpsha512()
fshp()
