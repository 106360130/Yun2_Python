print('The program supports three types of alerts, "namely danger zone", "humidity", and "temperature"')
print('The temperature range is between 21 c (70 f) and 28 c (82 f)')
print('The humidity range is between 40 and 70 percentage')
humidity_high = 70
humidity_low = 40
temperature_high = 21
temperature_low = 28
while True:
    baby_name = input('Enter baby name : ')
    if not baby_name :
        baby_name = 'baby'

    #print(baby_name)

    alert_type = input('Enter alert type : ("namely danger zone", "humidity", and "temperature")')

    if alert_type == 'danger zone' :
        zone_name = input('Enter zone name : ')
        print(baby_name + 'is entering the ' + zone_name + '. Take a look now!')

    elif alert_type == 'humidity' :
        humidity_now = input('Enter humidity : ')
        if humidity_now :
            if int(humidity_now) > 70 :
                print(baby_name + ' room humidity '+ humidity_now + ' seems quite high')
            elif int(humidity_now) < 40 :
                print(baby_name + ' room humidity '+ humidity_now + ' seems quite low')

            

    elif alert_type == 'temperature' :
        temperature = input('Enter temperature in Celsius : ')
        if temperature :
            temperature_uint = input('Enter user temperature uint, the value shold be "c" or "f" :')
            if temperature_uint == 'c' :
                if int(temperature) > temperature_high :
                    print(baby_name + ' room temperature ' + temperature + ' seems quite high')
                elif int(temperature) < temperature_high :
                    print(baby_name + ' room temperature ' + temperature + ' seems quite low')

            elif temperature_uint == 'f' :
                temperature = int(temperature)*(9/5) + 32
                temperature_high = int(temperature_high)*(9/5) + 32
                temperature_low = int(temperature_low)*(9/5) + 32
                if temperature > temperature_high :
                    print(baby_name + ' room temperature ' + str(int(temperature)) + ' seems quite high')
                elif temperature < temperature_low :
                    print(baby_name + ' room temperature ' + str(int(temperature)) + ' seems quite low')

