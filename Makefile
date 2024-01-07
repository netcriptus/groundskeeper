
push:
	rsync -r ~/projects/groundskeeper pi@raspberrypi:~

logs:
	ssh pi@raspberrypi sudo journalctl -f -u groundskeeper

restart:
	ssh pi@raspberrypi sudo systemctl restart groundskeeper.service

install:
	ssh pi@raspberrypi sudo pip3 install -U -r /home/pi/groundskeeper/requirements.txt

stop:
	ssh pi@raspberrypi sudo systemctl stop groundskeeper.service

deploy: push restart
