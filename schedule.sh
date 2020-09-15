fileLocation="/Users/Jacqueline/PycharmProjects/calendar"

(crontab -l ; echo "00 * * * * cd $fileLocation &&  python cal.py") | sort - | uniq - | crontab -

