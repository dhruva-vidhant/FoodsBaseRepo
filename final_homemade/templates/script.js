function add_item() {
  var food_name = document.getElementById("food_name").value
  var description = document.getElementById("description").value
  var price_cents = document.getElementById("price_cents").value
  var zipcode = document.getElementById("zipcode").value
  var quantity = document.getElementById("quantity").value
  var seller_name = document.getElementById("seller_name").value
  var email = document.getElementById("email").value
  var keywords = "{" + document.getElementById("keywords").value.split("\n") + "}"
  var ingredients = '{' + document.getElementById("ingredients").value.split("\n") +'}'
  var address = document.getElementById("address").value

  var http = new XMLHttpRequest()
  http.open("GET", "http://127.0.0.1:5000/"+food_name+"/"+description+"/"+price_cents+"/"+zipcode+"/"+quantity+"/"+seller_name+"/"+email+"/"+keywords+"/"+ingredients+"/"+address, false)
  http.send(null)
}

function add_order() {
var buyers_email = document.getElementById("buyers_email").value
var comments = document.getElementById("comments").value
var quantity = document.getElementById("quantity").value
var http = new XMLHttpRequest()

http.open("GET", "http://127.0.0.1:5000/"+buyers_email+"/"+comments+"/"+quantity, false)
http.send(null)
}

function searchByKeyword(keyword) {
var http = new XMLHttpRequest()
http.open("GET", "http://127.0.0.1:5000/" + "/keyword/"+ keyword, false)
http.send(null)
//console.log(http.responseText)
return http.responseText
}

function searchByTitle(title) {
var http = new XMLHttpRequest()
http.open("GET","http://127.0.0.1:5000/" + "/title/"+ title, false)
http.send(null)
return http.responseText
}

function search() {
const key = document.getElementById('key').value
console.log(key)
const keyword_matches = eval(searchByKeyword(key))
const title_matches = eval(searchByTitle(key))
console.log(keyword_matches)
document.write(`<Div Id="Search-Container">
      <input id='key' type="text" placeholder="Search for an item in your area...">
      <Button Id="Search" onclick="search()">Search</Button>
    </Div>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/buyers_styles.css') }}">`)
keyword_matches.forEach(match => {
  display(match)
  document.write("<hr class='solid'>")
});
title_matches.forEach (match => {
  display(match)
  document.write("<hr class='solid'>")
});
}

function display(result) {
let list = eval(result)
document.write(`<div class="items">`)
document.write(`<p id='name2'>Name: ${list[1]}</p>`)
document.write(`<p id='keywords'> Keywords: ${list[8]} </p>`)
document.write(`<a href = 'food_page/${list[0]}'> See More </a>`)
document.write(`</div>`)
}


/*document.write(`<p id='description'>Description: ${list[2]} </p>`)
document.write(`<div id='price_cents>Price: ${list[3]}</div>`)
document.write(`<div id='zipcode'>Zipcode: ${list[4]}</div>`)
document.write(`<div id="quantity"> Quanity Avaibible: ${list[5]}</div>`)
document.write(`<div id='seller_name'> Seller: ${list[6]} </div>`)
document.write(`<div id='email'> Seller's Email: ${list[7]} </div>`)
document.write(`<p id='ingredients'> Ingredients: ${list[9]} </p>`)
document.write(`<div id='address'>Address ${list[10]} </div>`)*/

