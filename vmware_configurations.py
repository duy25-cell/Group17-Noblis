import time
import pyautogui
import pygetwindow as gw  # To manage application windows

# Ensure VMware is in focus
print("Ensuring VMware is in focus...")
vmware_window = None
for window in gw.getAllTitles():
    if "VMware" in window:  # Adjust the title to match your VMware window
        vmware_window = gw.getWindowsWithTitle(window)[0]
        vmware_window.activate()
        print(f"VMware window '{window}' activated.")
        break

if not vmware_window:
    print("Could not find VMware window. Ensure VMware is running.")
    exit()
# Wait for the interface to load
time.sleep(5)

# Right-click on "GNS3VMBareMetal"
print("Attempting to right-click on 'GNS3VMBareMetal'...")
gns3_vm_bare_metal = pyautogui.locateOnScreen('gns3_vm_bare_metal.png', confidence=0.8)
if gns3_vm_bare_metal:
    pyautogui.rightClick(gns3_vm_bare_metal)
    print("'GNS3VMBareMetal' right-clicked.")
else:
    print("Could not find 'GNS3VMBareMetal'. Ensure the screenshot 'gns3_vm_bare_metal.png' is accurate.")
    exit()

# Click on "Settings"
print("Attempting to click on 'Settings'...")
settings_option = pyautogui.locateOnScreen('settings_option.png', confidence=0.8)
if settings_option:
    pyautogui.click(settings_option)
    print("'Settings...' clicked.")
else:
    print("Could not find 'Settings'. Ensure the screenshot 'settings_option.png' is accurate.")
    exit()

# Wait for the "Hardware" tab to load
time.sleep(2)

# Click on "Add..." in the Hardware tab
print("Attempting to click on 'Add...' in the Hardware tab...")
add_button = pyautogui.locateOnScreen('add_button.png', confidence=0.8)
if add_button:
    pyautogui.click(add_button)
    print("'Add...' button clicked.")
else:
    print("Could not find 'Add...' button. Ensure the screenshot 'add_button.png' is accurate.")
    exit()
time.sleep(5)
# Click on "Network Adapter"
print("Attempting to click on 'Network Adapter'...")
network_adapter_option = pyautogui.locateOnScreen('network_adapter_option.png', confidence=0.95)
if network_adapter_option:
    pyautogui.click(network_adapter_option)
    print("'Network Adapter' clicked.")
else:
    print("Could not find 'Network Adapter'. Ensure the screenshot 'network_adapter_option.png' is accurate.")
    exit()

# Click on "Finish"
print("Attempting to click on 'Finish'...")
finish_button = pyautogui.locateOnScreen('finish_button.png', confidence=0.7)
if finish_button:
    pyautogui.click(finish_button)
    print("'Finish' button clicked.")
else:
    print("Could not find 'Finish' button. Ensure the screenshot 'finish_button.png' is accurate.")
    exit()
    
