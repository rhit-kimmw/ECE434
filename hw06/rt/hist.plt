# This code is from Julia Cartwright julia@kernel.org

set terminal png medium size 800,600
# set terminal X11 persist
set output "RT.png"
set datafile commentschars "#"

set logscale y

# trim some of the distortion from the bottom of the plot
set yrang [0.85:*]

set xlabel "t (us)"
set ylabel "Count"

plot "rt_noload.hist" using 1:2 with histeps title "RT No load",    \
     "rt_load.hist" using 1:2 with histeps title "RT load"
