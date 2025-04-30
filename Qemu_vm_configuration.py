import pyautogui
import time

# Navigate to "Edit" in GNS3
print("Attempting to click on 'Edit' in GNS3...")
edit_menu = pyautogui.locateOnScreen('edit_menu_2.png', confidence=0.8)
if edit_menu:
    pyautogui.click(edit_menu)
    print("'Edit' menu clicked.")
else:
    print("Could not find 'Edit' menu. Ensure the screenshot 'edit_menu.png' is accurate.")
    exit()
time.sleep(2)
# Click on "Preferences"
print("Attempting to click on 'Preferences'...")
preferences_option = pyautogui.locateOnScreen('preferences_option1.png', confidence=0.8)
if preferences_option:
    pyautogui.click(preferences_option)
    print("'Preferences' clicked.")
else:
    print("Could not find 'Preferences'. Ensure the screenshot 'preferences_option1.png' is accurate.")
    exit()

# Wait for the Preferences window to load
time.sleep(2)

# Navigate to "Qemu VMs"
print("Attempting to click on 'Qemu VMs'...")
qemu_vms_option = pyautogui.locateOnScreen('qemu_vms_option.png', confidence=0.8)
if qemu_vms_option:
    pyautogui.click(qemu_vms_option)
    print("'Qemu VMs' clicked.")
else:
    print("Could not find 'Qemu VMs'. Ensure the screenshot 'qemu_vms_option.png' is accurate.")
    exit()

# Click on "Router"
print("Attempting to click on 'Router'...")
router_option = pyautogui.locateOnScreen('router_option.png', confidence=0.8)
if router_option:
    pyautogui.click(router_option)
    print("'Router' clicked.")
else:
    print("Could not find 'Router'. Ensure the screenshot 'router_option.png' is accurate.")
    exit()

# Click on "New"
print("Attempting to click on 'New'...")
new_button = pyautogui.locateOnScreen('new_button.png', confidence=0.8)
if new_button:
    pyautogui.click(new_button)
    print("'New' button clicked.")
else:
    print("Could not find 'New' button. Ensure the screenshot 'new_button.png' is accurate.")
    exit()

# Click on "Run this Qemu VM on the GNS3 VM"
print("Attempting to click on 'Run this Qemu VM on the GNS3 VM'...")
run_on_gns3_vm_option = pyautogui.locateOnScreen('run_on_gns3_vm_option.png', confidence=0.8)
if run_on_gns3_vm_option:
    pyautogui.click(run_on_gns3_vm_option)
    print("'Run this Qemu VM on the GNS3 VM' clicked.")
else:
    print("Could not find 'Run this Qemu VM on the GNS3 VM'. Ensure the screenshot 'run_on_gns3_vm_option.png' is accurate.")
    exit()

# Click "Next"
print("Attempting to click 'Next'...")
next_button = pyautogui.locateOnScreen('next_button.png', confidence=0.8)
if next_button:
    pyautogui.click(next_button)
    print("'Next' button clicked.")
else:
    print("Could not find 'Next' button. Ensure the screenshot 'next_button.png' is accurate.")
    exit()

# Enter the name "router"
print("Attempting to enter the name 'router'...")
name_field = pyautogui.locateOnScreen('name_field.png', confidence=0.8)
if name_field:
    pyautogui.click(name_field)
    pyautogui.typewrite('router')
    print("Name 'router' entered.")
else:
    print("Could not find the name field. Ensure the screenshot 'name_field.png' is accurate.")
    exit()

# Click "Next"
pyautogui.click(next_button)
print("'Next' button clicked.")

# Increase RAM to 2048 MB
print("Attempting to increase RAM to 2048 MB...")
ram_field = pyautogui.locateOnScreen('ram_field.png', confidence=0.8)
if ram_field:
    pyautogui.click(ram_field)
    pyautogui.typewrite('2048')
    print("RAM set to 2048 MB.")
