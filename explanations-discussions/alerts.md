# Alerts Explained 

*Alerts* is the **Premium feature only** (Alerts and everything related can be created only for a company of Premium type).

If you want to be notified that Alert triggered, read through and prepare notification Endpoint(s) first. It is possible to have an Alert without an Endpoint and check only the Alerts History in DMP, in that case, skip to Create Rule(s) below.

**Notice:** Permissions apply to Alerts.
* To read Alerts History, Rules, and Endpoints, you need to have *Alerts* permission *View*. 
* To see the create icon in Rules and Endpoints, and to be able to mark alerts read/unread, you need to have *Alerts* permission *Manage*


## To be Notified - Create Endpoint(s)

In Alerts -> Endpoints use the plus icon to prepare Endpoint for the Alert. This is simply the saved contact, that can be later chosen to be notified by the Alert rule. You can create as many as you want and then add multiple endpoints to an Alert to be notified. 

![Alerts create](/images/explanations-discussions/alerts/alerts_endpoint_create.png "Alerts create")

Note that the endpoint can be saved and is enabled by default (green color, play icon), but can be also disabled, so the alerts are not sent to this endpoint.

![Alerts endpoint](/images/explanations-discussions/alerts/alerts_endpoint.png "Alerts endpoint")

## Create Rule(s)

Use the plus icon to create a new Alert.

![Alerts rule create](/images/explanations-discussions/alerts/alerts_rule_create.png "Alerts rule create")

When **Target Type** is set to Company, the rule is automatically applied to all the devices in that company. When choosing the Single Device, only one device can be chosen.

Set up Parameters for the rule. The cooldown period starts always immediately after the Alert is being triggered. After the cooldown period, the check is done immediately and then again according to Period.

![Alerts rule](/images/explanations-discussions/alerts/alerts_rule.png "Alerts rule")

Choose the rule itself - what parameter should be evaluated (Field) and how. For the *NotInRange* Operator you can set up two values. Integer number values have to be filled. 
For Monitoring Data the unit is always the same as in graphs on Dashboards (Grafana).

**Important Notice:** *DeviceState* category of fields is evaluated differently than the other two. When a Monitoring or Auditing field is checked, it looks at the past “period” of minutes and if at any moment during that time the rule could be considered true, then the Alert will be triggered. When an Alert with a DeviceState field rule is checked, then only the situation at the time of the check is considered!

![Alerts rule](/images/explanations-discussions/alerts/alerts_rule_rule.png "Alerts rule")

Then the endpoint(s) to be notified by alert can be chosen. 

Note that the rule itself can be also disabled at the top, so it is not evaluated (grey color, pause icon).


## Mail and History

For Endpoint type Email the Alert looks like this in your mail inbox:

![Alerts mail](/images/explanations-discussions/alerts/alerts_mail.png "Alerts mail")

And always the Alert is recorded in Alerts -> History, even if no endpoint is selected at the rule.

![Alerts history](/images/explanations-discussions/alerts/alerts_history.png "Alerts history")

Alerts in History can be marked as read, or marked back as unread, by one or in a bulk using checkboxes. It is possible also filter read/unread Alerts via the icon at the top left.

Alerts stay in History, they are not automatically deleted.