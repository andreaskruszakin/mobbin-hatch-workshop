# Prompts / 프롬프트

Five steps. Paste one block at a time, in English or in Korean. Read what comes back before you
paste the next one. Blocks 2 to 5 run in the same chat as block 1, so your AI keeps the context.

다섯 단계입니다. 영어나 한국어 중 편한 쪽으로 한 블록씩 붙여 넣으세요. 답을 읽고 다음 블록으로
넘어가세요. 2~5단계는 1단계와 같은 채팅에서 진행해야 AI가 맥락을 기억합니다.

## What's wrong with the home screen / 홈 화면의 문제

Customers who use the app every day told us this. Block 1 hands it to your AI.
매일 이 앱을 쓰는 고객들이 말한 문제입니다. 1단계에서 AI에게 그대로 전달합니다.

1. A big ad for Liverpool FC football lessons is the first thing you see. "I'm the bank's customer,
   but it shows me ads like YouTube." / 첫 화면이 리버풀FC 축구 레슨 광고입니다. "은행 고객인데
   유튜브처럼 광고를 보여 줘요."
2. The accounts card lists eight rows with the same weight, and most say 0. The one real balance
   (99,749원) doesn't stand out. / 전체계좌 카드에 여덟 줄이 똑같은 무게로 나열되고, 대부분 0입니다.
   실제 잔액 99,749원이 눈에 띄지 않습니다.
3. 글로벌시황 (global markets) gets a big shortcut that almost nobody needs. / 거의 쓰지 않는
   글로벌시황이 큰 바로가기를 차지합니다.
4. The cards you already hold don't appear. The app only tries to sell new ones. / 내가 가진
   카드는 안 보이고 새 카드 판매만 보입니다.
5. 로그아웃 (log out) sits on the home screen as a black button. / 로그아웃 버튼이 홈 화면 상단에
   검은 버튼으로 있습니다.
6. The bottom bar has a big raised circle, and 이체 (transfer), the most common task, is just one
   small tab. / 하단 탭에 큰 원형 버튼이 튀어나와 있고, 가장 자주 쓰는 이체는 작은 탭 하나입니다.
7. Below that, twelve event and content cards in one long list. / 그 아래로 이벤트와 콘텐츠 카드
   열두 개가 길게 이어집니다.

## 1. Warm up / 준비 (during setup / 세팅 중)

```
This folder is the Mobbin MCP workshop. template/index.html is the home screen of SC제일은행's
SC Mobile app (Standard Chartered Bank Korea), rebuilt in React from the screenshots in
template/screens/ (01.png is the top of the screen, 05.png the bottom). It has Korean and English
copy; the 한국어 / English switch is at the top left. It is the only screen we redesign today,
for personal banking customers.

Customers told us what is wrong with it:
- A Liverpool FC ad banner is the first thing they see.
- Eight account rows with equal weight, mostly 0; the one real balance (99,749원) does not stand out.
- 글로벌시황 (global markets) gets a big shortcut nobody needs.
- Cards they already hold never appear; the app only sells new cards.
- A black 로그아웃 (log out) button sits on the home screen.
- The bottom bar has a big raised circle, and 이체 (transfer) is a small tab.
- Twelve event and content cards in one long list.

1. Read template/index.html and look at the five screenshots. Confirm the five problems that hurt
   most when you just want to check your balance or send money, in five short bullets.
2. List the Mobbin MCP tools you have access to, with one line each on what they search.
3. Search Mobbin for "banking app home screen with account balance and transfer button",
   platform ios, mode standard, limit 3. Show the app name and mobbin_url for each result.

Stop after that.
```

```
이 폴더는 Mobbin MCP 워크숍 자료입니다. template/index.html은 SC제일은행 SC Mobile 앱의 홈 화면을
template/screens/의 스크린샷(01.png가 화면 맨 위, 05.png가 맨 아래)을 보고 React로 다시 만든
것입니다. 한국어와 영어 문구가 있고, 왼쪽 위의 한국어 / English 버튼으로 바꿉니다. 오늘은 개인
뱅킹 고객을 위해 이 화면 하나만 다시 디자인합니다.

고객들이 말한 문제:
- 첫 화면이 리버풀FC 광고 배너입니다.
- 전체계좌 여덟 줄이 같은 무게로 나열되고 대부분 0이라, 실제 잔액(99,749원)이 눈에 띄지 않습니다.
- 거의 안 쓰는 글로벌시황이 큰 바로가기를 차지합니다.
- 내가 가진 카드는 보이지 않고 새 카드 판매만 보입니다.
- 홈 화면에 검은 로그아웃 버튼이 있습니다.
- 하단 탭에 큰 원형 버튼이 있고, 이체는 작은 탭 하나입니다.
- 이벤트와 콘텐츠 카드 열두 개가 길게 이어집니다.

1. template/index.html을 읽고 스크린샷 다섯 장을 보세요. 잔액을 확인하거나 송금만 하고 싶은
   사람에게 가장 불편한 문제 다섯 가지를 짧은 bullet 다섯 개로 정리해 주세요.
2. 사용할 수 있는 Mobbin MCP 도구를 나열하고, 각각 무엇을 검색하는지 한 줄로 알려 주세요.
3. Mobbin에서 "banking app home screen with account balance and transfer button"을
   platform ios, mode standard, limit 3으로 검색하세요. 결과마다 앱 이름과 mobbin_url을 보여 주세요.

여기서 멈추세요.
```

