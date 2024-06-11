import random

# Bước 1: Tạo thẻ Bingo ngẫu nhiên
def create_bingo_card():
    card = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    # Thêm số 0 vào vị trí (3, 3) để đại diện cho trung tâm không có số
    card['N'][2] = 0
    return card

# Bước 2: Kiểm tra thẻ thắng
def check_winning_card(card):
    # Kiểm tra dòng ngang
    for row in card.values():
        if all(num == 0 for num in row):
            return True
    
    # Kiểm tra dòng dọc
    for col in range(5):
        if all(card[key][col] == 0 for key in card):
            return True
    
    # Kiểm tra đường chéo
    if all(card[key][i] == 0 for i, key in enumerate(card)) or \
       all(card[key][4-i] == 0 for i, key in enumerate(card)):
        return True
    
    return False

# Bước 3: Chơi Bingo
def play_bingo():
    # Tạo thẻ Bingo
    bingo_card = create_bingo_card()
    print("Thẻ Bingo:")
    display_bingo_card(bingo_card)
    
    # Danh sách các số đã gọi
    called_numbers = random.sample(range(1, 76), 75)
    
    # Mô phỏng trò chơi
    called_count = 0
    while not check_winning_card(bingo_card):
        called_number = called_numbers.pop(0)
        called_count += 1
        
        # Đánh dấu số đã gọi trên thẻ
        for key in bingo_card:
            if called_number in bingo_card[key]:
                idx = bingo_card[key].index(called_number)
                bingo_card[key][idx] = 0
                
    print("\nSố lần gọi cần thiết để thắng:", called_count)

# Hiển thị thẻ Bingo
def display_bingo_card(card):
    print(" B   I   N   G   O")
    for i in range(5):
        for key in card:
            if card[key][i] == 0:
                print(" 0 ", end=" ")
            else:
                print(f"{card[key][i]:2d}", end=" ")
        print()

# Chạy chương trình
print("Chơi Bingo:")
play_bingo()
