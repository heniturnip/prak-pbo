class Robot:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
    
    def attack(self):
        return self.dmg
    
    def heal(self):
        self.hp += 4000
    
    def decrease_hp(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
    
    def choose_hand(self):
        return random.randint(1, 3)
    
    def __str__(self):
        return f"{self.name} ({self.hp} HP)"

    def perform_action(self, robot1, robot2, turn):
        hand1=int(input("Pilih tangan robotmu: "))
        hand2=int(input("Pilih tangan robot lawan: "))
        
        if hand1 == 1 and hand2 == 2:
            dmg = robot1.attack()
            robot2.decrease_hp(dmg)
            print(f"Robotmu ({robot1.name}) menyerang sebanyak {dmg} DMG")
            
        elif hand1 == 1 and hand2 == 3:
            dmg = robot2.attack()
            robot1.decrease_hp(dmg)
            print(f"Robot lawan ({robot2.name}) menyerang sebanyak {dmg} DMG")
            
        elif hand1 == 2 and hand2 == 1:
            dmg = robot2.attack()
            robot1.decrease_hp(dmg)
            print(f"Robot lawan ({robot2.name}) menyerang sebanyak {dmg} DMG")
            
        elif hand1 == 2 and hand2 == 3:
            dmg = robot1.attack()
            robot2.decrease_hp(dmg)
            print(f"Robotmu ({robot1.name}) menyerang sebanyak {dmg} DMG")
            
        elif hand1 == 3 and hand2 == 1:
            dmg = robot1.attack()
            robot2.decrease_hp(dmg)
            print(f"Robotmu ({robot1.name}) menyerang sebanyak {dmg} DMG")
            
        elif hand1 == 3 and hand2 == 2:
            dmg = robot2.attack()
            robot1.decrease_hp(dmg)
            print(f"Robot lawan ({robot2.name}) menyerang sebanyak {dmg} DMG")
            
        else:
            print("Kedua robot memilih tangan yang sama.")

print("Selamat datang di pertandingan robot Yamako")
print("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus)")
while True:
    robot_choice = int(input("Pilih robot yang akan kamu gunakan: "))
    if robot_choice == 1:
        robot1 = Robot("Antares", 50000, 5000)
    elif robot_choice == 2:
        robot1 = Robot("Alphasetia", 40000, 6000)
    elif robot_choice == 3:
        robot1 = Robot("Lecalicus", 45000, 5500)
    else:
        print("Input salah. Silakan pilih lagi.")
        continue
    break

while True:
    robot_choice = int(input("Pilih robot yang akan kamu gunakan: "))
    if robot_choice == 1:
        robot2 = Robot("Antares", 50000, 5000)
    elif robot_choice == 2:
        robot2 = Robot("Alphasetia", 40000, 6000)
    elif robot_choice == 3:
        robot2 = Robot("Lecalicus", 45000, 5500)
    else:
        print("Inputan salah. Silakan pilih lagi.")
        continue
    break

print("Robotmu: ", robot1)
print("Robot lawan: ", robot2)

turn = 1

print("Selanjutnya, pilih 1 untuk batu, 2 untuk gunting, 3 untuk kertas")

while True:
    print(f"----- Turn {turn} -----")
    
    if robot1.hp >0 and robot2.hp >0:
        robot1.perform_action(robot1, robot2, turn)

    elif robot1.hp <= 0:
        print(f"Maaf, {robot1.name} kalah dalam pertandingan ini.")
        break
    elif robot2.hp <= 0:
        print(f"Selamat, {robot1.name} menang dalam pertandingan ini!")
        break
    elif robot1.hp == robot2.hp:
        print("Pertandingan berakhir seri.")
        print(f"Robotmu ({robot1.name})dan robot lawan ({robot2.name}) sama-sama memiliki HP 0")
        break
    
    turn += 1
    
    

    




