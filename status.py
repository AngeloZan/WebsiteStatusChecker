'''Simple bot to check the status of my websites'''
import urllib.request
import json
from mail import Mail
import time

class WebsiteChecker():
    
    def __init__(self):
        with open('my_sites.json') as f:
            self.my_sites = json.load(f)

    def check_urls(self):
        '''this method checks for a 200 status on each url'''
        urls = self.my_sites
        self.my_sites_status = {}
        for url in urls:
            try:
                status_code = urllib.request.urlopen(url).getcode()
                self.my_sites_status[url] = {True: 'Up', False: 'Down'}[status_code == 200]
            except:
                self.my_sites_status[url] = "Couldn't complete request"

        return self.my_sites_status

    def send_mail(self):
        '''sends me an email with the status of each of my sites'''
        mail_subject = 'My Websites Status Update'
        status = self.my_sites_status
        status_str = ''''''
        for site in status.keys():
            status_str += '{url} - {url_status}\n'.format(url=site, url_status=status[site])
        
        with open('mail_content.txt', 'r') as f:
            # formatting the email with the current status and time
            mail_content = f.read()
            now = time.ctime()
            mail_formatted = mail_content.format(time=now,status=status_str)
        
        email = Mail(mail_subject, mail_formatted)
        email.send()

    def update_status(self):
        '''main function, checks urls and sends mail'''
        self.check_urls()
        self.send_mail()


if __name__ == '__main__':
    checker = WebsiteChecker()
    checker.update_status()
        
        


