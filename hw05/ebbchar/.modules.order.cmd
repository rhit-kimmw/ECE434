cmd_/home/debian/ECE434/hw05/ebbchar/modules.order := {   echo /home/debian/ECE434/hw05/ebbchar/ebbchar.ko; :; } | awk '!x[$$0]++' - > /home/debian/ECE434/hw05/ebbchar/modules.order
