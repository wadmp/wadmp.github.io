# Alerts Explained 

"Alerts" is the Premium feature only (Alerts and everything related can be created only for a company of Premium type).

Set up alerts from down to top in the menu: first create Endpoint(s), then create Rule(s) and then just wait for alerts and check the History.


## Create Endpoint(s)

Start by creating an endpoint in Alerts -> Endpoints using plus icon at the top. 
This is simply the saved contact, that can be later chosen to be notified by the Alert rule. You can create as many as you want and then add multiple endpoints to an Alert to be notified. 

![Alerts create](/images/explanations-discussions/alerts/alerts_endpoint_create.png "Alerts create")

Note that the endpoint can be saved and is enabled by default (green color, play icon), but can be also disabled, so the alerts are not sent to this endpoint.

![Alerts endpoint](/images/explanations-discussions/alerts/alerts_endpoint.png "Alerts endpoint")

## Create Rule(s)

Now create an Alert rule in Alerts -> Rules, using the plus icon at the top.

![Alerts rule create](/images/explanations-discussions/alerts/alerts_rule_create.png "Alerts rule create")

Most of the fields are self-explanatory or have hints. 
When **Target Type** is set to Company, the rule is automatically applied to all the devices in that company. When choosing the Single Device, only one device can be chosen.

You can set up time Parameters for the rule: Period of the check, after how many repetitions the Alert should be sent, and the cooldown period that starts always after the Alert is sent. After the cooldown period, the check is done immediately and then again according to Period.

![Alerts rule](/images/explanations-discussions/alerts/alerts_rule.png "Alerts rule")

Then the rule itself can be set - what parameter should be evaluated (Field) and how it should be evaluated (Operator and Value(s)). For NotInRange Operator you can set up two values. True/False values may be chosen, but in all other cases, integer number values have to be filled. For Monitoring Data the unit is always the same as in graphs on Dashboards (Grafana).

![Alerts rule](/images/explanations-discussions/alerts/alerts_rule_rule.png "Alerts rule")

Then the endpoint(s) to be notified by alert can be chosen. 

Note that the rule itself can be also disabled at the top, so it is not evaluated (grey color, pause icon).


## Mail and History

For Endpoint type Email the Alert looks like this in your mail inbox:

![Alerts mail](/images/explanations-discussions/alerts/alerts_mail.png "Alerts mail")

And always the Alert is recorded in Alerts -> History, even if no endpoint is selected at the rule.

![Alerts history](/images/explanations-discussions/alerts/alerts_history.png "Alerts history")

Alerts in History can be marked as read, or marked back as unread, by one or in a bulk using checkboxes. It is possible also filter read/unread Alerts via the icon at the top left.