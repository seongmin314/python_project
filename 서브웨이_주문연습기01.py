#메뉴들 리스트
All_menu = ['K-바비큐', '얼터밋', '에그마요', '햄', '터키 ', '스파이시 이탈리안', '베지', '참치', '미트볼', '비엘티', '클럽' ]

Bread_menu = ['화이트', '위트', '플랫 브레드', '파마산 오레가노', '허니 오트']

Cheese_menu = ['모짜렐라', '슈레드', '아메리칸']

Vegetable_menu = ['양상추', '토마토', '오이', '피망', '양파', '피클', '올리브', '할라피뇨']

Sauce_menu = ['랜치', '마요네즈', '스위트 어니언', '허니 머스타드', '스위트 칠리', '바베큐', '핫칠리','사우스 웨스트', '머스타드', '홀스 래디쉬', '사우전 아일랜드', '이탈리안 드레싱', '마리나라 소스', '레드와인 식초', '소금', '후추','올리브 오일' ]




def order_sequence11():

    def order_sequence22():
        
        print(Sauce_menu)
        c_sauce = str(input("소스를 골라주세요 : "))
        if c_sauce in Sauce_menu:
            takeout_or_not = int(input("드시고 가시나요?\n1.네\n2.아니오"))
            if(takeout_or_not == 1):
                print("준비해 드리겠습니다")
            else:
                print("준비해 드리겠습니다")    
        else:
            print("주문하신 소스는 없습니다.")    

    onoff = int(input("주문하시겠습니까?\n 1.예\n 2.아니오 :"))
    if(onoff== 1):
        state =True
    else:
        print("안녕히가세요")
        state =False
    if state:
        choice = str(input("무엇을 주문하시겠어요? : "))        #시작
        if choice in All_menu:
            c_bread = str(input("빵을 골라주세요 : "))          #빵 고르기
            if c_bread in Bread_menu:
                c_cheese = str(input("치즈를 골라주세요: "))    #치즈 고르기
                if c_cheese in Cheese_menu:
                    print(Vegetable_menu)
                    YesorNo = int(input("안드시는 야채 있으신가요?\n 1.네\n 2.아니오\n"))
                    if(YesorNo== 1):
                        c_vege  = str(input("어떤 야채를 안드시나요? : "))
                        if c_vege in Vegetable_menu:
                            print("알겠습니다. 입력하신 야채를 빼겠습니다.")
                            order_sequence22() 
                        else:
                            print("입력하신 야채는 존재하지 않습니다.")    
                    else:
                        order_sequence22()
                else:
                    print("주문하신 치즈는 존재하지 않습니다.")
            else:
                print("주문하신 빵은 없는 빵입니다")
        else:
            print("그 메뉴는 존재하지 않습니다")

   


order_sequence11()