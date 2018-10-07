import datetime
import time
import signal
import scrollphathd as sc
from scrollphathd.fonts import font5x7

sc.set_brightness(1.0)
sc.clear()
sc.rotate(180)
sc.write_string('null', x=0, y=0, font=font5x7)
sc.show()
time.sleep(10)
