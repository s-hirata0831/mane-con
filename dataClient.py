import requests
import json
import serial
import time
import datetime

def send_post_request(value):
    url='http://raspberrypi.local:5000/get_variable'
    data={'value': value}
    headers={'Content-type': 'application/json'}
	
    response=requests.post(url, data=json.dumps(data), headers=headers)
	
    if response.status_code == 200:
        print('POST request successfull --Temp--')
    else:
        print(f'POST request faiiled with status code: {response.status_code}')
		
def send_post_led(value):
    url='http://raspberrypi.local:5000/get_pet'
    data={'value': value}
    headers={'Content-type': 'application/json'}
	
    response=requests.post(url, data=json.dumps(data), headers=headers)
	
    if response.status_code == 200:
        print('POST request successfull --led--')
    else:
        print(f'POST request faiiled with status code: {response.status_code}')
		
def send_post_serial(value):
    url='http://172.20.10.2:5000/get_serial'
    data={'value': value}

    headers={'Content-type': 'application/json'}
	
    response=requests.post(url, data=json.dumps(data), headers=headers)
	
    if response.status_code == 200:
        print('POST request successfull --Serial--')
    else:
        print(f'POST request faiiled with status code: {response.status_code}')
        
def send_post_serial2(value):
    url='http://172.20.10.2:5000/get_serial2'
    data={'value': value}

    headers={'Content-type': 'application/json'}
	
    response=requests.post(url, data=json.dumps(data), headers=headers)
	
    if response.status_code == 200:
        print('POST request successfull --Serial2--')
    else:
        print(f'POST request faiiled with status code: {response.status_code}')
		
if __name__ == '__main__':
    #ser = serial.Serial('/dev/ttyACM0',9600,timeout=1000)
    #String_data = ser.read_all()
    #String_data2 = String_data.strip().decode('utf-8')
    while True:
        #Serial
        ser = serial.Serial('/dev/ttyACM0',9600,timeout=1000)

        #Temp
        target_prefix="Temp"
        received_lines=[]
		
        while not any(line.startswith(target_prefix) for line in received_lines):
            line = ser.readline().decode('utf-8').strip()
            received_lines.append(line)
			
            matching_lines = [line for line in received_lines if line.startswith(target_prefix)]
            if matching_lines:
                target_line_data = matching_lines[0]
                send_post_request(target_line_data[5:])
            else:
                send_post_request("Loading...")
			
        #led
        target_led="Humid"
        received_led=[]
		
        while not any(line.startswith(target_led) for line in received_led):
            line = ser.readline().decode('utf-8').strip()
            received_led.append(line)
            matching_lines = [line for line in received_led if line.startswith(target_led)]
            if matching_lines:
                target_led_data = matching_lines[0]
                send_post_led(target_led_data[6:])
            else:
                send_post_led("Loading...")
		
		#Serial
		#String_data = ser.read_all()
		#String_data2 = String_data.strip().decode('utf8')
		#send_post_serial(String_data2)
        time.sleep(1)
    ser.close()
