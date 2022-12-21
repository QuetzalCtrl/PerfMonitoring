import time
import psutil
import smtplib
from datetime import datetime  

# Set the interval at which to collect performance metrics (in seconds)
INTERVAL = 2

# Set the threshold values for CPU, memory, and disk usage
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 90
DISK_THRESHOLD = 90


def send_alert(message):
  # Set the email address and password for the account that will send the email
  sender_email = "your_email@example.com"
  sender_password = "your_email_password"

  # Set the recipient email address
  recipient_email = "test@mail.com"

  # Set the subject and body of the email
  subject = "Performance Alert"
  body = message

  # Build the email message
  msg = f"Subject: {subject}\n\n{body}"

  # Connect to the email server
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(sender_email, sender_password)

  # Send the email
  server.sendmail(sender_email, recipient_email, msg)

  # Disconnect from the email server
  server.quit()


while True:
  # Get the current timestamp
  timestamp = time.time()
  # Convert it to date_time readable format
  date_time = datetime.fromtimestamp(timestamp)

  # Collect CPU usage
  cpu_percent = psutil.cpu_percent()

  # Check if the CPU usage threshold has been exceeded
  if cpu_percent > CPU_THRESHOLD:
    # Send an alert if the threshold has been exceeded
    send_alert("High CPU usage detected: {cpu_percent}%")

  # Collect memory usage
  memory_info = psutil.virtual_memory()
  memory_used = memory_info.used
  memory_total = memory_info.total
  memory_percent = memory_info.percent

  # Check if the memory usage threshold has been exceeded
  if memory_percent > MEMORY_THRESHOLD:
    # Send an alert if the threshold has been exceeded
    send_alert("High memory usage detected: {memory_percent}%")

  # Collect disk usage
  disk_info = psutil.disk_usage("/")
  disk_used = disk_info.used
  disk_total = disk_info.total
  disk_percent = disk_info.percent

  # Check if the disk usage threshold has been exceeded
  if disk_percent > DISK_THRESHOLD:
    # Send an alert if the threshold has been exceeded
    send_alert("High disk usage detected: {disk_percent}%")

  # Print the collected metrics
  print(f"{date_time}: CPU usage = {cpu_percent}%, Memory usage = {memory_percent}%, Disk usage = {disk_percent}%")

  # Sleep for the specified interval before collecting the next set of metrics
  time.sleep(INTERVAL)

