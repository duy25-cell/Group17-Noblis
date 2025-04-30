import os
import time
import pyautogui

# Path to the GNS3 application
gns3_path = r"C:\Program Files\GNS3\gns3.exe"

#Open the GNS3 application
# if os.path.exists(gns3_path):
#     os.startfile(gns3_path)
#     print("Opening GNS3...")
#     # Wait for 30 seconds to allow GNS3 to load
#     time.sleep(3)
    
    # Locate and click the "File" menu
# print("Attempting to click on 'File' menu...")
# file_menu = pyautogui.locateOnScreen('file_menu.png', confidence=0.7)
# if file_menu:
#     pyautogui.click(file_menu)
#     print("'File' menu clicked.")
# else:
#     print("Could not find 'File' menu. Ensure the screenshot 'file_menu.png' is accurate.")
#     exit()

# # Locate and click "New blank project"
# print("Attempting to click on 'New blank project'...")
# new_project = pyautogui.locateOnScreen('new_blank_project.png', confidence=0.4)
# if new_project:
#     pyautogui.click(new_project)
#     print("'New blank project' clicked.")
# else:
#     print("Could not find 'New blank project'. Ensure the screenshot 'new_blank_project.png' is accurate.")
#     exit()

# # Locate and click "OK" to confirm
# print("Attempting to click 'OK'...")
# ok_button = pyautogui.locateOnScreen('ok_button.png', confidence=0.8)
# if ok_button:
#     pyautogui.click(ok_button)
#     print("'OK' button clicked. New blank project created.")
# else:
#     print("Could not find 'OK' button. Ensure the screenshot 'ok_button.png' is accurate.")
#     exit()

#Locate and click the "Edit" menu

print("Attempting to click on 'Edit' menu...")
edit_menu = pyautogui.locateOnScreen('edit_menu.png', confidence=0.8)
if edit_menu:
    pyautogui.click(edit_menu)
    print("'Edit' menu clicked.")
else:
    print("Could not find 'Edit' menu. Ensure the screenshot 'edit_menu.png' is accurate.")
    exit()
time.sleep(2)
# Locate and click "Preferences"
print("Attempting to click on 'Preferences'...")
preferences = pyautogui.locateOnScreen('preferences.png', confidence=0.8)
if preferences:
    pyautogui.click(preferences)
    print("'Preferences' clicked.")
else:
    print("Could not find 'Preferences'. Ensure the screenshot 'preferences.png' is accurate.")
    exit()
time.sleep(3)
# Locate and click "Server" tab
print("Attempting to click on 'Server' tab...")
server_tab = pyautogui.locateOnScreen("server_tab.png", confidence=0.8)
if server_tab:
    pyautogui.click(server_tab)
    print("'Server' tab clicked.")
else:
    print("Could not find 'Server' tab. Ensure the screenshot 'server_tab.png' is accurate.")
    exit()

# Ensure "Enable local server" checkbox is checked
print("Checking 'Enable local server' checkbox...")
enable_local_server = pyautogui.locateOnScreen('enable_local_server_checked.png', confidence=0.8)
if not enable_local_server:
    enable_local_server_unchecked = pyautogui.locateOnScreen('enable_local_server_unchecked.png', confidence=0.8)
    if enable_local_server_unchecked:
        pyautogui.click(enable_local_server_unchecked)
        print("'Enable local server' checkbox checked.")
    else:
        print("Could not find 'Enable local server' checkbox. Ensure the screenshots are accurate.")
        exit()

# Check if "Host Binding" says "localhost"
print("Checking 'Host Binding' value...")
host_binding = pyautogui.locateOnScreen('host_binding_localhost.png', confidence=0.8)
if not host_binding:
    host_binding_dropdown = pyautogui.locateOnScreen('host_binding_dropdown.png', confidence=0.8)
    if host_binding_dropdown:
        pyautogui.click(host_binding_dropdown)
        time.sleep(1)
        localhost_option = pyautogui.locateOnScreen('localhost_option.png', confidence=0.8)
        if localhost_option:
            pyautogui.click(localhost_option)
            print("'Host Binding' set to 'localhost'.")
        else:
            print("Could not find 'localhost' option in dropdown. Ensure the screenshot is accurate.")
            exit()
    else:
        print("Could not find 'Host Binding' dropdown. Ensure the screenshot is accurate.")
        exit()
else:
    print("'Host Binding' is already set to 'localhost'.")

# ...existing code...

# Locate and click "GNS3 VM"
print("Attempting to click on 'GNS3 VM'...")
gns3_vm_tab = pyautogui.locateOnScreen('gns3_vm_tab.png', confidence=0.8)
if gns3_vm_tab:
    pyautogui.click(gns3_vm_tab)
    print("'GNS3 VM' tab clicked.")
else:
    print("Could not find 'GNS3 VM' tab. Ensure the screenshot 'gns3_vm_tab.png' is accurate.")
    exit()

# Ensure "Enable the GNS3 VM" checkbox is checked
print("Checking 'Enable the GNS3 VM' checkbox...")
enable_gns3_vm = pyautogui.locateOnScreen('enable_gns3_vm_checked.png', confidence=0.8)
if not enable_gns3_vm:
    enable_gns3_vm_unchecked = pyautogui.locateOnScreen('enable_gns3_vm_unchecked.png', confidence=0.8)
    if enable_gns3_vm_unchecked:
        pyautogui.click(enable_gns3_vm_unchecked)
        print("'Enable the GNS3 VM' checkbox checked.")
    else:
        print("Could not find 'Enable the GNS3 VM' checkbox. Ensure the screenshots are accurate.")
        exit()

# Locate and click "VMware"
print("Attempting to click on 'VMware'...")
vmware_tab = pyautogui.locateOnScreen('vmware_tab.png', confidence=0.8)
if vmware_tab:
    pyautogui.click(vmware_tab)
    print("'VMware' tab clicked.")
else:
    print("Could not find 'VMware' tab. Ensure the screenshot 'vmware_tab.png' is accurate.")
    exit()

# Locate and click "Advanced local settings"
print("Attempting to click on 'Advanced local settings'...")
advanced_settings = pyautogui.locateOnScreen('advanced_local_settings.png', confidence=0.8)
if advanced_settings:
    pyautogui.click(advanced_settings)
    print("'Advanced local settings' clicked.")
else:
    print("Could not find 'Advanced local settings'. Ensure the screenshot 'advanced_local_settings.png' is accurate.")
    exit()

# Locate and click "Configure" button
print("Attempting to click on 'Configure' button...")
configure_button = pyautogui.locateOnScreen('configure_button.png', confidence=0.8)
if configure_button:
    pyautogui.click(configure_button)
    print("'Configure' button clicked.")
else:
    print("Could not find 'Configure' button. Ensure the screenshot 'configure_button.png' is accurate.")
    exit()
time.sleep(30)
# Locate and click "Apply" button
print("Attempting to click on 'Apply' button...")
apply_button = pyautogui.locateOnScreen('apply_button.png', confidence=0.8)
if apply_button:
    pyautogui.click(apply_button)
    print("'Apply' button clicked.")
else:
    print("Could not find 'Apply' button. Ensure the screenshot 'apply_button.png' is accurate.")
    exit()


#else:
#print("GNS3 application not found at the specified path.")

