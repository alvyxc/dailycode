
#There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N,
#write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

#For
#example,
#if N is 4, then there are 5 unique ways:

#    1, 1, 1, 1
#    2, 1, 1
#    1, 2, 1
#    1, 1, 2
#    2, 2


import argparse


def num_steps(steps):
    step_1 = [[1]]
    step_2 = [[1, 1], [2]]

    if steps == 1:
        return step_1

    if steps == 2:
        return step_2

    last_step = step_2
    last_last_step = step_1
    for i in range(3, steps+1):
        c_steps = []
        for s in last_last_step:
            if sum(s) + 2 == i:
                c_step = s.copy()
                c_step.append(2)
                c_steps.append(c_step)
        for s in last_step:
            if sum(s) + 1 == i:
                c_step = s.copy()
                c_step.append(1)
                c_steps.append(c_step)
        last_last_step = last_step
        last_step = c_steps

    return last_step


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, required=True,
                        help="number of steps")

    args = parser.parse_args()
    steps = num_steps(args.steps)
    print(steps)