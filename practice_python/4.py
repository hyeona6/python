money=input("금액을 넣어주세요: ")
if int(money)<500:
  print("그지세요?")
elif int(money)<5500:
  print("잔액이 두배이상 부족합니다")
elif int(money)<11000:
  print("잔액이 부족합니다")
else:
  print("정상 처리되었습니다") 