Three results with links means you're ready. If Mobbin times out, paste the block again.
링크가 있는 결과가 세 개 나오면 준비 끝입니다. 시간 초과가 나면 블록을 다시 붙여 넣으세요.

## 2. Search / 검색

```
Stay in this chat. Use the five problems you confirmed in the warm-up.

Using Mobbin MCP, find real banking apps that fix those problems. Platform ios, limit 4 each:

1. search_screens, mode deep, twice. Describe each screen in one sentence: what it shows and how
   its parts relate. Good examples:
   - "banking home screen where the main account balance and a send money button come first"
   - "banking home screen grouping accounts by type with totals"
2. search_flows, once: "send money flow from the home screen to confirmation".
3. search_sections, once: "account summary card with balance and quick actions".
Change the queries to match your problems. Try Korean apps too, like Toss or KakaoBank.

For every result, give me the app name, the mobbin_url, and one sentence about what is actually in
the image. Do not describe a screen from the app's reputation. Look at it.

Do not redesign anything yet. Stop after the list.
```

```
이 채팅에서 계속합니다. 준비 단계에서 정리한 문제 다섯 가지를 기준으로 하세요.

Mobbin MCP로 그 문제를 해결한 실제 뱅킹 앱을 찾아 주세요. platform ios, 각각 limit 4:

1. search_screens, mode deep, 두 번. 화면 하나를 한 문장으로, 무엇이 보이고 요소들이 어떻게
   배치되는지 설명하세요. 좋은 예:
   - "banking home screen where the main account balance and a send money button come first"
   - "banking home screen grouping accounts by type with totals"
2. search_flows, 한 번: "send money flow from the home screen to confirmation".
3. search_sections, 한 번: "account summary card with balance and quick actions".
문제에 맞게 검색어를 바꾸세요. 토스나 카카오뱅크 같은 한국 앱도 찾아보세요.

결과마다 앱 이름, mobbin_url, 이미지에 실제로 보이는 내용 한 문장을 주세요. 앱의 평판으로
설명하지 말고 화면을 직접 보세요.

아직 리디자인하지 마세요. 목록까지만 하고 멈추세요.
```

## 3. Pick / 선택

This step is yours, not the AI's. Choose one to three references from step 2. For each one, write
one sentence: which problem on the SC Mobile home it fixes, and why. Post your picks on the board.
이 단계는 AI가 아니라 여러분이 합니다. 2단계 결과에서 한~세 개를 고르고, 각각 SC Mobile 홈의 어떤
문제를 왜 해결하는지 한 문장으로 쓰세요. 고른 레퍼런스를 보드에 올려 주세요.

```
These are my picks:
1. [mobbin_url], because [the problem it fixes, and why]
2. [mobbin_url], because [...]
3. [mobbin_url], because [...]

Before building, tell me in two lines how each pick changes the structure of the home screen.
Do not start building yet.
```

```
제가 고른 레퍼런스입니다:
1. [mobbin_url], 이유: [해결하는 문제와 그 이유]
2. [mobbin_url], 이유: [...]
3. [mobbin_url], 이유: [...]

만들기 전에, 각 레퍼런스가 홈 화면의 구조를 어떻게 바꾸는지 두 줄로 알려 주세요.
아직 만들지 마세요.
```

## 4. Redesign / 리디자인

```
Build mine/index.html from template/index.html using my picks and the search results above.
Every part you move should fix one of the five problems.

Rules:
- Keep the React structure: the copy object with ko and en, the art object, one component per part.
- Keep SC Mobile's content: every label, balance, count, date and event title, in both languages.
  You may remove or demote parts (an ad, a shortcut), but do not invent balances, cards,
  transactions or events the template does not have. The customer holds no cards (현대카드 0개),
  so a cards slot needs an empty state with one clear action.
- Change how the screen is arranged, not only the colours and fonts.
- Reuse images and React with relative paths (../template/assets/..., ../template/vendor/...).
- One HTML file, no build step, it must open by double-click, and the 한국어 / English switch must work.
- Put my picks as mobbin_url links in an HTML comment at the top.

When you are done, list which parts of the screen moved and which parts you removed.
```

