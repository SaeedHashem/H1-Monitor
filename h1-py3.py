import requests
import time
from datetime import datetime

start = input("\nEnter the last report you know about [Ignore if before #171490]: ")
if start == '' :
    start = 171490
else :
    start = int(start)

if start < 171490 :
    start = 171490

def getReport(report):
    url = 'https://hackerone.com/reports/%s.json' % str(report)
    res = requests.get(url)
    l = len(res.text)
    if l == 36 :
        return 0 
    else:
        return 1 

def lastReport(start):
    for report in range( start ,1000000):
        if getReport(report):
            continue
        else :
            #Some times report or two drops off from the line for unknown resonse , this section is here to assure that doesn't affect the results
            test = report 
            for x in range(1,5):
                test = test + x
                if getReport(test):
                   report = lastReport(test) + 1
                else :
                    continue
            report = report - 1
            return report

last = lastReport(start)
print("\n[+]Last submitted report is : #%s\n" % str(last))

def getNext(last):
    report = last + 1
    if getReport(report):
        now = datetime.now()
        print("Report number #%s has been submited at %s/%s/%s %s:%s\n" % (report , now.month, now.day, now.year, now.hour, now.minute))
        last = report
        getNext(last)
    else :
        time.sleep(30)
        last = report - 1
        getNext(last)


getNext(last)






    
    
