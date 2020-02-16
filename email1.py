import smtplib
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("userforusing321@gmail.com", "userforusing321@")
server.sendmail("userforusing321@gmail.com", "tejamaramreddy@gmail.com", "this message is from python")
server.quit()
