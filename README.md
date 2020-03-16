# EMail-Pattern-Analysis
Generation of a statistical report of the messages in your Gmail.

### Getting started
- Register a Gmail account(or login into it if you already have one).
- Change the string `username = "email@gmail.com"` to your Gmail ID.
- Change the string `password = "password"` to your Gmail password.
- Enable IMAP in your Gmail account.
- Make sure you **Allow less secure apps** like Python CLI on your Gmail settings.

### Execution
- Install the required libraries.
- Run GMailAnalysis.py, this should generate a inbox_email.csv file containing information of your Gmail inbox.
- Run GMailAnalysisStats.py, this uses the .csv file to generate a statistical report of the data in your inbox.

### Examples
![MailDensity--Rahul Hegde](https://github.com/rahulhegde99/EMail-Pattern-Analysis/blob/master/MailDensity.png)
![MessageLength--Rahul Hegde](https://github.com/rahulhegde99/EMail-Pattern-Analysis/blob/master/MessageLength.png)
![KernelDensity--Rahul Hegde](https://github.com/rahulhegde99/EMail-Pattern-Analysis/blob/master/KDPlot.png)

### Todo
- Make the tool available to all the email server(currently accessible to only Google mail servers).
- More statistics and graphical data.
- Top senders to be listed in the console.
