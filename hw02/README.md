# HW02--GPIO Speed
### Martino Kim

---

>test files in testFile folder.
>blinkLED, toggle1, toggle2 are compiled c files to run.
>blinkLED.py, toggle1.py, toggle2.py, toggle1.c, toggle2.c are used to blink the LED faster.
>for python files, use ./filename.py to execute
>for c files, use ./compiled_c_files_name to execute.

---

## Buttons and LEDs
> ./buttonLED.py for running the Buttons and LEDs code. 
> pins P9_11 to P_14 are assigned for buttons, and P9_15 to P9_18 are assigned for LEDs. Each buttons and LEDs are paired each other, and the assigned LED is turned on when the corresponding button is pressed.

---

## Measuring a gpio pin on an Oscilloscope
1. What's the min and max voltage?
* min voltage: 4.2803mV, max voltage: 3.1655V

2. What period and frequency is it?
* Period: 1.0227s, frequency: 0.97782 Hz

3. Run htop and see how much processor you are using.
* htop is using 1.9% to 3.9% of the CPU.
* There are total 42 tasks with total 42% CPU using.
* ./blinkLED.sh is using up to 1.3% of the CPU.

4. Try different values for the sleep time. What's the shortest period you can get? Make a table of the fastest values you try and the corresponding period and processor usage. Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables

|sleep time|period|CPU Usage|
|---|---|---|
|0.5|1022.7ms|1.3 %|
|0.1|229.87ms|2.0 %|
|0.01|47.609ms|10.7 %|
|0.001|24.021 ms|20.9 %|

5. How stable is the period?
* as sleep time increases, the period gets very unstable.

6. Try launching something like vi. How stable is the period?
* the period has been much unstable when launching vi

7. Try cleaning up blinkLED.sh and removing unneeded lines. Does it impact the period?
* No. the period still oscillates from 20ms to 24ms

8. What's the shortest period you can get?
* I got 24.021ms.

---

## Python

1. What period and frequency is it?
* Period: 283.23 us, frequency:3.5402 kHz

2. Run htop and see how much processor you are using.
* it is using 70.2% of the memory

3. Present the shell script and Python script results in a table for easy comparison
* table at the bottom

---

## C
* table at the bottom

## gpiod
* 

### getsetEvent.py
Modify getsetEvent.py to read your four buttons and turn on the corresponding LED.
* done at buttonLED.py 
* run the code by ./buttonLED.py

## Etch-a-sketch
* run etch_a_sketch2.py by ./etch_a_sketch.py
* Buttons are connected at pin P9_11 to P9_14, each corresponding to 'up', 'down', 'left', 'right' button.
* Pressing 'up' and 'down' button at a same time clears the game, and pressing 'up' and 'right' (button1 & button4) exits the program.

## blinkLED table
|method|period|frequency|CPU Usage|
|---|---|---|---|
|sh|24.021ms|41.6 Hz|18.2 %|
|Python|282.23 us|3.5402 kHz|95%|
|C|160.86 ns|6.2165 MHz|64.2 %|
|toggle1.py|210.15 us|4.7585 kHz|66.7 %|
|toggle1.c|180.2 us|5.5493 kHz|54.0 %|
|toggle2.py|225.35 us|4.4376 kHz| 77.1 %|
|toggle2.c|168.62 us|5.9305 kHz|48.4%|
