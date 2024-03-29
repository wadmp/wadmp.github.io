# 2.4.3: June 7, 2022

This release contains UI improvements, appearance changes, and bug fixes.

### Improvements:

* The **date format has been changed into an ISO standard (YYYY-MM-DD)** across the UI.
![Date Format](./date-format.png "Date Format")

*  Added an option to **export Audit Logs to the CSV file**.
 ![Auditing CSV Export](./auditing-csv-export.png "Auditing CSV Export") 

* **Users with more than 10 companies will now have an autocomplete search bar** as a company filter.
![Company Filter](./company-filter.png "Company Filter")

* The latest **Company filter state will now be remembered** while navigating across the UI.

* The **Pagination setting will be remembered** as well while navigating across the UI.
![Pagination Remember](./pagination-remember.png "Pagination Remember")

* Added an **alphabetical sorting and an autocomplete feature** to all forms having the Company, Device Type, and Country fields across the UI, so it's easier to select what you are looking for as you are writing down.
![Company Search](./company-autocomplete.png "Company Search")

* **The *Install Router Apps* section has been improved**:

  1. Router Apps are now sorted alphabetically. The sorting order can be changed.
  2. Added a search box to find a Router App quickly.
  3. *CANCEL* and *INSTALL* buttons are always visible.
  4. Removed the *mark all apps* checkbox.
  5. Widedened the *Version* field, so the whole version string is visible.
![Router Apps Search](./router-apps-search.png "Router Apps Search")

* The icons of the *Playbooks* and *Audit Logs Action Type* filters changed to a classic filter icon.
![Classic Filter Icon](./picture-11.png "Classic Filter Icon") 

* Changed the position of the *Aggregated Dashboard* graphs legend, which is now under the graphs.
![Graph Legend](./graph-legend.png "Graph Legend") 

* Changed the data amount unit symbol from MBs to MiBs everywhere in the GUI, so the data units are unified (1 MiB is counted as 1024 KiBs).

* Removed the Breadcrumb panels on the top of the pages.
![Panel Removal](./panel-removal.png "Panel Removal") 

* Added the text "Press ESC for more options" to the Company dashboard, so the graph tunning settings can be found easier.
![Escape Options](./escape-options.png "Escape Options") 
  
*  The Premium label at the Alerts menu now disappears once the user is a member of Premium companies only.

* Added spaces to the Alert Rule *Operators* so they are more human-readable.
![Escape Options](./rule-operator.png "Rule Operator") 

### Bugfixes:
 
* Fixed multiple visual bugs and details: alignments, cropped company filter pills, unified bold text usage, and added missing description tooltips.

* Fixed visual bug of the Invoice PDF that it did not have alignment borders. 

* Alerts: Fixed *Target Type* not being changed when switching between *Single Device* and *Company* values, despite the successful message being shown.

* Alerts: Fixed the device selection was offering devices that do not belong to the selected company.
  
* Auditing: Fixed an issue where some events did not show because the minute accurate time filter wrongly did not include them. The time filter shows events in all 59 seconds of the selected minute.

* Playbooks: Fixed showing of Router Apps with is_aggreagate parameter set to true. These Routers Apps are now not offered to be installed but are automatically installed along with other Router App.
