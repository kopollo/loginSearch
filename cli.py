import argparse
from src.data_extracter import DataExtractor
parser = argparse.ArgumentParser(description="Домен")
parser.add_argument("-n", help="Введите домен компании")
args = parser.parse_args()
# print(args.n)

dt = DataExtractor("gazprom")
dt.save_docs()

