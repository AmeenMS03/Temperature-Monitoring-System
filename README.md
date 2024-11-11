# Factory Temperature Monitoring System

## Project Overview
This project is an embedded system for monitoring and managing temperature conditions in a factory setting. Designed as part of a computer engineering course, the system leverages both software (Python with GPIO and GUI libraries) and hardware components (temperature sensor, LEDs, servo motor, push buttons, and a buzzer) to transition between states based on real-time temperature readings and user inputs.

### Key Components
- **Temperature Sensor**: Simulated for monitoring ambient temperature.
- **LED Indicators**:
  - **On LED**: Signals when the system is actively monitoring the temperature.
  - **Emergency LED**: Lights up during emergency conditions.
- **Servo Motor**: Controls ventilation window angle based on temperature levels.
- **Push Buttons**:
  - **Start Button**: Initiates the temperature monitoring process.
  - **Reset Button**: Resets the system from the emergency state to idle.
- **Buzzer**: Sounds during emergency conditions to alert personnel.

### System Operation
- **Idle State**: Initial state where LEDs and buzzer are off, and servo is positioned at 0°. The system remains idle until the Start button is pressed or after a 10-second wait.
- **Monitor Temperature State**: Activated by pressing the Start button, turning on the On LED to signify temperature monitoring.
- **High Temperature State**: Triggered if temperature is between 30°C and 40°C, partially opening the ventilation by setting the servo to 90°.
- **Emergency State**: For temperatures above 40°C, the system activates the Emergency LED, sounds the buzzer, and fully opens the ventilation by setting the servo to 180°. The system stays in this state until the Reset button is pressed.

### State Diagram
[Link to the Diagram](https://github.com/AmeenMS03/Temperature-Monitoring-System/blob/main/FSM%20State%20Diagram.png)

## Code
The code is written in Python and uses the following libraries:
- **gpiozero**: Controls GPIO components such as LEDs, servo motor, push buttons, and buzzer.
- **guizero**: Manages the GUI for temperature monitoring, including slider control.
- **tkgpio**: Simulates the circuit for testing without actual hardware.

The system smoothly transitions between states based on real-time inputs and temperature thresholds, making it a versatile and educational example of combining hardware and software for environmental control.

## Installation
1. Clone the repository:
```bash
   git clone https://github.com/YourGitHubUsername/Factory-Temperature-Monitoring-System.git
```
2. Install the required Python libraries:
  ```bash
  pip install gpiozero guizero tkgpio
  ```
3. Run the main code:
  ```bash
  python main.py
  ```
