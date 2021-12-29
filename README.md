## plug ir module into pin 18

## install following
sudo apt-get install lirc liblircclient-dev

## add following to /etc/modules
lirc_dev
lirc_rpi gpio_in_pin=18 gpio_out_pin=22

## add following to /etc/lirc/hardware.conf

```vim
# /etc/lirc/hardware.conf
#
# Arguments which will be used when launching lircd
LIRCD_ARGS="--uinput"
 
# Don't start lircmd even if there seems to be a good config file
# START_LIRCMD=false
 
# Don't start irexec, even if a good config file seems to exist.
# START_IREXEC=false
 
# Try to load appropriate kernel modules
LOAD_MODULES=true
 
# Run "lircd --driver=help" for a list of supported drivers.
DRIVER="default"
# usually /dev/lirc0 is the correct setting for systems using udev
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
 
# Default configuration files for your hardware if any
LIRCD_CONF=""
LIRCMD_CONF=""
```

## run command and follow instructions very carefully
(note that "the next button" is not a button labeled "next" on your remote)

`irrecord -d /dev/lirc0 ~/lircd.conf`

## replace lirc.conf file with new conf file

`sudo cp lircd.conf /etc/lirc/lircd.conf`

## test with `irw` command

## create your own audio files of insults and add them to explicit or clean folders

## run following script and press buttons
