function checkpassword(){
    if (document.getElementById("pass1").value != document.getElementById("pass2").value){
      document.getElementById("rpass").innerHTML = "Password Doesn't match"
      document.getElementById("submitButton").disabled = true;
      if(document.getElementById("pass2").value == ""){
        document.getElementById("rpass").innerHTML = ""
      }
  }
  else {
    document.getElementById("submitButton").disabled = false;
    document.getElementById("rpass").innerHTML = ""

  }
  
 
  }