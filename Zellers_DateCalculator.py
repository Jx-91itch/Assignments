class DateCalculator:
    def __init__(self):
        self.month_guide={
            "January":13,  "Jan": 13,
            "February":14, "Feb": 14,
            "March": 3,    "Mar": 3,
            "April": 4,    "Apr": 4,
            "May": 5,
            "June": 6,     "Jun": 6,
            "July":7,      "Jul": 7,
            "August":8,    "Aug": 8,
            "September":9, "Sep": 9,
            "October":10,  "Oct": 10,
            "November":11, "Nov": 11,
            "December":12, "Dec": 12,

        }

    def getMonth_Date_Year(self, month: str, date: int, year: int):
        month=month.capitalize()

        if month not in self.month_guide:
            print("Invalid month entered.")
            return

        m= self.month_guide[month]
        q= date


        if m==13 or m==14:
            year-= 1

        K = year % 100
        J = year // 100
        h = (q + (13 * (m + 1) // 5) + K + (K // 4) + (J // 4) + 5 * J) % 7

        print(f" Day : {q}")
        print(f" Month : {m}")
        print(f" Adjusted year: {year}")
        print(f"Year of the Century : {K}")
        print(f" Zero-based Century : {J}")

        days =["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
        print("The day of the week is :", days[h])


dc= DateCalculator()
#dc.getMonth_Date_Year("sep", 15, 1589)

#User Input:

month=input("Enter the month (e.g. January, Feb, August): ")
date = int(input("Enter the date: "))
year = int(input("Enter the year: "))
dc.getMonth_Date_Year(month, date, year)
