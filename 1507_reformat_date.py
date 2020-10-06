"""
Given a date string in the form Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the range [1900, 2100].
Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.

 >>> reformatDate("20th Oct 2052")
    '2052-10-20'
>>> reformatDate("6th Jun 1933")
    '1933-06-06'
""" 

 
def reformatDate(date):
        month = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06', "Jul": '07', "Aug": '08', "Sep": '09', "Oct":'10', "Nov":'11', "Dec":'12'}
        date_string = ''
        split_date = date.split() 
        day = split_date[0]
        month_month = split_date[1]
        year = split_date[2]
        date_string += year
        date_string += '-'
        date_string += month[month_month]
        date_string += '-'
        if len(day) < 4:
            date_string += '0' + day[:1]
        else:
            date_string += day[:2]
        return date_string
        
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')