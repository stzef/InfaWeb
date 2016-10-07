from infa_web.config.domaindb import DOMAINS

def get_subdomain_by_name_db(name_db):
	domain = ""
	for nempresa, ndb in DOMAINS.iteritems():
		if ndb == name_db:
			domain =nempresa
	return domain
