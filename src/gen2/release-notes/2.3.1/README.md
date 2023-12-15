# 2.3.1: 4th June 2021

* This release contains mainly bug fixes. 

* User Modules were renamed to **Router Apps** to be unified with other Advantech Router Apps sources. 


### UI

* Maintenance: User Modules were renamed to Router Apps across the DMP.
* Improvement: The CSS styles were changed to statically linked, so the 3rd party APIs are not used for this (a prerequisite for deploying the app in private networks).
* Improvement: The notice will pop up when moving the device to another group. Groups work like folders, and the device can be in a single group at a time. Tags can be used for multiple markings of the devices.
* Bug fixes: e-mail change followed by a refresh of the page (F5) no longer causes too many redirects error.
* Bug fixes: Fixed login screen - corrected some redirects, fixed forms where labels were overlapping the autocompleted content, fixed incorrect behavior in forms.
* Bug fixes: Fixed search in Users and Playbooks.


### Code / API

* Bug fixes: unified error messages and types for several API endpoints.
* Bug fixes: fixed devices' startup script parsing that was causing sync problems in some cases.
* Bug fixes: fixed playbooks considering failed installations as completed.
* Bug fixes: fixed permissions of viewing apps that were not global.

