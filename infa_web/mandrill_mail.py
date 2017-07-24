from django.core.mail.message import EmailMessage
from email.MIMEBase import MIMEBase
from email import encoders
from settings import *
from infa_web.parameters import ManageParameters

def enviarmail(subject,mails,attachments,template_name,name_db):
	manageParameters = ManageParameters(name_db)

	email = "fitnessjuice@fitnessjuicevidasaludable.com"
	# email = manageParameters.get_param_value('from_email')

	mensaje = EmailMessage(subject=subject, from_email=email, to=mails)

	for attachment in attachments:
		filename = attachment
		fp = open(filename,'rb')
		adjunto = MIMEBase('multipart', 'encrypted')
		#lo insertamos en una variable
		adjunto.set_payload(fp.read())
		fp.close()
		#lo encriptamos en base64 para enviarlo
		encoders.encode_base64(adjunto)
		#agregamos una cabecera y le damos un nombre al archivo que adjuntamos puede ser el mismo u otro
		adjunto.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
		#adjuntamos al mensaje
		mensaje.attach(adjunto)

	mensaje.template_name=template_name
	mensaje.send()

def emailsender(subject,mails,data,template_name,name_db):
	manageParameters = ManageParameters(name_db)

	email = "fitnessjuice@fitnessjuicevidasaludable.com"
	# email = manageParameters.get_param_value('from_email')

	mensaje = EmailMessage(subject=subject, from_email=email, to=mails)
	mensaje.template_name=template_name
	mensaje.global_merge_vars = data
	mensaje.send()

