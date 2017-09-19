### Inbox messaging and alerts for company's main website

Duration: September - November 2015  
Role-played: Developer  
Skills used: Yii, Flask/Python, NodeJS, AngularJS, MySQL, MongoDB, Bower, REST, Vagrant, Gulp

This project integrates nodejs to an existing website which enables support to communicate messages and alerts to tutors

- Messages and alerts are received by tutors on a realtime basis, thanks to nodejs
- Data is handled via api calls by angularjs apps to an api server developed in flask
- This inbox project also tracks down offline messages (counter) for tutors and support


### Chatter and ChatterAdmin

Duration: on-going development / new feature requests  
Role-played: Designer, Developer, and Tester  
Skills used: Yii, RBAC, Vagrant, CentOS, MySQL, AmazonS3, GitHub, AngularJS, Bower

**Chatter**

- displays chatter’s profile
- interface to save & submit chatter’s schedules
- displays pdf manuals
- display notifications from admins
- manages attendance
- uses angularjs to manage ajax requests

**ChatterAdmin**

- manages chatter profiles
- handles the approval/modifications of schedules submitted by chatters
- uploading of manuals and notifications for chatters
- attendance reports
- manages chatter’s work records
- view chat history
- ticket management (free chat minutes)
- email subscriptions and management (marketing tool)


### Chatpage

Duration: On-going development / new feature requests  
Role-played: Maintainer / Tester  
Skills used: NodeJS/ExpressJS, AngularJS, Github, Vagrant, CakePHP, GruntJS, Bower

**Frontend**

- website used by chatters to communicate via chat with users using IOS app

**Backend**

- uses CakePHP & NodeJS server to handle backend services such as database operations, socket connections, and authentication


### Password Change Schedule

Duration: June 2014  
Role-played: Designer, Developer, and Tester  
Skills used: PHP, Yii, Xampp, Centos, MySQL  

This component will force users to change their passwords in all Yii systems based on the set schedules  
(every June 30 & December 30)


### Email Queuing

Duration: June 2014  
Role-played: Designer, Developer, and Tester  
Skills used: Yii, Xampp, API, Centos, MySQL  

This component will allow yii-systems to queue their emails and sends them at a later time.  

- this can be used with Email CMS
- allow admins to resend emails with failed status
- has cron job to clear db entries leaving only a month’s worth of data


### Staff API

Duration: May 2013  
Role-played: Designer, Developer, and Tester  
Skills used: PHP, Yii, RBAC, Xampp, Centos, MySQL  

This is used to sync staff tables from jp servers to ph servers. This is called via curl in staff cms system.


### Staff CMS

Duration: May 2013  
Role-played: Designer, Developer, and Tester  
Skills used: PHP, Yii, RBAC, Xampp, Centos, MySQL  

CRUD management of staffs ie. team assignments, job positions/promotions, resignations.
This module provides reset for forgotten passwords.


### Biometrics

Duration: Sept 2012 - May 2013  
Role-played: Designer, Developer, and Tester  
Skills used: PHP, Yii, RBAC, PHPExcel, Xampp, Centos, MySQL  

By May 2013, this project was passed on to a new developer so I can focus on other projects.

- this system accepts a csv-formatted document containing staffs' time entries for a specified cutoff. Afterwards, the system will rectify the time records based on the rules provided by the Personnel team. Lastly, the system will compute for an employee's rendered work hours/minutes
- Personnel team may view the final results either through the web browser or by exporting it to excel
- sub modules includes: uploading of employees' schedules, special entries (ie adjustments), 
and holidays
- the system will take into consideration these sub-modules and process the work hours accordingly ie. work rendered on a holiday should be treated differently than work rendered on a regular work day
- the system also logs errors and actions made by users for tracking purposes (developers/debugging)


### Jobsworth

Duration: Report-Bug/Fix cycle  
Role-played: Developer and Tester (Maintenance/Improvements)  
Skills used: Ruby, Rails, CentOS, MySQL  

This system allows developers to plan and schedule their projects

- it lets the developers know if they're slipping behind and why
- time tracking and extensive reports help clients what the developers have done and for how long.


### Web-based Overtime (WebOT)

Duration: Sept 2013  
Role-played: Developer & Tester  
Skills used: PHP, Yii, RBAC, Xampp, Centos, MySQL  

Online interface to allow users to apply for overtime requests

- managers can easily approve/disapprove requests of employees under their respective teams
- this system is integrated with the Biometrics System, thereby considering approved OTs in the computation for rendered work hours


### Email CMS

Duration: August 2013  
Role-played: Designer, Developer, & Tester  
Skills used: PHP, Yii, Xampp, MySQL  

This module provides crud management of email templates that is used by other systems

- this allows dynamic changes in email templates without changing codes in the systems


### Mass Email

- Duration: August 2013  
- Role-played: Designer, Developer, & Tester  
- Skills used: PHP, Yii, Xampp, MySQL  

This module allows the user to send/broadcast an email message to selected recipients


### Post CMS

Duration: June 2013
Role-played: Designer & Developer
Skills used: PHP, Yii, Xampp, MySQL

This system provides crud management of posts/announcements in the "What's new" section of the company's website

- posts/announcements are shown depending to the type of broadcast: all, certain employees, etc.


### Deletion/Cleanup of RegistrationLogs

Duration: Sept 2013  
Role-played: Developer  
Skills used: PHP, Yii, Xampp, CRON, MySQL  

This module is run via cron which deletes all logs, leaving only a month's worth of data in reference to the run/execution date
