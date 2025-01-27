import datetime
import time

from plyer import notification
while True:
    notification.notify(
        title ="To-Do List".format(datetime.date.today()),
        message="1.Live Classes \n2.Projects \n3.",
        app_icon="bell.ico",
        timeout=7
    )

    time.sleep(60*60*2)
    