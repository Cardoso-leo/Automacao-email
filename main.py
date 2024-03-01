import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    
    servidor_smtp = 'smtp.example.com'
    porta_smtp = 587
    email_rem = 'seu_email@example.com'
    senha = 'sua_senha'

    msg = MIMEMultipart()
    msg['From'] = email_rem
    msg['To'] = destinatario
    msg['Subject'] = assunto

    corpo = mensagem
    msg.attach(MIMEText(corpo, 'plain'))

    servidor = smtplib.SMTP(host=servidor_smtp, port=porta_smtp)
    servidor.starttls()

    servidor.login(email_rem, senha)

    servidor.send_message(msg)

    servidor.quit()

if __name__ == "__main__":
    destinatario = 'destinatario@example.com'
    assunto = 'Teste de automação em Python'
    mensagem = 'Olá, este é um teste de automação de e-mail em Python!'
    enviar_email(destinatario, assunto, mensagem)
    print("E-mail enviado com sucesso!")
