### Tutor website

This project help tutors to manage their schedules, conduct their lessons,
and receive important announcements and information

**Duration**: September 2012 - Present  
**Roles played**: Developer, Project Lead, Tester  
**Skills used**: `Yii` `Flask` `NodeJs` `AngularJS` `MySQL` `Redis`
`MongoDb` `REST API` `Vagrant` `Gulp` `Codeception`

- Continuous development of new features and/or change requests depending 
on the need of the company
- Fix bugs encountered/reported by staffs, tutors, or students

---

### Inbox messaging and alerts for company's main website

This project integrates nodejs to an existing website which enables support to
communicate messages and alerts to tutors

**Duration**: September - November 2015  
**Role-played**: Developer  
**Skills used**: `Yii` `Flask/Python` `NodeJS` `AngularJS` `MySQL` `MongoDB` `Redis` 
`Bower` `REST API` `Vagrant` `Gulp`

- Messages and alerts are received by tutors on a realtime basis, thanks to nodejs
- Data is handled via api calls by angularjs apps to an api server developed in flask
- This inbox project also tracks down offline messages (counter) for tutors and support

---

### Chatter and ChatterAdmin

This project manages chatter's account, schedules, and timecard entries. Also handles file
management using AmazonS3

**Duration**: on-going development / new feature requests  
**Role-played**: Designer, Developer, and Tester  
**Skills used**: `Yii` `RBAC` `Vagrant` `CentOS` `MySQL` `AmazonS3` `GitHub` `AngularJS` `Bower`

- **Chatter**
    - displays chatter’s profile
    - interface to save & submit chatter’s schedules
    - displays pdf manuals
    - display notifications from admins
    - manages attendance
    - uses angularjs to manage ajax requests

- **ChatterAdmin**
    - manages chatter profiles
    - handles the approval/modifications of schedules submitted by chatters
    - uploading of manuals and notifications for chatters
    - attendance reports
    - manages chatter’s work records
    - view chat history
    - ticket management (free chat minutes)
    - email subscriptions and management (marketing tool)

---

### Chatpage

This project allows chatters to chat with their students on IOS app

**Duration**: On-going development / new feature requests  
**Role-played**: Maintainer / Tester  
**Skills used**: `ExpressJS` `AngularJS` `Github` `Vagrant` `CakePHP` `GruntJS` `Bower`

- **Frontend**
    - website used by chatters to communicate via chat with users using IOS app

- **Backend**
    - uses `CakePHP` & `NodeJS` server to handle backend services such as database operations, 
    socket connections, and authentication

---

### Password Change Schedule

This component will force users to change their passwords in all Yii systems based on the set schedules  
(every June 30 & December 30)

**Duration**: June 2014  
**Role-played**: Designer, Developer, and Tester  
**Skills used**: `Yii` `Xampp` `Centos` `MySQL`  

---

### Email Queuing
This component will allow yii-systems to queue their emails and sends them at a later time. Can also
be used by other frameworks.

**Duration**: June 2014  
**Role-played**: Designer, Developer, and Tester  
**Skills used**: `Yii` `Xampp` `REST API` `Centos` `MySQL`  

- this can be used with Email CMS
- allow admins to resend emails with failed status
- has cron job to clear db entries leaving only a month’s worth of data

---

### Staff API
This is used to sync staff tables from jp servers to ph servers. This is called via curl in staff cms system.

**Duration**: May 2013  
**Role-played**: Designer, Developer, and Tester  
**Skills used**: `Yii` `RBAC` `Xampp` `Centos` `MySQL`  

---

### Staff CMS
CRUD management of staffs ie. team assignments, job positions/promotions, resignations.
This module provides reset for forgotten passwords.

**Duration**: May 2013  
**Role-played**: Designer, Developer, and Tester  
**Skills used**: `Yii` `RBAC` `Xampp` `Centos` `MySQL`  

---

### Biometrics
Calculates the number of hours an employee rendered on a given range.

**Duration**: Sept 2012 - May 2013  
**Role-played**: Designer, Developer, and Tester  
**Skills used**: `Yii` `RBAC` `PHPExcel` `Xampp` `Centos` `MySQL`  

By May 2013, this project was passed on to a new developer so I can focus on other projects.

- this system accepts a csv-formatted document containing staffs' time entries for a specified cutoff. Afterwards, the system will rectify the time records based on the rules provided by the Personnel team. Lastly, the system will compute for an employee's rendered work hours/minutes
- Personnel team may view the final results either through the web browser or by exporting it to excel
- sub modules includes: uploading of employees' schedules, special entries (ie adjustments), 
and holidays
- the system will take into consideration these sub-modules and process the work hours accordingly ie. work rendered on a holiday should be treated differently than work rendered on a regular work day
- the system also logs errors and actions made by users for tracking purposes (developers/debugging)

---

### Jobsworth

This system allows developers to plan and schedule their projects  
(discontinued as of 2014, in favor of redmine)

**Duration**: Report-Bug/Fix cycle  
**Role-played**: Developer and Tester (Maintenance/Improvements)  
**Skills used**: `RubyOnRails` `CentOS` `MySQL`  

- lets the developers know if they're slipping behind and why
- time tracking and extensive reports help clients what the developers have done and for how long.

---

### Web-based Overtime (WebOT)

Online interface to allow users to apply for overtime requests

**Duration**: Sept 2013  
**Role-played**: Developer & Tester  
**Skills used**: `Yii` `RBAC` `Xampp` `Centos` `MySQL`  

- managers can easily approve/disapprove requests of employees under their respective teams
- this system is integrated with the Biometrics System, thereby considering approved OTs in the computation for rendered work hours

---

### Email CMS

This module provides crud management of email templates that is used by other systems

**Duration**: August 2013  
**Role-played**: Designer, Developer, & Tester  
**Skills used**: `Yii` `Xampp` `MySQL`  

- allows dynamic changes in email templates without changing codes in the systems

---

### Mass Email

This module allows the user to send/broadcast an email message to selected recipients

**Duration**: August 2013  
**Role-played**: Designer, Developer, & Tester  
**Skills used**: `Yii` `Xampp` `MySQL`  

---

### Post CMS

CRUD management of posts/announcements in the "What's new" section of the company's website

**Duration**: June 2013
**Role-played**: Designer & Developer
**Skills used**: `Yii` `Xampp` `MySQL`

- posts/announcements are shown depending to the type of broadcast: all, certain employees, etc.

---

### Deletion/Cleanup of RegistrationLogs

This module is run via cron which deletes all logs, leaving only a month's worth of data in reference to the run/execution date

**Duration**: Sept 2013  
**Role-played**: Developer  
**Skills used**: `Yii` `Xampp` `CRON` `MySQL`  
