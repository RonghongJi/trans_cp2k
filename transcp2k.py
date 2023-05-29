import json

with open ('BMIM-pos-1.xyz') as xyz:
    data = xyz.readlines()
    information = []
    for i,item_data in enumerate(data):
        if "time" in item_data:
            atom_num = int(data[i-1])
            atom_index = i
            information.append(data[atom_index+1:atom_index+1+atom_num])
    xyz = []
    for i,value in enumerate(information):
        xyz_item = []
        for j,value_1 in enumerate(value):
            xyz_item.append((float(value_1.split()[1]),float(value_1.split()[2]),float(value_1.split()[3])))
        xyz.append(xyz_item)

with open ('BMIM.inp') as cell:
    data = cell.readlines()
    cell_size = []
    for i,item_data in enumerate(data):
        if "&CELL" in item_data:
            for j in range(3):
                cell_size.append(float(data[i+1+j].split()[j+1]))

with open('ll_out') as energyforce:
    data = energyforce.readlines()

    force_information = []
    for i ,item_data in enumerate(data):
        if "ATOMIC FORCES in [a.u.]" in item_data:
            force_information.append(data[i+3:i+3+180])
    force = []
    for i,value in enumerate(force_information):
        force_item = []
        for j,value_1 in enumerate(value):
            force_item.append((float(value_1.split()[3]),float(value_1.split()[4]),float(value_1.split()[5])))
        force.append(force_item)

    energy = []
    for i ,item_data in enumerate(data):
        if "outer SCF iter =    1" in item_data:
            energy.append(float(data[i-2].split()[-1]))

with open('[bmim][bf4]_cp2k.json', 'a') as f:
    for i in range (10001):
        # content = {}
        # content["Energy"] = energy[i],
        # content["Positions"] = xyz[i],
        # content["Forces"] = force[i],
        # content["Cell-Size"] = cell_size,
        # content["Natoms"] = atom_num
        content = {"Energy":energy[i], "Positions":xyz[i], "Forces":force[i], "Cell_size":cell_size, "Natoms":atom_num}
        json_str = json.dumps(content)
        f.write(json_str)
        f.write('\n')