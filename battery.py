import psutil
import time
from winotify import Notification

notified=False

while True:
    
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    print(f"Battery: {percent}% | charger: {plugged}")
    if percent <=40 and not plugged :
        if not notified :
            notification=Notification(
                app_id="Battery monitor",
                title="Battery low",
                msg=f"{percent}% battery remaining"
            )

            notification.show()
            notified=True

    else:
        notified=False

    time.sleep(60)
