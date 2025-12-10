from datetime import datetime
napoleon_bm = datetime(year=1812, month=9, day=14)
date = datetime.now()
days = date.toordinal() - napoleon_bm.toordinal()
print(days)
