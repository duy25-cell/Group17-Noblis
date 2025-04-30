import pyautogui
import time

# Wait for the GNS3 interface to load

# Click on "End devices"
print("Attempting to click on 'End devices'...")
end_devices_icon = pyautogui.locateOnScreen('end_devices_icon.png', confidence=0.7)
if end_devices_icon:
    pyautogui.click(end_devices_icon)
    print("'End devices' clicked.")
else:
    print("Could not find 'End devices'. Ensure the screenshot 'end_devices_icon.png' is accurate.")
    exit()

# Locate the "Cloud icon"
print("Attempting to locate the 'Cloud icon'...")
cloud_icon = pyautogui.locateOnScreen('cloud_icon.png', confidence=0.4)
if cloud_icon:
    # Drag the "Cloud icon" to the specified coordinates
    print("Dragging 'Cloud icon' to the environment...")
    pyautogui.moveTo(cloud_icon)
    pyautogui.dragTo(1469, 519, duration=1)  # Drag to X:1469, Y:519
    print("'Cloud icon' dragged to the environment.")
else:
    print("Could not find 'Cloud icon'. Ensure the screenshot 'cloud_icon.png' is accurate.")
    exit()

# Click "OK"
print("Attempting to click 'OK'...")
ok_button = pyautogui.locateOnScreen('ok_button.png', confidence=0.8)
if ok_button:
    pyautogui.click(ok_button)
    print("'OK' button clicked.")
else:
    print("Could not find 'OK' button. Ensure the screenshot 'ok_button.png' is accurate.")
    exit()

# Go to "All devices"
print("Attempting to click on 'All devices'...")
all_devices_icon = pyautogui.locateOnScreen('all_devices_icon.png', confidence=0.8)
if all_devices_icon:
    pyautogui.click(all_devices_icon)
    print("'All devices' clicked.")
else:
    print("Could not find 'All devices'. Ensure the screenshot 'all_devices_icon.png' is accurate.")
    exit()

# Drag devices to specified coordinates
devices = [
    ('router_icon.png', 1506, 586),  # Router 1
    ('router_icon.png', 1429, 606),  # Router 2
    ('router_icon.png', 1575, 607),  # Router 3
    ('switch_icon.png', 1378, 646),  # Switch 1
    ('switch_icon.png', 1633, 659),  # Switch 2
    ('linux_vm_1_icon.png', 1387, 702),  # Linux-VM-1
    ('linux_vm_2_icon.png', 1632, 698),  # Linux-VM-2
]

for device, x, y in devices:
    print(f"Attempting to locate and drag '{device}' to X:{x}, Y:{y}...")
    device_icon = pyautogui.locateOnScreen(device, confidence=0.8)
    if device_icon:
        pyautogui.moveTo(device_icon)
        pyautogui.dragTo(x, y, duration=1)
        print(f"'{device}' dragged to X:{x}, Y:{y}.")
    else:
        print(f"Could not find '{device}'. Ensure the screenshot '{device}' is accurate.")
        exit()