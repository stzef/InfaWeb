from django.core.mail.message import EmailMessage
from email.MIMEBase import MIMEBase 
from email import encoders 
from settings import *

def enviarmail():

    mensaje = EmailMessage(subject='prueba', from_email='fitnessjuice@fitnessjuicevidasaludable.com', to=['sistematizaref.programador4@gmail.com'])
    fp = open('infa_web/static/prueba.pdf','rb')
    adjunto = MIMEBase('multipart', 'encrypted')
    #lo insertamos en una variable
    adjunto.set_payload(fp.read()) 
    fp.close()  
    #lo encriptamos en base64 para enviarlo
    encoders.encode_base64(adjunto) 
    #agregamos una cabecera y le damos un nombre al archivo que adjuntamos puede ser el mismo u otro
    adjunto.add_header('Content-Disposition', 'attachment', filename='prueba.pdf')
    #adjuntamos al mensaje
    mensaje.attach(adjunto) 
    mensaje.template_name='pr'

    mensaje.send()
