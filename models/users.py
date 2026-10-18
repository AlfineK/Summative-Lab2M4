from models.project import Projects

class Users:
    _customers={}
    def __init__(self,name,email,projects=None):
        self.name=name
        self.email=email
        self.projects=projects if projects is not None else []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not value or not value.strip():
            raise ValueError("User Name cannot be empty")
        self._name=value.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,value):
        if not value or "@" not in value or "." not in value:
            raise ValueError("Invalid email format. Email must contain @ or . in the format")
        self._email=value.strip()

    @property
    def projects(self):
        return self._projects

    @projects.setter
    def projects(self,value):
        if value == None:
            self._projects=[]
        elif isinstance(value,list):
            self._projects=value
        else:
            raise ValueError("Projects must be provided as a list")

    def to_dict(self):
        return {
            "name":self.name,
            "email":self.email,
            "projects":[project.to_dict() for project in self.projects]
        }