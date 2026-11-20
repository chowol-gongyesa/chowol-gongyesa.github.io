// 장인 경력 연수. 2026년에 "40년"이 맞다고 하셨으므로 1986년에 시작하신 것으로 계산합니다 (사용자 확인 2026-11-20).
// 빌드할 때의 연도로 계산하므로, 매년 1월 1일에 자동으로 다시 만들도록
// .github/workflows/deploy.yml 에 일정(schedule)을 넣어 두었습니다.
export const START_YEAR = 1986;
export const YEARS = new Date().getFullYear() - START_YEAR;
