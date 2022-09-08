from dis import dis
from gitstats import display, is_not_git, get_logs, filter_logs, get_relative_count
from parser import args
from validate.check_args import validate


def main():
    if is_not_git():
        print('Git is not initialized. Please initialize using "git init"')

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

    filtered = filter_logs(logs, args.author, args.frequency)
    normalized_logs = get_relative_count(filtered)

    display(normalized_logs)


if __name__ == "__main__":
    main()
