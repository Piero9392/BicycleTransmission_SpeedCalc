# Transmission list
transmission = {
    'Wheel size': (26, 27.5, 28, 29),
    'Pinion P1.18': {
        'name': 'Pinion P1.18',
        'front_cog': 34,
        'rear_cog': 32,
        'gear_ratio': (0.55, 0.61, 0.68, 0.76, 0.84, 0.94, 1.05, 1.18, 1.32, 1.45, 1.61, 1.82, 2.04, 2.27, 2.5, 2.78, 3.13, 3.45)},
    'Pinion C1.12': {
        'name': 'Pinion C1.12',
        'front_cog': 34,
        'rear_cog': 32,
        'gear_ratio': (0.55, 0.64, 0.76, 0.89, 1.05, 1.23, 1.45, 1.72, 2.04, 2.38, 2.78, 3.33)},
    'Rohloff': {
        'name': 'Rohloff',
        'front_cog': 50,
        'rear_cog': 22,
        'gear_ratio': (0.279, 0.316, 0.360, 0.409, 0.464, 0.528, 0.600, 0.682, 0.774, 0.881, 1.000, 1.135, 1.292, 1.467)},
    'Shimano Alfine 11': {
        'name': 'Shimano Alfine 11',
        'front_cog': 42,
        'rear_cog': 20,
        'gear_ratio': (0.527, 0.681, 0.770, 0.878, 0.995, 1.134, 1.292, 1.462, 1.667, 1.888, 2.153)},
    'Shimano 3x10': {
        'name': 'Shimano 3x10',
        'front_cog': (22, 30, 40),
        'cassette': (36, 32, 28, 24, 21, 19, 17, 15, 13, 11)},
    'Shimano 2x11': {
        'name': 'Shimano 2x11',
        'front_cog': (30, 46),
        'cassette': (42, 37, 32, 28, 24, 21, 19, 17, 15, 13, 11)},
    'Shimano 1x11': {
        'name': 'Shimano 1x11',
        'front_cog': 40,
        'cassette': (46, 37, 32, 28, 24, 21, 19, 17, 15, 13, 11)},
    'Shimano 1x12': {
        'name': 'Shimano 1x12',
        'front_cog': 34,
        'cassette': (51, 45, 39, 33, 28, 24, 21, 18, 16, 14, 12, 10)}
}

# Speed calculation function
def calculate_speed(name, gear_ratio, wheel_size, cadence, front_cog=None, rear_cog=None, drive_type='chain'):
    range_percent = round((gear_ratio[-1] / gear_ratio[0]) * 100)
    header = f"{name} - Total range: {range_percent}%\nGear | Ratio | Speed (km/h)"
    print(header)
    
    with open('Data/Text.txt', 'a') as file:
        file.write(header + '\n')
        
        for i, ratio in enumerate(gear_ratio):
            if drive_type == 'belt':
                speed = ratio * wheel_size * 0.0000254 * 3.14159 * cadence * 60 * (front_cog / rear_cog)
            else:  # chain drive
                speed = ratio * wheel_size * 0.0000254 * 3.14159 * cadence * 60
            
            output_line = f"{i + 1} | {ratio:.2f} | {round(speed, 1)} km/h"
            print(output_line)
            file.write(output_line + '\n')
        
        file.write('---------------------\n')
    print('---------------------')

# User input for wheel size and cadence
wheel_size = float(input('Enter wheel size (inch): '))
cadence = int(input('Enter cadence (rpm): '))
print('---------------------')

# Validate wheel size and cadence
if wheel_size in transmission['Wheel size'] and 0 < cadence <= 120:
    with open('Data/Text.txt', 'w') as file:
        file.write(f'Wheel size: {wheel_size} inch\nCadence: {cadence} rpm\n--------------------\n')

    # Calculate speeds for belt-driven transmissions
    belt_drives = ['Pinion P1.18', 'Pinion C1.12', 'Rohloff', 'Shimano Alfine 11']
    for drive in belt_drives:
        t = transmission[drive]
        calculate_speed(
            name=t['name'],
            gear_ratio=t['gear_ratio'],
            wheel_size=wheel_size,
            cadence=cadence,
            front_cog=t['front_cog'],
            rear_cog=t['rear_cog'],
            drive_type='belt'
        )

    # Calculate speeds for chain-driven transmissions
    chain_drives = ['Shimano 3x10', 'Shimano 2x11', 'Shimano 1x11', 'Shimano 1x12']
    for drive in chain_drives:
        t = transmission[drive]
        
        if drive == 'Shimano 3x10':
            # Combining three gear ratios based on front cog sets
            gear_ratio = [t['front_cog'][0] / i for i in t['cassette'][0:4]] + \
                         [t['front_cog'][1] / i for i in t['cassette'][3:7]] + \
                         [t['front_cog'][2] / i for i in t['cassette'][6:]]
        elif drive == 'Shimano 2x11':
            # Combining two gear ratios based on front cog sets
            gear_ratio = [t['front_cog'][0] / i for i in t['cassette'][0:7]] + \
                         [t['front_cog'][1] / i for i in t['cassette'][4:]]
        else:
            gear_ratio = [t['front_cog'] / i for i in t['cassette']]
        
        calculate_speed(name=t['name'], gear_ratio=gear_ratio, wheel_size=wheel_size, cadence=cadence)
else:
    error_message = 'Non-existent value of wheel size or cadence!\n' \
                    'Wheel size options: 26, 27.5, 28, or 29 inches\n' \
                    'Cadence should be more than 0 and less than or equal to 120 rpm\n'
    print(error_message)
    with open('Data/Text.txt', 'a') as file:
        file.write(f'Wheel size: {wheel_size}"\nCadence: {cadence} rpm\n')
        file.write('-----------------\n')
        file.write(error_message)
