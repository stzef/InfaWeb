import subprocess
def send_to_print(file_path, name_printer):
	print("file_path")
	print(file_path)
	print('name_printer')
	print(name_printer)
	cmd = "/usr/bin/lpr -P %s %s" % (name_printer, file_path)

	lpr =  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	return lpr
