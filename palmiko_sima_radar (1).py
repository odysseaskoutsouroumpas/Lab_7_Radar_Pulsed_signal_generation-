import numpy as np
import matplotlib.pyplot as plt


# Ορισμός παραμέτρων
f = 10e9  # Συχνότητα ημιτόνου (10 GHz)
T = 1 / f  # Περίοδος του ημιτόνου (100 ps)
num_periods_signal = 5  # Διάρκεια παλμού: 5 περίοδοι ημιτόνου
num_periods_zero = 50  # Διάρκεια σιγής: 50 περίοδοι ημιτόνου
num_cycles = 3  # Πλήρεις κύκλοι λειτουργίας του ραντάρ

# Δείγματα ανά περίοδο (100 δείγματα για ακρίβεια)
samples_per_period = 100
samples_signal = num_periods_signal * samples_per_period
samples_zero = num_periods_zero * samples_per_period

# Δημιουργία ημιτονοειδούς σήματος για 5 περιόδους
t_signal = np.linspace(0, num_periods_signal * T, samples_signal, endpoint=False)
sin_wave = np.sin(2 * np.pi * f * t_signal)

# Δημιουργία τετραγωνικού παλμού (1 όπου υπάρχει το ημίτονο, 0 αλλού)
square_pulse = np.ones_like(sin_wave)

# Πολλαπλασιασμός του τετραγωνικού παλμού με το ημίτονο
pulse_signal = square_pulse * sin_wave

# Δημιουργία μηδενικών τιμών για 50 περιόδους (σιγή)
zero_signal = np.zeros(samples_zero)

# Δημιουργία ενός κύκλου λειτουργίας του ραντάρ
radar_cycle = np.concatenate((pulse_signal, zero_signal))

# Επαναλαμβάνουμε τον κύκλο 3 φορές
total_signal = np.tile(radar_cycle, num_cycles)

# Δημιουργία χρονικού άξονα
t_total = np.linspace(0, num_cycles * (num_periods_signal + num_periods_zero) * T,
                      len(total_signal), endpoint=False)

# Σχεδίαση του σήματος ραντάρ
plt.figure(figsize=(10, 4))
plt.plot(t_total * 1e9, total_signal, label="x(t) - Παλμικό Σήμα Radar")
plt.xlabel("Χρόνος (ns)")
plt.ylabel("Πλάτος Σήματος")
plt.title("Παλμικό Radar - 3 Κύκλοι Λειτουργίας")
plt.grid(True)
plt.legend()
plt.show()
