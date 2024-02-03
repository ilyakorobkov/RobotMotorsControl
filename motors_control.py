class MotorControl:
    def __init__(self):
        # Инициализация параметров двигателя
        pass

    def forward(self, speed):
        # Код для движения вперед с заданной скоростью
        print(f"Moving forward with speed {speed}")

    def backward(self, speed):
        # Код для движения назад с заданной скоростью
        print(f"Moving backward with speed {speed}")

    def stop(self):
        # Код для остановки двигателя
        print("Stopping motors")

if __name__ == "__main__":
    motor_control = MotorControl()
    motor_control.forward(10)
    motor_control.backward(5)
    motor_control.stop()
