import numpy as np
import matplotlib.pyplot as plt


def read_wrdata_complex_pair(fname):
    freqs = []
    out_re, out_im = [], []
    in_re, in_im = [], []
    with open(fname, "r") as f:
        for line in f:
            if not line.strip() or line.startswith("#") or "frequency" in line.lower():
                continue
            parts = line.split()
            # Expect: freq  v(out).real  v(out).imag  v(in).real  v(in).imag
            freqs.append(float(parts[0]))
            out_re.append(float(parts[1]))
            out_im.append(float(parts[2]))
            in_re.append(float(parts[4]))
            in_im.append(float(parts[5]))
    freqs = np.array(freqs)
    vout = np.array(out_re) + 1j * np.array(out_im)
    vin = np.array(in_re) + 1j * np.array(in_im)
    return freqs, vout, vin


freq, vout, vin = read_wrdata_complex_pair("ac_output_2.log")
A = vout / vin
A_db = 20 * np.log10(np.abs(A))
A_phase = np.angle(A, deg=True)

plt.figure(figsize=(8, 5))
plt.semilogx(freq, A_db, label="|Vout/Vin| (dB)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Gain (dB)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()
plt.savefig("gain_db.png")
plt.show()
