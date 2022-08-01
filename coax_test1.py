mport hashlib
s = "Python Bootcamp"

# MD5 самый простой, но в тоже время самый незащищенный тип хеширования
hash_md5_object = hashlib.md5(b'Python Bootcamp')
hash1_object = hashlib.md5(s.encode())
print("MD5:", hash1_object.hexdigest())
# SHA1 защищен незначительно лучше, чем MD5 за счет большего количества символов
hash2_object = hashlib.sha1(s.encode())
print("SHA1:",hash2_object.hexdigest())

# SHA 256 - этим видом хэширования пользуется Биткоин
hash3_object = hashlib.sha256(s.encode())
print("SHA256:",hash3_object.hexdigest())
# SHA-3 / Keccak является одним из самых безопасных и эффективных алгоритмов хеширования.
hash4_object = hashlib.sha384(s.encode())
hex_dig = hash4_object.hexdigest()
print("SHA3:",hex_dig)