* Multiple MOSFETs 

* Bias sources
Vd1 d1 0 1.8
Vg1 g1 0 1.2
Vs1 s1 0 0

Vd2 d2 0 1.8
Vg2 g2 0 0.5
Vs2 s2 0 0

Vd3 d3 0 0.5
Vg3 g3 0 1.2
Vs3 s3 0 0

* MOSFETs (use model name NMOS)
M1 d1 g1 s1 s1 NMOS W=10u L=1u
M2 d2 g2 s2 s2 NMOS W=10u L=1u
M3 d3 g3 s3 s3 NMOS W=10u L=1u

* MOSFET model
.model NMOS nmos level=8 vto=0.7 kp=100e-6 lambda=0.02

.control
  op
  set filetype=ascii
  write mos_multi.log @m1[gm] @m1[vgs] @m1[vds] @m1[vth]
  quit
.endc

.end
