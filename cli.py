import argparse

parser = argparse.ArgumentParser(description="Домен")
parser.add_argument("-n", help="Введите домен компании")
args = parser.parse_args()
print(args.n)
