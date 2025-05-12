from gurobipy import Model, GRB, quicksum

def build_model(plants, dcs, rdcs, rdc_demand, dc_capacity, dc_fixed_cost, dc_var_cost, plant_var_cost, inbound_cost, outbound_cost):
    # Create a new model
    model = Model("Facility_Location")

    # Create variables
    x = model.addVars(dcs, rdcs, name="x", vtype=GRB.CONTINUOUS) #Quantities shipped from DCs to RDCs
    y = model.addVars(dcs, name="y", vtype=GRB.BINARY) #Binary variable for opening DCs (Whether DC is open)
    z = model.addVars(plants, dcs, name="z", vtype=GRB.CONTINUOUS) #Quantities shipped from Plants to DCs

    # Set objective: minimize total cost
    # Total cost includes fixed costs for opening DCs, variable costs for shipping from DCs to RDCs
    model.setObjective(
        quicksum(dc_fixed_cost[i] * y[i] for i in dcs) +
        quicksum((dc_var_cost[i] + outbound_cost[i, j]) * x[i, j] for i in dcs for j in rdcs) +
        quicksum((plant_var_cost[p] + inbound_cost[p, i]) * z[p, i] for p in plants for i in dcs),
        GRB.MINIMIZE
    )

    # Add constraints
    # C1: Meet demand at each RDC
    for j in rdcs:
        model.addConstr(quicksum(x[i, j] for i in dcs) == rdc_demand[j])
    
     # C2: Respect capacity at each DC (only if opened)
    for i in dcs:
        model.addConstr(quicksum(x[i, j] for j in rdcs) <= dc_capacity[i] * y[i])

    # C3: Flow balance at DC: In = Out
    for i in dcs:
        model.addConstr(quicksum(z[p, i] for p in plants) == quicksum(x[i, j] for j in rdcs))

    return model, x, y, z