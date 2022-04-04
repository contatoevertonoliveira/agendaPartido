verificaInt = function(){
  var verifyInt = /\d+/g;
  if ($("#nomeC").val().match(verifyInt) != null) {
      alert("A input Nome contém caracteres numéricos!");
  }
}