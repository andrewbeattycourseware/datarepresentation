
import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()

def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):
    
    response = requests.post(url, json=book)
    #headers ={ "Content-type": "application/json"}
    #response = requests.post(url, data=json.dumps(book), headers=headers)
    
    return response.json()


def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()
    pass

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()
   

if __name__ == "__main__":
    book= {
        'Author':"test",
        'Title':"test title",
        "Price": 123
    }
    bookdiff= {
        "Price": 123
    }
    #print(getAllBooks())
    #print(getBookById(1))
    print (deleteBook(76))
    print (deleteBook(81))
    #print (createBook(book))
    #print (updateBook(1, bookdiff))