import argparse
import git
from pathlib import Path

def is_not_git():
    """ Check if git is initialized in the repository """
    try:
        current_path = Path(__file__).parent.resolve()
        _ = git.Repo(current_path).git_dir
        return False
    except git.exc.InvalidGitRepositoryError:
        return True