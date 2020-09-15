crontab -l | { cat; echo "00 * * * * cd /Users/Your/Folder/Path &&  python cal.py"; } | crontab -
