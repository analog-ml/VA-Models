import numpy as np
import matplotlib.pyplot as plt


# Function to read NGSpice AC output (ASCII format)
def read_ngspice_ac_output(filename):
    data = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            # Skip headers or empty lines
            if line.strip() and not line.startswith("#"):
                parts = line.split()
                freq = float(parts[0])
                vinp_real = float(parts[1])
                vinp_imag = float(parts[2].strip("i"))

                vinn_real = float(parts[4])
                vinn_imag = float(parts[5].strip("i"))

                voutp_real = float(parts[7])
                voutp_imag = float(parts[8].strip("i"))

                voutn_real = float(parts[10])
                voutn_imag = float(parts[11].strip("i"))
                # Compute differential voltages
                # vin_diff = complex(vinp_real, vinp_imag) - complex(vinn_real, vinn_imag)
                vin_diff = (vinp_real + 1j * vinp_imag) - (vinn_real + 1j * vinn_imag)
                # print("vinp:", vinp_real, vinp_imag)
                # print("vinn:", vinn_real, vinn_imag)
                print("vin_diff:", vin_diff)
                vout_diff = complex(voutp_real, voutp_imag) - complex(
                    voutn_real, voutn_imag
                )
                # Compute magnitudes
                vin_diff_mag = np.abs(vin_diff)
                vout_diff_mag = np.abs(vout_diff)
                data.append([freq, vin_diff_mag, vout_diff_mag])
    return np.array(data)


# Calculate differential gain
def calculate_gain(data):
    freq = data[:, 0]
    vin_diff = data[:, 1]
    vout_diff = data[:, 2]
    # Linear gain: |Vout_diff| / |Vin_diff|
    gain_linear = vout_diff / vin_diff
    # Gain in dB: 20 * log10(|Vout_diff| / |Vin_diff|)
    gain_db = 20 * np.log10(gain_linear)
    return freq, gain_linear, gain_db


# Plot gain vs frequency
def plot_gain(freq, gain_db):
    plt.figure(figsize=(10, 6))
    plt.semilogx(freq, gain_db, label="Differential Gain (dB)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Gain (dB)")
    plt.title("Fully Differential Folded Cascode Amplifier Gain")
    plt.grid(True)
    plt.legend()
    plt.savefig("gain_plot.png")
    plt.show()


# Main script
if __name__ == "__main__":
    # Specify the NGSpice AC output file
    filename = "ac_output.log"

    # Read data
    data = read_ngspice_ac_output(filename)

    # Calculate gain
    freq, gain_linear, gain_db = calculate_gain(data)

    # Print gain at a specific frequency (e.g., mid-band)
    mid_idx = len(freq) // 2  # Rough approximation for mid-band
    print(f"Mid-band frequency: {freq[mid_idx]:.2e} Hz")
    print(f"Mid-band gain (linear): {gain_linear[mid_idx]:.2f}")
    print(f"Mid-band gain (dB): {gain_db[mid_idx]:.2f} dB")

    # Plot gain
    plot_gain(freq, gain_db)
