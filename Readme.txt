https://fastapi.tiangolo.com/

https://www.uvicorn.org/

ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.

https://fastapi.tiangolo.com/async/   [MUST READ ARTICLE]



Asynchronous Code¶

Asynchronous code just means that the language 💬 has a way to tell the computer / program 🤖 that at some point in the code, it 🤖 will have to wait for something else to finish somewhere else. Let's say that something else is called "slow-file" 📝.

So, during that time, the computer can go and do some other work, while "slow-file" 📝 finishes.

Then the computer / program 🤖 will come back every time it has a chance because it's waiting again, or whenever it 🤖 finished all the work it had at that point. And it 🤖 will see if any of the tasks it was waiting for have already finished, doing whatever it had to do.

Next, it 🤖 takes the first task to finish (let's say, our "slow-file" 📝) and continues whatever it had to do with it.

That "wait for something else" normally refers to I/O operations that are relatively "slow" (compared to the speed of the processor and the RAM memory), like waiting for:

    the data from the client to be sent through the network
    the data sent by your program to be received by the client through the network
    the contents of a file in the disk to be read by the system and given to your program
    the contents your program gave to the system to be written to disk
    a remote API operation
    a database operation to finish
    a database query to return the results
    etc.


HTTP request methods

HTTP defines a set of request methods to indicate the desired action to be performed for a given resource. Although they can also be nouns, these request methods are sometimes referred as HTTP verbs. Each of them implements a different semantic, but some common features are shared by a group of them: e.g. a request method can be
1. Safe, 2. Idempotent or 3. Cacheable

GET request:

Requests using GET should only retrieve data.

HEAD request:

The HEAD method asks for a response identical to a GET request but without the response body

POST request:

The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.

PUT request:

The PUT method replaces all current representations of the target resource with the request payload.

DELETE request:

The DELETE method deletes the specified resource

CONNECT request: 

This method establishes a tunnel to the server.

OPTIONS:

TRACE:

PATCH:

___________________________________________________________________________________________________________________________________________________________

from our web browser we can only send GET request. We cannot send POST request.

