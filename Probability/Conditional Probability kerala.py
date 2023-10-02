import pandas as pd

df = pd.read_csv("kerala.csv")
df["FLOODS"] = df["FLOODS"].map({"YES": 1, "NO": 0})
df["JUN_GT_500"] = (df["JUN"] > 500).astype("int")
df["JUL_GT_500"] = (df["JUL"] > 500).astype("int")
df_small = df.loc[:, ["YEAR", "JUN_GT_500", "JUL_GT_500", "FLOODS"]]
df_small["COUNT"] = 1
P_F = (6 + 54) / (6 + 54 + 19 + 39)
P_J = (39 + 54) / (6 + 54 + 19 + 39)
P_F_intersect_J = 54 / (6 + 54 + 19 + 39)
print((df, df_small.head(), df_small.shape),(f"P(Flood): {P_F}"), (f"P(June): {P_J}"),(f"P(Flood AND June): {P_F_intersect_J}"))
P_F_J = P_F_intersect_J / P_J
print("Probailitity of flood given it rained more than 500 mm in June (P(A|B)): ")
print(f"P(Flood|June): {P_F_J}")
P_J_F = (P_F_J * P_J) / P_F
print("Probability of rain more than 500 mm in June given it flooded that year (P(B|A)): ")
print(f"P(June|Flood): {P_J_F}")
P_F = (3 + 57) / (3 + 57 + 19 + 39)
P_J = (39 + 57) / (3 + 57 + 19 + 39)
P_F_intersect_J = 57 / (3 + 57 + 19 + 39)
print(f"P(Flood): {P_F}") 
print(f"P(July): {P_J}")
print(f"P(Flood AND July): {P_F_intersect_J}")
P_F_J = P_F_intersect_J / P_J
print("Probabilitity of flood given it rained more than 500 mm in July: ")
print(f"P(Flood|July): {P_F_J}")
P_J_F = (P_F_J * P_J) / P_F
print("Probability of rain more than 500 mm in July given it flooded that year (P(B|A)): ")
print(f"P(July|Flood): {P_J_F}")
