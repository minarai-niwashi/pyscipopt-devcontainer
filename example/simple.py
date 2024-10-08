"""pyscipoptのExample"""

from pyscipopt import Model


def main():
    model = Model("Example")  # model name is optional

    x = model.addVar("x")
    y = model.addVar("y", vtype="INTEGER")
    model.setObjective(x + y)
    model.addCons(2 * x - y * y >= 0)
    model.optimize()
    sol = model.getBestSol()
    return sol[x], sol[y]


if __name__ == "__main__":
    x, y = main()
    print(f"x: {x}")
    print(f"y: {y}")
