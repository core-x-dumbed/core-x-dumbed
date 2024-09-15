import datetime 

class Todo:

    def __init__(self, content, deadline, priority):
        self.entry_date = datetime.datetime.now()
        self.content = content
        self.deadline: datetime = deadline
        self.priority = priority