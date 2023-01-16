# HW03--i2c and LED
### Martino Kim

---

> pins P9_19 and P9_20 for SCL and SDA pin

> pins P9_21 and P9_22 for ALERT pins for TMP101

> pins P8_11 and P8_12, P8_33 and P8_35 for Rotary Encoders.

>matrix8x8 is a files from examples

> to execute the homework files, run the command './filename'.

> For exception, to execute etch_a_sketch3_encoder.py, run 'setup.sh' first by ./setup.sh command, and then execute ./etch_a_sketch3_encoder.py


---

## TMP101

> ./readTempF.sh for running the TMP101 temperature sensing with a shell file

> ./readTempF.py for TMP101 temperature sensing with python

> ./readTempAlert.py for setting temperature limits for each TMP101 with interrupt on the ALERT pin.

---

## Etch-a-sketch

> ./etch_a_sketch3.py runs a etch-a-sketch game with LED matrix. 

---

## Rotary Encoders

> ./etch_a_sketch3_encoder.py runs a etch-a-sketch game with LED matrix and rotary encoders.

> to run a game, you should first run ./setup.sh file, which sets up the pins to be in eqep mode for the rotary encoders.

> also needed to disable the hdmi pins too.

