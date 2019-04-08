import os
import PySpin
import datetime
import homepage_tabs as gui
global camR


def runApp(cam, nodemap, nodemap_tldevice) :

    # Main area to run UI
	gui.runUI()
    # Call function to bring up user interface

    # User interface should call all relative functions



def shutdown():
    ## shutdown L.E.Ds etc

    return True

def stopCam(cam) :
    cam.DeInit()
    return True

def savImg(myimg) :
    now = datetime.datetime.now()
    myimg.Save(now.strftime("%Y_%m_%d_%H_%M"))
    return True

def getallImgs() :
    list_imgs = os.listdirs("dickpics/")

    return list_imgs

def getmyImg() :
    image_result = cam.GetNextImage()
    #  Convert image to mono 8
    #
    #  *** NOTES ***
    #  Images can be converted between pixel formats by using
    #  the appropriate enumeration value. Unlike the original
    #  image, the converted one does not need to be released as
    #  it does not affect the camera buffer.
    #
    #  When converting images, color processing algorithm is an
    #  optional parameter.
    #image_converted = image_result.Convert(PySpin.PixelFormat_Mono8, PySpin.HQ_LINEAR)

    return image_result

def releaseImg(image_result) :
    image_result.Release()
    return True

def acquire_images(cam, nodemap, nodemap_tldevice) :
    result = True

    node_acquisition_mode = PySpin.CEnumerationPtr(nodemap.GetNode('AcquisitionMode'))
    if not PySpin.IsAvailable(node_acquisition_mode) or not PySpin.IsWritable(node_acquisition_mode):
        print 'Unable to set acquisition mode to continuous (enum retrieval). Aborting...'
        return False

    node_acquisition_mode_continuous = node_acquisition_mode.GetEntryByName('Continuous')
    if not PySpin.IsAvailable(node_acquisition_mode_continuous) or not PySpin.IsReadable(node_acquisition_mode_continuous):
        print 'Unable to set acquisition mode to continuous (entry retrieval). Aborting...'
        return False

    # Retrieve integer value from entry node
    acquisition_mode_continuous = node_acquisition_mode_continuous.GetValue()

    # Set integer value from entry node as new value of enumeration node
    node_acquisition_mode.SetIntValue(acquisition_mode_continuous)

    cam.BeginAcquisition()

    return cam
