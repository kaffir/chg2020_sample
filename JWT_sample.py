import jwt

# JWT Example
secret = "secret1234567890"
# Encode JWT
encoded = jwt.encode({'some': 'payload', 'foo': 'bar'}, secret, algorithm='HS256')
print(encoded)

# Decode JWT
decoded = jwt.decode(encoded, secret, algorithms=['HS256'])
print(decoded)