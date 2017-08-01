import subprocess
def send_to_print(file_path, name_printer):
	cmd = "cat %s | /usr/bin/lpr -P %s" % (file_path, name_printer)

	lpr =  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	return lpr
