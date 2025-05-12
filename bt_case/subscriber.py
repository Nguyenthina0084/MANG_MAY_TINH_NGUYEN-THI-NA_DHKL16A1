import paho.mqtt.client as mqtt 

def on_connect(client, userdata, flags, rc): 
    if rc == 0: 
        print("✅ Kết nối MQTT thành công!") 
        client.subscribe("iot/khdl/esp32") 
    else: 
        print("❌ Lỗi kết nối, mã lỗi:", rc) 
def on_message(client, userdata, msg): 
    print(f"{msg.topic}: {msg.payload.decode()}") 
    
client = mqtt.Client() 
