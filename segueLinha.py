def control(left_sensor, right_sensor, speed):
    error = right_sensor - left_sensor
    if(0 <= speed <=100):
        engTorque = 5000
    elif(100 < speed <= 110):
        engTorque = 4000
    elif(110 < speed <= 120):
        engTorque = 2800
    else:
        engTorque = 1400
   
    if(error <= 0):
        P = 0.5
    else:
        P = 0.3
       
    return {
        'engineTorque': engTorque,
        'brakingTorque': 0,
        'steeringAngle': error * P,
        'log': [
            { 'name': 'Speed', 'value': speed, 'min': 0, 'max': 200 },
            { 'name': 'Left_sensor', 'value': left_sensor, 'min': 0, 'max': 1 },
            { 'name': 'Right_sensor', 'value': right_sensor, 'min': 0, 'max': 1 }
        ]
    }