# Wake on lan

Python CLI for magic packet creation and sending WOL packets

# use it on your machine

```py
# Clone this repository
git clone https://github.com/stevenaubertin/wol.py
# Go into the repository
cd wol.py
# Run the app
python3 wol.py [YOUR_MAC_ADDRESS]
```

### you may also just create your own .py file and paste the contents of wol.py into your file

## usage

### as a command:

```py
python3 wol.py [YOUR_MAC_ADDRESS]
```

### as a module in another file

```py
#import the file (needs to be in the same directory)
import wol

#code to only create magic packet
magic_packet = wol.create_magic_packet('AB:CD:EF:GH:IJ:KL')

#code to wake up and machine
wol.wake_up('AB:CD:EF:GH:IJ:KL')
```
