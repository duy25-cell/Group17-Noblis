import os
import time
import pyautogui

# Path to the GNS3 application
gns3_path = r"C:\Program Files\GNS3\gns3.exe"

# Open the GNS3 application
if os.path.exists(gns3_path):
    os.startfile(gns3_path)
    print("Opening GNS3...")
    # Wait for 30 seconds to allow GNS3 to load
    time.sleep(30)
    
    # Locate and click the GNS3 tab to bring it to focus
    print("Attempting to click on the GNS3 tab...")
    gns3_tab = pyautogui.locateOnScreen('gns3tab.png', confidence=0.8)
    if gns3_tab:
        pyautogui.click(gns3_tab)
        print("GNS3 tab clicked.")
    else:
        print("Could not find the GNS3 tab. Ensure the screenshot 'gns3tab.png' is accurate.")
        exit()

    # Locate and click the "Recent Projects" button
    print("Attempting to click 'Recent Projects'...")
    recent_projects_button = pyautogui.locateOnScreen('recent_projects_button.png', confidence=0.8)
    if recent_projects_button:
        pyautogui.click(recent_projects_button)
        print("'Recent Projects' button clicked.")
        
        time.sleep(2)
        
        # Locate and click the project "1. Group17BareMetal.gns3"
        print("Attempting to locate and click on '1. Group17BareMetal.gns3'...")
        project_button = pyautogui.locateOnScreen('1_Group17BareMetal_gns3.png', confidence=0.8)
        if project_button:
            pyautogui.click(project_button)
            print("'1. Group17BareMetal.gns3' project opened.")
        else:
            print("Could not find '1. Group17BareMetal.gns3' button. Ensure the screenshot is accurate.")
    else:
        print("Could not find 'Recent Projects' button. Ensure the screenshot is accurate.")
else:
    print("GNS3 application not found at the specified path.")