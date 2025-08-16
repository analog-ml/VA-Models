import pandas as pd


def get_variable_names(log_path):
    variable_names = []
    with open(log_path, "r") as f:
        in_variables_section = False
        for line in f:
            if line.strip() == "Variables:":
                in_variables_section = True
                continue
            if in_variables_section:
                if line.strip() == "" or line.startswith("Values:"):
                    break
                # Each variable line: <index> <name> <type>
                parts = line.strip().split()
                if len(parts) >= 2:
                    variable_names.append(parts[1])
    return variable_names


def get_values(log_path):
    values = []
    with open(log_path, "r") as f:
        in_values_section = False
        for line in f:
            if line.strip() == "Values:":
                in_values_section = True
                continue
            if in_values_section:
                if line.strip() == "":
                    break
                # Each value line: <index> <value>
                parts = line.strip().split()
                for part in parts:
                    try:
                        values.append(float(part))
                    except ValueError:
                        pass
    return values[1:]  # Skip the first value which is usually an index or header


vals = get_values("output.log")
names = get_variable_names("output.log")

# print("length of names:", len(names))
# Output: ['v(voutp)', 'i(v0)', '@nm0[gm]', '@nm0[ids]', '@nm0[vth]', 'vgs_nm0', 'vds_nm0', '@nm1[gm]', '@nm1[ids]', '@nm1[vth]', 'vgs_nm1', 'vds_nm1', '@nm2[gm]', '@nm2[ids]', '@nm2[vth]', 'vgs_nm2', 'vds_nm2', '@nm3[gm]', '@nm3[ids]', '@nm3[vth]', 'vgs_nm3', 'vds_nm3', '@nm4[gm]', '@nm4[ids]', '@nm4[vth]', 'v(vgs_nm4)', 'v(vds_nm4)', '@nm5[gm]', '@nm5[ids]', '@nm5[vth]', 'vgs_nm5', 'vds_nm5', '@nm6[gm]', '@nm6[ids]', '@nm6[vth]', 'vgs_nm6', 'vds_nm6', '@nm7[gm]', '@nm7[ids]', '@nm7[vth]', 'vgs_nm7', 'vds_nm7', '@nm8[gm]', '@nm8[ids]', '@nm8[vth]', 'vgs_nm8', 'vds_nm8', '@nm9[gm]', '@nm9[ids]', '@nm9[vth]', 'v(vgs_nm9)', 'v(vds_nm9)', '@nm10[gm]', '@nm10[ids]', '@nm10[vth]', 'v(vgs_nm10)', 'v(vds_nm10)']

# Ensure the number of values matches the number of column names
assert len(vals) == len(names), "Mismatch between values and column names length"

# turn "vals" and "names" into a pandas DataFrame
df = pd.DataFrame([vals], columns=names)


# Helper function to determine PMOS region
def get_pmos_region(vgs, vds, vth):
    if vgs > vth:
        return 0  # cut-off
    else:
        if vds > vgs - vth:
            return 1  # triode
        else:
            return 2  # saturation


def get_nmos_region(vgs, vds, vth):
    if vgs < vth:
        return 0  # cut-off
    else:
        if vds < vgs - vth:
            return 1  # triode
        else:
            return 2  # saturation


# Add region columns for PMOS transistors: nm5, nm6, nm2, nm1
pmos_list = ["nm5", "nm6", "nm2", "nm1"]
for pmos in pmos_list:
    # Get column names for Vgs, Vds, Vth
    vgs_col = f"vgs_{pmos}"
    vds_col = f"vds_{pmos}"
    vth_col = f"@{pmos}[vth]"
    # Some Vgs/Vds columns are named as v(vgs_nmX), v(vds_nmX)
    if vgs_col not in df.columns:
        vgs_col = f"v(vgs_{pmos})"
    if vds_col not in df.columns:
        vds_col = f"v(vds_{pmos})"
    # Compute region
    df[f"@{pmos}[region]"] = df.apply(
        lambda row: get_pmos_region(row[vgs_col], row[vds_col], -row[vth_col]), axis=1
    )

# Add region columns for NMOS transistors: nm8, nm7, nm3, nm0, nm10, nm9, nm4
nmos_list = ["nm8", "nm7", "nm3", "nm0", "nm10", "nm9", "nm4"]
for nmos in nmos_list:
    vgs_col = f"vgs_{nmos}"
    vds_col = f"vds_{nmos}"
    vth_col = f"@{nmos}[vth]"
    # Some Vgs/Vds columns are named as v(vgs_nmX), v(vds_nmX)
    if vgs_col not in df.columns:
        vgs_col = f"v(vgs_{nmos})"
    if vds_col not in df.columns:
        vds_col = f"v(vds_{nmos})"
    df[f"@{nmos}[region]"] = df.apply(
        lambda row: get_nmos_region(row[vgs_col], row[vds_col], row[vth_col]), axis=1
    )

print(df)
