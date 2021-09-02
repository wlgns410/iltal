# Iltal TEAM Project
# 팀원 : 설지우, 안희수, 이지훈

<img width="693" alt="스크린샷 2021-09-02 오후 2 42 22" src="https://user-images.githubusercontent.com/81137234/131788376-d7efec2d-67f8-458f-be66-d286bbb7ccdd.png">

- [유투브 시연 영상](https://youtu.be/s0_o4pgfNQQ)

## 작성한 엔드포인트

- 회원가입
```
class SignupView(View):
    def post(self, request):

        data = json.loads(request.body)
        EMAIL_REGES    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        PASSWORD_REGES = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,16}$'

        try:

            if not re.search(EMAIL_REGES, data["email"]):
                return JsonResponse ({"MESSAGE":"INVALID EMAIL"}, status = 400)

            if not re.search(PASSWORD_REGES, data["password"]):
                return JsonResponse ({"MESSAGE": "INVALID PASSWORD"}, status = 400)

            if User.objects.filter(email=data["email"]).exists():
                return JsonResponse ({"MESSAGE":"EXIST EMAIL"}, status = 400)

            hashed_passwored = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode()

            User.objects.create(
                email           = data["email"],
                password        = hashed_passwored,
                name            = data["name"],
            )

            return JsonResponse ({"MESSAGE":"SUCCESS"}, status = 201)
        except KeyError:
            return JsonResponse ({"MESSAGE":"KEY_ERROR"}, status = 400)
```

![스크린샷_2021-07-22_오전_10 51 43 (1)](https://user-images.githubusercontent.com/81137234/131797575-af029543-3616-46fb-9c35-e50dd4708912.png)

<br>

- 로그인
```
class SigninView(View):
    def post(self, request):

        try:
            data = json.loads(request.body)
            
            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message" : "INVALID_USER"}, status=401)

            user = User.objects.get(email=data["email"])
            
            if not bcrypt.checkpw(data["password"].encode("utf-8"), user.password.encode("utf-8")):
                return JsonResponse({"message": "INVALID_USER"}, status=401)
            
            access_token = jwt.encode({"user_id": user.id}, SECRET_KEY, ALGORITHM)
            
            return JsonResponse({"message":"success","access_token": access_token}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)
```
<br>
<img width="974" alt="스크린샷_2021-07-24_오후_7 20 31" src="https://user-images.githubusercontent.com/81137234/131797984-8b159147-4d6c-42dd-a9a2-18efdbc3499c.png">


- 소셜 로그인
```
class KakaoSigninView(View):
    def get(self, request):
        try:
            kakao_access_token     = request.headers.get('Authorization')
            headers                = {'Authorization': f'Bearer {kakao_access_token}'}
            kakao_user             = requests.get('https://kapi.kakao.com/v2/user/me', headers=headers).json()                
            user, is_created       = User.objects.get_or_create(kakao_id=kakao_user['id'])
            access_token           = jwt.encode({'user_id': user.id}, SECRET_KEY, ALGORITHM)

            if is_created:
                kakao_account    = kakao_user['kakao_account']
                properties       = kakao_user['properties']
                user.email       = kakao_account["email"]
                user.name        = properties["nickname"]
                user.profile_url = properties["profile_image"]
                user.save()
                return JsonResponse({"message":"success", "TOKEN": access_token}, status=201)

            return JsonResponse({"message":"success", "TOKEN": access_token}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)     
```
<br>

<img width="576" alt="스크린샷 2021-09-02 오후 3 59 07" src="https://user-images.githubusercontent.com/81137234/131798094-4894e0f6-47b0-4453-9a4e-457557362b5a.png">

<img width="734" alt="스크린샷_2021-07-26_오후_8 20 46" src="https://user-images.githubusercontent.com/81137234/131798078-884407cc-25e6-4f07-be3f-4a63f1a9f255.png">



<br>

## 프로젝트 소개
- 호스트와 게스트를 연결하여 다양한 액티비티 제공하는 사이트입니다.
- 우리의 프로젝트는, 탈잉의 기능(여행 및 액티비티 리스트, 검색 필터링, 호스트 등록 등)을 대한민국의 실제 여행 및 액티비티 데이터를 모티브로 만든 프로젝트입니다.
- 짧은 프로젝트 기간동안 개발에 집중해야 하므로 디자인 및 기능의 기획 부분만 클론했습니다.
- 개발은 초기 세팅부터 전부 직접 구현했으며, 모두 프론트와 연결하여 실제 사용할 수 있는 서비스 수준으로 개발하려고 노력했습니다.
- [백엔드 github 링크](https://github.com/wecode-bootcamp-korea/22-2nd-iltal-backend)
- [프론트엔드 github 링크](https://github.com/wecode-bootcamp-korea/22-2nd-iltal-frontend)

### 개발 인원 및 기간
- 개발기간 : 2021/7/19 ~ 2030/7/30
- 개발 인원 : 백엔드 3명, 프론트엔드 3명
- 백엔드    : [설지우](https://github.com/Jacesoul), [안희수](https://github.com/heesu-ahn), [이지훈](https://github.com/wlgns410)
- 프론트엔드 : [이수정(PM)](https://github.com/eeesssooo), [최재상](https://github.com/Higher77), [김수종](https://github.com/jaykim5)

### 프로젝트 선정이유
- 위코드 커리큘럼에서 배운 기술들을 그대로 적용하고 응용하는 데에 있어 새로운 기능을 적용하기에 적합한 난이도라고 판단했습니다.
- 사용자의 선택에 따라 구분되는 필터링이 매력적이라고 생각했습니다.
- 호스트를 통해 여행 및 액티비티 등록 후, 사용자의 참여 과정이 흥미로웠습니다.

<br>

## 적용 기술 및 구현 기능

### 협업 툴

> - [Notion](https://www.notion.so/API-8ea4af1e82ad494d9a9f9f696946ac94)
> - [Trello](https://trello.com/b/RkgLsPe1/iltal%F0%9F%8F%83%F0%9F%8F%BB%E2%99%82%EF%B8%8F)
> - Aquerytool

<img width="965" alt="스크린샷 2021-09-02 오후 2 39 31" src="https://user-images.githubusercontent.com/81137234/131788273-69ace31c-de7a-4bf8-9549-0ee3fcac7b03.png">


### 적용 기술

> - Front-End : javascript, React.js framwork, sass, hook
> - Back-End : Python, Django web framework, MySQL, Bcrypt, Pyjwt, AWS, Docker
> - Common : POSTMAN, Kakao REST API
### Back-End 구현 기능

#### 회원가입 / 로그인 모달
- 회원가입 시 정규식을 통한 유효성 검사. (소문자, 대문자, 숫자, 특수문자의 조합)
- 로그인을 이후 토큰 발행, 계정 활성화
- KaKao social login 이후 토큰 발행 및 적용
- Kakao 회원가입 이후 data를 받아 유저 정보 등록

#### 메인페이지

- Query parameter와 Q객체를 이용한 전체페이지 필터링 
- Select_related & Prefetch를 이용한 ORM 최적화
- AWS(EC2, RDS) & Docker 배포 

#### 상세페이지
- Path parameter를 통한 상품ID별 상세페이지 표현 
- Public / Private 페이지를 통해 좋아요 기능 구현 

#### 호스트페이지

- 호스트 등록 (데코레이터로 사용자 아이디 받아오기)
- 호스트 사진 등록 (AWS S3 서버에 업로드)
- 호스트 수정 (닉네임 프로필 사진 프론트 폼데이터로 받아서 처리)
- 여행 액티비티 등록 (호스트에 대한 여행 혹은 액티비티 등록)

### Front-End 구현 기능

#### 회원가입 / 로그인
- validtaion을 통한 일반 회원가입, 로그인 기능 구현
- 카카오 API를 이용한 소셜 로그인 기능 구현

#### 메인
- Card Components 구현
- 카테고리 지역 필터링 기능
- 카테고리 가격 필터링 기능
- 카테고리 그룹 필터링 기능

#### 호스트 등록
- 네이버지도 API 구현
- 타이틀, 배경 이미지, 프로필 사진 등록
- 여행 카테고리, 서브 카테고리, 그룹, 상세 주소 입력 후 호스트 등록

#### 상세 페이지
- access token 따른 Public / Private 구분
- Public / Private 에따른 좋아요, 예약하기 버튼 기능 구현



<br>

## Reference

- 이 프로젝트는 [탈잉](https://taling.me/?utm_source=google&utm_medium=cpc&utm_campaign=p2p&utm_content=pc_%EB%B8%8C%EB%9E%9C%EB%93%9C_00.%EC%9D%BC%EB%B0%98&utm_term=%ED%83%88%EC%9E%89&gclid=CjwKCAjwo4mIBhBsEiwAKgzXOOU7682iUwVGL5gIGtaiAGHjO8bo3TfunHMecCkw8uvJMCbWnGe3FhoCSlAQAvD_BwE) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무 수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
