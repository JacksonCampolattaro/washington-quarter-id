from pypylon import pylon
import cv2


def main():
    # Connect to the first camera found
    camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
    camera.Open()

    # Print the device name
    print(f"Connected to device \"{camera.GetDeviceInfo().GetModelName()}\"")

    # Choose the right camera settings
    camera.AutoFunctionROIUseBrightness.SetValue(True)

    # Tell the camera to start taking pictures
    camera.StartGrabbingMax(1)
    while camera.IsGrabbing():

        # Get a result from the camera, with an appropriate timeout
        grab_result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        # Let the user know if we couldn't get a result
        if not grab_result.GrabSucceeded():
            raise Exception("Failed to grab image")

        # Indicate that we got an image
        print(f"Grabbed image of size {grab_result.Width}x{grab_result.Height}")

        # Convert the image to an OpenCV-style image
        image = grab_result.Array

        # Save the image
        cv2.imwrite("test.png", image)

        # Allow the camera to take another image
        grab_result.Release()

    # Disconnect from the camera
    camera.Close()


if __name__ == '__main__':
    main()
