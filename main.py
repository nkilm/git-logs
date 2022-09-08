from gitstats import *


def main():
    if(is_not_git()):
        print("Git is not initialized. Please initialize using \"git init\"")
    
    p = argparse.ArgumentParser(description="Display information from .git")
    args = p.parse_args()

    
main()
