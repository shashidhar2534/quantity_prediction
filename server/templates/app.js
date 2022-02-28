

alert("please wait page is loading")
function onPageLoad() {
  console.log( "document loaded" );
  var url1 = "http://127.0.0.1:5000/get_store_branches";
  var url2="http://127.0.0.1:5000/product";
 
  $.get(url1,function(data, status) {
      console.log("got response for get_store_branches request");
      if(data) {
          var storebranches = data.storebranches;

          var uiStoreBranches = document.getElementById("uiStoreBranches");
          $('#uiStoreBranches').empty();
          for(var i in storebranches) {
              var opt = new Option(storebranches[i]);
              $('#uiStoreBranches').append(opt);
          }

      }
  });
   $.get(url2,function(data, status) {
      console.log("got response for get_store_branches request");
      if(data) {
          var products = data.products;

          var uiProductName = document.getElementById("uiProductName");
          $('#uiProductName').empty();
          for(var i in products) {
              var opt = new Option(products[i]);
              $('#uiProductName').append(opt);
          }

      }
  });
}

window.onload = onPageLoad;
