import os
import shutil
import subprocess

domain="mediawiki-new"
directory="/var/www/html/" + domain

vhost_file="mediawiki-new"
vhost_dir="/etc/httpd/conf.d/" + vhost_file + ".conf"

log_file=domain+"_error_log"
log_dir="/var/log/httpd/"+log_file

print("DEBUG: "+vhost_dir)
print("DEBUG: "+directory)
# print ("Directory: " + directory)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def create_ssl_vhost(servername, serveralias, documentroot):
	if not (os.path.exists(vhost_dir) and not (os.path.exists(directory))):
		print(bcolors.OKGREEN + "It doesn't exists. Continuing with vhost creation" + bcolors.ENDC)


		current_dir = os.getcwd()
		print(current_dir)

		os.chdir("/etc/httpd/conf.d/")

		f=open(vhost_file + ".conf", "w+")
		f.write("<VirtualHost *:80>\n")
		f.write("\tServerName "+servername+"\n")
		f.write("\tServerAlias "+serveralias+"\n")
		f.write("\t#DocumentRoot "+DocumentRoot+"\n")
		f.write("\tErrorLog "+log_dir+"\n")
		f.write("</VirtualHost>")
		f.close()

		current_dir_after = os.getcwd()
		print(current_dir_after)
		os.chdir(current_dir)
		print(current_dir)

		restart_httpd()
	else:
		print(bcolors.WARNING + "One of the files/dirs already exist and vhost creation was interrupted" + bcolors.ENDC)

def create_vhost(servername, serveralias, documentroot):
	if not (os.path.exists(vhost_dir) and not (os.path.exists(directory))):
		print(bcolors.OKGREEN + "It doesn't exists. Continuing with vhost creation" + bcolors.ENDC)


		current_dir = os.getcwd()
		print(current_dir)

		os.chdir("/etc/httpd/conf.d/")

		f=open(vhost_file + ".conf", "w+")
		f.write("<VirtualHost *:80>\n")
		f.write("\tServerName "+servername+"\n")
		f.write("\tServerAlias "+serveralias+"\n")
		f.write("\t#DocumentRoot "+DocumentRoot+"\n")
		f.write("\tErrorLog "+log_dir+"\n")
		f.write("</VirtualHost>")
		f.close()

		current_dir_after = os.getcwd()
		print(current_dir_after)
		os.chdir(current_dir)
		print(current_dir)

		restart_httpd()
	else:
		print(bcolors.WARNING + "One of the files/dirs already exist and vhost creation was interrupted" + bcolors.ENDC)

def clear_dirs():
	try:
		os.remove(vhost_dir)
		print(bcolors.OKGREEN + "FILE REMOVED: " + vhost_dir + bcolors.ENDC)
	except OSError as e:
		print(bcolors.WARNING + "COULD NOT REMOVE: File " + vhost_dir + " doesnt exist." + bcolors.ENDC)
		print(bcolors.WARNING + str(e) + bcolors.ENDC)
		pass

	# try:
	# 	shutil.rmtree(directory)
	# 	print(bcolors.OKGREEN + "DIR REMOVED: " + directory + bcolors.ENDC)
	# except OSError as e:
	# 	print(bcolors.WARNING + str(e) + bcolors.ENDC)		
	# 	pass

def restart_httpd():
	subprocess.check_call("service httpd restart".split())

# How to call specific function in Python module
#==================================================================
#  ls -al /var/www/html/mediawiki-new
# sudo /usr/local/bin/python3.8 -c 'import /home/bledar.mema/scripts/create_vhosts; create_vhosts.clear_dirs()'
# python3.8 -c 'import create_vhosts; create_vhosts.create_vhost("wiki.gtspt.corp", "wiki.gtspt.corp")'
