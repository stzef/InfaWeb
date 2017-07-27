import subprocess

class ManagePrinter(object):
	"""docstring for ManagePrinter"""
	def __init__(self):
		super(ManagePrinter, self).__init__()
		self.name_printer = "default_printer"

	def send_to_print(self, file_path, name_printer):
		
		name_printer = name_printer if name_printer is not None else self.name_printer

		print(name_printer)

		cmd = "/usr/bin/lpr %s" % (file_path)
		if self.name_printer is not None:
			cmd = "/usr/bin/lpr -P %s %s" % (name_printer, file_path)

		lpr =  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return lpr
