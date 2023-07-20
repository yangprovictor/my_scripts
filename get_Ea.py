import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = input("please input filename:")
data = pd.read_excel(file)

def estamate_num(data_group):
    if len(data_group) <= 2:
        non_list.append(formula)
    else:
        x = data_group["1000/T"]    
        y = data_group["ln(sig*T)"] 
        coefficients = np.polyfit(x, y, 1)
        slope = coefficients[0]  # 斜率
        Ea = (-8.6173*slope)/100
        
        Ea_list = []
        for i in range(len(data_group)):
            Ea_list.append(Ea)
        data_group["Ea(eV)"] = Ea_list
    return data_group

formula_list = data["Pretty_Formula"].unique().tolist()

non_list = []
data_total = pd.DataFrame()
for formula in formula_list:
    data_group = data[data["Pretty_Formula"] == formula]

    if len(data_group) <= 2:
        non_list.append(formula)
   
    else:   
        data_group = data_group.sort_values(by='T_Kelvin', ascending=False)
        data_group_0 = data_group[data_group["Phase_Transition"] == 0]
        data_group_1 = data_group[data_group["Phase_Transition"] == 1]

        data_group_0 = estamate_num(data_group_0)
        data_group_1 = estamate_num(data_group_1)
        
        data_group_10 = pd.concat([data_group_0,data_group_1],axis=0)
        data_group_10 = data_group_10.sort_values(by='T_Kelvin', ascending=False)
        
    data_total = pd.concat([data_total,data_group_10],axis=0)
data_total.to_excel(file+"_Ea.xlsx")

print("The following structures only own two points:")
print(non_list)

