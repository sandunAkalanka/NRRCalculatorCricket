from decimal import Decimal, getcontext

print("This one is for Limited Over matches.")
print("If a team gets all out before all allocated overs, their over quota will be considered as completed.")

runs_for = input("Total runs scored: ")
overs_for = input("Total allocated overs quota to face: ")
runs_against = input("Total runs conceded: ")
overs_against = input("Total allocated overs quota to bowl: ")

getcontext().prec = 4

nrr_for = Decimal(runs_for) / Decimal(overs_for)
nrr_against = Decimal(runs_against) / Decimal(overs_against)
nrr = nrr_for - nrr_against 

print("NRR For: " , nrr_for)
print("NRR Against: " , nrr_against)
print("Final NRR: " , nrr)