import os
from pathlib import Path

LINKEDIN_PATH='C:\\Users\\RobindeGuzman\\Documents\\LinkedInCertificates'
CERTIFICATES_MD_PATH='src\\certificates.md'

def update_certificates(path):
	os.remove(CERTIFICATES_MD_PATH);
	with open(CERTIFICATES_MD_PATH,'a') as outfile:
		outfile.write("# Certificates\n\n")
		outfile.write("## LinkedIn Learning\n\n")
		for f in os.scandir(path):
			if os.path.isfile(f):
				fname=Path(f).stem
				fname=fname.replace('CertificateOfCompletion_', '')
				outfile.write("- {}\n".format(fname))
	
	
if __name__=='__main__':
	update_certificates(LINKEDIN_PATH)