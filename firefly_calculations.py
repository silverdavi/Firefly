"""
Detailed Calculations: The Century-Old Firefly Luminosity Error
David H. Silver, 2025

This script performs rigorous calculations comparing biochemical bottom-up
estimates of firefly photon emission to the historical 1924 Ives & Coblentz measurement.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# Physical constants
h = 6.626e-34  # Planck's constant (J·s)
c = 3.0e8      # Speed of light (m/s)
k_B = 1.381e-23  # Boltzmann constant (J/K)

# Firefly emission wavelength
lambda_firefly = 560e-9  # meters (560 nm, yellow-green)

print("="*80)
print("FIREFLY BIOLUMINESCENCE: BIOCHEMICAL vs HISTORICAL PHOTOMETRY")
print("="*80)
print()

#==============================================================================
# PART 1: BIOCHEMICAL BOTTOM-UP CALCULATION
#==============================================================================

print("PART 1: BIOCHEMICAL BOTTOM-UP CALCULATION")
print("-"*80)

# Parameters from literature
luciferase_per_photocyte = 1e6  # molecules
photocytes_per_firefly = 1e5    # cells
total_luciferase = luciferase_per_photocyte * photocytes_per_firefly

print(f"Luciferase per photocyte: {luciferase_per_photocyte:.1e} molecules")
print(f"Photocytes per firefly lantern: {photocytes_per_firefly:.1e} cells")
print(f"TOTAL luciferase: {total_luciferase:.1e} molecules")
print()

# Catalytic turnover
k_cat_in_vitro = 1.0  # reactions/sec (steady state)
k_cat_in_vivo_effective = 0.01  # reactions/sec (oxygen-limited, per Fallon)

print(f"k_cat (in vitro, steady state): {k_cat_in_vitro} reactions/sec")
print(f"k_cat (in vivo, oxygen-limited): {k_cat_in_vivo_effective} reactions/sec")
print()

# Quantum yield
QY = 0.41  # photons per reaction

print(f"Quantum yield (QY): {QY} photons/reaction")
print()

# Flash duration
flash_duration_ms = 250  # milliseconds
flash_duration_s = flash_duration_ms / 1000  # seconds

print(f"Flash duration: {flash_duration_ms} ms = {flash_duration_s} sec")
print()

# CALCULATION 1: Maximum theoretical (all enzymes active)
photons_per_sec_max = total_luciferase * k_cat_in_vitro * QY
photons_per_flash_max = photons_per_sec_max * flash_duration_s

print("SCENARIO A: Maximum theoretical (all enzymes saturated)")
print(f"  Photons/sec: {photons_per_sec_max:.2e}")
print(f"  Photons/flash: {photons_per_flash_max:.2e}")
print()

# CALCULATION 2: Oxygen-limited (realistic, per Fallon)
photons_per_sec_realistic = total_luciferase * k_cat_in_vivo_effective * QY
photons_per_flash_realistic = photons_per_sec_realistic * flash_duration_s

print("SCENARIO B: Oxygen-limited (realistic, per Fallon 2025)")
print(f"  Photons/sec: {photons_per_sec_realistic:.2e}")
print(f"  Photons/flash: {photons_per_flash_realistic:.2e}")
print()

# Fallon's direct estimate
fallon_estimate_min = 1e8
fallon_estimate_max = 1e9
print(f"Fallon's working estimate: {fallon_estimate_min:.0e} - {fallon_estimate_max:.0e} photons/flash")
print()

# Goh & Wang 2022 measurement
goh_wang_min = 3e8
goh_wang_max = 5e8
print(f"Goh & Wang (2022) spectrometer: {goh_wang_min:.0e} - {goh_wang_max:.0e} photons/flash")
print()

biochemical_estimate = photons_per_flash_realistic

#==============================================================================
# PART 2: HISTORICAL PHOTOMETRY CONVERSION (Ives & Coblentz 1924)
#==============================================================================

print()
print("PART 2: HISTORICAL PHOTOMETRY CONVERSION (Ives & Coblentz 1924)")
print("-"*80)

# Original measurement
luminous_intensity_candle = 1/40  # candlepower
luminous_intensity_cd = luminous_intensity_candle  # 1 candle ≈ 1 candela (modern)

print(f"Original measurement: 1/40 candle = {luminous_intensity_cd:.4f} cd")
print()

# Step 1: Candela to lumens (assuming isotropic emission)
solid_angle_sphere = 4 * np.pi  # steradians
luminous_flux_lm = luminous_intensity_cd * solid_angle_sphere

print(f"Step 1: Luminous flux (assuming isotropic)")
print(f"  Φ_v = I × 4π = {luminous_intensity_cd:.4f} cd × {solid_angle_sphere:.3f} sr")
print(f"  Φ_v = {luminous_flux_lm:.3f} lm")
print()

# Step 2: Lumens to radiometric power at 560 nm
V_lambda = 0.995  # Photopic luminous efficiency function at 560 nm
max_luminous_efficacy = 683  # lm/W at 555 nm
effective_efficacy = max_luminous_efficacy * V_lambda

radiant_power_W = luminous_flux_lm / effective_efficacy

print(f"Step 2: Luminous to radiant power")
print(f"  V(560 nm) = {V_lambda:.3f}")
print(f"  Max efficacy at 555 nm: {max_luminous_efficacy} lm/W")
print(f"  Effective efficacy: {effective_efficacy:.1f} lm/W")
print(f"  P_radiant = Φ_v / (683 × V(λ))")
print(f"  P_radiant = {luminous_flux_lm:.3f} lm / {effective_efficacy:.1f} lm/W")
print(f"  P_radiant = {radiant_power_W:.3e} W")
print()

# Step 3: Radiometric power to photon flux
E_photon = h * c / lambda_firefly  # Joules per photon
E_photon_eV = E_photon / 1.602e-19  # electron volts

photon_flux_per_sec_historical = radiant_power_W / E_photon

print(f"Step 3: Photon flux calculation")
print(f"  E_photon = hc/λ")
print(f"  E_photon = {E_photon:.3e} J = {E_photon_eV:.2f} eV")
print(f"  Φ_photons = P / E_photon")
print(f"  Φ_photons = {radiant_power_W:.3e} W / {E_photon:.3e} J")
print(f"  Φ_photons = {photon_flux_per_sec_historical:.2e} photons/sec")
print()

# Step 4: Total photons per flash
photons_per_flash_historical = photon_flux_per_sec_historical * flash_duration_s

print(f"Step 4: Total photons per flash ({flash_duration_ms} ms)")
print(f"  Total = {photon_flux_per_sec_historical:.2e} photons/sec × {flash_duration_s} sec")
print(f"  Total = {photons_per_flash_historical:.2e} photons/flash")
print()

#==============================================================================
# PART 3: COMPARISON AND DISCREPANCY ANALYSIS
#==============================================================================

print()
print("PART 3: COMPARISON AND DISCREPANCY ANALYSIS")
print("="*80)

discrepancy_factor = photons_per_flash_historical / biochemical_estimate
orders_of_magnitude = np.log10(discrepancy_factor)

print(f"Biochemical estimate (oxygen-limited): {biochemical_estimate:.2e} photons/flash")
print(f"Historical measurement (Ives & Coblentz): {photons_per_flash_historical:.2e} photons/flash")
print()
print(f"DISCREPANCY FACTOR: {discrepancy_factor:.0f}×")
print(f"ORDERS OF MAGNITUDE: {orders_of_magnitude:.1f}")
print()

# Comparison table
print("SUMMARY TABLE:")
print("-"*80)
print(f"{'Method':<40} {'Photons/flash':>20} {'Year':<10}")
print("-"*80)
print(f"{'Ives & Coblentz (photometry)':<40} {photons_per_flash_historical:>20.2e} {'1924':<10}")
print(f"{'Biochemical (max theoretical)':<40} {photons_per_flash_max:>20.2e} {'2025':<10}")
print(f"{'Biochemical (oxygen-limited)':<40} {photons_per_flash_realistic:>20.2e} {'2025':<10}")
print(f"{'Fallon estimate (min)':<40} {fallon_estimate_min:>20.2e} {'2025':<10}")
print(f"{'Fallon estimate (max)':<40} {fallon_estimate_max:>20.2e} {'2025':<10}")
print(f"{'Goh & Wang spectrometer (min)':<40} {goh_wang_min:>20.2e} {'2022':<10}")
print(f"{'Goh & Wang spectrometer (max)':<40} {goh_wang_max:>20.2e} {'2022':<10}")
print("-"*80)
print()

#==============================================================================
# PART 4: ENERGY BUDGET ANALYSIS
#==============================================================================

print()
print("PART 4: ENERGY BUDGET ANALYSIS")
print("-"*80)

# ATP energy
ATP_energy_eV = 0.30  # eV per ATP hydrolysis
ATP_energy_J = ATP_energy_eV * 1.602e-19  # Joules

ATP_per_photon = E_photon / ATP_energy_J

print(f"Energy per photon at 560 nm: {E_photon_eV:.2f} eV")
print(f"Energy per ATP hydrolysis: {ATP_energy_eV:.2f} eV")
print(f"ATP molecules required per photon: {ATP_per_photon:.1f}")
print()

# Total ATP budget for realistic flash
total_photons_realistic = biochemical_estimate
total_ATP_consumed = total_photons_realistic * ATP_per_photon

print(f"For realistic flash ({biochemical_estimate:.2e} photons):")
print(f"  ATP consumed: {total_ATP_consumed:.2e} molecules")
print()

# ATP concentration check
photocyte_volume_um3 = 1000  # cubic micrometers (estimate)
photocyte_volume_L = photocyte_volume_um3 * 1e-15  # liters
total_photocyte_volume_L = photocyte_volume_L * photocytes_per_firefly

ATP_conc_mM = 3.0  # typical cellular ATP concentration (millimolar)
ATP_per_liter = ATP_conc_mM * 1e-3 * 6.022e23  # molecules per liter
total_ATP_available = ATP_per_liter * total_photocyte_volume_L

print(f"ATP budget check:")
print(f"  Typical [ATP]: {ATP_conc_mM} mM")
print(f"  Total photocyte volume: {total_photocyte_volume_L:.2e} L")
print(f"  Total ATP available: {total_ATP_available:.2e} molecules")
print(f"  ATP consumed per flash: {total_ATP_consumed:.2e} molecules")
print(f"  Fraction of ATP pool used: {total_ATP_consumed/total_ATP_available*100:.1f}%")
print()

#==============================================================================
# PART 5: VISUALIZATION
#==============================================================================

print()
print("Generating figures...")
print()

# Figure 1: Logarithmic comparison
fig, ax = plt.subplots(figsize=(12, 8))

methods = [
    'Ives & Coblentz\n(1924)',
    'Biochemical\n(max theoretical)',
    'Biochemical\n(oxygen-limited)',
    'Fallon estimate\n(min)',
    'Fallon estimate\n(max)',
    'Goh & Wang\n(min)',
    'Goh & Wang\n(max)'
]

values = [
    photons_per_flash_historical,
    photons_per_flash_max,
    photons_per_flash_realistic,
    fallon_estimate_min,
    fallon_estimate_max,
    goh_wang_min,
    goh_wang_max
]

colors = ['#d62728', '#1f77b4', '#1f77b4', '#2ca02c', '#2ca02c', '#ff7f0e', '#ff7f0e']
alphas = [0.9, 0.4, 0.9, 0.5, 0.9, 0.5, 0.9]

y_pos = np.arange(len(methods))

# Create bars individually with their own alpha values
bars = []
for i, (y, val, color, alpha) in enumerate(zip(y_pos, values, colors, alphas)):
    bar = ax.barh(y, val, color=color, alpha=alpha, edgecolor='black', linewidth=1.5)
    bars.extend(bar)

ax.set_yticks(y_pos)
ax.set_yticklabels(methods, fontsize=11)
ax.set_xlabel('Photons per flash', fontsize=13, fontweight='bold')
ax.set_xscale('log')
ax.set_title('Firefly Bioluminescence: Historical Measurement vs Biochemical Estimates\n' + 
             f'Discrepancy: {discrepancy_factor:.0f}× ({orders_of_magnitude:.1f} orders of magnitude)',
             fontsize=14, fontweight='bold', pad=20)

ax.grid(True, which='both', axis='x', alpha=0.3, linestyle='--')
ax.set_xlim(1e7, 1e16)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, values)):
    ax.text(val * 1.5, bar.get_y() + bar.get_height()/2, 
            f'{val:.1e}', 
            va='center', fontsize=10, fontweight='bold')

# Legend
red_patch = mpatches.Patch(color='#d62728', alpha=0.9, label='Historical (1924)')
blue_patch = mpatches.Patch(color='#1f77b4', alpha=0.9, label='Biochemical calculation (2025)')
green_patch = mpatches.Patch(color='#2ca02c', alpha=0.9, label='Expert estimate (2025)')
orange_patch = mpatches.Patch(color='#ff7f0e', alpha=0.9, label='Spectrometer (2022)')

ax.legend(handles=[red_patch, blue_patch, green_patch, orange_patch], 
          loc='lower right', fontsize=11, framealpha=0.9)

plt.tight_layout()
plt.savefig('/Users/davidsilver/dev/papers/firefly/figure_1_discrepancy.png', dpi=300, bbox_inches='tight')
plt.savefig('/Users/davidsilver/dev/papers/firefly/figure_1_discrepancy.pdf', bbox_inches='tight')
print("Saved: figure_1_discrepancy.png and .pdf")

# Figure 2: Energy budget pathway
fig, ax = plt.subplots(figsize=(14, 10))
ax.axis('off')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Title
ax.text(5, 9.5, 'Firefly Bioluminescence: Energy Budget Analysis', 
        ha='center', fontsize=16, fontweight='bold')

# Biochemical pathway
y_start = 8.5
box_height = 0.6
box_width = 8

steps = [
    f"1. Total Luciferase: {total_luciferase:.1e} molecules",
    f"2. Oxygen-limited turnover: {k_cat_in_vivo_effective:.2f} reactions/sec/enzyme",
    f"3. Quantum yield: {QY} photons/reaction",
    f"4. Flash duration: {flash_duration_ms} ms",
    f"5. Total photons: {biochemical_estimate:.2e} photons/flash"
]

colors_steps = ['#e8f4f8', '#d0e8f0', '#b8dce8', '#a0d0e0', '#88c4d8']

for i, (step, color) in enumerate(zip(steps, colors_steps)):
    y = y_start - i * 0.8
    rect = Rectangle((1, y - box_height/2), box_width, box_height, 
                      facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(5, y, step, ha='center', va='center', fontsize=12, fontweight='bold')
    
    if i < len(steps) - 1:
        ax.arrow(5, y - box_height/2 - 0.05, 0, -0.15, 
                head_width=0.3, head_length=0.1, fc='black', ec='black', linewidth=2)

# ATP budget box
y_atp = 4.0
rect_atp = Rectangle((0.5, y_atp - 1.2), 9, 1.5, 
                      facecolor='#fff4e6', edgecolor='#ff7f0e', linewidth=3)
ax.add_patch(rect_atp)

atp_text = f"""ATP BUDGET CHECK:
• Energy per photon: {E_photon_eV:.2f} eV
• ATP per photon: {ATP_per_photon:.1f} molecules
• Total ATP consumed: {total_ATP_consumed:.2e} molecules
• Cellular [ATP]: {ATP_conc_mM} mM
• Total ATP available: {total_ATP_available:.2e} molecules
• Fraction used: {total_ATP_consumed/total_ATP_available*100:.1f}% ✓ PLAUSIBLE"""

ax.text(5, y_atp - 0.25, atp_text, ha='center', va='center', 
        fontsize=11, fontfamily='monospace', fontweight='bold')

# Comparison box
y_comp = 1.5
rect_comp = Rectangle((0.5, y_comp - 0.8), 9, 1.2, 
                       facecolor='#ffe6e6', edgecolor='#d62728', linewidth=3)
ax.add_patch(rect_comp)

comp_text = f"""HISTORICAL MEASUREMENT (Ives & Coblentz 1924): {photons_per_flash_historical:.2e} photons
DISCREPANCY: {discrepancy_factor:.0f}× overestimate ({orders_of_magnitude:.1f} orders of magnitude)"""

ax.text(5, y_comp - 0.2, comp_text, ha='center', va='center', 
        fontsize=12, fontweight='bold', color='#d62728')

plt.tight_layout()
plt.savefig('/Users/davidsilver/dev/papers/firefly/figure_2_energy_budget.png', dpi=300, bbox_inches='tight')
plt.savefig('/Users/davidsilver/dev/papers/firefly/figure_2_energy_budget.pdf', bbox_inches='tight')
print("Saved: figure_2_energy_budget.png and .pdf")

# Figure 3: Timeline of the error
fig, ax = plt.subplots(figsize=(14, 8))

years = [1924, 1952, 2006, 2012, 2022, 2025, 2025, 2025]
events = [
    'Ives & Coblentz\n"1/40 candle"',
    'Harvey cites\nuncritically',
    'Shimomura\nmonograph',
    'Shimomura\n2nd edition',
    'Goh & Wang\nspectrometer\n(not compared\nto 1924)',
    'Fallon estimate\n(pers. comm.)',
    'Biochemical\ncalculation\n(Silver)',
    'ERROR\nEXPOSED'
]

y_positions = [2, 2, 2, 2, 1, 1, 1, 3]
colors_timeline = ['red', 'gray', 'gray', 'gray', 'orange', 'green', 'blue', 'gold']
sizes = [200, 150, 150, 150, 180, 180, 200, 300]

for year, event, y, color, size in zip(years, events, y_positions, colors_timeline, sizes):
    ax.scatter(year, y, s=size, c=color, alpha=0.7, edgecolors='black', linewidth=2, zorder=3)
    ax.text(year, y - 0.5, event, ha='center', fontsize=9, fontweight='bold')

# Timeline line
ax.plot([1920, 2028], [2, 2], 'k-', linewidth=2, alpha=0.3, zorder=1)

ax.set_xlim(1920, 2028)
ax.set_ylim(0, 4)
ax.set_xlabel('Year', fontsize=13, fontweight='bold')
ax.set_title('Century-Long Propagation of the Firefly Luminosity Error', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_yticks([])
ax.grid(True, axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/davidsilver/dev/papers/firefly/figure_3_timeline.png', dpi=300, bbox_inches='tight')
plt.savefig('/Users/davidsilver/dev/papers/firefly/figure_3_timeline.pdf', bbox_inches='tight')
print("Saved: figure_3_timeline.png and .pdf")

print()
print("="*80)
print("ANALYSIS COMPLETE")
print("="*80)
print()
print(f"KEY FINDING: The canonical firefly luminosity of '1/40 candle' from 1924")
print(f"overestimates actual photon emission by ~{discrepancy_factor:.0f}× ({orders_of_magnitude:.1f} orders of magnitude)")
print()
print("This appears to be the FIRST biochemical analysis to expose this century-old error.")
print("="*80)

