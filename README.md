# fullscreencamera_mqtt
This python script will subscribe to an mqtt topic and on receipt of an "ON" message open a camera feed in a chromium browser in kiosk mode.  On receiving an "OFF" message it will close the feed and return to your preset url.

I use it to switch to fullscreen camera when motion is detected and then return to my home automation dashboard when motion stops.
