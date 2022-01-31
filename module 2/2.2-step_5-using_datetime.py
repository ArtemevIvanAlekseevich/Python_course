import datetime

def calculate_date(start_date, days):
    start_year, start_month, start_day = map(int, start_date.split()) 
    new_date = datetime.date(start_year, start_month, start_day)
    new_date += datetime.timedelta(days = int(days))
    print(new_date.year, new_date.month, new_date.day)

if __name__ == "__main__":
    calculate_date(input(), input())

