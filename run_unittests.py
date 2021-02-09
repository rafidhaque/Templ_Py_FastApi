import os


def run_tests():
    os.system("python -m unittest discover -s testing -p ""*_test.py""")


if __name__ == "__main__":
    run_tests()
