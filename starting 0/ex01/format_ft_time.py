import datetime
import time

time_res = time.time()
datestr = datetime.datetime.now().strftime("%b %d %Y")

print(f'Seconds since January 1, 1970: {time_res} or {time_res:.3e} in scientific notation\n{datestr}')

