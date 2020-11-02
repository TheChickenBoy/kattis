l = input().split()
count = 0
for s in l:
    if 'ae' in s:
        count+=1
print("dae ae ju traeligt va") if count/len(l) >= 0.4 else print("haer talar vi rikssvenska")