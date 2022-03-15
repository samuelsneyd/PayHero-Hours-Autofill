# PayHero Hours Autofill
A small Python script for Selenium to automatically fill out hours worked in the PayHero online app.

To use, create a file named `.env` in the payhero_autofiller folder.

The file should have the following contents.

```
APP_USERNAME=<username>
APP_PASSWORD=<password>
```

Replace \<username> and \<password> with the login credentials without the <>'s and with no spaces after the =.

The default hours are Monday-Friday 8 hours, and 0 hours in the weekend. You can edit these in main.py if needed.

Run by typing `python main.py` or `python3 main.py` into the command line from the program directory.

Currently, it only supports settings hours for the current week.
