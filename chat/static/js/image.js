window.onload = function() {
    const ilist = document.getElementById('ilist')
    fetch(`http://localhost:5000/api/getImages`, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        
        
        
    })
        .then(resp => {
            if (resp.status === 200) {
                console.log(resp)
                for (let i = 0; i < resp.length; i++) {
                    dat = resp[i]
                    temp = document.createElement(card)
                    temp.image = dat.thumb
                    temp.description = temp.prompt
                    
                    temp.title = temp.status
                    
    
                    ilist.appendChild(card)
    



                }

            } else {
                console.log("Status: " + resp.status)
                return Promise.reject("server")
            }
        })
        .catch(err => {
            if (err === "server") return
            console.log(err)
        })

        

        document.getElementById('form').onsubmit = ev => {
            ev.preventDefault();
            const oprompt = document.getElementById('txt');
            let prompt = oprompt.value
            console.log(prompt)
            var oheight = document.getElementById("height");
            var height = oheight.value;
            var owidth = document.getElementById("width");
            var width = owidth.value;
            
            let msg = {
                "img_height" : height,
                "img_width":  width,
                "prompt" : prompt
             

            }

            fetch(`http://localhost:5000/api/queueimage`, {
            method: "post",
            headers: { "Content-Type": "application/json" },
            body:JSON.stringify(msg) 
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
        
        
        
                
              
             // textField.value = '';
            };




}