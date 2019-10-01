# WIFI_based_RFID_attendance-system_using_NodeMcu_and_Django

-> This attendance system is based on RFID technology for identification. It sends the attendance data to the server using wifi.

-> For reading RFID card and sending data to server RFID module RC522 and NodeMCU is used. The server side code is written using django and frontend is made using Bootstrap 4.

-> It also do not requires the wifi credentials to be hard coded inside it. I have used Arduino's Wifi manager library for this. It automatically creates a hotspot when it doesn't find previous or saved wifi. You can simply connect with its hotspot using a device and can give required wifi credentials and it will connect to that easily.
