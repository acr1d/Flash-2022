def summa_cht(x):
    summ = 0
    while x > 0:
        summ += x % 10
        x //= 10
    if summ % 2 !=0:
        return summ
bukvi = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
kolvo_buk = 0
max_ascii_buk = -1
for buk in range(0, len(bukvi)):
    if ord(bukvi[buk]) % 2 == 0 and ord(bukvi[buk]) % 4 != 0:
        if ord(bukvi[buk].lower()) % 2 == 0 and ord(bukvi[buk].lower()) % 4 != 0 and summa_cht(ord(bukvi[buk].lower())):
            kolvo_buk+=1
            max_ascii_buk = max(max_ascii_buk, ord(bukvi[buk]))
print(kolvo_buk,chr(max_ascii_buk))
        
