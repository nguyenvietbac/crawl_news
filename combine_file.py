import json
import os
print("save old file")

file_out = []
###########################
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
######################################
if os.stat("reuters.json").st_size != 0:
	with open("reuters.json", "r") as f:
		file_data = json.load(f)

with open("old_reuters.json", "w") as f:
	json.dump(file_data, f, indent=4)
######################################
if os.stat("economist.json").st_size != 0:
	with open("economist.json", "r") as f:
		file_data = json.load(f)

with open("old_economist.json", "w") as f:
	json.dump(file_data, f, indent=4)
######################################
if os.stat("imf.json").st_size != 0:
	with open("imf.json", "r") as f:
		file_data = json.load(f)

with open("old_imf.json", "w") as f:
	json.dump(file_data, f, indent=4)
######################################
if os.stat("fed.json").st_size != 0:
	with open("fed.json", "r") as f:
		file_data = json.load(f)

with open("old_fed.json", "w") as f:
	json.dump(file_data, f, indent=4)
######################################
print("old file saved")

