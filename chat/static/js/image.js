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
    

}