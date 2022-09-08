import git
import sys
import subprocess
from pathlib import Path
from collections import OrderedDict
from datetime import datetime


def is_not_git() -> bool:
    """Check if git is initialized in the repository"""
    try:
        current_path = Path(__file__).parent.resolve()
        _ = git.Repo(current_path).git_dir
        return False
    except git.exc.InvalidGitRepositoryError:
        return True


def get_logs(before="", after="", reverse="") -> list:
    """Return results of git log [args]"""

    # < day, date, author >
    args = ["git", "log", "--pretty=format:%ai,%aN"]

    commit_logs = []
    try:
        if after:
            args.append("--after=%s" % (after,))
        if before:
            args.append("--before=%s" % (before,))

        logs = subprocess.check_output(
            args, shell=False, universal_newlines=True
        ).split("\n")

        # Process each line
        for line in logs:
            time_stamp, author = line.split(",")
            commit_logs.append({"time_stamp": time_stamp, "author": author})

        if reverse:
            return commit_logs.reverse()

        return commit_logs

    except Exception as e:
        print(e)


def filter_logs(logs: list, author: str, frequency="day") -> dict:
    """Filter the logs based on author and frequency(day, week, month, year)"""

    commit_count_by_freq = OrderedDict()

    for commit_info in logs:
        commit_date = commit_info["time_stamp"].split(" ")[0]

        is_weekend = False

        if frequency == "week":
            # %V gives number of weeks so far in a given year
            commit_date = datetime.strptime(commit_date, "%Y-%m-%d").strftime("%Y/%V")
        elif frequency == "month":
            commit_date = commit_info["time_stamp"][:7]  # YYYY-MM
        elif frequency == "year":
            commit_date = commit_info["time_stamp"][:4]  # YYYY
        else:
            # return the day of the week
            is_weekend = datetime.strptime(commit_date, "%Y-%m-%d").weekday() > 4
            # Monday=0, Tuesday=1, Wednesday=2 and so on..

        if author != "":
            if author not in commit_info["author"]:
                continue

        if commit_date not in commit_count_by_freq:
            # Add entry for that commit date
            commit_count_by_freq[commit_date] = {
                "time_stamp": commit_info["time_stamp"],
                "commits": 0,
                "weekend": is_weekend,
            }

        # Entry already exists for that commit date so increment
        commit_count_by_freq[commit_date]["commits"] += 1
    return commit_count_by_freq


def normalize(value: int, xmin: int, xmax: int) -> float:
    
    return float(value - xmin) / float(xmax - xmin)

def get_relative_count(filtered_commits: OrderedDict) -> OrderedDict:
    """Compute normalized score/count based on given filter"""

    values = [item["commits"] for item in filtered_commits.values()]
    values.append(0) # To handle the case where only 1 value is present

    xmin = min(values)
    xmax = max(values)

    normalized_info = OrderedDict()
    
    for commit_date in filtered_commits.keys():
        normalized_info[commit_date] = filtered_commits[commit_date].copy()
        # add normalized value 
        normalized_info[commit_date]["score"] = normalize(filtered_commits[commit_date]["commits"], xmin, xmax)

    return normalized_info