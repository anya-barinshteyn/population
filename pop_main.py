import matplotlib.pyplot as plt
import pop_module as pm

#
# Main program which uses function from the pop_module module
#
subplots = plt.subplots(2, 2, figsize=(20, 10))

# File name variables
file_1_deg = 'project2/data/gpw_v4_population_density_rev11_2020_1_deg.asc'
file_2pt5_min = 'project2/data/gpw_v4_population_density_rev11_2020_2pt5_min.asc'

# Placing charts to subplots with a module function
# 2 files with different scaling are used processed with the same function
pm.get_subplot(subplots=subplots, ax_idx1=0, ax_idx2=0,
               file_name=file_2pt5_min, area=('Африка', -30, 60, 40, -40))
pm.get_subplot(subplots=subplots, ax_idx1=0, ax_idx2=1,
               file_name=file_2pt5_min, area=('Австралия', 110, 180, 10, -60))
pm.get_subplot(subplots=subplots, ax_idx1=1, ax_idx2=0,
               file_name=file_1_deg, area=('Весь мир', -180, 180, 90, -90))
pm.get_subplot(subplots=subplots, ax_idx1=1, ax_idx2=1,
               file_name=file_1_deg, area=('Евразия', -20, 180, 0, 80))

plt.suptitle('Плотность населения регионов мира, чел/кв.км.', fontsize=16)
plt.tight_layout()
plt.show()
