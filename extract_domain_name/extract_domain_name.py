import re


def domain_name(url):
    return re.findall(r"(?:https?\:\/\/)?(?:www\.)?([^\.]+)\.", url)[0]
