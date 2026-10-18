import argparse
from utils.storage import load_data ,save_data
from models.user import User
from models.project import Project
from models.task import Task

def main():
    parser=argparse.ArgumentParser(description="Command-Line Project Management Tool")
    subparsers=parser.add_subparsers(dest="command", help="Available commands")

    #1.add user-I'm keeping the notes for revising because I'm new to this
    parser_user=subparsers.add_parser("add-user", help="Add a new user")
    parser_user.add_argument("--name", required=True, help="User's name")
    parser_user.add_argument("--email", required=True, help="User's email")

    #2List users
    subparsers.add_parser("list-users", help="List all users")

    #3.Add project
    parser_proj=subparsers.add_parser("add-project",help="Add a project to a user")
    parser_proj.add_argument("--user", required=True, help="User's email or name")
    parser_proj.add_argument("--title", required=True, help="Project title")
    parser_proj.add_argument("--description" ,required=True, help="Project description")
    parser_proj.add_argument("--due", required=True, help="Project due date (YYYY-MM-DD)")

    #4. List projects
    parser_list_proj=subparsers.add_parser("list-projects", help="List projects for a user")
    parser_list_proj.add_argument("--user", required=True, help="user's email or name")

    #5.Add task
    parser_task=subparsers.add_parser("add-task",help="Add task to a project")
    parser_task.add_argument("--user", required=True,help="User's email or name")
    parser_task.add_argument("--project", required=True,help="Project title")
    parser_task.add_argument("--title", required=True, help="Task title")
    parser_task.add_argument("--assigned",default="Unassigned", help="Assigned person")

    #6.Complete tasks
    parser_comp=subparsers.add_parser("complete-task", help="mark a task as complete")
    parser_comp.add_argument("--user",required=True, help="user's email or name")
    parser_comp.add_argument("--project",required=True, help="Project Title")
    parser_comp.add_argument("--task", required=True,help="Task title")

    args=parser.parse_args()
    users=load_data()

    if args.command=="add-user":
        if any(u.email ==args.email for u in users):
            print(f"Error: User with email {args.email} already exists")
            return

        users.append(User (name=args.name, email=args.email))
        save_data(users)
        print(f"Success. User {args.name!r} added successfully")

    elif args.command=="list-users":
        if not users:
            print("No users found in the system")
            return
        print("Registered users:")
        for u in users:
            print(f"-{u.name} ({u.email}) [Projects:{len(u.projects)}]")

    elif args.command=="add-project":
        user=next((u for u in users if u.email==args.user or u.name==args.user),None)
        if not user:
            print(f"Error:User {args.user!r} not found")
            return
        user.projects.append(Project(title=args.title,description=args.description, due_date=args.due))
        save_data(users)
        print(f"Success! project{args.title!r} added to {user.name!r}")

    elif args.command=="list-projects":
        user=next((u for u in users if u.email==args.user or u.name==args.user),None)
        if not user:
            print(f"Error: user{args.user!r} not found")
            return
        if not user.projects:
            print(f"No projects found for {user.name}")
            return
        print(f"Projects for {user.name}:")
        for p in user.projects:
            print(f"\n{p.title} (Due:{p.due_date})")
            print(f"Description: {p.description}")
            print("Tasks:")
            if not p.tasks:
                print("-No tasks assigned")
            for t in p.tasks:
                status_icon="+" if t.status=="Complete" else "**"
                print(f"{status_icon} {t.title} [Assigned:{t.assigned_to}]" )

    elif args.command =="add-task":
        user=next((u for u in users if u.email==args.user or u.name==args.user),None)
        if not user:
            print(f"Error: user{args.user!r} not found")
            return
        project=next((p for p in user.projects if p.title == args.project),None)
        if not project:
            print(f"Error: {args.project!r} not found")
            return
        project.tasks.append(Task(title=args.title ,assigned_to= args.assigned))
        save_data(users)
        print(f"Success! Task {args.title!r} added to {project.title!r}")

    elif args.command=="complete-task":
        user=next((u for u in users if u.email==args.user or u.name==args.user),None)
        if not user:
            print(f"Error: user{args.user!r} not found")
            return
        project=next((p for p in user.projects if p.title == args.project),None)
        if not project:
            print(f"Error: {args.project!r} not found")
            return
        task=next((t for t in project.tasks if t.title==args.task),None)
        if not task:
            print(f"Error: Task {args.task!r} not found")
            return
        task.status="Complete"
        save_data(users)
        print(f"Success! Task{task.title!r} marked as complete")

    else:
        parser.print_help()

if __name__=="__main__":
    main()

    