import random



# Bước 1: Tạo thẻ Bingo ngẫu nhiên
def creatBroad():
    card = {
        'B': random.sample(range(1, 16), 5), # random.sample: lấy ngẫu nhiên 5 số từ 1 đến 15 và không trùng nhau
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    card['N'][2] = 0 # Thêm số 0 vào vị trí (3, 3) để đại diện cho trung tâm không có số
    return card

def broad(card):
    print(" B   I   N   G   O")
    for i in range(5):
        for key in card:
            if card[key][i] == 0:
                print(" 0 ", end="  ")
            else:
                print(f"{card[key][i]:2d}", end="  ")
        print()

# Bước 2: Kiểm tra thẻ thắng
def check_winning_card(card):
    # Kiểm tra dòng dọc
    for key, col in zip(card.keys(), card.values()):
        if all(num == 0 for num in col):
            print(f"Cột {key} thắng")
            return True
    # Kiểm tra dòng ngang
    for col in range(5):
        if all(card[key][col] == 0 for key in card):
            print(f"Hàng {col} thắng")
            return True
    # Kiểm tra đường chéo
    # index // key: 0 // B, 1 // I, 2 // N, 3 // G, 4 // O
                #    4 // B, 3 // I, 2 // N, 1 // G, 0 // O 
    if all(card[key][i] == 0 for i, key in enumerate(card)) or \
        all(card[key][4-i] == 0 for i, key in enumerate(card)):
        print('chéo thắng')
        return True
    return False

# Bước 3: Chơi Bingo
def main():    
    # Mô phỏng trò chơi
    called_count = 0
    while not check_winning_card(bingo_card):
        print("Thẻ Bingo:")
        broad(bingo_card)
        called_number = called_numbers.pop(0)
        called_count += 1
        
        # Đánh dấu số đã gọi trên thẻ
        for key in bingo_card:
            if called_number in bingo_card[key]:
                print("Số đã gọi:", called_number)
                idx = bingo_card[key].index(called_number)
                bingo_card[key][idx] = 0
    
        print('\n\n')
    print("\nSố lần gọi để thắng:", called_count)
    print("Thẻ Bingo:")
    broad(bingo_card)


if __name__ == '__main__':
        # Tạo thẻ Bingo
    bingo_card = creatBroad()    
    # Danh sách các số đã gọi
    called_numbers = random.sample(range(1, 76), 75)
    print(called_numbers)
    main()