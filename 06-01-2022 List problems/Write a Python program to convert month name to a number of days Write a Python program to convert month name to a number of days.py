print('No.of months:January,February,March,April,May,June,July,August,September,October,November,December')
month=input('enter the month:')
if month in ('january','march','may','july','august','october','december'):
    print('31 days')
elif month=='february':
    print('28 or 29 days')
elif month in ('april','june','september','november'):
    print('30 days')
else:
    print('wrong month name')