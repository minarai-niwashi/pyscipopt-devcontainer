"""pyscipoptのExample"""

from pyscipopt import Model

model = Model("Example")  # model name is optional

x = model.addVar("x")
y = model.addVar("y", vtype="INTEGER")
model.setObjective(x + y)
model.addCons(2 * x - y * y >= 0)
model.optimize()
sol = model.getBestSol()
print(f"x: {sol[x]}")
print(f"y: {sol[y]}")
