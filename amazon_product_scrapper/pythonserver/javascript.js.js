console.log('Extension Loaded')
var websiteurl = window.location.href
function passwebsite(){
    console.log('Button Clicked');
    $.ajax(
                    {
                        type:'POST',
                        contentType:'application/json;charset-utf-08',
                        dataType:'json',
                        
                        url:'http://127.0.0.1:5000/pass_val?value='+ websiteurl,
                        success:function (data) {
                            var reply=data.reply;
                            if (reply=="success")
                                {
                                    return;
                                }
                            else
                                {
                                    alert("some error ocured in session agent")
                                }
    
                        }
                    }
                );
}
var container = document.getElementById("nav-tools");
var btn = document.createElement("button");
btn.setAttribute("role","button");
btn.innerText = "Import";
btn.id = "importbtn"
container.appendChild(btn);
btn.addEventListener("click" , passwebsite);
btn.style.border= "none";
btn.style.padding = "16px 12px";
btn.style.color= "white";
btn.style.display= "inline-block";
btn.style.fontSize = "15px";
btn.style.fontWeight = "bold";
btn.style.backgroundColor = "#131921";