path=$1
(crontab -l ; echo "00 * * * * cd $path &&  python cal.py") | sort - | uniq - | crontab -

