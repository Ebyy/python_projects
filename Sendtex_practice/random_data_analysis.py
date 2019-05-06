import csv
from datetime import datetime as dt
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


enrollments_filename = "\\Users\\Home\\Downloads\\enrollments.csv"
submissions_filename = "\\Users\\Home\\Downloads\\project_submissions.csv"
engagements_filename = "\\Users\\Home\\Downloads\\daily_engagement.csv"

with open(enrollments_filename, 'r') as f:
    reader = csv.DictReader(f)
    enrollments = list(reader)

with open(submissions_filename, 'r') as f_1:
    reader_1 = csv.DictReader(f_1)
    project_submissions = list(reader_1)

with open(engagements_filename, 'r') as f_2:
    reader_2 = csv.DictReader(f_2)
    daily_engagements = list(reader_2)


def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)


def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')


for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['join_date'] = parse_date(enrollment['join_date'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])

# print(enrollments[0])

for submission in project_submissions:
    submission['creation_date'] = parse_date(submission['creation_date'])
    submission['completion_date'] = parse_date(submission['completion_date'])

# print(project_submissions[10])
for engagement in daily_engagements:
    engagement['utc_date'] = parse_date(engagement['utc_date'])
    engagement['num_courses_visited'] = int(float(engagement['num_courses_visited']))
    engagement['total_minutes_visited'] = int(float(engagement['total_minutes_visited']))
    engagement['lessons_completed'] = int(float(engagement['lessons_completed']))
    engagement['projects_completed'] = int(float(engagement['projects_completed']))

# print(daily_engagements[3])

# function to get students unique data


def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

# Trying to rename daily engagement['acct'] to daily_engagement[account_key']

for engagement in daily_engagements:
    engagement['account_key'] = engagement['acct']
    del engagement['acct']

# finding the differences between the rows in the dataset and the unique-students dataset

# print("The number of rows in the enrollment table is " + str(len(enrollments)))
#

unique_enrolled_students = get_unique_students(enrollments)
#
# print("The number of unique students enrolled is " + str(len(unique_enrolled_students)) + '.\n')
#
# print("The number of rows in the engagement table is " + str(len(daily_engagements)))
#
unique_engaged_students = get_unique_students(daily_engagements)
#
# print("The actual number of students engaged is " + str(len(unique_engaged_students)) + '.\n')
#
# print("The number of rows in the project submission table is " + str(len(project_submissions)))

unique_project_submissions = get_unique_students(project_submissions)
# print("The number of projects actually submitted is " + str(len(unique_project_submissions)))
# #
# missing_engagement_data = set()
# for engagement in daily_engagements:
#     if engagement['num_courses_visited'] >= 1:
#         continue
#     else:
#         missing_engagement_data.add(engagement['account_key'])
#
#
# print(len(missing_engagement_data))

missing_engagement_data2 = set()
for enrollment_record in enrollments:
    student = enrollment_record['account_key']
    if student not in unique_engaged_students and enrollment_record['days_to_cancel'] != 0:
        # print(enrollment_record)
        missing_engagement_data2.add(student)
    elif student not in unique_engaged_students and enrollment_record['days_to_cancel'] == int:
        # print(enrollment_record)
        missing_engagement_data2.add(student)
# print(len(missing_engagement_data2))

udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])

# print(len(udacity_test_accounts))


def remove_test_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data


# Rid the data of test account by calling the function above on all 3 datasets
non_udacity_enrollments = remove_test_accounts(enrollments)
non_udacity_engagements = remove_test_accounts(daily_engagements)
non_udacity_submissions = remove_test_accounts(project_submissions)

# print(len(non_udacity_engagements))
# print(len(non_udacity_enrollments))
# print(len(non_udacity_submissions))

paid_students = {}
for enrollment in non_udacity_enrollments:
    if not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7:
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if account_key not in paid_students or enrollment_date > paid_students[account_key]:
            paid_students[account_key] = enrollment_date

# print(len(paid_students))

# trying to make more sense of the data by looking at
# student records within one week so have to create variables
# and adjust our data to show just one week activity


def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7 and time_delta.days >= 0


