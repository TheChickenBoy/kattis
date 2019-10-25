n = int(input())
books=l=temp= []
for i in range(0,n):
    books.append(int(input()))
books = sorted(books, reverse=True)

tot = x = 0
while x+2 < n:
    tot += books[x] + books[x+1]
    x+=3
while x < n:
    tot+=books[x]
    x+=1
print(tot)
