from survey import AnonymousSurvey

#Define question and make survey.

question = 'What language did you first learn to speak? '
my_survey = AnonymousSurvey(question)
#Show the question and store responses
my_survey.show_question()
print("Enter 'q' to quit anytime.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

    #Show results of survey
print("\nThank you to everyone who participated in the survey.")
my_survey.show_results()