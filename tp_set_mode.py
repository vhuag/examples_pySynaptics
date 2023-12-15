##
## Example script to set rmi mode
##
import pySynaptics
import sys

if len(sys.argv) != 2:
    print("Usage: python tp_set_rmi_mode.py <mode>")
    sys.exit(1)
mode = int(sys.argv[1])

target_pid = 0xcfa0

def main():
    target_dev = {}
    target_dev['pid'] = target_pid
    response = pySynaptics.set_mode(target_dev, mode)
    if response['result'] != 0:
        print("set_mode failed.")
        return
    else:
        print("set_mode %d success." % mode)

if __name__ == "__main__":
    main()