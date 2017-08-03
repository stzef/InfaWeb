import subprocess
def send_to_print(file_path, name_printer):
	cmd_print = '/usr/bin/lpr -P %s %s' % (name_printer, file_path)
	subprocess.Popen(cmd_print, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	cmd_delete = 'rm %s' % file_path
	# subprocess.Popen(cmd_delete, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

