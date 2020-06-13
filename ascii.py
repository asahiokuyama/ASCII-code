# encode
x = input('文字')

# key
KEY = 3

enc = ""

for i in list(x):
    # 1文字取り出してasciiへ変換
    ascii = ord(i)
    # 秘密鍵の生成
    num = ascii - 97
    num = (num + KEY) % 26
    ascii = num + 97
    # 文字に変換
    enc += chr(ascii)

print(enc)


# decode
x = ""

for i in list(enc):
    ascii = ord(i)
    num = ascii - 97
    num = (num-KEY) % 26
    ascii = num + 97
    x += chr(ascii)

print(x);
