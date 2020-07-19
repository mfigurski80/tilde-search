init:
	virtualenv env
	source env/bin/activate
	pip3 install -r requirements.txt

discover:
	scp -r ./discovery mikofigs@tilde.club:python/
	ssh mikofigs@tilde.club python3 ~/python/discovery/users.py && python3 ~/python/discovery/websites.py
	scp -r mikofigs@tilde.club:python/discovery ./