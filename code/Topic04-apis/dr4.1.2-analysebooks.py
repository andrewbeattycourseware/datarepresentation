from bookapidao import getAllBooks

books = getAllBooks()
total = 0
count = 0
for book in books:
    total += book["Price"]
    count += 1

print ("average of ", count, "books is ", total/count )