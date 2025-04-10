import numpy as np
import matplotlib.pyplot as plt

# Ορισμός παραμέτρων
f = 10e9  # Συχνότητα ημιτόνου (10 GHz)
T_period = 1 / f  # Περίοδος του ημιτόνου
N_pulse = 5  # Πλήθος περιόδων του ημιτόνου σε έναν παλμό
N_silence = 50  # Πλήθος περιόδων σιγής
N_cycles = 3  # Πλήθος κύκλων λειτουργίας του ραντάρ
T_cycle = (N_pulse + N_silence) * T_period  # Συνολική διάρκεια κύκλου ραντάρ
c = 3e8  # Ταχύτητα του φωτός (m/s)

# Δημιουργία χρονικού άξονα
samples_per_period = 100  # Δειγματοληψία ανά περίοδο
T_total = N_cycles * T_cycle  # Συνολικός χρόνος
samples_total = int(T_total * f * samples_per_period)
t = np.linspace(0, T_total, samples_total)

# Δημιουργία παλμικού σήματος
pulse_train = np.zeros_like(t)
for i in range(N_cycles):
    start_idx = int(i * (N_pulse + N_silence) * samples_per_period)
    end_idx = start_idx + N_pulse * samples_per_period
    pulse_train[start_idx:end_idx] = 1

# Δημιουργία ημιτονικού σήματος
sine_wave = np.sin(2 * np.pi * f * t)

# Δημιουργία τελικού σήματος ραντάρ
x_t = pulse_train * sine_wave

# Υπολογισμός τυχαίας ταχύτητας αντικειμένου
v_object = np.random.uniform(-30, 30)  # Τυχαία ταχύτητα αντικειμένου σε m/s

# Υπολογισμός της συχνότητας Doppler
f_reflected = f * (c / (c + v_object))

# Δημιουργία ημιτονικού σήματος αντανάκλασης με Doppler
sine_wave_reflected = np.sin(2 * np.pi * f_reflected * t)

# Δημιουργία επιστρεφόμενου σήματος με Doppler και καθυστέρηση
T_reflected = np.random.randint(5, 50) * T_period  # Τυχαία καθυστέρηση
A_reflected = max(0.1, T_reflected / T_cycle)  # Εξασθένηση λόγω απόστασης, με ελάχιστη τιμή 0.1
samples_delay = int(T_reflected * f * samples_per_period)
x_reflected_doppler = np.roll(pulse_train * sine_wave_reflected, samples_delay) * A_reflected

# Υπολογισμός ταχύτητας αντικειμένου μέσω της εξίσωσης Doppler
v_calculated = ((f - f_reflected) / f_reflected) * c

# Απεικόνιση του σήματος πομπού και του επιστρεφόμενου με Doppler
plt.figure(figsize=(10, 4))
plt.plot(t[:5000] * 1e9, x_t[:5000], label="Σήμα Πομπού")
plt.plot(t[:5000] * 1e9, x_reflected_doppler[:5000], label="Σήμα Αντανάκλασης με Doppler", linestyle="dotted")
plt.xlabel("Χρόνος (ns)")
plt.ylabel("Απόκριση σήματος")
plt.title("Ανίχνευση Ταχύτητας Αντικειμένου μέσω Doppler")
plt.legend()
plt.grid()
plt.show()

print(f"Πραγματική ταχύτητα αντικειμένου: {v_object:.2f} m/s")
print(f"Υπολογισμένη ταχύτητα αντικειμένου: {v_calculated:.2f} m/s")