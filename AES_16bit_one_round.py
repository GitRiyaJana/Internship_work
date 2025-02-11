import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("two_round_aes")

x = [model.addVar(vtype=GRB.BINARY, name=f"x{i}") for i in range(16)]
y = [model.addVar(vtype=GRB.BINARY, name=f"y{i}") for i in range(16)]
d = [model.addVar(vtype=GRB.BINARY, name=f"d{i}") for i in range(4)]

model.setObjective(sum(x) + sum(y), GRB.MINIMIZE)

# Add constraints
model.addConstr(sum(x) >= 1, "c0")
model.addConstr(x[0] + x[1] + x[2] + x[3] + y[0] + y[1] + y[2] + y[3] >= 5 * d[0], "c1")
model.addConstr(x[4] + x[5] + x[6] + x[7] + y[4] + y[5] + y[6] + y[7] >= 5 * d[1], "c2")
model.addConstr(x[8] + x[9] + x[10] + x[11] + y[8] + y[9] + y[10] + y[11] >= 5 * d[2], "c3")
model.addConstr(x[12] + x[13] + x[14] + x[15] + y[12] + y[13] + y[14] + y[15] >= 5 * d[3], "c4")

# Adjust constraints to use correct indices
for i in range(4):
    model.addConstr(-x[i] + d[0] >= 0, f"c{x[i]}")
    model.addConstr(-y[i] + d[0] >= 0, f"c{y[i]}")
for i in range(4, 8):
    model.addConstr(-x[i] + d[1] >= 0, f"c{x[i]}")
    model.addConstr(-y[i] + d[1] >= 0, f"c{y[i]}")
for i in range(8, 12):
    model.addConstr(-x[i] + d[2] >= 0, f"c{x[i]}")
    model.addConstr(-y[i] + d[2] >= 0, f"c{y[i]}")
for i in range(12, 16):
    model.addConstr(-x[i] + d[3] >= 0, f"c{x[i]}")
    model.addConstr(-y[i] + d[3] >= 0, f"c{y[i]}")

model.optimize()

if model.status == GRB.OPTIMAL:
    x_values = [var.X for var in x]
    y_values = [var.X for var in y]
    print(f"x = {x_values}")
    print(f"y = {y_values}")
else:
    print("No feasible solution found")

