from pypylon import pylon
from copy import deepcopy


def capture():
    images = []

    capture.camera.StartGrabbingMax(1)
    while capture.camera.IsGrabbing():

        # Get a result from the camera, with an appropriate timeout
        grab_result = capture.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

        # Let the user know if we couldn't get a result
        if not grab_result.GrabSucceeded():
            raise Exception("Failed to grab image")

        # Indicate that we got an image
        print(f"Grabbed image of size {grab_result.Width}x{grab_result.Height}")

        # Convert the image to an OpenCV-style image
        images.append(deepcopy(grab_result.Array))  # FIXME: There's a better way of doing this, I hope

        # Allow the camera to take another image
        grab_result.Release()

    # Disconnect from the camera
    capture.camera.StopGrabbing()
    capture.camera.Close()

    # Return the first (only) image taken
    return images[0]


capture.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
