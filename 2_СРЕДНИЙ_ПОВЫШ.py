a = [ch1 for ch1 in range(30000, 50001)]
b = [ch2 for ch2 in range(100001, 130002)]
kolvo_par = 0
maxsum = 0
if len(b) >= len(a):
    newb = [ch3 for ch3 in range(b[0], b[len(b) - 1] - (len(b) - len(a) - 1))]
    for i in range(0, len(newb)):
        if (newb[i] + a[i]) % 7 == 0 and newb[i] % 3 != 0 and newb[i] % 5 == 0 and a[i] % 3 == 0 and a[i] % 4 != 0 and a[i] % 6 != 0:
            kolvo_par+=1
            maxsum = max(maxsum, newb[i] + a[i])
print(kolvo_par, maxsum)
