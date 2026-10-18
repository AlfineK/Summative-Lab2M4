class Task:

    def __init__(self,title,status="Pending",assigned_to="Unassigned"):
        self.title=title
        self.status=status
        self.assigned_to=assigned_to

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if not value or not value.strip():
            raise ValueError("Task title cannot be empty")
        self._title=value.strip()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,value):
        valid_statuses=["Pending","In progress","Complete"]
        if  value not in valid_statuses:
            raise ValueError(f"Invalid status {value}.Status must be one of these:{valid_statuses}")
        self._status=value

    @property
    def assigned_to(self):
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self,value):
        if not value or not value.strip():
            self._assigned_to="Unassigned"
        self._assigned_to=value.strip()

    def to_dict(self):
        return {
            "title":self.title,
            "status":self.status,
            "assigned_to":self.assigned_to
        }
    