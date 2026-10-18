# Start here / 시작하기

**Research Fast and Design Live with Mobbin MCP.** Designed Minds, in person in Seoul,
Saturday 24 October 2026, 12:00 to 2:00 PM.
**Mobbin MCP로 빠르게 리서치하고 바로 디자인하기.** Designed Minds 서울 오프라인 워크숍,
2026년 10월 24일 토요일 오후 12시 ~ 2시.

Today you redesign one real screen, the home screen of SC제일은행's SC Mobile app (Standard
Chartered Bank Korea), with your AI tool and real banking screens from Mobbin. You don't need a
terminal, Node or Python. Just the AI tool you already use.

오늘은 실제 화면 하나, SC제일은행 SC Mobile 앱의 홈 화면을 여러분의 AI 도구와 Mobbin의 실제
뱅킹 앱 화면으로 다시 디자인합니다. 터미널, Node, Python은 필요 없습니다. 평소 쓰는 AI 도구면
충분합니다.

Board / 보드: **[FigJam](https://www.figma.com/board/ta8xP6bThj8jAshgtjOIXE)**.
Mobbin MCP setup / 설정: **[mobbin.com/mcp](https://mobbin.com/mcp)**.

![The template: SC Mobile home screen / 템플릿: SC Mobile 홈 화면](template/preview.png)

## Before the session (5 minutes) / 워크숍 전에 (5분)

0. **Join the Designed Minds team on Mobbin.** Open the
   [team link](https://mobbin.com/team/join/0fba9939-3fe3-4f87-adfe-c29ee0211caf), then log in or
   create a free account. The page should say "join team, Designed Minds". An admin approves you,
   and from then on Mobbin MCP works on your account. Is your work account on Mobbin Enterprise?
   Join with a personal or test account instead.
   **Mobbin에서 Designed Minds 팀에 가입하세요.** [팀 링크](https://mobbin.com/team/join/0fba9939-3fe3-4f87-adfe-c29ee0211caf)를
   열고 로그인하거나 무료 계정을 만드세요. 화면에 "join team, Designed Minds"가 보이면 맞습니다.
   관리자가 승인하면 그때부터 Mobbin MCP를 쓸 수 있습니다. 회사 계정이 Mobbin Enterprise라면
   개인 계정이나 테스트 계정으로 가입하세요.
1. **Get the kit.** You're reading this, so you probably have it. If not:
   [download kit.zip](https://github.com/andreaskruszakin/mobbin-hatch-workshop/releases/download/seoul-2026-10-24/kit.zip)
   and unzip it.
   **키트를 받으세요.** 이 파일을 읽고 있다면 이미 받으신 겁니다. 아니라면
   [kit.zip을 내려받아](https://github.com/andreaskruszakin/mobbin-hatch-workshop/releases/download/seoul-2026-10-24/kit.zip)
   압축을 푸세요.
2. **Use a personal account if you can.** Company (enterprise) Cursor or Claude accounts often
   block MCP servers. If your work account is locked down, sign in with a personal one.
   **가능하면 개인 계정을 쓰세요.** 회사(엔터프라이즈) Cursor나 Claude 계정은 MCP 서버를 막아 둔
   경우가 많습니다. 회사 계정이 막혀 있으면 개인 계정으로 로그인하세요.
3. **Add Mobbin MCP to your AI tool**, then open this folder in it.
   **AI 도구에 Mobbin MCP를 추가하고**, 이 폴더를 여세요.
   - **Cursor.** Install the Mobbin plugin from the Cursor Marketplace (mobbin.com/mcp > Cursor,
     or Customize > Browse Marketplace > Mobbin), then Customize > Installed > Mobbin >
     **Authenticate** and sign in. Then File > Open Folder and pick this folder.
     Cursor Marketplace에서 Mobbin 플러그인을 설치하고 Customize > Installed > Mobbin >
     **Authenticate**로 로그인하세요. 그다음 File > Open Folder로 이 폴더를 엽니다.
   - **Claude Desktop.** Open [claude.ai/directory/mobbin](https://claude.ai/directory/mobbin)
     and add it, or go to Customize > Connectors > Add > Browse connectors and search "Mobbin".
     Claude Desktop can't open a folder, so drag `template/index.html`, the five images in
     `template/screens/` and `prompts.md` into the chat instead.
     [claude.ai/directory/mobbin](https://claude.ai/directory/mobbin)에서 추가하거나
     Customize > Connectors > Add에서 "Mobbin"을 검색하세요. Claude Desktop은 폴더를 열 수
     없으니 `template/index.html`, `template/screens/`의 이미지 다섯 장, `prompts.md`를 채팅창에
     끌어다 놓으세요.
   - **Claude Code.** If you connected Mobbin in Claude Desktop or on claude.ai, Claude Code
     already has it. Otherwise: `cd` into this folder, run `claude`, trust the project's
     `.mcp.json`, then type `/mcp`, pick **mobbin**, choose **Authenticate**.
     Claude Desktop이나 claude.ai에서 연결했다면 이미 됩니다. 아니라면 이 폴더에서 `claude`를
     실행하고 `.mcp.json`을 신뢰한 뒤 `/mcp` > **mobbin** > **Authenticate**.
   - **Codex.** Run `codex mcp add mobbin --url https://api.mobbin.com/mcp`, then
     `codex mcp login mobbin`, then run `codex` inside this folder.
   - **Anything else / 그 밖의 도구.** Add an MCP server named `Mobbin` with the URL
     `https://api.mobbin.com/mcp`. Help / 도움말: [docs.mobbin.com/mcp](https://docs.mobbin.com/mcp/clients/overview).
4. **Run step 1 from `prompts.md`.** If three results come back, you're ready.
   **`prompts.md`의 1단계를 실행하세요.** 결과가 세 개 나오면 준비 끝입니다.

The first Mobbin search is often slow or times out. Run it again. The second try almost always works.
첫 Mobbin 검색은 느리거나 시간 초과가 나는 경우가 많습니다. 한 번 더 실행하면 거의 항상 됩니다.

## If something breaks / 문제가 생기면

Raise your hand. Eunji and Luany walk the room and help. / 손을 들어 주세요. Eunji와 Luany가 도와드립니다.

- **Mobbin says "Upgrade".** You're not on the team yet, or the admin hasn't approved you. Open the
  [team link](https://mobbin.com/team/join/0fba9939-3fe3-4f87-adfe-c29ee0211caf) with the same
  Mobbin account, then ask a host to approve you.
  **Mobbin에 "Upgrade"가 뜨면** 아직 팀에 가입하지 않았거나 승인 전입니다. 같은 계정으로 팀 링크를
  열고 호스트에게 승인을 요청하세요.
- **Mobbin times out, or says "Failed to execute search".** Wait a few seconds and run it again. If
  it keeps failing, reconnect Mobbin (Cursor: Authenticate again; Claude Code: `/mcp`).
  **시간 초과나 "Failed to execute search"가 뜨면** 몇 초 뒤 다시 실행하세요. 계속 실패하면 Mobbin을
  다시 연결하세요.
- **Mobbin is blocked (enterprise account).** Switch to a personal account. If you can't, use the
  backup links at the bottom of `prompts.md`: open them, take screenshots, paste them into your AI tool.
  **회사 계정이라 막혀 있으면** 개인 계정으로 바꾸세요. 안 되면 `prompts.md` 맨 아래 백업 링크를
  열어 스크린샷을 찍고 AI 도구에 붙여 넣으세요.
- **The AI invents balances, cards or events.** The app has one balance (99,749원) and no cards.
  Tell it to keep only the content in `template/index.html`.
  **AI가 잔액, 카드, 이벤트를 지어내면** 앱에는 잔액 하나(99,749원)와 카드 0개뿐입니다.
  `template/index.html`의 내용만 쓰라고 하세요.
- **The redesign looks like the same screen with new colours.** Ask which parts of the screen it
  moved. If the layout is the same, send it back to your picks.
  **색만 바뀐 같은 화면이면** 무엇을 옮겼는지 물어보고, 배치가 같으면 고른 레퍼런스로 돌려보내세요.
- **Free plan runs out of messages.** Paste one block at a time and keep the same chat. Switch to
  Claude Desktop or Codex if your tool stops.
  **무료 플랜 한도가 차면** 한 번에 한 블록씩, 같은 채팅에서 진행하세요.

## What Mobbin MCP can search / Mobbin MCP로 검색할 수 있는 것

| Tool | Use it for / 용도 | Example / 예시 |
| --- | --- | --- |
| `search_screens` | One screen, like a bank home / 화면 하나 | "banking home screen with total balance and a transfer button" |
| `search_flows` | A journey across screens / 여러 화면의 흐름 | "send money flow from home to confirmation" |
| `search_sections` | One section of a website / 웹사이트의 한 섹션 | "account summary card with balances" |

This is a mobile app, so search with platform `ios`. The team plan includes Finance+, which has
many banking home screens.
모바일 앱이니 플랫폼은 `ios`로 검색하세요. 팀 플랜에 Finance+가 포함되어 있어 뱅킹 홈 화면이 많습니다.

## What is in this folder / 폴더 구성

| File | What it is / 설명 |
| --- | --- |
| `template/index.html` | The screen you redesign, rebuilt in React. Double-click to open. Top left switches 한국어 / English. / 다시 디자인할 화면(React). 더블클릭으로 열고, 왼쪽 위에서 언어를 바꿉니다. |
| `template/screens/` | Five screenshots of the real app, top to bottom. / 실제 앱 스크린샷 다섯 장. |
| `template/assets/` | Photos, illustrations and icons cropped from those screenshots. / 스크린샷에서 잘라 낸 이미지. |
| `prompts.md` | Five prompts, English and Korean. Paste one at a time. / 프롬프트 다섯 개(영어, 한국어). |

The screenshots were taken on 17 October 2026. The customer's name is replaced with 홍길동, the
Korean placeholder name. `template/index.html` works offline: React sits in `template/vendor/`.
스크린샷은 2026년 10월 17일에 찍었고, 고객 이름은 홍길동으로 바꿨습니다. React가
`template/vendor/`에 들어 있어 오프라인에서도 열립니다.

## In the session / 워크숍 진행

Follow the board. We run the five prompts together, one step at a time.
보드를 따라오세요. 다섯 개의 프롬프트를 한 단계씩 함께 실행합니다.

1. **Warm up / 준비.** Your AI reads the template and the screenshots, and Mobbin wakes up.
2. **Search / 검색.** Mobbin shows real banking home screens that fix what's wrong.
3. **Pick / 선택.** You choose one to three and say why. Post your picks on the board.
4. **Redesign / 리디자인.** Your AI builds `mine/index.html` from your picks, in both languages.
5. **Share / 공유.** Paste your before and after into your lane on the board.
