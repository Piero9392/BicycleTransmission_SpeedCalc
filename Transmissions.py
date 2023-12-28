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
# Speed function for transmission with belt
def belt(name, gear_ratio, front_cog, rear_cog, wheel_size, cadence):
    print(f'{name} - Total range: {round(gear_ratio[-1] / gear_ratio[0] * 100)}%')
    print('Gear | Ratio | Speed')
    file = open('Data/Text.txt', 'a')
    file.write(f'{name} (Total range: {round(gear_ratio[-1] / gear_ratio[0] * 100)}%)\n')
    file.write('Gear | Ratio | Speed\n')
    for i in range(0, len(gear_ratio)):
        speed = gear_ratio[i] * float(wheel_size) * 0.0000254 * 3.14159 * float(cadence) * 60 * (front_cog / rear_cog)
        print(f'{i+1} | {"%.2f" % gear_ratio[i]} | {round(speed, 1)} km/h')
        file = open('Data/Text.txt', 'a')
        file.write(f'{i+1} | {"%.2f" % gear_ratio[i]} | {round(speed, 1)} km/h\n')
        file.close()
    file = open('Data/Text.txt', 'a')
    file.write('---------------------\n')
    print('---------------------')
# Speed function for transmission with derailleur
def chain(name, gear_ratio, wheel_size, cadence):
    print(f'{name} - Total range: {round(gear_ratio[-1] / gear_ratio[0] * 100)}%')
    print('Gear | Ratio | Speed')
    file = open('Data/Text.txt', 'a')
    file.write(f'{name} (Total range: {round(gear_ratio[-1] / gear_ratio[0] * 100)}%)\n')
    file.write('Gear | Ratio | Speed\n')
    for i in range(0, len(gear_ratio)):
        speed = gear_ratio[i] * float(wheel_size) * 0.0000254 * 3.14159 * float(cadence) * 60
        print(f'{i+1} | {"%.2f" % gear_ratio[i]} | {round(speed, 1)} km/h')
        file = open('Data/Text.txt', 'a')
        file.write(f'{i+1} | {"%.2f" % gear_ratio[i]} | {round(speed, 1)} km/h\n')
        file.close()
    file = open('Data/Text.txt', 'a')
    file.write('---------------------\n')
    file.close()
    print('---------------------')
# Input data of 'wheel size' and 'cadence'
wheel_size = float(input('Enter wheel size (inch): '))
cadence = int(input('Enter cadence (rpm): '))
print('---------------------')
# Range for wheel size of 'Transmission list' and 'cadence' from 0 to 120 rpm
if wheel_size == transmission['Wheel size'][0] or wheel_size == transmission['Wheel size'][1] or wheel_size == transmission['Wheel size'][2] or wheel_size == transmission['Wheel size'][3]:
    if cadence > 0 and cadence <= 120:
        # Write data file
        file = open('Data/Text.txt', 'w')
        file.write('Wheel size: '+ str(wheel_size) + 'inch\n')
        file.write('Cadence: '+ str(cadence) + 'rpm\n')
        file.write('--------------------\n')
        file.close()
        # Result for Pinion P1.18 with Gates Carbon Drive
        name = transmission['Pinion P1.18']['name']
        gear_ratio = transmission['Pinion P1.18']['gear_ratio']
        front_cog = transmission['Pinion P1.18']['front_cog']
        rear_cog = transmission['Pinion P1.18']['rear_cog']
        belt(name, gear_ratio, front_cog, rear_cog, wheel_size, cadence)
        # Result for Pinion C1.18 with Gates Carbon Drive
        name = transmission['Pinion C1.12']['name']
        gear_ratio = transmission['Pinion C1.12']['gear_ratio']
        front_cog = transmission['Pinion C1.12']['front_cog']
        rear_cog = transmission['Pinion C1.12']['rear_cog']
        belt(name, gear_ratio, front_cog, rear_cog, wheel_size, cadence)
        # Result for Rohloff 500/14 with Gates Carbon Drive
        name = transmission['Rohloff']['name']
        gear_ratio = transmission['Rohloff']['gear_ratio']
        front_cog = transmission['Rohloff']['front_cog']
        rear_cog = transmission['Rohloff']['rear_cog']
        belt(name, gear_ratio, front_cog, rear_cog, wheel_size, cadence)
        # Result for Shimano Alfine 11 with Gates Carbon Drive
        name = transmission['Shimano Alfine 11']['name']
        gear_ratio = transmission['Shimano Alfine 11']['gear_ratio']
        front_cog = transmission['Shimano Alfine 11']['front_cog']
        rear_cog = transmission['Shimano Alfine 11']['rear_cog']
        belt(name, gear_ratio, front_cog, rear_cog, wheel_size, cadence)
        # Result for Shimano Deore 3x10
        name = transmission['Shimano 3x10']['name']
        gear_ratio_1 = [transmission['Shimano 3x10']['front_cog'][0] / i for i in transmission['Shimano 3x10']['cassette'][0:4]]
        gear_ratio_2 = [transmission['Shimano 3x10']['front_cog'][1] / i for i in transmission['Shimano 3x10']['cassette'][3:7]]
        gear_ratio_3 = [transmission['Shimano 3x10']['front_cog'][2] / i for i in transmission['Shimano 3x10']['cassette'][6:]]
        gear_ratio = gear_ratio_1 + gear_ratio_2 + gear_ratio_3
        chain(name, gear_ratio, wheel_size, cadence)
        # Result for Shimano  GRX 2x11
        name = transmission['Shimano 2x11']['name']
        gear_ratio_1 = [transmission['Shimano 2x11']['front_cog'][0] / i for i in transmission['Shimano 2x11']['cassette'][0:7]]
        gear_ratio_2 = [transmission['Shimano 2x11']['front_cog'][1] / i for i in transmission['Shimano 2x11']['cassette'][4:]]
        gear_ratio = gear_ratio_1 + gear_ratio_2
        chain(name, gear_ratio, wheel_size, cadence)
        # Result for Shimano GRX 1x11
        name = transmission['Shimano 1x11']['name']
        gear_ratio = [transmission['Shimano 1x11']['front_cog'] / i for i in transmission['Shimano 1x11']['cassette']]
        chain(name, gear_ratio, wheel_size, cadence)
        # Result for Shimano Deore XT 1x12
        name = transmission['Shimano 1x12']['name']
        gear_ratio = [transmission['Shimano 1x12']['front_cog'] / i for i in transmission['Shimano 1x12']['cassette']]
        chain(name, gear_ratio, wheel_size, cadence)
    # If 'wheelsize' is true and cadence is out of range (0 - 120rpm):
    else:
        print('Non-existent value of cadence!\nCadence should be more 0 and less than 120rpm')
        file = open('Data/Text.txt', 'a')
        file.write('Wheel size: ' + str(wheel_size) + '"\n')
        file.write('Cadence: '+ str(cadence) + 'rpm\n')
        file.write('-----------------\n')
        file.write('Non-existent value of cadence!\nCadence should be more 0 and less than 120rpm\n')
        file.close()
# If 'wheelsize' is out of range
else:
    print('Non-existent value of wheel size!\nExisting sizes: 26, 27, 28 or 29inch')
    file = open('Data/Text.txt', 'a')
    file.write('Wheel size: ' + str(wheel_size) + '"\n')
    file.write('Cadence: '+ str(cadence) + 'rpm\n')
    file.write('-----------------\n')
    file.write('Non-existent value of wheel size!\nExisting sizes: 26, 27, 28 or 29inch\n')
    file.close()