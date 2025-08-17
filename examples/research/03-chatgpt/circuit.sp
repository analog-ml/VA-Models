* Fully-differential opamp (behavioral VCVS) - target differential gain = 5 dB (~1.778)
* How it works:
*  Vout+ =  +Ad/2 * (Vin+ - Vin-)
*  Vout- =  -Ad/2 * (Vin+ - Vin-)
* => Vout_diff = Vout+ - Vout- = Ad * (Vin+ - Vin-)

.param Ad = 1.778          ; linear differential gain (5 dB)
* Supply rails (not used by the behavioral sources but kept for completeness)
Vdd vdd 0 DC 5
Vss vss 0 DC -5

* Input nodes
VinP vinp 0 AC 0.5        ; AC stimulus on + input (0.5 V AC)
VinN vinn 0 AC 0.0        ; AC stimulus on - input (set to 0 here).
                         ; If you want opposite-phase drive, set AC 0.5 and use "phase=180"
                         ; or set VinN to AC 0.5 and add a .step param for phase if needed.

* Behavioral VCVS pair implementing the fully-differential amp
EOUTP outp 0 vinp vinn {Ad/2}   ; Vout+ = +Ad/2 * (Vin+ - Vin-)
EOUTN outn 0 vinn vinp {Ad/2}   ; Vout- = +Ad/2 * (Vin- - Vin+) = -Ad/2*(Vin+ - Vin-)

* Output loads (user can change to any load or connect next stage)
RLp outp 0 10k
RLn outn 0 10k

* A small DC bias on inputs to avoid floating nodes (optional)
Rb1 vinp 0 1Meg
Rb2 vinn 0 1Meg

* AC analysis (frequency sweep)
.ac dec 100 10 10Meg

* Print single-ended outputs and differential output
*.print ac V(outp) V(outn) V(outp,outn)


* run a transient to capture time-domain signals
.tran 1u 2m
* write voltages to "log_tran.txt"

.control
  set wr_vecnames
  option numdgt=7

  run
  wrdata ac_output.log v(vinp) v(vinn) v(outp) v(outn)
.endc


* Measure differential magnitude and convert to dB at 1kHz
* Note: some ngspice builds support VDB() directly in .meas; if not, compute from mag(V(outp,outn))
.meas AC Vdiff_mag FIND mag(V(outp,outn)) AT=1k
.meas AC Vdiff_dB PARAM = 20*log10(Vdiff_mag)

* Run a short transient example (optional) to see time-domain
* VinP_s vinp_s 0 SIN(0 10m 1k)
* VinN_s vinn 0 SIN(0 0    1k)   ; single-ended drive example
* .tran 1u 2m

.end
