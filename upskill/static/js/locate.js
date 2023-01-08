submit.addEventListener("click" , (e) =>{
    e.preventDefault();
    console.log(state.value);
    let url = `http://localhost:8000/locate/${state.value}`;
    let r = fetch(url, {
        headers:{
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        }
    });

    r.then((response) => {
        console.log(response)
        return response.json()
      }).then((resp) => {
        console.log(resp);
        
        let htmlstr = ` <div class = "container mt-4 mx-4">
        <h2>Showing Results for the state: <b>  ${resp.state} </b> </h2>
       <p class = "my-2"> Link to College Website :  ${resp.link} </p>
       <p class = "my-2"> College Name : ${resp.name} </p>
       <p class = "my-2"> Country : ${resp.country} </p>
       </div> `

       mine.innerHTML = htmlstr;
       return resp;

      })
      state.value = ""
})

