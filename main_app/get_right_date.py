import datetime


# right now, I have to put these in manually. Can I set it up so that it populates when
# a lesson is generated? Do a Lesson.objects.all() then get out the .date?
# and it should be in this format too, because that's how the anchors work
# maybe I should make this into some kind of function....

# get out all the dates from the Lesson objects and return them as a list of formatted dates: 'March 28, 2018'
def format_lesson_dates():
    pass

# lesson_dates = get_lesson_dates()
lesson_dates = ['March 2, 2018','March 4, 2018','March 6, 2018','March 28, 2018']


def get_next_lesson_date(lsn_dates):
    # today = datetime.date.today() # use this to set website to actual time-now. Just uncomment
    today = datetime.date(2018,3,10) # use this to assign arbitrary date for testing.

    for i in range(30):
        formatted_time = today.strftime('%B %d, %Y').replace(" 0", " ")
        if formatted_time not in lsn_dates:
            today += datetime.timedelta(days=1)
            print("Not correct: " + formatted_time)
        else:
            print(formatted_time)
            return formatted_time
            

# will eventutally move this thing into another file, or just import this function as needed?
x = get_next_lesson_date(lesson_dates)
