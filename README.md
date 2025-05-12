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
- P: Set of plants
- I: Set of candidate DCs
- J: Set of regional DCs (RDCs)

**Parameters**
- Dⱼ: Weekly demand at RDCⱼ
- Cᵢ: Capacity of DCᵢ (barrels/week)
- fᵢ: Fixed weekly cost of opening DCᵢ
- cᵢⱼ: Cost per barrel from DCᵢ to RDCⱼ (handling + outbound transport)
- vₚᵢ: Cost per barrel from plantₚ to DCᵢ (production + inbound transport)

**Decision Variables**
- yᵢ ∈ {0, 1}: 1 if DCᵢ is opened, 0 otherwise
- xᵢⱼ ≥ 0: Quantity shipped from DCᵢ to RDCⱼ
- zₚᵢ ≥ 0: Quantity shipped from plantₚ to DCᵢ

**Objective Function**: Minimize total weekly cost= ∑ᵢfᵢyᵢ + ∑ᵢ∑ⱼcᵢⱼ.xᵢⱼ + ∑ₚ∑ᵢvₚᵢ.zₚᵢ

**subject to constraints:**
- Demand satisfaction (RDCs): ∑ᵢxᵢⱼ = Dⱼ    ∀ⱼ ∈ J
- DC capacity (only if opened): ∑ⱼ xᵢⱼ ≤ Cᵢ.yᵢ    ∀ᵢ ∈ I
- Flow conservation at DCs (input = output): ∑ₚ zₚᵢ = ∑ⱼ xᵢⱼ    ∀ᵢ ∈ I
- Non-negativity constraints: xᵢⱼ, zₚᵢ ≥ 0  ∀ᵢ ∈ I, ∀ⱼ ∈ J, ∀ₚ ∈ P;   yᵢ ∈ {0, 1} ∀ᵢ ∈ I

To view the model declaration in Python, open the file ...

## ✅ Model Results

After solving the facility location optimization problem using Gurobi, the model identified the optimal configuration of distribution centers (DCs) and shipment flows that minimize total operational cost while satisfying all customer demands. To view the data handling and model running code, view the file ...

**Key results of the model:**

- **Total cost:** 68,264.50$, in that
    - Fixed DC Costs: 20000.00$
    - Inbound Costs: 9825.00$
    - Outbound Costs: 38439.50$
      
- **Opened DCs**: 3 DCs (NA,SP, WO)
  
- **Inbound shipments (plant → DC):**
     BFP → NA: 500.0 barrels;
     SCP → SP: 500.0 barrels;
     SCP → WO: 1000.0 barrels.

- **Outbound shipments (DC → RDC):**
     NA → BR: 50.0 barrels;
     NA → CO: 80.0 barrels;
     NA → MN: 110.0 barrels;
     NA → NA: 140.0 barrels;
     NA → PO: 120.0 barrels;
     SP → HA: 130.0 barrels;
     SP → NH: 140.0 barrels;
     SP → NL: 30.0 barrels;
     SP → SP: 200.0 barrels;
     WO → BO: 450.0 barrels;
     WO → BR: 10.0 barrels;
     WO → NL: 40.0 barrels;
     WO → PR: 310.0 barrels;
     WO → WO: 190.0 barrels.
  
- **All RDC demands are fully satisfied**.
  
-**All DC capacity and flow constraints respected**.

## 🤝 Project Closing & Collaboration
This project explores a facility location problem using small-scale synthetic data, inspired by academic case studies. It serves as a practical testbed for formulating and solving optimization problems with Python and Gurobi.

**Feel free to:**
- Comment or open issues to discuss ideas
- Fork and experiment with model extensions
- Collaborate on improvements or real-world applications

I'm always open to feedback, suggestions, or collaboration opportunities — especially in the areas of supply chain analytics, optimization, and data-driven operations.

