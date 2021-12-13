from argparse import ArgumentParser
import json
from os import path


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument("-f", "--file", default="")
    ap.add_argument("-M", "--major", default=0)
    ap.add_argument("-m", "--minor", default=0)

    args = ap.parse_args()

    if path.exists(args.file):
        with open(args.file, "r") as f:
            versions = json.load(f)
    else:
        versions = {}
    if args.major not in versions:
        versions[args.major] = {}
    if args.minor not in versions[args.major]:
        versions[args.major][args.minor] = -1

    versions[args.major][args.minor] += 1

    with open(args.file, "w") as f:
        json.dump(versions, f, indent=2)

    print(versions[args.major][args.minor])
