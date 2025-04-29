import mouse
import cv2
import pyautogui
import time

def click_element_failed(image_path, click = True):
    # Locate the element on screen using the preloaded image
    try:
        location = pyautogui.locateCenterOnScreen(image_path, grayscale=True, confidence=0.85)
        if location:
            if click:
                pyautogui.click(location)  # Click the center of the located element
                print("CLICK AND RETURN FALSE")
            return False
        return True
    except pyautogui.ImageNotFoundException:
        return True

def main():
    while True:
        mouse.wait(button='left', target_types=('down'))
        time.sleep(0.4)
        
        original_position = pyautogui.position()
        
        # Step 1: Look for element 1 and click
        if(click_element_failed('not_interested_sidebar.png')):
            print("SFAIL")
            continue
        else:
            print("CLICKED NOT INTERESTED")
            pyautogui.moveTo(original_position)
            pyautogui.move(-200, 110)
            time.sleep(0.1)
            pyautogui.click()
                
        start_time = time.time()
        while time.time() < start_time + 4:
            time.sleep(0.03)
            if not click_element_failed('dont_like_video_centered.png'):
                break
        else:
            print("CLICK DON'T LIKE FAILED")
            continue
        
        time.sleep(0.1)
        
        if(click_element_failed('submitv2_perms.png')):
            print("CLICK SUMBIT FAILED")
            continue
            
        pyautogui.moveTo(original_position)
        print("CLICKED SUMBIT")
        pyautogui.scroll(-75)

if __name__ == "__main__":
    main()
