import time
import pyautogui
import argparse

def auto_click(interval, end_time):
    start_time = time.time()
    i = 0

    print(f"Auto Clicker Started In ({start_time})")
    print(f"==> Interval Time ({interval})")
    print(f"==> End Time ({end_time})")
    print(f"==> Type ({methodType})")
    print("=====================================")

    while time.time() - start_time < end_time:
        i += 1

        if (methodType == 'click'):
            pyautogui.move(10, 0)  # Move cursor 10 pixels to the right
            pyautogui.move(-10, 0)  # Move cursor back 10 pixels to the left
            pyautogui.click(button='left')
            time.sleep(interval)
            print(f"Auto Click ({i})")
        elif (methodType == 'drag'):
            x, y = pyautogui.position()  # Get current mouse cursor position
            pyautogui.moveTo(x, y)  # Move the cursor to the current position (optional)
            pyautogui.drag(10, 0, duration=0.5, button='left')  # Drag the window 10 pixels to the right
            pyautogui.drag(-10, 0, duration=0.5, button='left')  # Drag the window back 10 pixels to the left
            time.sleep(interval)
            print(f"Auto Click ({i})")
        else:
            print(f"Auto Clicker {i} | without action type")

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--time', type=float, help='Duration in seconds')
    parser.add_argument('--endtime', type=int, help='Duration in seconds')
    parser.add_argument('--type', type=str, help='click | drag')
    args = parser.parse_args()

    interval = args.time if args.time else 10  # Default interval in seconds
    end_time = args.endtime if args.endtime else 7200  # 2 hour in seconds
    methodType = args.type if args.type else 'drag'

    try:
        auto_click(interval, end_time)
    except KeyboardInterrupt:
        print("Auto clicker stopped.")