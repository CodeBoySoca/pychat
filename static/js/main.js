var chatroomID = document.querySelector('chatroom_id')
var ws = new WebSocket(`ws://localhost:8000/chat/${chatroomID}`)
