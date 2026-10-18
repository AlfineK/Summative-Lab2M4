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


