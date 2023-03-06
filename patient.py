class Patient:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.full_name = self.first_name + self.last_name

    def is_at_risk(self):
        if self.sex == 'M':
            return self.age > 60
        else:
            return self.age > 70

    def has_cancer(self, cancer_score):
        if self.age > 60 and cancer_score > 60:
            return True
        elif cancer_score > 120:
            return True
        else:
            return False

    def is_family(self, patient):
        if not isinstance(patient, Patient):
            return f'{patient}, is not patient object'
        return self.last_name == patient.last_name

    def __str__(self):
        return f'{self.full_name}, {self.age}, {self.sex}'

    def __repr__(self):
        return f'{self.full_name}'
