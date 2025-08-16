🧪 What This Netlist Does:
Models a CMOS inverter with:

PMOS (M1): Connected to vdd
NMOS (M0): Connected to ground

Input is biased at 0.7 V (mid-rail)
Uses BSIM3 (level=8) for both PMOS and NMOS, enabling @mX[...] probing

✅ How to Run:
Save this to a file (e.g., cmos_inverter.sp)

Run in ngspice:

```bash
ngspice cmos_inverter.sp
```


✅ Example Output:

```bash
--- NMOS M0 ---
@m0[ids] = 1.12e-04
@m0[vgs] = 0.70
@m0[vds] = 0.65
@m0[gm]  = 2.31e-04
@m0[region] = 2

--- PMOS M1 ---
@m1[ids] = -1.12e-04
@m1[vgs] = -0.50
@m1[vds] = -0.55
@m1[gm]  = 1.95e-04
@m1[region] = 2
```