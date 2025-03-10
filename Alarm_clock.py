import time
import winsound

def set_alarm():
    current_time = time.strftime("%H:%M")
    print(current_time)
    alarm_time = input("Enter alarm time (HH:MM): ")

    while True:
        current_time = time.strftime("%H:%M")
        # print(current_time)
        if current_time == alarm_time:
            print("⏰ Time to wake up! ⏰")
            for _ in range(5):  # Rings 5 times
                winsound.Beep(2500, 1000)
                time.sleep(1)
            alarm_menu()
            break
        time.sleep(30)  # Check every 30 seconds

def snooze_alarm():
    print("🛏 Snoozing for 5 minutes...")
    time.sleep(5*60)  # Wait 5 minutes
    print("⏰ Snooze over! Wake up!")
    for _ in range(5):
        winsound.Beep(2500, 1000)
        time.sleep(1)

def stop_alarm():
    print("🚫 Alarm stopped.")

def alarm_menu():
    while True:
        print("\n1️⃣ Snooze (5 min)  \n2️⃣ Stop Alarm")
        choice = input("Enter your choice: ")

        if choice == '1':
            snooze_alarm()
        elif choice == '2':
            stop_alarm()
            break
        else:
            print("❌ Invalid choice! Try again.")

while True:
    print("\n1️⃣ Set Alarm  \n2️⃣ Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        set_alarm()
    elif choice == '2':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice! Try again.")
