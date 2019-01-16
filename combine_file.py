import json
import os
print("save old file")

file_out = []
###########################3
if os.stat("dantri.json").st_size != 0:
	with open("dantri.json", "r") as f:
		file_data = json.load(f)

# if os.stat("dantri.json").st_size != 0:
with open("old_dantri.json", "w") as f:
	json.dump(file_data, f, indent=4)

#############################
# file_out.extend(file_data)

if os.stat("vne.json").st_size != 0:
	with open("vne.json", "r") as f:
		file_data = json.load(f)

with open("old_vne.json", "w") as f:
	json.dump(file_data, f, indent=4)
# file_out.extend(file_data)

###########################################
if os.stat("mof.json").st_size != 0:
	with open("mof.json", "r") as f:
		file_data = json.load(f)
# file_out.extend(file_data)

with open("old_mof.json", "w") as f:
	json.dump(file_data, f, indent=4)

########################################
if os.stat("mpi.json").st_size != 0:
	with open("mpi.json", "r") as f:
		file_data = json.load(f)
# file_out.extend(file_data)

with open("old_mpi.json", "w") as f:
	json.dump(file_data, f, indent=4)

#########################################
if os.stat("moit.json").st_size != 0:
	with open("moit.json", "r") as f:
		file_data = json.load(f)
# file_out.extend(file_data)

with open("old_moit.json", "w") as f:
	json.dump(file_data, f, indent=4)

#####################################
if os.stat("sbv.json").st_size != 0:
	with open("sbv.json", "r") as f:
		file_data = json.load(f)
# file_out.extend(file_data)

with open("old_sbv.json", "w") as f:
	json.dump(file_data, f, indent=4)
########################################
if os.stat("vcb.json").st_size != 0:
	with open("vcb.json", "r") as f:
		file_data = json.load(f)
# file_out.extend(file_data)

with open("old_vcb.json", "w") as f:
	json.dump(file_data, f, indent=4)

######################################
if os.stat("vib.json").st_size != 0:
	with open("vib.json", "r") as f:
		file_data = json.load(f)

with open("old_vib.json", "w") as f:
	json.dump(file_data, f, indent=4)
# file_out.extend(file_data)
print("old file saved")