else:
    print("Could not find the RAM field. Ensure the screenshot 'ram_field.png' is accurate.")
    exit()

# Click "Next"
pyautogui.click(next_button)
print("'Next' button clicked.")

# Click "Next" again
pyautogui.click(next_button)
print("'Next' button clicked again.")

# Click "New Image"
print("Attempting to click on 'New Image'...")
new_image_button = pyautogui.locateOnScreen('new_image_button.png', confidence=0.8)
if new_image_button:
    pyautogui.click(new_image_button)
    print("'New Image' button clicked.")
else:
    print("Could not find 'New Image' button. Ensure the screenshot 'new_image_button.png' is accurate.")
    exit()

# Click "Browse"
print("Attempting to click on 'Browse'...")
browse_button = pyautogui.locateOnScreen('browse_button.png', confidence=0.8)
if browse_button:
    pyautogui.click(browse_button)
    print("'Browse' button clicked.")
else:
    print("Could not find 'Browse' button. Ensure the screenshot 'browse_button.png' is accurate.")
    exit()
time.sleep(2)
# Navigate to "Documents" and select "vios-adventerprisek9-m.vmdk"
print("Attempting to select 'vios-adventerprisek9-m.vmdk.png'...")
documents_folder = pyautogui.locateOnScreen('documents_folder.png', confidence=0.6)
if documents_folder:
    pyautogui.click(documents_folder)
    print("'Documents' folder opened.")
    # Click on the "File Name" field
    vmdk_file = pyautogui.locateOnScreen('vios-adventerprisek9-m.vmdk.png', confidence=0.8)
    if vmdk_file:
        pyautogui.click(vmdk_file)
        print("'vios-adventerprisek9-m.vmdk.png' clicked and selected.")
    else:
        print("Could not find 'vios-adventerprisek9-m.vmdk.png'. Ensure the screenshot is accurate.")
        exit()
else:
    print("Could not find 'Documents' folder. Ensure the screenshot is accurate.")
    exit()


# Click "Open"
print("Attempting to click 'Open'...")
open_button = pyautogui.locateOnScreen('open_button.png', confidence=0.5)
if open_button:
    pyautogui.click(open_button)
    print("'Open' button clicked.")
else:
    print("Could not find 'Open' button. Ensure the screenshot 'open_button.png' is accurate.")
    exit()
time.sleep(5)
# Click "Finish"
print("Attempting to click 'Finish'...")
finish_button = pyautogui.locateOnScreen('finish_button1.png', confidence=0.8)
if finish_button:
    pyautogui.click(finish_button)
    print("'Finish' button clicked.")
else:
    print("Could not find 'Finish' button. Ensure the screenshot 'finish_button.png' is accurate.")
    exit()

    # Navigate to "Switch" in Qemu VMs
print("Attempting to click on 'Switch'...")
switch_option = pyautogui.locateOnScreen('switch_option.png', confidence=0.8)
if switch_option:
    pyautogui.click(switch_option)
    print("'Switch' clicked.")
else:
    print("Could not find 'Switch'. Ensure the screenshot 'switch_option.png' is accurate.")
    exit()

# Click on "New"
print("Attempting to click on 'New'...")
new_button = pyautogui.locateOnScreen('new_button.png', confidence=0.8)
if new_button:
    pyautogui.click(new_button)
    print("'New' button clicked.")
else:
    print("Could not find 'New' button. Ensure the screenshot 'new_button.png' is accurate.")
    exit()

# Click on "Run this Qemu VM on the GNS3 VM"
print("Attempting to click on 'Run this Qemu VM on the GNS3 VM'...")
run_on_gns3_vm_option = pyautogui.locateOnScreen('run_on_gns3_vm_option.png', confidence=0.8)
if run_on_gns3_vm_option:
    pyautogui.click(run_on_gns3_vm_option)
    print("'Run this Qemu VM on the GNS3 VM' clicked.")
