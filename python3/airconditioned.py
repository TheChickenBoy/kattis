# d={
#     UpperLimit: n
# }
#
# om l är mindre än någon tidigares u -> öka det rummet? Behövs ej
# 
#
intervals=[]
for _ in range(int(input())):
    intervals.append(list(map(int, input().split())))
intervals.sort(key=lambda i: (i[0], -i[1]))
#print(intervals)

res = [intervals[0]]
for l,r in intervals[1:]:
    prevL, prevR = res[-1]
    if prevR >= l:# and prevR >= r:
        continue
    res.append([l,r])
print(len(res))



# # c_h = l[0][1]
# # for e in l[1:]:
# #     if e[0] > c_h:
# #         c_h = e[1]
# #         i+=1
# # print(i)




# n = int(input())
# l,u = map(int, input().split())
# nr_r = [u]
# for _ in range(n-1):
#     l,u = map(int, input().split())
#     if not any(x>=l for x in nr_r):
#         #print()
#         nr_r.append(u)
# print(len(nr_r))

# intervals.sort(ket=lambda i: (i[0], -i[1]))
# 
