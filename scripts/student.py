class Student:

    def __init__(self, name, last_name, student_mail, stundent_code, card_code, stundent_carrer):
        self.name = name
        self.last_name = last_name
        self.student_mail = student_mail
        self.stundent_code = stundent_code
        self.card_code = card_code
        self.stundent_carrer = stundent_carrer

    
    def __str__(self):
        return "%d, '%s', '%s', '%s', '%s', '%s'" % (self.stundent_code, self.card_code, self.name, self.last_name, self.student_mail, self.stundent_carrer) 