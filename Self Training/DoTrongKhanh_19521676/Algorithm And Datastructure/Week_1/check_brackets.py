from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            pass

        if next in ")]}":
            pass


def main():
    text = input()
    mismatch = find_mismatch(text)


if __name__ == "__main__":
