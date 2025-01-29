if __name__ == "__main__":
    import os
    idk = f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}"
    year = idk.split("\\")[-1]
    idk = idk.replace(f"\\{year}", "")
    print(idk)
    exec(open(f"{idk}\\setup.txt").read())
    import time
    start = time.time()

    data = [e.split(":") for e in data]
    data = [(int(e[0]), [int(n) for n in e[1].split(" ") if n != ""])
            for e in data]

    length = set(len(line[1]) for line in data)
    ops = ("+", "*", "||")

    ops_orders = {1: set((o,) for o in ops)}
    for i in range(1, max(length)):
        ops_orders[i+1] = {order+(o,) for o in ops for order in ops_orders[i]}

    correct = set()
    for e, numbers in data:
        # print(e, numbers)
        for ops in ops_orders[len(numbers)]:
            ans = numbers[0]
            for i, o in enumerate(ops):
                if i < len(numbers)-1:
                    if o == "+":
                        ans += numbers[i+1]
                    elif o == "*":
                        ans *= numbers[i+1]
                    else:
                        ans = int(str(ans) + str(numbers[i+1]))

            if ans == e:
                print("correct", e, numbers)
                correct.add(e)
                break

    print(correct, sum(correct))
    print(time.time()-start)