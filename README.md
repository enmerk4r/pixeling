## Pixeling
Pixeling is an experiment in pixel streaming that connects Rhino / Grasshopper to the Unreal Engine. This project has been developed by a team of collaborators for the 2021 AEC Tech Hackathon hosted by CORE Studio at Thornton Tomasetti.

### Team Members
* Edwin Bailey 
* Alfredo Chavez
* Jeanne Li
* Eesha Khanna
* Brad Lei
* Daniel Escobar
* Amit Nambiar
* Sergey Pigach
* Jeroen Janssen

### Rhino Bridge
![](https://github.com/enmerk4r/pixeling/blob/main/Misc/Demo_1.gif)

### Unity Blueprint
![](https://github.com/enmerk4r/pixeling/blob/main/Misc/image%20(23).png)

### Grasshopper Converter
![](https://github.com/enmerk4r/pixeling/blob/main/Misc/image%20(24).png)

### Remote Pixel Streaming
The Unreal Project is deployed on a remote instance of AWS, enabling Pixel Streaming through the browser for multiple participants to call into the model vis.
---gif

There's a few steps to go through to set this up:
# Prerequisites:
1. Create an [AWS account](https://aws.amazon.com/) with proper permissions and quota to launch the correct instances, etc., etc.
We noticed it works best with at least a g4dn.xlarge, but if you need more performance you might want to beef it up to a g4dn.8xlarge type. Make sure the EBS volume is large enough. Unreal Engine is big... We used a 150 Gb General Purpose SSD volume which works well.
2. Launch the machine with Windows Server 2019
3. Make sure on the security rules for the instance to open port 80 (we have 9999 open as well) for incoming traffic
4. Set up an Elastic IP address and take note of the 'Public IPv4 address'.
5. The NVIDIA gaming drivers are not installed by default... Follow these steps otherwise Unreal Engine won't run: https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/install-nvidia-driver.html#nvidia-gaming-driver
6. Install [Unreal Engine](https://www.unrealengine.com/en-US/) (at least v4.27.1)
7. Install [Node.js](https://nodejs.org/en/) including the additional required packages - which will install a bunch of different stuff such as Python and [Chocolatey](https://chocolatey.org/)

# We are very greatful for these helpful resources:
7. https://github.com/aws-samples/deploying-unreal-engine-pixel-streaming-server-on-ec2
8. https://docs.unrealengine.com/4.26/en-US/SharingAndReleasing/PixelStreaming/PixelStreamingIntro/ 
9. Make sure you go through these steps carefully. For *section 2 - Start the Servers* for us that SignallingWebserver was actually saved under: 'C:\Program Files\Epic Games\UE_4.27\Samples\PixelStreaming\WebServers\SignallingWebServer\platform_scripts\cmd' and instead of running the 'run.bat' file, on the AWS instance you want to run the 'runAWS_WithTURN.bat' file.
10. This will spin up the Signalling Server and you'll see the following in the console window:
> WebSocket listening to Streamer connections on :8888
> WebSocket listening to Players connections on :80
> Http listening on : 80
11. And you're good to go! how you can start the Packaged Unreal Engine application with your project loaded (the amended shortcut to the .exe file - in step 8)

12. On the AWS instance you can now browse to http://127.0.0.1 to see the model in your local browser (on the remote instance that is).
13. And the rest of the world can now access the Elastic IP address you set up in step 4! **Hooray!**
