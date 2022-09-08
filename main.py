import argparse

from gitstats import is_not_git, get_logs


def main():
    if is_not_git():
        print('Git is not initialized. Please initialize using "git init"')

    p = argparse.ArgumentParser(description="Display information from .git")

    p.add_argument("-u", "--author", action="store", dest="author",
                   type=str, required=False, default="",
                   help="filter by author's e-mail (substring)")

    p.add_argument("-a", "--after", action="store", dest="after",
                   type=str, required=False, default="",
                   help="after date (yyyy-mm-dd hh:mm)")

    p.add_argument("-b", "--before", action="store", dest="before",
                   type=str, required=False, default="",
                   help="before date (yyyy-mm-dd hh:mm)")

    p.add_argument("-r", "--reverse", action="store", dest="reverse",
                   type=bool, required=False, default=False,
                   help="reverse date order")
    
    args = p.parse_args()

    """Program start"""
    items = []
    try:
        items = get_logs(args.after, args.before, args.reverse)
        
    except Exception as e:
        print("error running 'git log': %s" % (e,))
        return

if __name__ == "__main__":
    main()