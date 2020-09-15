fileLocation = /Users/Your/Folder/Path
(crontab -l | grep "00 * * * * cd $fileLocation &&  python cal.py") || { crontab -l; "00 * * * * cd $fileLocation &&  python cal.py"; } | crontab