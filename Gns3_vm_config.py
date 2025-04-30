import time
import pyautogui

# Navigate to "Edit" in GNS3
print("Attempting to click on 'Edit' in GNS3...")
edit_menu = pyautogui.locateOnScreen('edit_menu_1.png', confidence=0.8)
if edit_menu:
    pyautogui.click(edit_menu)
    print("'Edit' menu clicked.")
else:
    print("Could not find 'Edit' menu. Ensure the screenshot 'edit_menu.png' is accurate.")
    exit()

# Click on "Preferences"
print("Attempting to click on 'Preferences'...")
preferences_option = pyautogui.locateOnScreen('preferences_option.png', confidence=0.8)
if preferences_option:
    pyautogui.click(preferences_option)
    print("'Preferences' clicked.")
else:
    print("Could not find 'Preferences'. Ensure the screenshot 'preferences_option.png' is accurate.")
    exit()

# Wait for the Preferences window to load
time.sleep(2)

# Navigate to "VMware VMs"
print("Attempting to click on 'VMware VMs'...")
vmware_vms_option = pyautogui.locateOnScreen('vmware_vms_option.png', confidence=0.8)
if vmware_vms_option:
    pyautogui.click(vmware_vms_option)
    print("'VMware VMs' clicked.")
else:
    print("Could not find 'VMware VMs'. Ensure the screenshot 'vmware_vms_option.png' is accurate.")
    exit()

# Select "Linux-VM-1"
print("Attempting to select 'Linux-VM-1'...")
linux_vm_1_option = pyautogui.locateOnScreen('linux_vm_1_option.png', confidence=0.8)
if linux_vm_1_option:
    pyautogui.click(linux_vm_1_option)
    print("'Linux-VM-1' selected.")
else:
    print("Could not find 'Linux-VM-1'. Ensure the screenshot 'linux_vm_1_option.png' is accurate.")
    exit()
time.sleep(2)
# Click on "Edit"
print("Attempting to click on 'Edit' for 'Linux-VM-1'...")
edit_button = pyautogui.locateOnScreen('edit_button.png', confidence=0.7)
if edit_button:
    pyautogui.click(edit_button)
    print("'Edit' button clicked.")
else:
    print("Could not find 'Edit' button. Ensure the screenshot 'edit_button.png' is accurate.")
    exit()

# Wait for the Network settings to load
time.sleep(2)

# Click on "Network"
print("Attempting to click on 'Network'...")
network_tab = pyautogui.locateOnScreen('network_tab.png', confidence=0.8)
if network_tab:
    pyautogui.click(network_tab)
    print("'Network' tab clicked.")
else:
    print("Could not find 'Network' tab. Ensure the screenshot 'network_tab.png' is accurate.")
    exit()

# Click on "Allow GNS3 to override non-custom VMware adapter"
print("Attempting to click on 'Allow GNS3 to override non-custom VMware adapter'...")
override_adapter_option = pyautogui.locateOnScreen('override_adapter_option.png', confidence=0.9)
if override_adapter_option:
    pyautogui.click(override_adapter_option)
    print("'Allow GNS3 to override non-custom VMware adapter' clicked.")
else:
    print("Could not find 'Allow GNS3 to override non-custom VMware adapter'. Ensure the screenshot 'override_adapter_option.png' is accurate.")
    exit()

    # Click "OK" for "Linux-VM-1"
print("Attempting to click 'OK' for 'Linux-VM-1'...")
ok_button = pyautogui.locateOnScreen('ok_button.png', confidence=0.8)
if ok_button:
    pyautogui.click(ok_button)
    print("'OK' button clicked for 'Linux-VM-1'.")
else:
    print("Could not find 'OK' button. Ensure the screenshot 'ok_button.png' is accurate.")
    exit()
time.sleep(2)
# Select "Linux-VM-2"
print("Attempting to select 'Linux-VM-2'...")
linux_vm_2_option = pyautogui.locateOnScreen('linux_vm_2_option.png', confidence=0.96)
if linux_vm_2_option:
    pyautogui.click(linux_vm_2_option)
    print("'Linux-VM-2' selected.")
else:
    print("Could not find 'Linux-VM-2'. Ensure the screenshot 'linux_vm_2_option.png' is accurate.")
    exit()

# Click on "Edit" for "Linux-VM-2"
print("Attempting to click on 'Edit' for 'Linux-VM-2'...")
edit_button = pyautogui.locateOnScreen('edit_button.png', confidence=0.7)
if edit_button:
    pyautogui.click(edit_button)
    print("'Edit' button clicked for 'Linux-VM-2'.")
else:
    print("Could not find 'Edit' button. Ensure the screenshot 'edit_button.png' is accurate.")
    exit()

# Wait for the Network settings to load
time.sleep(2)

# Click on "Network" for "Linux-VM-2"
print("Attempting to click on 'Network' for 'Linux-VM-2'...")
network_tab = pyautogui.locateOnScreen('network_tab.png', confidence=0.8)
if network_tab:
    pyautogui.click(network_tab)
    print("'Network' tab clicked for 'Linux-VM-2'.")
else:
    print("Could not find 'Network' tab. Ensure the screenshot 'network_tab.png' is accurate.")
    exit()

# Click on "Allow GNS3 to override non-custom VMware adapter" for "Linux-VM-2"
print("Attempting to click on 'Allow GNS3 to override non-custom VMware adapter' for 'Linux-VM-2'...")
override_adapter_option = pyautogui.locateOnScreen('override_adapter_option.png', confidence=0.4)
if override_adapter_option:
    pyautogui.click(override_adapter_option)
    print("'Allow GNS3 to override non-custom VMware adapter' clicked for 'Linux-VM-2'.")
else:
    print("Could not find 'Allow GNS3 to override non-custom VMware adapter'. Ensure the screenshot 'override_adapter_option.png' is accurate.")
    exit()

# Click "OK" for "Linux-VM-2"
print("Attempting to click 'OK' for 'Linux-VM-2'...")
ok_button = pyautogui.locateOnScreen('ok_button.png', confidence=0.8)
if ok_button:
    pyautogui.click(ok_button)
    print("'OK' button clicked for 'Linux-VM-2'.")
else:
    print("Could not find 'OK' button. Ensure the screenshot 'ok_button.png' is accurate.")
    exit()