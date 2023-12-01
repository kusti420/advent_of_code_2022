if __name__ == "__main__":
    # import os; exec(open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}\\setup.txt").read())
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    # print(idk)
    import os; exec(open(f"{idk}\\setup.txt").read())

if __name__ != "__main__":
    print("That would break the script. Please run it directly.")
