# HW07
### Martino Kim


---

## 1-wire Temperature Sensors

> sudo ./oneWire.py command reads the three one-wire temperature sensors using port P9_12. First, load /lib/firmware/BB-W1-P9.12-00A0.dtbo at /boot/uEnv.txt uboot overlay before running the code. 

> to change port to P9_14, wire the temperature sensors to P9_14, change /boot/uEnv.txt from P9_12 to P9_14, reboot, and run sudo./oneWire.py again.

---

## systemd

> Flask service runs automatically when bone boots up. 