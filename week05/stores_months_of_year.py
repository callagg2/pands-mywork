# this program stores the months of the year, from that tuple create
# another tuple with just the summer months (May, June, July), print out the
# summer months one at a time.

# author: gerry callaghan

months =("January","February","March","April","May","June","July","August","September",
"October","November","December")

# summer is months May which is the 4th element (starting with 0) while August is the sixth
# remember with arrays the last number is not included
summer = months[4:7]

for month in summer:
    print(month)