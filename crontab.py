# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                       7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * *  command_to_execute

#---------- O N E  ------------------------
# This cronjob will run on sundays at 11am, 2pm & 5pm to grab all the images from desktop and move them to _ARCHIVE folder and the sub file them based on the type, and then again sub file based on the archive date!.
# the reason it run three times is because If I am not using computer in one of those times,
# it will run next time, when I might be 'possible' online.
0 11,14,17 * * 0 /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/alikhundmiri/Desktop/pythons/image_manuplation/desktop_cleaner.py auto


#---------- T W O  ------------------------
# Remove this in next few days...
# This script will run daily at 5 PM when I am connected to the internet.

# Function: Post Hafsa's Tution advert of Expatriate.com. We might need to post daily to stay on the top of every day post.
35 17 * * * /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/alikhundmiri/Desktop/pythons/housekeeping/code/hafsa_tutions.py


#---------- T H R E E  ------------------------
# Function: Post Star Play Group's advert of Expatriate.com. We might need to post daily to stay on the top of every day post.
40 17 * * * /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5 /Users/alikhundmiri/Desktop/pythons/housekeeping/code/mummy_school.py
