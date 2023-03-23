.PHONY: tests tgg tgp

CURLHEADERS=-H "Content-Type: application/json"
# OBJID=6402bd14a635084ac191cb6b
OBJID=641bccca2202b3b7d4a06032





tests:
	NOSE_NOCAPTURE=1 nose2


tgg: # Test group GET
	curl http://localhost:6543/api/group/$(OBJID)

tgp: # Test group POST
	curl $(CURLHEADERS) -X POST \
		http://localhost:6543/api/group/$(OBJID) \
		-d '{"name": "New Name"}'

tgi: # Test group PUT
	curl $(CURLHEADERS) -X PUT \
		http://localhost:6543/api/groups \
		-d '{"name": "New Name", "code":9876}'
