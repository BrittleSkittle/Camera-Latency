# Camera Latency

`sudo modprobe usbmon`
`tcpdump -i usbmon2 -vvvv -A -w nameFramerate.pcap`
Open file in WireShark, and save packets as csv and C array. Change the type of the c array to txt. 
