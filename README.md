## Stay: in
좋은 숙박 시설을 찾아보자!
좋은 여행 숙박 시설을 찾고 싶을 때 사용해봐요!

항해 99 1주차 프로젝트 


## 제작기간 
22.05.09(월) ~ 22.05.12(목)

## 팀원 및 역할 분담
```
조장 이은총
Role
```
```
조원 박민수
Role
```
```
조원 박세열
Role
```
## 프로젝트 소개


<hr>

## 1. 개발 환경

* 운영체제 : Windows, mac
* 개발 도구 : pycharm, visual studio code
* 개발 언어 : html, python
* 데이터베이스 : MongoDB

## 2. 기능 요약 설명
* 회원가입/로그인을 통한 계정 정보 저장 및 관리
* 회원가입 후 로그인으로 메인페이지에서 호텔 설명 카드 열람
* 상세 리뷰 버튼으로 상세 리뷰 페이지 이동하여 호텔에 대한 여러 코멘트들 열람 가능
* 마음에 드는 코멘트에 좋아요를 표시하여 좋아요 집계 가능
* 로그인으로 받은 토큰이 없다면 로그인 페이지 이외의 타 페이지 강제 이동 불가능

## 3. 데이터베이스 구조
![image](https://user-images.githubusercontent.com/79959576/167780696-03502869-1c8d-48b4-870a-65438e718e2a.png)


### hotel 데이터베이스
호텔의 전체적인 데이터들을 저장하는 데이터베이스
* __hotel_id__\
호텔이 생성될 때 할당 받는 아이디
* __name__\
호텔 이름
* __hotel rate__\
호텔이 몇성급인지 보여주는 인스턴스
* __hotel address__\
호텔 주소

<hr>

### user 데이터베이스
회원가입한 사용자의 데이터들을 저장하는 데이터베이스
* __user id__\
사용자의 아이디
* __password__\
사용자의 패스워드
* __nickname__\
사용자의 닉네임

<hr>

### comment 데이터베이스
호텔의 id와 유저의 id를 이용해 누가 어느 호텔에 코멘트를 달았는지 볼 수 있는 데이터베이스
* __comment id__\
코멘트가 생성될 때 자체적으로 생기는 아이디
* __comment rate__\
사용자가 코멘트를 작성할 때 매기는 별점
* __nickname__\
사용자의 닉네임
* __hotel_id__\
호텔이 생성될 때 할당 받는 아이디


<hr>

### Likes 데이터베이스
누가 무슨 코멘트를 좋아요를 했는지 알 수 있는 데이터베이스
* __likes id__\
좋아요가 생성될 때 자체적으로 생기는 아이디
* __comment id__\
코멘트가 생성될 때 자체적으로 생기는 아이디
* __nickname__\
사용자의 닉네임
