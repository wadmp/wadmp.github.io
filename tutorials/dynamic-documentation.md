# How the API Dynamic Documentation works

### How to find it
Go to api.wadmp.com (or for the testing site, api.staging.com)
To access the documentation, go to API Gallery and click on the only API there.

### What is the Dynamic Documentation
The API is a list of all operations that can be called to interact with WebAccess DMP. The dynamic documentation is a description of those operations, or endpoints, grouped by sections. Each endpoint is described along with its parameters and possible responses.

The documentation is dynamic because it allows to execute the endpoints. Prior to that you need to login in the top right of the page and the Authenticate in the documentation itself.


----------------This is what the video will say. It will be deleted from this page once the video is uploaded----------------
Welcome. In this video we will see the API Dynamic Documentation and how to explore it. You probably already accessed the UI and have a user to access it. You will use it on the Dynamic Documentation too, so if you need help creating it, please refer to the first tutorial, "Sign Up and create your company".

To access the API Dynamic Documentation you have to prepend "api." to the address of DMP. If you are, like me, on the production plattform your URL will be api.wadmp.com. To access the documentation we have to go to API Gallery, and then click on the API. The first you see is the list of sections in which the API is divided into. To see the endpoints we click on the section and then in the endpoint we are interested in. In this case, the endpoint GET /applications returns all applications available for installation to us, to install in our devices. We can also see the parameters available and if they are required or not. Under parameters we can see all possible responses the endpoint can return with some details if needed.
There is no way to Try out the endpoint, and this is because we are not logged in. Let's go ahead and click in the link on the top right side of the page. We click on the button "Sign in with WebAccess/DMP" and we see the login happens automatically, no input from us. This is because we are already logged in the UI, so the browser already has our credentials. Now we need to Authenticate again, this time clicking on the Authorize button. We fill the client_id with the value swagger_ui and we check all the scopes. This is to provide the Try it out functionality with our credentials too. Now when we authorize and then close, we can go to the endpoint we wanted. See how now we have the Try it out button and when we click on it we can Execute the endpoint. This will actually call the endpoint and show the returned result, all applications available.