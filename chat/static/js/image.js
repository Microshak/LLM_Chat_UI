window.onload = function() {

    fetch(`http://localhost:5000/api/historicImage`, {
        method: "post",
        headers: { "Content-Type": "application/json" },
        body: mss
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
    

}