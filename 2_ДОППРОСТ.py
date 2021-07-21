kolvo_ch = 0
step = 0
while 2**step <1000:
    step+=1
while 2**step >= 1000 and 2**step<10**10:
    step+=1
    kolvo_ch+=1
    if 2**step<10**10:
        newstep = step
        newkolvo_ch = kolvo_ch
        print(newkolvo_ch, 2**newstep)
print(newkolvo_ch, 2**newstep)
        
