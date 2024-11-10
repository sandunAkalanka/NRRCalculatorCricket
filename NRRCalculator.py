from decimal import Decimal, ROUND_UP

print("This one is for Limited Over matches.")
print("Even if a team gets all out before all allocated overs, their over quota will be considered as completed.")

runs_for = input("Total runs by team: ")
overs_for = input("Total allocated overs quota to face: ")
runs_against = input("Total runs conceded: ")
overs_against = input("Total allocated overs quota to bowl: ")

nrr_for = float(runs_for) / float(overs_for)
nrr_against = float(runs_against) / float(overs_against)
nrr = nrr_for - nrr_against 
nrr_rounded = Decimal(nrr).quantize(Decimal('.001'),rounding = ROUND_UP)

print("Final NRR: " , nrr_rounded)
