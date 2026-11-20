# 초월공예사 홈페이지

자동 로구로 전문 초월공예사의 홈페이지입니다. (제작 중)

## 자주 고치는 곳

| 바꾸고 싶은 것                   | 파일                                                    |
| -------------------------------- | ------------------------------------------------------- |
| 전화번호·주소·영업시간·작업 분야 | `src/data/shop.ts`                                      |
| 작업물 사진 목록·설명            | `src/data/works.ts` (사진은 `src/assets/images/works/`) |
| 화면 문구                        | `src/i18n/ko.ts`                                        |
| 소식(블로그) 글                  | `src/data/post/` 에 `.md` 파일 추가                     |
| 색상·글꼴                        | `src/components/CustomStyles.astro`                     |

## 실행

```bash
npm ci            # 처음 한 번
npm run dev       # 개발 서버 http://localhost:4322
npm run build     # 배포용 빌드 확인
npm run preview   # 빌드 결과 미리보기 (사진까지 확인)
```

## 라이선스

[AstroWind](https://github.com/arthelokyo/astrowind) 템플릿(MIT, `LICENSE.md`)을 바탕으로 만들었습니다.
작업 사진과 가게 정보의 권리는 초월공예사에 있습니다.
