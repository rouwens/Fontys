import datetime
from datetime import datetime
import pytz
utc = "1664547897"
#utc_datetime = datetime.now(tzutc())
local_timezone = pytz.timezone('Europe/Amsterdam')
local_datetime = local_datetime.astimezone(local_timezone)
print(local_datetime)