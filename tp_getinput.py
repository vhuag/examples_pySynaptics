import pySynaptics
import os
# if this is windows
if os.name == 'nt':
    import msvcrt

def main():

    target_dev = {}
    target_dev['pid'] = 0xcfa0

    if target_dev != None:
        while True:
            if os.name == 'nt':
                if msvcrt.kbhit() and msvcrt.getch() == b'\x1b':  # ESC key is '\x1b'
                    break  # Exit the loop if ESC is pressed
            x = pySynaptics.read_hid_report(target_dev, 0x0c, 512)
            if x['result'] == 0:  # Assuming 0 indicates success
                data = x['data'][:64]
                hex_data = ' '.join(f"{byte:02x}" for byte in data)
                print(hex_data)

if __name__ == "__main__":
    main()