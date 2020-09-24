KOREK-WifiLora-GPS_tracker

Live GPS-tracker for KOREK

##### Hardware:

- 1 Heltec V2 ESP32 Board

##### Feature:

  - Control Motor rotation & stop on sensors limit
  
##### Video:

<figure class="video_container">
  <iframe width="1280" height="721" src="https://www.youtube.com/embed/qHuMAlqzE4M?list=TLPQMjQwOTIwMjAgqT6ALYmxbw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</figure>

##### Configure your env & Copy micropython on Board:
```
sudo apt-get install python3-pip
sudo pip3 install esptool rshell
wget https://micropython.org/resources/firmware/esp32-idf4-20191220-v1.12.bin
sudo esptool.py --port /dev/ttyUSB0 erase_flash
sudo esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash 0x1000 esp32-idf4-20191220-v1.12.bin
```

##### Installation
```
# 1. Clone this repo
# 2. Set receiver to True/False in main.py (Default is the Lora sender)
# 3. Upload to Heltec v2 board
sudo rshell -p /dev/ttyUSB0 -b 115200
cd MyStore/ && cp -r * /pyboard/
# 4. Wire pins according to common.py
# 5. Trigger the motor by putting 3.3V to pins 34 and 35 
(you should need an external relay radio remote command)
```

#### Debug
```
sudo rshell -p /dev/ttyUSB0
repl
```
