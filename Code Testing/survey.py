class AnonymousSurvey():
    """Collect anonymous answers to survey question."""


    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses =[]


    def show_question(self):
        """Show survey question."""
        print(self.question)


    def store_response(self,new_response):
        """Store a single reponse to the survey to list."""
        self.responses.append(new_response)


    def show_results(self):
        """Show all responses that have been given."""
        print("Survey results: ")
        for response in self.responses:
            print("- " + response)