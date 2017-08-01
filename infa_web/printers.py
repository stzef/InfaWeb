import subprocess
def send_to_print(file_path, name_printer):
	cmd = 'echo "%s" | /usr/bin/lpr -P %s' % (file_path, name_printer)
	print "....................."
	print cmd
	print "....................."

	lpr =  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	return lpr
