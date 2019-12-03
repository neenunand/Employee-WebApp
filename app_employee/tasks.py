import sys
import traceback
import csv
from datetime import datetime
from datetime import timedelta
from django.db.models import Q
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from app_employee.models import *


@periodic_task(
    run_every=(crontab(minute=55, hour=23, day_of_week=5)),
    name="task_status",
    ignore_result=True
)
def task_status():
    try:
        week_day_num = datetime.today().weekday()
        week_start = datetime.today() - timedelta(days=week_day_num)
        week_end = week_start + timedelta(days=6)

        filename = "media/documents/Task_Status_Export"+ str(datetime.now().date()) + ".csv"
        tasks = Task.objects.select_related('assignee').filter(
            Q(start_date__date__lte=week_start.date(),end_date__date__gte=week_start.date())|
            Q(start_date__date__gte=week_start.date(),end_date__date__lte=week_end.date())|
            Q(start_date__date__lte=week_end.date(),end_date__date__gte=week_end.date())
            )
        # tasks = Task.objects.all()
        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerow(['Sl No', 'Task Name', 'Assignee', 'Start Date', 'End Date', 'Status'])
            index = 1
            for task in tasks:
                taskname = task.taskname
                assignee = task.assignee.firstname
                start_date = datetime.strftime(task.start_date, '%d/%b/%Y')
                end_date = datetime.strftime(task.end_date, '%d/%b/%Y')
                status = task.status
                writer.writerow([index,taskname,assignee,start_date,end_date,status])
                index += 1                
        
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print(err)