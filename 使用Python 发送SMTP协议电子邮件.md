#### 使用Python 发送SMTP协议电子邮件

```python
import smtplib
from email.mime.text import MIMEText

msg_from='username@163.com'
passwd = 'password'
msg_to = 'username@163.com'

subject = 'python email test'
content = 'this is content'
msg = MIMEText(content)
msg['subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to

try:
    s = smtplib.SMTP_SSL('smtp.163.com',465)
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print('Send Success')
except Exception as e:
    print('Send Failed')
finally:
    s.quit()
```

