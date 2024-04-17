# User management


To start using WebAccess/DMP, you need a user account first.

Use Sign Up link only if you are the first from your company to access the platform. If someone else has already Signed Up, ask them to create a user to add you to the company.

## 1- Sign up / Sign in


- Go to [wadmp3.com](https://wadmp3.com). You will be redirected to the login page.

![Login Page](./LogIn.png)

- Click on the Sign Up link and fill in your details.

![Sign Up Page](./SignUp.png)

- After clicking the Create Account button, enter your email inbox and confirm your new user.

![Email Confirmation](./EmailConfirm.png)

- After clicking the confirmation in your email, your account will be ready to log in to WebAccess/DMP with your login data on the main page.

![Email Click](./emailconfirm2.png)


### Using other identity providers to sign up/sign in

 Sign in with External Provider 

If your company is listed as an external provider, you can sign in immediately.

![External provider](./external_provider.png "External provider")

OAuth/OpenIP type of authentication is supported for external providers. Don't hesitate to contact us if you want your company to be listed as an external provider.


## 2- Add users


### Invite existing users
You can invite existing or new users who just created their account to any company you have permission to. You can do it similarly, like when creating a new user.

You can check your permissions if you edit your user. Your assigned permissions are shown as check marks.

![permissions_user](./images/permissions_user-1.png)

To invite a user:

1. Make sure that you're in the right company where you want to invite the user, then select *Users* from the *Title Menu*.
2. On the *Users* page, click the *Invite User* action button on the right top of the page.

3. To the invitation form, fill in the user's email and set up your specific permissions for him to use.

![users-invite](./images/invite-user.png)

4. Now, the user needs to head to his email to confirm the sent invitation by clicking on the link in the email.

![email-invitation](./images/email-invite.png)

5. After clicking on the invitation, the link will redirect him to our main page, where he will be notified that he has been added to the company.

![invite-confirmation](./images/accept-invite2.png)

6. From now on, the user can click the "Continue to Dashboard" link and check that he's in the company.

![check-company](./images/check-company.png)



### Create new users

Creating them yourself is the only way to add users to your companies. When a user signs up, he can also make a company with no relation to yours.

As with companies, remember that the creation of a user depends on two conditions:
- You can log in to the platform and
- That you have permission to create companies

You can check your permissions if you edit your user. Your assigned permissions are shown as check marks.

![permissions_user](./images/permissions_user-1.png)

To create a user, you can do it in two almost identical ways:

1. Make sure that you're in the right company where you want to invite the user, then select *Users* from the *Title Menu*.
2. On the *Users* page, click the *Invite User* action button on the right top of the page.

![users-invite](./images/users-invite.png)

3. To the invitation form, fill in the user's email and set up your specific permissions for him to use.

![user-permissions](./images/user-inviteform.png)

4. Now, the user needs to head to his email to confirm the sent invitation by clicking on the link in the email.

![email-invitation](./images/email-invitation.png)

5. After clicking on the invitation, the link will redirect him to our main page, where he will need to fill up his login data and click the *Create Account* button, as shown in the picture below. The email is already set up from the link and cannot be changed.

![test_subject](./images/test_subject.png)

6. After clicking the create account button, you will get a message that your registration has been completed. You can now access your account by clicking the *Dashboard* link or logging in on the main page.

![subject_success](./images/subject_success.png)

The second way to create a user:

1. Select "Companies" from the *Title Menu*. 
2. On the Companies page, click on your desired company, then on the "Invite User" action button.

![companies-invite](./images/companies-invite(1).png)

3. From now on, the process is the same as in the first way of creating a user.



## 3- Remove users 


### A- Remove a user from a company

 **To remove a user**:

1. Make sure that you're in the right company where you want to remove the user, then select *Users* from the *Title Menu*.

2. On the *"Users"* page, click the *"Remove User from Company"* action button on the right of the schedule.

![users-remove](./images/remove-user.png)


### B- Delete a user account

#### General User Permissions:

- Normal users cannot delete other users.

- They can remove users from a company (kick out).

---

#### System Administrator Privileges:

- Only system administrators have the authority to delete other users.

---

#### Self-deletion of User Account:

- Users have the capability to delete their own account.

- This functionality is currently not available in the User Interface (UI).

-Until it is added to the UI, users must delete their accounts directly using the "API".

## 4- Two-Factor authentication (2-FA)

**2FA** (*Two-Factor authentication*) provides an additional level of security to protect your account.

Suppose it is enabled and already set up after a successful login. In that case, you will be asked for a one-time password to enter from your Auth App (Microsoft Authenticator, Google Authenticator, Authy, etc.)

 **Authenticator Apps**

To configure 2FA, you should first download the Authenticator app to your phone. We support a wide array of Auth apps.

- [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en&gl=US)

- [Microsoft Authenticator](https://play.google.com/store/apps/details?id=com.azure.authenticator&hl=en&gl=US)

- [Google Authenticator (IOS)](https://apps.apple.com/us/app/google-authenticator/id388497605)

- [Microsoft Authenticator (IOS)](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)

### How to enable 2-FA

You can activate 2FA in the *Company Edit Form*.

![2FA](./images/2f/fa1.png "2fA")

After turning it on, you can configure a 2FA using your Auth application.

 <font color="red">**Important Notice:**</font> Enabling 2FA will add an extra option, “Service Account” (in the user's permissions settings), so company admins can enable/disable this feature for users in a company having 2FA enabled (this will allow users to use the scripts even if they have 2FA enabled otherwise they will not be able to).

![Enable 2FA](./images/2f/2fa.png "Enable 2fA")

When you enable 2FA for a company, all users will be forced to set up the 2FA after they log in. They cannot use the system until they complete the 2FA setup.


### Using 2-FA

Once you have downloaded the application, you must scan the QR code or enter the given code manually.

![2FA app](./images/2f/fa3.png "2fA app")

Type in the unique password you see in your Auth app to sign in.

![2FA app password](./images/2f/fa4.png "2fA app password")

 :warning: <font color="red">**Important Notice:**</font>  

**Turning 2FA off for the company will turn it off for all users in that company.**

## 5- Permissions 

### Permissions management

xxxxxxx


### Explanations of individual permissions

xxxxx

