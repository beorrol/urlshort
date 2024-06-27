# URL 단축기

Flask로 ChatGPT와 함께 만든 URL 단축기.

## 설정

1. 저장소를 클론합니다:
    ```sh
    git clone https://github.com/beorrol/urlshort.git
    cd url_shortener
    ```

2. 가상 환경을 생성하고 필요한 패키지를 설치합니다:
    ```sh
    python -m venv venv
    source venv/bin/activate  # 윈도우에서는 `venv\Scripts\activate`를 사용하세요.
    pip install Flask
    pip install Flask-SQLAlchemy
    ```

3. SSL 인증서를 생성합니다:
    ```sh
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
    ```

    생성된 `key.pem`과 `cert.pem` 파일을 프로젝트 루트 디렉토리로 이동시킵니다.

4. 애플리케이션을 실행합니다:
    ```sh
    python run.py
    ```

## 예제 SSL 인증서

이 저장소에는 참조용 예제 SSL 인증서 파일 `cert_example.pem`과 `key_example.pem`이 포함되어 있습니다. 이는 유효한 인증서가 아니므로 실제로 사용하려면 자신의 인증서를 생성해야 합니다.

---

© 2024 Juhyun.
