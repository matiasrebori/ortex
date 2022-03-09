from datetime import datetime
import calendar
'''
This task is to fix this code to write out a simple monthly report. The report should look professional.
The aim of the exercise is to:
- Ensure that the code works as specified including date formats
- Make sure the code will work correctly for any month
- Make sure the code is efficient
- Ensure adherence to PEP-8 and good coding standards for readability
- No need to add comments unless you wish to
- No need to add features to improve the output, but it should be sensible given the constraints of the exercise.
Code should display a dummy sales report
'''
### Do not change anything in the section below, it is just setting up some sample data
# test_data is a dictionary keyed on day number containing the date and sales figures for that day
month = "02"
test_data = {f"{x}": {"date": datetime.strptime(f"2021{month}{x:02d}", "%Y%m%d"),
                      'sales': float(x ** 2 / 7)} for x in range(1, 29)}
### Do not change anything in the section above, it is just setting up some sample data
year = datetime.now().year
last_day_month = calendar.monthrange(year, int(month))[1]
start=test_data['1']
end=test_data[str(last_day_month)]


def date_to_string(date):
    # E.g. Monday 8th February, 2021
    return (f"""{date.strftime("%a")} {date.strftime("%d")}th {date.strftime("%B")}, {date.strftime("%Y")}""")


print("Sales Report\n\nReport start date: " + date_to_string(start["date"]) + "; first sales: " + str(start["sales"]) \
    + "\nReport end date: " + date_to_string(end["date"]) + "; last sales: " + str(end["sales"]) + "\n")
total=float(0)
print ("{:<35} {:<8} {:<10}".format('Date','Sales','Sales to Date '))
for k, v in test_data.items():
    if month=="02" and k=="29":
        print("Leap year") # Must be displayed if data is for a leap year
    print ("{:<35} {:<8} {:<10}".format(date_to_string(v['date']), round(v['sales']), round(total)))
    total=v['sales']+total
print(f"Total sales for the month {total}")
