from parser import args
from validate.check_args import validate
from gitstats import display, is_not_git, get_logs, filter_logs, get_relative_count
from utils.bcolors import bcolors


def main():
    """ Check if git is initialized or not """
    if is_not_git():
        print(bcolors.fail('Git is not initialized in current folder.')+'\nPlease initialize using '+bcolors.ok('\"git init\"'))
        exit(1)

    """ Check if correct Arguments given """
    all_correct = validate(
        args.before, args.after, args.frequency, args.author, args.reverse
    )
    if not all_correct:
        exit(1)

    """ Program start """
    logs = []
    try:
        logs = get_logs(args.before, args.after, args.reverse)
    except Exception as e:
        print(f"error running 'git log': {e}")
        exit(1)
    
    if(len(logs)<1):
        print(bcolors.fail("No commits to plot"))
        exit(0)
    
    filtered = filter_logs(logs, args.author, args.frequency)
    normalized_logs = get_relative_count(filtered)
    
    print("%d commits over %d %s(s)\n" %(sum([filtered[f]["commits"] for f in filtered]),len(normalized_logs),args.frequency))
    display(normalized_logs)
        
   
if __name__ == "__main__":
    main()