// 0: {type: 'programming', setup: 'An IPv6 packet is walking out of the house.', punchline: 'He goes nowhere.', id: 374}

// fetch('https://official-joke-api.appspot.com/jokes/programming/random')
// .then(
//     (res=>
//         {
//             if(res.ok)
//                 console.log("success")
//             else
//                 console.log("failed")

//             return res.json()
//         })
// )
// .then((msg)=>(console.log(msg[0].setup, msg[0].punchline))) 
// .catch((err)=>console.log(err))


//GETTING THE DATA FROM API
// fetch('https://jsonplaceholder.typicode.com/todos/1')
//       .then(response => response.json())
//       .then(json => console.log(json))

//POSTING A DATA
fetch('https://jsonplaceholder.typicode.com/todos', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        userId: 22, 
        id: 456, 
        title: 'test', 
        completed: false
    })
})
.then(response => response.json())
.then(json => console.log(json))
.catch(error => console.error('Error:', error));


// type: 'programming', setup: 'There are 10 types of people in this world...', punchline: "Those who understand binary and those who don't", id: 29



