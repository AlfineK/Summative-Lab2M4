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
    parser_proj.add_argument("--name", required=True, help="User's email or name")
    parser_proj.add_argument("--title", required=True, help="Project title")
    parser_proj.add_argument("--description" ,required=True, help="Project description")
    parser_proj.add_argument("--due", required=True, help="Project due date (YYYY-MM-DD)")