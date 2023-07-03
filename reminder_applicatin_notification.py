import time
from plyer import notification


while True:
    notification.notify(
        title="** Please Drink Water Now!!"
        message="""Keep a normal temperature
        Lubricate and cushion joints.
        Protect your spinal cord and other sensitive tissues.
        Get rid of wastes through urination, perspiration, and bowel movements.""",
        #app_icon="C:\Users\Amarjeet Yadav\Downloads\wp.png",
        timeout=10
    )
    time.sleep(60*60)
