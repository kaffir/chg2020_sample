import jwt

# JWT Example
secret = "secret1234567890" # real_secret "Ayyv5NekhSPJ7zTMSUccmk5Eq5uR8Pne"
# Encode JWT
encoded = jwt.encode({'some': 'payload', 'foo': 'bar'}, secret, algorithm='HS256')
print(encoded)

# Decode JWT
decoded = jwt.decode(encoded, secret, algorithms=['HS256'])
print(decoded)