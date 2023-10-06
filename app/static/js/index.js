
var curState = {"bot":"simple"} 

function changeBot(that)
{
    curState["bot"] =that.getAttribute("id")

    var title = that.getAttribute("title")
    var src = that.getAttribute('img')
    var tags = that.getAttribute('tags')
    var description = that.getAttribute('description')

    console.log(src)
    var bot = document.getElementById('bot');
    bot.setAttribute("title", title);
    bot.setAttribute("description", description)
    bot.setAttribute("img", src)
    bot.setAttribute("tags", tags)
 
}


function uuidv4() {
    return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, c =>
      (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
  }
var chatNum = 0
var ChatId = "";
curState["id"] = uuidv4();

const log = (text, className, id, chatNum) => {
    console.log(id)
    console.log(chatNum)

    var ChatId = id+chatNum; 
    console.log(ChatId)
    
    var ChatId2 = ChatId+className;
    
    var div = document.getElementById(ChatId2)
    if(!document.body.contains(document.getElementById(ChatId2)))
    {
        console.log('new ' + ChatId2)
        div = document.createElement('div')
        div.className=className + " rounded-lg  p-4 shadow-xl  w-50 rounded-md"
        div.id = ChatId2
        document.getElementById('log').appendChild(div)
    
    }
    
    div.innerHTML += `<span class="resp  ${className}S"  >${text.replace(/\n/g, "<br>")}</span>`;
    
    
};


    
var cache = new WebSocket('ws://' + location.host + '/socket');
cache.addEventListener('message', ev => {
    res = '['+ ev.data.replaceAll('}{','},{')+']'
    
    datarr = JSON.parse(res)
    
    datarr.forEach(dat => {
        log( dat["token"], 'answer', dat["id"], dat["chatNum"]);
        
    });
});

window.onload = function() {
    // do something when the page loads
  
document.getElementById('form').onsubmit = ev => {
    ev.preventDefault();
    chatNum++;
    const textField = document.getElementById('text');
    id = curState["id"];
    msg = JSON.stringify({"txt":textField.value,"id":id, "chatNum":chatNum})
    cache.send(msg);
    botstate = curState["bot"]
    log( textField.value, 'question', curState["id"],chatNum);
    
    fetch(`http://localhost:5000/${botstate}`, {
    method: "post",
    headers: { "Content-Type": "application/json" },
    body: msg
    })
    .then(resp => {
        if (resp.status === 200) {
            console.log(resp)
        } else {
            console.log("Status: " + resp.status)
            return Promise.reject("server")
        }
    })
    .catch(err => {
        if (err === "server") return
        console.log(err)
    })



        
      
      textField.value = '';
    };
};