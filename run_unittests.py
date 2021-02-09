import os


def run_tests():
    os.system("alembic revision --autogenerate")


if __name__ == "__main__":
    run_tests()
