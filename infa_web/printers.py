import subprocess

class ManagePrinter(object):
	"""docstring for ManagePrinter"""
	def __init__(self, name_printer):
		super(ManagePrinter, self).__init__()
		self.name_printer = name_printer

	def __init__(self):
		super(ManagePrinter, self).__init__()
		self.name_printer = None

	def send_to_print(self, file_path):

		cmd = "/usr/bin/lpr %s" % (file_path)
		if self.name_printer is not None:
			cmd = "/usr/bin/lpr -P %s %s" % (self.name_printer, file_path)

		lpr =  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		return lpr
