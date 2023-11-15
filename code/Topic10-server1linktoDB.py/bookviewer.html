<html>
    <head>
        <title> view Books</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
       
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    </head>
    <body>
        <h1>Books</h1>
        <div> <button id="showCreateButton" onclick="showCreate()">Create</button></div>
        <div>
            <table class="table" id="bookTable">
                <tr>
                        <th>id</th>
                        <th>Title</th>
                        <th>
                            Author
                        </th>
                        <th>Price</th>
                        <th>Update</th>
                        <th>Delete</th>
                </tr>
                
            </table>
        </div>
        <div id='createUpdateForm' style="display: none">
                <h2><span id="createLabel">Create a</span> <span id="updateLabel">update</span> Book</h2>
                <input type="hidden" name="id"/>
                Title <input type="text" name="title" /><br/>
                Author <input type="text" name="author"/> <br/>
                Price <input type="number" name="price"/> <br/>
                <span><button id="doCreateButton" onclick="doCreate()">Create</button></span>
                <span><button id="doUpdateButton" onclick="doUpdate()">Update</button></span>
        </div>
    </body>
    <script>
    function showCreate(){
        document.getElementById('showCreateButton').style.display="none"
        document.getElementById('bookTable').style.display="none"
        document.getElementById('createUpdateForm').style.display="block"

        document.getElementById('createLabel').style.display="inline"
        document.getElementById('updateLabel').style.display="none"

        document.getElementById('doCreateButton').style.display="block"
        document.getElementById('doUpdateButton').style.display="none"

    }
    function showViewAll(){
        document.getElementById('showCreateButton').style.display="block"
        document.getElementById('bookTable').style.display="block"
        document.getElementById('createUpdateForm').style.display="none"
    }
    function showUpdate(buttonElement){
        document.getElementById('showCreateButton').style.display="none"
        document.getElementById('bookTable').style.display="none"
        document.getElementById('createUpdateForm').style.display="block"

        document.getElementById('createLabel').style.display="none"
        document.getElementById('updateLabel').style.display="inline"

        document.getElementById('doCreateButton').style.display="none"
        document.getElementById('doUpdateButton').style.display="block"


        var rowElement = buttonElement.parentNode.parentNode
        // these is a way of finding the closest <tr> which would safer, closest()
        
        var book = getBookFromRow(rowElement)
        populateFormWithBook(book)
    }
    function doCreate(){
        var form = document.getElementById('createUpdateForm')

        var book = {}
       
        book.title = form.querySelector('input[name="title"]').value
        book.author = form.querySelector('input[name="author"]').value
        book.price = form.querySelector('input[name="price"]').value
        console.log(JSON.stringify(book))
        createBookAjax(book)
        
        
    }
    function doUpdate(){
        var book = getBookFromForm();
        var rowElement = document.getElementById(book.id);
        updateBookAjax(book);
        setBookInRow(rowElement,book);
       
        clearForm();
        showViewAll();
    }
    function doDelete(r){
        var tableElement = document.getElementById('bookTable');
        var rowElement = r.parentNode.parentNode;
        var index = rowElement.rowIndex;
        deleteBookAjax(rowElement.getAttribute("id"));
        tableElement.deleteRow(index);
    }
    function addBookToTable(book){
        var tableElement = document.getElementById('bookTable')
        var rowElement = tableElement.insertRow(-1)
        rowElement.setAttribute('id',book.id)
        var cell1 = rowElement.insertCell(0);
        cell1.innerHTML = book.id
        var cell2 = rowElement.insertCell(1);
        cell2.innerHTML = book.title
        var cell3 = rowElement.insertCell(2);
        cell3.innerHTML = book.author
        var cell4 = rowElement.insertCell(3);
        cell4.innerHTML = book.price
        var cell5 = rowElement.insertCell(4);
        cell5.innerHTML = '<button onclick="showUpdate(this)">Update</button>'
        var cell6 = rowElement.insertCell(5);
        cell6.innerHTML = '<button onclick=doDelete(this)>delete</button>'

    }

    function clearForm(){
        var form = document.getElementById('createUpdateForm')

        form.querySelector('input[name="title"]').value=''
        form.querySelector('input[name="author"]').value=''
        form.querySelector('input[name="price"]').value=''
    }
    function getBookFromRow(rowElement){
        var car ={}
        book.id  = rowElement.getAttribute('id')
        book.title = rowElement.cells[1].firstChild.textContent
        book.author = rowElement.cells[2].firstChild.textContent
        book.price = parseInt(rowElement.cells[3].firstChild.textContent,10)
        return book
    }
    function setBookInRow(rowElement, book){
        rowElement.cells[0].firstChild.textContent= book.id  
        rowElement.cells[1].firstChild.textContent= book.title 
        rowElement.cells[2].firstChild.textContent= book.author
        rowElement.cells[3].firstChild.textContent= book.price
    }
    function populateFormWithBook(book){
        var form = document.getElementById('createUpdateForm')
        form.querySelector('input[name="id"]').disabled = true

        form.querySelector('input[name="id"]').value  = book.id
        form.querySelector('input[name="title"]').value= book.title
        form.querySelector('input[name="author"]').value= book.author
        form.querySelector('input[name="price"]').value= book.price
        return book
    }
    function getBookFromForm(){
        var form = document.getElementById('createUpdateForm')
        var book = {}
        book.id = form.querySelector('input[name="id"]').value
        book.title = form.querySelector('input[name="title"]').value
        book.author = form.querySelector('input[name="author"]').value
        book.price = parseInt(form.querySelector('input[name="price"]').value,10)
        console.log(JSON.stringify(book))
        return book
    }
    function getAllAjax(){
        $.ajax({
            "url": "http://127.0.0.1:5000/books",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                //console.log(result);
                for (book of result){
                    addBookToTable(book);
                }
                
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }
    function createBookAjax(book){
        //var car = {"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}
        console.log(JSON.stringify(book));
        $.ajax({
            "url": "http://127.0.0.1:5000/books",
            "method":"POST",
            "data":JSON.stringify(book),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                //console.log(result);
                book.id = result.id
                addBookToTable(book)
                clearForm()
                showViewAll()
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    function updateBookAjax(book){
        //var car = {"reg":"12 D 1234","price":8000}
        console.log(JSON.stringify(book));
        $.ajax({
            "url": "http://127.0.0.1:5000/books/"+encodeURI(book.id),
            "method":"PUT",
            "data":JSON.stringify(book),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
               // console.log(result);
                  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    function deleteBookAjax(id){
        
        //console.log(JSON.stringify('deleting '+id));
        $.ajax({
            "url": "http://127.0.0.1:5000/books/"+encodeURI(id),
            "method":"DELETE",
            "data":"",
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                //console.log(result);
                  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    getAllAjax();
  

    
    </script>
</html>