else:
    print("Could not find 'Run this Qemu VM on the GNS3 VM'. Ensure the screenshot 'run_on_gns3_vm_option.png' is accurate.")
    exit()

# Click "Next"
print("Attempting to click 'Next'...")
next_button = pyautogui.locateOnScreen('next_button.png', confidence=0.8)
if next_button:
    pyautogui.click(next_button)
    print("'Next' button clicked.")
else:
    print("Could not find 'Next' button. Ensure the screenshot 'next_button.png' is accurate.")
    exit()

# Enter the name "switch"
print("Attempting to enter the name 'switch'...")
name_field = pyautogui.locateOnScreen('name_field.png', confidence=0.8)
if name_field:
    pyautogui.click(name_field)
    pyautogui.typewrite('switch')
    print("Name 'switch' entered.")
else:
    print("Could not find the name field. Ensure the screenshot 'name_field.png' is accurate.")
    exit()

# Click "Next"
pyautogui.click(next_button)
print("'Next' button clicked.")

# Increase RAM to 2048 MB
print("Attempting to increase RAM to 2048 MB...")
ram_field = pyautogui.locateOnScreen('ram_field.png', confidence=0.8)
if ram_field:
    pyautogui.click(ram_field)
    pyautogui.typewrite('2048')
    print("RAM set to 2048 MB.")
else:
    print("Could not find the RAM field. Ensure the screenshot 'ram_field.png' is accurate.")
    exit()

# Click "Next"
pyautogui.click(next_button)
print("'Next' button clicked.")

# Click "Next" again
pyautogui.click(next_button)
print("'Next' button clicked again.")

# Click "New Image"
print("Attempting to click on 'New Image'...")
new_image_button = pyautogui.locateOnScreen('new_image_button.png', confidence=0.8)
if new_image_button:
    pyautogui.click(new_image_button)
    print("'New Image' button clicked.")
else:
    print("Could not find 'New Image' button. Ensure the screenshot 'new_image_button.png' is accurate.")
    exit()

# Click "Browse"
print("Attempting to click on 'Browse'...")
browse_button = pyautogui.locateOnScreen('browse_button.png', confidence=0.8)
if browse_button:
    pyautogui.click(browse_button)
    print("'Browse' button clicked.")
else:
    print("Could not find 'Browse' button. Ensure the screenshot 'browse_button.png' is accurate.")
    exit()
time.sleep(3)
# Navigate to "Downloads" and select "vios_12-adventerprisek9-m.vmdk"
print("Attempting to select 'vios_12-adventerprisek9-m.vmdk'...")
documents_folder = pyautogui.locateOnScreen('documents_folder.png', confidence=0.8)
if documents_folder:
    pyautogui.click(documents_folder)
    vmdk_file = pyautogui.locateOnScreen('vios_12-adventerprisek9-m.vmdk.png', confidence=0.8)
    if vmdk_file:
        pyautogui.click(vmdk_file)
        print("'vios_12-adventerprisek9-m.vmdk' selected.")
    else:
        print("Could not find 'vios_12-adventerprisek9-m.vmdk'. Ensure the screenshot is accurate.")
        exit()
else:
    print("Could not find 'Documents' folder. Ensure the screenshot is accurate.")
    exit()

# Click "Open"
print("Attempting to click 'Open'...")
open_button = pyautogui.locateOnScreen('open_button.png', confidence=0.8)
if open_button:
    pyautogui.click(open_button)
    print("'Open' button clicked.")
else:
    print("Could not find 'Open' button. Ensure the screenshot 'open_button.png' is accurate.")
    exit()

# Click "Finish"
print("Attempting to click 'Finish'...")
finish_button = pyautogui.locateOnScreen('finish_button1.png', confidence=0.8)
if finish_button:
    pyautogui.click(finish_button)
    print("'Finish' button clicked.")
else:
    print("Could not find 'Finish' button. Ensure the screenshot 'finish_button1.png' is accurate.")
    exit()