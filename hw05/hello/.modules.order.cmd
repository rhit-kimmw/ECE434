cmd_/home/debian/ECE434/hw05/hello/modules.order := {   echo /home/debian/ECE434/hw05/hello/hello.ko; :; } | awk '!x[$$0]++' - > /home/debian/ECE434/hw05/hello/modules.order
