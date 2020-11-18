from pypylon import pylon


def main():
    # Connect to the first camera found
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    camera.Open()

    # Print the device name
    print(f"Connected to device \"{camera.GetDeviceInfo().GetModelName()}\"")


if __name__ == '__main__':
    main()
