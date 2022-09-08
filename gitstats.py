import git
from pathlib import Path
import subprocess


def is_not_git():
    """ Check if git is initialized in the repository """
    try:
        current_path = Path(__file__).parent.resolve()
        _ = git.Repo(current_path).git_dir
        return False
    except git.exc.InvalidGitRepositoryError:
        return True


def get_logs():
    """Return results of git log [args]"""

    # < day, date, author >
    args = ["git", "log", '--pretty=format:%aD,%aN']

    commit_logs = [] 
    try:
        logs = subprocess.check_output(args,shell=False,universal_newlines=True).split("\n")

        # Process each line
        for line in logs:
            day,time_stamp,author = line.split(",")
            time_stamp = f"{day} -{time_stamp}"
            commit_logs.append({"time_stamp":time_stamp,"author":author})

    except Exception as e:
        print(e)