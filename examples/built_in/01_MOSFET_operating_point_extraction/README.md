🧪 What it does:
Creates a common-source NMOS stage

Uses BSIM3 so you can access detailed operating point data

Prints:

```bash
@m0[ids]: Drain current
@m0[vgs]: Gate-to-source voltage
@m0[vds]: Drain-to-source voltage
@m0[gm]: Transconductance
@m0[region]: Region of operation (2 = saturation)
```

✅ How to Run It:
Save to mosfet_test.sp and in terminal:

```bash
ngspice mosfet_test.sp
```

Expected output:

```bash
@m0[ids]   = 1.23e-4
@m0[vgs]   = 0.700
@m0[vds]   = 0.800
@m0[gm]    = 2.50e-4
@m0[region]= 2
```