def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data


paid_enrollments = remove_free_trial_cancels(enrollments)
paid_engagements = remove_free_trial_cancels(daily_engagements)
paid_submissions = remove_free_trial_cancels(project_submissions)

# print(len(paid_enrollments))
# print(len(paid_engagements))
# print(len(paid_submissions))

# ANALYSING THE NUMBER OF COURSES VISITED
for record in paid_engagements:
    if record['num_courses_visited'] > 0:
        record['has_visited'] = 1
    else:
        record['has_visited'] = 0

paid_engagement_in_first_week = []

for engagement_record in paid_engagements:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']
    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

# print(len(paid_engagement_in_first_week))

# print(paid_engagement_in_first_week[0])


# to look at the average time spent in the classroom by all the students


def group_data(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

# FOR TOTAL MINUTES ENGAGED BY ACCOUNT IN THE FIRST WEEK
engagement_by_account = group_data(paid_engagement_in_first_week,
                                   'account_key')


def sum_grouped_items(grouped_data, field_name):
    totalled_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        totalled_data[key] = total
    return totalled_data


total_minutes_by_account = sum_grouped_items(engagement_by_account, 'total_minutes_visited')
lessons_completed_by_account = sum_grouped_items(engagement_by_account, 'lessons_completed')


def prepare_overall_data(data_dictionary):
    dictionaried_list = data_dictionary.values()
    overall_data = []
    for data_value in dictionaried_list:
        overall_data.append(data_value)
    return overall_data

overall_minutes_engaged = prepare_overall_data(total_minutes_by_account)
overall_lessons_completed = prepare_overall_data(lessons_completed_by_account)


def describe_data(data):
    print("Mean: " + str(np.mean(data)))
    print("Standard Deviation: " + str(np.std(data)))
    print("Min Value: " + str(np.min(data)))
    print("Max Value: " + str(np.max(data)))
    plt.hist(data)
    plt.show()


# ~~~~~~~ NOW WE CAN LOOK MORE INTO THE MINUTES ENGAGED AND LESSONS COMPLETED ~~~~~

# describe_data(overall_minutes_engaged)
# describe_data(overall_lessons_completed)


# a really high max(overall_minutes) that was greater than
# a week's worth was gotten so we have to examine what is being
#  calculated and find what went wrong by print the student's
# engagement record for the first week.
student_with_max_minutes = None
max_minutes = 0

for student, total_minutes in total_minutes_by_account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_max_minutes = student

print(max_minutes)

# for engagement_record in paid_engagement_in_first_week:
#     if engagement_record['account_key'] == student_with_max_minutes:
#         print(engagement_record)

# resultant check printed more than records beyond one
# week so have to adjust the code written earlier to enable
# it specifically check for records within one week of enrolling

# FOR LESSONS COMPLETED IN THE FIRST WEEK BY ACCOUNT
#
# lessons_completed_by_account = {}
#
# for account_key,lessons_completed in engagement_by_account.items():
#     lessons_record = 0
#     for completed_lesson in engagement_for_student:
#         lessons_record =+ completed_lesson['lessons_completed']
#     lessons_completed_by_account[account_key] = lessons_record
#
# #print(lessons_completed_by_account)
#
# lessons_completed_list = lessons_completed_by_account.values()
#
# overall_completed_lessons = []
#
# for item in lessons_completed_list:
#     overall_completed_lessons.append(item)

# print(np.mean(overall_completed_lessons))
# print(np.std(overall_completed_lessons))
# print(np.min(overall_completed_lessons))
# print(np.max(overall_completed_lessons))

# ~~~~~~~ EXPLORING THE DATA ON DAYS VISITED BY THE STUDENT ~~~~~~~~

days_visited_by_account = sum_grouped_items(engagement_by_account, 'has_visited')

overall_days_visited_by_student = prepare_overall_data(days_visited_by_account)

# describe_data(overall_days_visited_by_student)

# ~~~~~~~~~~SPLITTING THE DATA INTO THOSE WHO PASSED AND THOSE THAT DIDN'T THE FIRST PROJECT(ON SUBWAY) ~~~~~~~~~

subway_project_lesson_keys = ['746169184', '3176718735']
distinguished_grades = ['PASSED', 'DISTINCTION']

pass_subway_project = set()

# print(paid_submissions)
for submission_record in paid_submissions:
    project = submission_record['lesson_key']
    rating = submission_record['assigned_rating']
    if project in subway_project_lesson_keys and rating in distinguished_grades:
        pass_subway_project.add(submission_record['account_key'])

print(len(pass_subway_project))

passing_engagement = []
non_passing_engagement = []

for record in paid_engagement_in_first_week:
    if record['account_key'] in pass_subway_project:
        passing_engagement.append(record)
    else:
        non_passing_engagement.append(record)

print(len(passing_engagement))
print(len(non_passing_engagement))

# print(overall_minutes_engaged)
# print(total_minutes_by_account)
# print(lessons_completed_by_account)
# print(overall_lessons_completed)
# print(pass_subway_project)

# EXPLORE MORE INFO FROM THE DATA

# # # # # My first attempt ~~~~~~~~
# minutes_spent_trend_of_passed = []
#
# for student, total_minutes in total_minutes_by_account.items():
#     if student in pass_subway_project:
#         minutes_spent_trend_of_passed.append(total_minutes)
#
# print(np.mean(minutes_spent_trend_of_passed))
# lessons_trend_of_passed = []
# for student, number_of_lessons in lessons_completed_by_account.items():
#     if student in pass_subway_project:
#         lessons_trend_of_passed.append(number_of_lessons)
#
# print(lessons_trend_of_passed)

# DISTINGUISHING THE STUDENTS THAT PASSED FROM THOSE WHO DIDNT WILL HELP US EXPLORE FURTHER
# ~~~~~~~~~~~ NOW LOOKING AT THE TREND ON MINUTES SPENT, LESSONS COMPLETED FOR BOTH PARTIES

# FIRST THE DIFFERENCES IN THE TOTAL MINUTES SPENT

passing_engagement_by_account = group_data(passing_engagement, 'account_key')
non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')

total_minutes_spent_by_passing = sum_grouped_items(passing_engagement_by_account, 'total_minutes_visited')
total_minutes_spent_by_non_passing = sum_grouped_items(non_passing_engagement_by_account, 'total_minutes_visited')

overall_minutes_spent_by_passing = prepare_overall_data(total_minutes_spent_by_passing)

overall_minutes_spent_by_non_passing = prepare_overall_data(total_minutes_spent_by_non_passing)
# print("\nFor Passing Students")
# describe_data(overall_minutes_spent_by_passing)
# print("\nFor Non-Passing Students")
# describe_data(overall_minutes_spent_by_non_passing)

# ~~~~~ NOW  THE DIFFERENCE IN THE LESSONS COMPLETED BY BOTH ~~~~~~~~~

lessons_completed_by_passing = sum_grouped_items(passing_engagement_by_account, 'lessons_completed')
lessons_completed_by_non_passing = sum_grouped_items(non_passing_engagement_by_account, 'lessons_completed')

overall_lessons_completed_by_passing = prepare_overall_data(lessons_completed_by_passing)
overall_lessons_completed_by_non_passing = prepare_overall_data(lessons_completed_by_non_passing)

# print("\nLESSONS: For Passing students")
# describe_data(overall_lessons_completed_by_passing)
#
# print("\nLESSONS: For Non-Passing Students")
# describe_data(overall_lessons_completed_by_non_passing)

# ~~~~~ THEN FOR DAYS VISITED

days_visited_by_passing = sum_grouped_items(passing_engagement_by_account, 'has_visited')
days_visited_by_non_passing = sum_grouped_items(non_passing_engagement_by_account, 'has_visited')

overall_days_visited_by_passing = prepare_overall_data(days_visited_by_passing)
overall_days_visited_by_non_passing = prepare_overall_data(days_visited_by_non_passing)

# print("DAYS_VISITED: For Passing")
# describe_data(overall_days_visited_by_passing)
#
# print("\nDAYS VISITED: For Non-Passing")
# describe_data(overall_days_visited_by_non_passing)
