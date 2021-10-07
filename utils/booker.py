from datetime import datetime, timedelta
import time


def reservataion(driver, configs):

  login(driver, configs)


  ReservationDate = configs.ReservationDate
  ReservationSeq = configs.ReservationSeq
  Form = 'ReservationForm(\'160\', \'' + ReservationDate + '\', \'' + ReservationSeq + '\');'
  ReservationOK = 'Reservation(\'ok\');'



  ReservationYear = ReservationDate[:4]
  ReservationMonth = ReservationDate[4:6]
  ReservationDay = ReservationDate[6:]
  reservationDateTime = datetime(int(ReservationYear), int(ReservationMonth), int(ReservationDay), 9, 0, 0)

  if(reservationDateTime.weekday() == 6):
    targetDateTime = reservationDateTime - timedelta(days=12)
  elif(reservationDateTime.weekday() == 5):
    targetDateTime = reservationDateTime - timedelta(days=11)
  else:
    targetDateTime = reservationDateTime - timedelta(days=7)

  now = datetime.now()
  prev_time = now

  print('=================================================================')
  print(f'예약자 ID: {configs.ID}')
  print('=================================================================')
  print(f'목표 예약 날짜: {reservationDateTime}')
  print(f'목표 예약 시간: {Form}')
  print('=================================================================')
  print(f'예약 실행 시간: {targetDateTime}')
  print(f'현재 시간: {now}')
  print('=================================================================')


  ReservationURL = 'https://www.daegucc.co.kr/Booking/ReservationCalendar?day=' + ReservationDate
  driver.get(url=ReservationURL)

  while(1):
    now = datetime.now()
    countDown = targetDateTime - now
  
    if((countDown.seconds / 60) > 30):
      print(countDown, end = '\r')
      time.sleep(10)
      continue


    if(now.second - prev_time.second >= 1):
      print(f'예약까지 남은 시간: {countDown}', end = '\r')

    if(now.year == targetDateTime.year and now.month == targetDateTime.month and now.day == targetDateTime.day and now.hour == targetDateTime.hour and now.minute == targetDateTime.minute and now.second == targetDateTime.second):
      startingTime = now
      print('=================================================================')
      print(f'시작 시간: {startingTime}')


      print('=================================================================')
      print(f'폼 입력 중 ({Form})')
      driver.execute_script(Form)
      print(f'폼 작성 완료')



      print('=================================================================')
      print(f'예약 확인 중')
      print(ReservationOK)
      driver.execute_script(ReservationOK)
      print(f'예약 완료')
      print('=================================================================')
      
      result = driver.switch_to_alert()
      result.accept()

      endTime = now
      print(f'종료 시간: {endTime}')
      print('총 소요 시간: ', endTime - startingTime)
      print('=================================================================')
      
      break

    prev_time = now







def login(driver, configs):

  ID = configs.ID
  Password = configs.Password


  LoginURL = 'https://www.daegucc.co.kr/Member/Login'
  inputIDElement = 'memberId'
  inputPWElement = 'memberPw'



  driver.get(url=LoginURL)
  idBox = driver.find_element_by_id(inputIDElement)
  idBox.send_keys(ID)
  pwBox = driver.find_element_by_id(inputPWElement)
  pwBox.send_keys(Password)
  driver.execute_script('login()')
  #Login alert
  result = driver.switch_to_alert()
  result.accept()


