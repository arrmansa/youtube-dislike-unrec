import cv2
import pyautogui
import keyboard
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
        if not keyboard.is_pressed('alt+x'):
            keyboard.wait()
            continue
    
        print("Trigger")
        
        # Step 1: Look for element 1 and click
        if(click_element_failed('Subscribe.png', False)):
            print("SFAIL")
            continue
            
        print("SPASS")
        
        # Step 2: Look for element 1 and click
        while click_element_failed('dislike.png'):
            print("DFAIL")
            time.sleep(0.1)
            
        print("Disliked")
            
        # Step 3: Look for element 2 and click
        assert click_element_failed('options.png') == False

        print("Options")
        
        # Step 4: Poll for element 3 and click when found
        while click_element_failed('block.png'):
            time.sleep(0.1)

            
        print("Blocked")
            
if __name__ == "__main__":
    main()