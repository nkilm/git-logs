import argparse

from gitstats import is_not_git,get_logs


def main():
    if(is_not_git()):
        print("Git is not initialized. Please initialize using \"git init\"")
    
    p = argparse.ArgumentParser(description="Display information from .git")
    args = p.parse_args()

    
main()
