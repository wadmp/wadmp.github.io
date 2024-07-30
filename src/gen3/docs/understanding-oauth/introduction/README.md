
## Introduction

You are probably already familiar with the concept. When you visit a particular website or use a specific mobile app, instead of asking you to create a new account, *it prompts you to log in using an existing account on some other service*, such as Google, Facebook, or Twitter.

![alt text](./sign-in_examples.png "Example screenshot showing sign-in options")

There are several advantages:
* You do not have to create and remember yet another password!
* You do not have to give your password to a website or app you possibly do not trust.
* Only the "identity provider" (in this case, Google, Facebook, or Twitter) handles your user credentials.

WebAccess/DMP uses the same concept.

> Remember that the User Interface or web app that you see at [wadmp.com]([https://wadmp.com) is only one example
> of a client application that consumes the WebAccess/DMP API.

WebAccess/DMP (the platform) acts as the "identity provider" for users. *Any* client application that consumes the WebAccess/DMP API should redirect to our built-in Sign-In page. You can see this when you connect to [wadmp.com]([https://wadmp.com) for the first time (or try it in an Incognito window). The browser is redirected to [gateway.wadmp.com/public/auth/public/auth/login](https://gateway.wadmp.com/public/auth/public/auth/login):

![alt text](./wadmp_sign-in.png "WA/DMP sign-in page")

Another good example is Grafana. Our main UI utilizes Grafana to display dashboards for device monitoring data. These dashboards are embedded in the [wadmp.com](https://wadmp.com) web pages, but you can also access Grafana directly at [grafana.wadmp.com](https://grafana.wadmp.com).
Note that *you do not have to create an account* with Grafana: click "Sign in with OAuth":

![alt text](./grafana_sign-in.png "Grafana sign-in page")

You are automatically redirected to the WebAccess/DMP sign-in page.
