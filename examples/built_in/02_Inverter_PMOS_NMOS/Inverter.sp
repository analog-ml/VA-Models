* CMOS inverter - BSIM3 model - ngspice-compatible

* Supply voltage
VDD vdd 0 DC 1.2

* Input voltage
VIN in 0 DC 0.7

* PMOS pull-up
M1 out in vdd vdd pmos L=180n W=2u

* NMOS pull-down
M0 out in 0 0 nmos L=180n W=1u

* Use built-in BSIM3 models (Level 8)
.model nmos nmos level=8 version=3.2.4
.model pmos pmos level=8 version=3.2.4

* Analysis
.op

.control
  set filetype=ascii
  run
  echo "--- NMOS M0 ---"
  print @m0[ids] @m0[vgs] @m0[vds] @m0[gm] @m0[region]
  echo "--- PMOS M1 ---"
  print @m1[ids] @m1[vgs] @m1[vds] @m1[gm] @m1[region]
.endc

.end
