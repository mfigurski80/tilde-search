upload-discovery:
	scp -r ./discovery mikofigs@tilde.club:python/

download-discovery:
	scp -r mikofigs@tilde.club:python/discovery ./
