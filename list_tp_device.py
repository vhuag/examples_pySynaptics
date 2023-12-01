##
## Example of how to list all touchpad devices
##
import pySynaptics

def main():
    devices = pySynaptics.list_devices()
    tp_devices = [device for device in devices if device['devtype'] == "Touchpad"]

    print(f"Total touchpad devices: {len(tp_devices)}")
    
    for i, device in enumerate(tp_devices):
        print(f"=====================================\n"
              f"Touchpad device index: {i}\n"
              f"Touchpad device PID value: {hex(device['pid'])}")

if __name__ == "__main__":
    main()