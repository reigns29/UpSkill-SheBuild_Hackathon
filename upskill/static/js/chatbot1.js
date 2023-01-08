const { Configuration, OpenAIApi } = require("openai"); 
require('dotenv').config();

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
  });
const openai = new OpenAIApi(configuration);

let response = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
    temperature: 0.9,
    max_tokens: 150,
    top_p: 1,
    frequency_penalty: 0.0,
    presence_penalty: 0.6,
    stop: [" Human:", " AI:"],
  })


submit.addEventListener("click" , (e) =>{
    e.preventDefault();
    console.log(question.value)
   
    // let response = await openai.createCompletion({
    //     model: "text-davinci-003",
    //     prompt: "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
    //     temperature: 0.9,
    //     max_tokens: 150,
    //     top_p: 1,
    //     frequency_penalty: 0.0,
    //     presence_penalty: 0.6,
    //     stop: [" Human:", " AI:"],
    //   })

    r.then((response) => {
        console.log(response)
        return response.json()
      }).then((resp) => {
        console.log(resp);
        
        let htmlstr = ` <div class = "container mt-4 mx-4">
        <h2>Showing Results for the state: <b>  ${resp.question} </b> </h2>
       <p class = "my-2"> Link to College Website :  ${resp.link} </p>
       <p class = "my-2"> College Name : ${resp.name} </p>
       <p class = "my-2"> Country : ${resp.country} </p>
       </div> `

       mine.innerHTML = htmlstr;
       return resp;

      })
      question.value = ""
})

