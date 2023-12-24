$(document).ready(function(){
    $('#action_menu_btn').click(function(){
        $('.action_menu').toggle();
    });
        });

console.log('hhhhhhhhhh',sender)



//ajax for chat

function get_chat(user_id){
    console.log(user_id)
    $.ajax({
        url:'/chat/'+ user_id,
        type:'POST',
        
        success:function(response){
    
            var chat_box = $(response).find('#chat_box').html()
            var action_menu = $(response).find('#action_menu').html()
            var action_ul = $(response).find('#action_ul').html()
            var socket_msg = $(response).find('#message_content').html()
            $('#chat_box').html(chat_box)
            $('#action_menu').html(action_menu)
            $('#action_ul').html(action_ul)
            $('#message_content').html(socket_msg)
            
        }
    })
    
}
function sendMessage(user_id,receciver_room){
    console.log("rec",receciver_room)
    if(document.getElementById("message").value){
        let message = document.getElementById("message").value
        console.log(message,receciver_room)
        socket.send({message,sender,receciver_room,time})
        // user_id = document.getElementById("message").dataset.userId;
        console.log(user_id)
        // $.ajax({
        //     url:'/save_messages',
        //     type:'POST',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     data:JSON.stringify({
        //         message:message,
        //         userId:user_id
        //     }),
        //    success:function(){
        //         console.log("hello")
        //     }
        // })
    }document.getElementById("message").value ="";
}

//socket connect

const socket = io();
const time = new Date();

socket.on('message',function(data){
    createMessage(data.message,data.from,data.to,data.time);
})
const message_content  = document.getElementById("mm");


console.log("man",message_content)
const createMessage = (msg,from,to,time)=>{
    const reciver_room = document.getElementById("receiver").dataset['receiver_room']
    console.log("rec room",reciver_room)
    console.log(msg,from,to,time)
    var isOwner = sender === from;
    if ((from == sender && to == reciver_room)||(from == reciver_room && to == sender)){
        msg_content = isOwner ? `<div class="d-flex justify-content-end mb-4">
        <div class="msg_cotainer_send">
            ${msg}
            <span class="msg_time_send">${time}</span>
        </div>
        <div></div>
        <div class="img_cont_msg">

        </div>
    </div>` : `
    <div class="d-flex justify-content-start mb-4">
								<div class="img_cont_msg">
									<img src="https://static.turbosquid.com/Preview/001292/481/WV/_D.jpg" class="rounded-circle user_img_msg">
								</div>
								<div class="msg_cotainer">
									${msg}
									<span class="msg_time"${time}</span>
								</div>
							</div>
    `

    console.log(msg_content)
    $("#socket_message").append(msg_content);
    }
}
document.addEventListener("DOMContentLoaded", function() {
    var container = document.querySelector("#my_mesage");
  
    if (container) {
      container.scrollTop = container.scrollHeight;
    } 
  });
  