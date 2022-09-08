from gitstats import is_not_git, get_logs, filter_logs, get_relative_count
from parser import args


def main():
    if is_not_git():
        print('Git is not initialized. Please initialize using "git init"')

    """Program start"""
    logs = []
    try:
        logs = get_logs(args.after, args.before, args.reverse)
    except Exception as e:
        print(f"error running 'git log': {e}")
        exit(1)

    filtered = filter_logs(logs, args.author, args.frequency)
    normalized_logs = get_relative_count(filtered)


if __name__ == "__main__":
    main()
