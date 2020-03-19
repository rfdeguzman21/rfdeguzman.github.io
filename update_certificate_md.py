import os, re
from datetime import datetime
from pathlib import Path

LINKEDIN_PATH='/home/user/Documents/LinkedInCertificates'
CERTIFICATES_MD_PATH='./src/certificates.md'

def update_certificates(path):
	os.remove(CERTIFICATES_MD_PATH);
	with open(CERTIFICATES_MD_PATH,'a') as outfile:
		outfile.write("# Certificates\n\n")
		outfile.write("[Download Resume](downloads/RobinDeGuzmanCv.docx)\n\n")
		outfile.write("## LinkedIn Learning\n\n")
		for cert in get_certifications(path):
			outfile.write("- {}\n".format(cert))


def get_certifications(path):
	certList=[]
	for f in os.scandir(path):
		if not os.path.isfile(f):
			continue
		fname=Path(f).stem
		fname=fname.replace('CertificateOfCompletion_', '')
		date=re.search(r'\((.*?)\)', fname).group(1)
		certList.append([
			datetime.strptime(date, '%b %Y'),
			fname
		])
	certList=sorted(certList, key=lambda x: x[0], reverse=True)
	# flatten list containing only the cert title
	certList=[c[1] for c in certList]
	return certList

	
if __name__=='__main__':
	update_certificates(LINKEDIN_PATH)