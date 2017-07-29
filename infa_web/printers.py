import subprocess
def send_to_print(file_path, name_printer):
	cmd = "/usr/bin/lpr -P %s %s" % (name_printer, file_path)

	lpr =  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	return lpr
