##
## Example script to reset sensor
##
import pySynaptics

target_pid = 0xcfa0
reset_addr = 0x2a


def main():
    target_dev = {}
    target_dev['pid'] = target_pid
    data = [0x01]
    response = pySynaptics.write_rmi_register(target_dev, reset_addr, data)
    if response['result'] != 0:
        print("write_rmi_register failed.")
        return
    else:
        print("write_rmi_register success.")

if __name__ == "__main__":
    main()