# prior
P_notC = 0.99
P_C = 0.01

P_Pos_C = 0.9
P_Neg_notC = 0.9
P_Pos_notC = 1 - P_Pos_C

# posterior
P_C_Pos = P_C * P_Pos_C
P_notC_Pos = P_notC * P_Pos_notC

print("P_C_Pos =",P_C_Pos)
print("P_notC_Pos =",P_notC_Pos)