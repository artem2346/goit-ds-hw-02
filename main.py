from subprocess import run


def run_files():

    try:
        run(["python3", "create_table.py"])
        run(["python3", "seed.py"])
        run(["python3", "select_data.py"])
        run(["python3", "modify_data.py"])
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    run_files()
