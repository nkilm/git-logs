import argparse

p = argparse.ArgumentParser(description="Display information from .git")

p.add_argument("-p", "--periodicity", action="store", dest="periodicity",
                   type=str, required=False, default="month",
                   choices=["day", "week", "month", "year"])

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