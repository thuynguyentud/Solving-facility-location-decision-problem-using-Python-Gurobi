# 📦 Facility Location Optimization with Python & Gurobi

This project is a hands-on implementation of the **Facility Location Problem (FLP)** using Python and the Gurobi optimization solver. The scenarios and data used are based on a case study from the [MITx MicroMasters program in Supply Chain Management](https://micromasters.mit.edu/scm/), module [Supply Chain Design](https://www.edx.org/learn/supply-chain-design/massachusetts-institute-of-technology-supply-chain-design), which I took in 2022. This project is for educational and personal portfolio use only.

---

## 🧠 Problem Definition: Facility Location Problem (FLP)

The **Facility Location Problem (FLP)** is a classic optimization problem in supply chain management. It involves choosing the optimal locations for facilities (e.g., warehouses, distribution centers, plants) and determining product flows to minimize total operational costs while satisfying customer demands and capacity constraints.

In this project, the FLP is formulated as a **mixed-integer linear program (MILP)** with the objective to minimize:
- Fixed costs of opening distribution centers (DCs),
- Variable handling and shipping costs from plants to DCs and from DCs to regional demand points,
- While ensuring all customer demands are met and no DC exceeds its capacity.

---

## 🏭 Case Study:
**New England Root Beer Distributors (NERD)** is a historic beverage company that has grown from a small, family-run root beer maker into a regional leader in the Northeastern United States. Originally operating multiple small plants, NERD consolidated production into a **single modern manufacturing facility in Scranton, Pennsylvania (SCP)** to reduce costs and improve scalability.

### 🚚 Supply Chain Structure
NERD’s current supply chain includes:
- **1 main manufacturing plant** in Scranton, PA; and potential addition of a **second plant** in Bellows Falls, VT (BFP), which could decentralize production
- **5 candidate distribution centers (DCs)** in New England
- **12 regional demand points (RDCs)** that receive shipments from the DCs

![NERD supply chain network](https://github.com/user-attachments/assets/d7d0581d-429f-4967-a62c-36354d45f4f2)

The supply chain operates in two stages:
1. **Inbound logistics**: shipping root beer barrels from plant(s) to DCs.
2. **Outbound logistics**: Local couriers deliver barrels from DCs to RDCs.

---

### ⚠️ Challenges Faced
Despite operational success at the Scranton plant, NERD's **New England distribution network is inefficient and fragmented**, with facilities added over time through mergers and acquisitions rather than design.

NERD management has raised concerns such as:
- Are there too many DCs currently in operation?
- Should the Bellows Falls plant be used to support distribution?
- Are service levels and capacities appropriate under current and future demand?
- Can the overall network cost be reduced through better design?

Read in detail about the case study and relevant data at [The case study file](case_study_file.pdf). This file belongs to Caplice, C. (2016). *New England Root Beer Distributors (NERD4) Case Study*. MITx MicroMasters in Supply Chain Management.
---

### 💡 Solution Approach in This Project

To support decision-making, this project builds a **network design optimization model** to:
- Determine which DCs should remain open (or be closed),
- Optimize the flow of goods from plant(s) to DCs to RDCs,
- Evaluate the cost-effectiveness of using the Bellows Falls plant,
- Ensure customer demand is satisfied without exceeding facility capacities,
- Minimize total system cost, including fixed, variable, and transportation costs.

---

## 🧩 Main Project Tasks

- ✅ **Model the supply chain network** using mathematical programming
- ✅ **Build and solve the MILP model** with Python and Gurobi
- ✅ **Decide which DCs to open** by running the model

---

## 🚀 Tools Used

- **Python** (data handling & model setup)
- **Gurobi** (optimization solver). This project used a free academic license from [Gurobi Optimizer](https://www.gurobi.com/)

---

## 🧮 Mathematical Model
This problem is modeled as a Mixed Integer Linear Program (MILP) to determine optimal facility locations, flows, and total cost minimization.

**Sets**
P: Set of plants
I: Set of candidate distribution centers (DCs)
J: Set of regional demand centers (RDCs)

Parameters
𝐷
𝑗
D 
j
​
 : Weekly demand at RDC j ∈ J

C_i: Capacity of DC i ∈ I (barrels/week)

f_i: Fixed weekly cost of opening DC i

c_ij: Cost per barrel from DC i to RDC j (handling + outbound transport)

v_pi: Cost per barrel from plant p ∈ P to DC i (production + inbound transport)
