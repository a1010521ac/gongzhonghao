import sys, base64
b = base64.b64decode(sys.argv[1].encode('ascii'))
with open(sys.argv[2], 'wb') as f:
    f.write(b)
print('written', len(b), sys.argv[2])
