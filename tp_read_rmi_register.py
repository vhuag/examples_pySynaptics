##
## Example script to read a rmi register from the touchpad.
##
import pySynaptics

target_pid = 0xcfa0
target_addr = 0xe9
target_size = 6

def main():

    target_dev = {}
    target_dev['pid'] = target_pid

    response = pySynaptics.read_rmi_register(target_dev, target_addr, target_size)
    if response['result'] == 0:
        data = response['data'][1:target_size+1]
        hex_data = ' '.join(f"{byte:02x}" for byte in data)
        print(hex_data)

if __name__ == "__main__":
    main()