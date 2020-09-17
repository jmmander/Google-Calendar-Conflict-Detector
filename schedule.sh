path=$1
(crontab -l 2>/dev/null | fgrep -v "00 * * * * cd $path && python cal.py"; echo "00 * * * * cd $path && python cal.py") | crontab -



