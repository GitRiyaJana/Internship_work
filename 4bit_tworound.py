import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("two_round_aes_4bit")

# Variables for initial state (round 0)
x = [model.addVar(vtype=GRB.BINARY, name=f"x{i}") for i in range(4)]

# Variables for state after first round (round 1)
y = [model.addVar(vtype=GRB.BINARY, name=f"y{i}") for i in range(4)]

# Variables for state after second round (round 2)
z = [model.addVar(vtype=GRB.BINARY, name=f"z{i}") for i in range(4)]

# Additional binary variable
d = model.addVar(vtype=GRB.BINARY, name="d")

# Set the objective: Dummy objective to ensure feasibility
model.setObjective(sum(x) + sum(y), GRB.MINIMIZE)
model.setObjective(sum(y) + sum(z), GRB.MINIMIZE)

# Add constraints for the first round
model.addConstr(x[0] + x[1] + x[2] + x[3] >= 1, "c0")
model.addConstr(x[0] + x[1] + x[2] + x[3] + y[0] + y[1] + y[2] + y[3] >= 5 * d, "c1")
model.addConstr(-x[0] + d - x[1] + d - x[2] + d - x[3] + d -y[0] + d - y[1] + d - y[2] + d - y[3] + d>= 0, "c2")

# Add constraints for the second round
model.addConstr(y[0] + y[1] + y[2] + y[3] + z[0] + z[1] + z[2] + z[3] >= 5 * d, "c3")
model.addConstr(-y[0] + d - y[1] + d - y[2] + d - y[3] + d -z[0] + d - z[1] + d - z[2] + d - z[3] + d >= 0, "c4")

# Optimize the model
model.optimize()

# Print the solution
if model.status == GRB.OPTIMAL:
    for v in model.getVars():
        print(f'{v.varName} {v.x}')
else:
    print("No feasible solution found")

