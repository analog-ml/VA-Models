*fully_differential_folded_cascode.css (ledro)

.include ../Modelcards/ptm-mg-lstp.nmos
.include ../Modelcards/ptm-mg-lstp.pmos

* Parameters
.param tempc=27
.param nA1=65n nB1=3
.param nA2=65n nB2=3
.param nA3=65n nB3=3
.param nA4=65n nB4=3
.param nA5=65n nB5=3
.param nA6=65n nB6=3
.param vdd=1.5 vcm=0.7 vbiasp1=0.7 vbiasp2=0.7
.param vbiasn0=0.7 vbiasn1=0.7 vbiasn2=0.7

NM6 Voutp Vbiasp2 net23 vdd pmos L={nA1} NFIN={nB1}
NM5 Voutn Vbiasp2 net24 vdd pmos L={nA1} NFIN={nB1}
NM2 net23 Vbiasp1 vdd vdd pmos L={nA2} NFIN={nB2}
NM1 net24 Vbiasp1 vdd vdd pmos L={nA2} NFIN={nB2}
NM8 Voutp Vbiasn2 net27 0 nmos L={nA3} NFIN={nB3}
NM7 Voutn Vbiasn2 net25 0 nmos L={nA3} NFIN={nB3}
NM3 net24 Vinp net13 0 nmos L={nA4} NFIN={nB4}
NM0 net23 Vinn net13 0 nmos L={nA4} NFIN={nB4}
NM10 net27 Vbiasn1 0 0 nmos L={nA5} NFIN={nB5}
NM9 net25 Vbiasn1 0 0 nmos L={nA5} NFIN={nB5}
NM4 net13 Vbiasn0 0 0 nmos L={nA6} NFIN={nB6}

* Voltage sources
* VS gnd 0 DC 0
V0 vdd 0 DC {vdd}
V2 in 0 DC 1
E1 Vinp cm in 0 0.5
E0 Vinn cm in 0 -0.5
V1 cm 0 DC {vcm}
VP1 Vbiasp1 0 DC {vbiasp1}
VP2 Vbiasp2 0 DC {vbiasp2}
VN Vbiasn0 0 DC {vbiasn0}
VN1 Vbiasn1 0 DC {vbiasn1}
VN2 Vbiasn2 0 DC {vbiasn2}


* --- DC Analysis ---

* --- Transient Analysis ---
*.tran 10n 2u

.control
op
pre_osdi ../../../osdilibs/bsimcmg.osdi
set xbrushwidth=3
run

let vgs_nm0 = v(Vinn) - v(net13)
let vds_nm0 = v(net23) - v(net13)

let vgs_nm1 = v(Vbiasp1) - v(vdd)
let vds_nm1 = v(net24) - v(vdd)

let vgs_nm2 = v(Vbiasp1) - v(vdd)
let vds_nm2 = v(net23) - v(vdd)

let vgs_nm3 = v(Vinp) - v(net13)
let vds_nm3 = v(net24) - v(net13)

let vgs_nm4 = v(Vbiasn0) 
let vds_nm4 = v(net13) 

let vgs_nm5 = v(Vbiasp2) - v(net24)
let vds_nm5 = v(Voutn) - v(net24)

let vgs_nm6 = v(Vbiasp2) - v(net23)
let vds_nm6 = v(Voutp) - v(net23)

let vgs_nm7 = v(Vbiasn2) - v(net25)
let vds_nm7 = v(Voutn) - v(net25)

let vgs_nm8 = v(Vbiasn2) - v(net27)
let vds_nm8 = v(Voutp) - v(net27)

let vgs_nm9 = v(Vbiasn1)
let vds_nm9 = v(net25)

let vgs_nm10 = v(Vbiasn1) 
let vds_nm10 = v(net27) 

wrdata output.log @nm0[gm] @nm0[ids] @nm0[vth] vgs_nm0 vds_nm0
+ @nm1[gm] @nm1[ids] @nm1[vth] vgs_nm1 vds_nm1
+ @nm2[gm] @nm2[ids] @nm2[vth] vgs_nm2 vds_nm2 
+ @nm3[gm] @nm3[ids] @nm3[vth] vgs_nm3 vds_nm3
+ @nm4[gm] @nm4[ids] @nm4[vth] vgs_nm4 vds_nm4
+ @nm5[gm] @nm5[ids] @nm5[vth] vgs_nm5 vds_nm5 
+ @nm6[gm] @nm6[ids] @nm6[vth] vgs_nm6 vds_nm6
+ @nm7[gm] @nm7[ids] @nm7[vth] vgs_nm7 vds_nm7
+ @nm8[gm] @nm8[ids] @nm8[vth] vgs_nm8 vds_nm8
+ @nm9[gm] @nm9[ids] @nm9[vth] vgs_nm9 vds_nm9
+ @nm10[gm] @nm10[ids] @nm10[vth] vgs_nm10 vds_nm10

quit
.endc

.end