```
위의 레퍼런스와 검색 결과로 template/index.html을 바탕으로 mine/index.html을 만들어 주세요.
옮기는 부분마다 다섯 가지 문제 중 하나를 해결해야 합니다.

규칙:
- React 구조를 유지하세요: ko와 en이 있는 copy 객체, art 객체, 부분마다 컴포넌트 하나.
- SC Mobile의 내용을 유지하세요: 모든 라벨, 잔액, 개수, 날짜, 이벤트 제목을 두 언어 모두.
  광고나 바로가기 같은 부분은 빼거나 아래로 내려도 되지만, 템플릿에 없는 잔액, 카드, 거래, 이벤트는
  지어내지 마세요. 고객은 카드가 없으니(현대카드 0개), 카드 영역에는 분명한 행동 하나가 있는
  빈 상태가 필요합니다.
- 색과 폰트만이 아니라 화면의 배치를 바꾸세요.
- 이미지와 React는 상대 경로로 다시 쓰세요 (../template/assets/..., ../template/vendor/...).
- HTML 파일 하나, 빌드 없이 더블클릭으로 열려야 하고, 한국어 / English 전환이 작동해야 합니다.
- 제가 고른 mobbin_url 링크를 맨 위 HTML 주석에 넣어 주세요.

다 만들면 화면에서 무엇을 옮겼고 무엇을 뺐는지 알려 주세요.
```

Open `mine/index.html` next to `template/index.html`. If they look like the same screen in new
colours, you changed the paint, not the plan. Go back to step 3.
`mine/index.html`과 `template/index.html`을 나란히 열어 보세요. 색만 바뀐 같은 화면이라면 계획이
아니라 페인트를 바꾼 겁니다. 3단계로 돌아가세요.

## 5. Share / 공유

Screenshot `template/index.html` and `mine/index.html` in the browser (Cmd+Shift+4 on Mac,
Win+Shift+S on Windows) and paste both into your lane: Before on the left, After on the right. Your
picks go on stickies next to them.
브라우저에서 `template/index.html`과 `mine/index.html`을 캡처해(Mac Cmd+Shift+4, Windows
Win+Shift+S) 보드의 내 레인에 붙여 넣으세요. 왼쪽이 Before, 오른쪽이 After입니다. 고른
레퍼런스는 옆에 스티커로 붙이세요.

**Extra points: put it online. / 추가 점수: 온라인에 올리기.**

```
Deploy the mine/ folder to Vercel as a static site. It needs ../template/assets/ and
../template/vendor/, so first copy the files it uses into mine/ and update the paths. Then run
npx vercel deploy mine --prod and give me the live URL.
```

```
mine/ 폴더를 Vercel에 정적 사이트로 배포해 주세요. ../template/assets/와 ../template/vendor/가
필요하니 먼저 쓰는 파일을 mine/ 안으로 복사하고 경로를 고쳐 주세요. 그다음
npx vercel deploy mine --prod를 실행하고 주소를 알려 주세요.
```

If Vercel asks you to log in and you can't, or the deploy fails, skip it. The screenshots are enough.
Vercel 로그인이 안 되거나 배포가 실패하면 건너뛰세요. 스크린샷이면 충분합니다.

## More prompts to try / 더 해 볼 프롬프트

- Make 이체 (transfer) one tap from the balance. / 잔액에서 한 번에 이체할 수 있게 하세요.
- Turn the twelve event cards into one row the customer can scroll past. / 이벤트 카드 열두 개를
  넘겨 볼 수 있는 한 줄로 바꾸세요.
- Design the screen with 편한뱅킹 (easy mode) turned on. / 편한뱅킹을 켰을 때의 화면을 디자인하세요.
- Rebuild the bottom bar without the raised circle. / 튀어나온 원형 버튼 없이 하단 탭을 다시 만드세요.
- Build a second version at `mine-2/index.html` with your other pick. / 다른 레퍼런스로
  `mine-2/index.html`에 두 번째 버전을 만드세요.

## Backup links (if Mobbin MCP is blocked) / 백업 링크 (Mobbin MCP가 막혔을 때)

Open these in the browser, screenshot what you like, and paste the screenshots into your AI tool.
브라우저에서 열어 마음에 드는 화면을 캡처하고 AI 도구에 붙여 넣으세요.

- [Toss, each account with its own 송금 (send) button](https://mobbin.com/screens/b5315413-f78c-4e36-9d05-316633c10e7c)
- [Toss, 운세 (fortune) and card offers as small rows below the money](https://mobbin.com/screens/44c0d237-000a-4dac-8b60-c9b19b80366a)
- [SoFi, total balance, two accounts, then Transfer, Deposit, Pay](https://mobbin.com/screens/47aa4a02-90c9-4c29-ba5e-3618f1f36e06)
- [Lloyds, accounts grouped into Everyday, Save & Invest, Borrow](https://mobbin.com/screens/c300d0ae-2f85-4443-8df9-8fed6887390c)
- [N26, balance with Add money and Send money as the two big actions](https://mobbin.com/screens/52ecfd8a-5c0a-4a0d-bf1f-518ee3b88767)
- [Quicken, one card summing every account type](https://mobbin.com/screens/48ef3fe1-d56a-4b3b-ac48-34375808e966)
