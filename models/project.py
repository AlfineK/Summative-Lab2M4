from models.task import Task


class Projects:
    _projects={}
    def __init__(self,title,description,due_date, tasks=None):
        self.title=title
        self.description=description
        self.due_date=due_date
        self.tasks=tasks if tasks is not None else []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,value):
        if not value or not value.strip():
            raise ValueError("Project Title cannot be empty.")
        self._title=value.strip()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self,value):
        if not value or not value.strip():
            self._description="No description provided"
        else:
            self._description=value.strip()

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self,value):
        if not value or not value.strip():
            raise ValueError("No due date provided")
        self._due_date=value.strip()

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self,value):
        if value is None:
            self._tasks=[]
        elif isinstance(value,list):
            self._tasks=value
        else:
            raise ValueError("Tasks must be provided as a list")

    def to_dict(self):
        return {
            "title":self.title,
            "description":self.description,
            "due_date":self.due_date,
            "tasks":[task.to_dict() for task in self.tasks]
        }

    @classmethod
    def from_dict(cls,data):
        tasks=[Task.from_dict(t) for t in data.get("tasks",[])]
        return cls (
            title=data.get("title"),
            description=data.get("description"),
            due_date=data.get("due_date"),
            tasks=tasks

        )

    @classmethod
    def get(cls, project_title):
        return cls._projects.get(project_title)

    @classmethod
    def all(cls):
        return list(cls._projects.values())

    def __repr__(self):
        return f"Project(title={self.title!r},description={self.description!r},due_date={self.due_date!r}, tasks_count={len(self.tasks)!r})"