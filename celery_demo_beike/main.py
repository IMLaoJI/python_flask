#encoding: utf-8

from tasks import send_mail

if __name__ == '__main__':
    send_mail.delay()