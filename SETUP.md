# Суулгах заавар (SETUP)

Энэ фолдерын бүх файлыг `JinreP/JinreP` гэдэг нэртэй **public** репо руу хуулж push хийнэ.
(Репо нь GitHub username-тэйгээ яг ижил нэртэй байх ёстой — тэгж байж profile README болдог.)

```
JinreP/
├── README.md
├── SETUP.md                     ← push хийхийн өмнө устгаж болно
├── assets/
│   ├── banner.svg
│   ├── Subeedei_CV_EN.pdf
│   └── Subeedei_CV_MN.pdf
├── scripts/
│   ├── update_activity.py
│   └── build_cv.py              ← CV-гийн эх файл (EN + MN); засаад дахин PDF болгоход хэрэгтэй
└── .github/workflows/
    ├── snake.yml
    ├── waka-readme.yml
    ├── metrics.yml
    ├── profile-3d.yml
    └── recent-activity.yml
```

## 1. Репо үүсгэх

1. github.com → New repository → нэр: `JinreP` → Public → Create
2. Энэ фолдерыг бүхэлд нь хуулж push хийнэ:
   ```bash
   cd JinreP
   git init
   git add .
   git commit -m "feat: new profile README"
   git branch -M main
   git remote add origin https://github.com/JinreP/JinreP.git
   git push -u origin main
   ```

## 2. Actions-д бичих эрх өгөх (заавал)

Repo → **Settings → Actions → General → Workflow permissions** →
**"Read and write permissions"** сонгоод Save. Үүнгүйгээр snake, 3D graph, activity шинэчлэгдэхгүй.

## 3. Secrets нэмэх

Repo → **Settings → Secrets and variables → Actions → New repository secret**

| Secret нэр | Хаанаас авах |
|---|---|
| `WAKATIME_API_KEY` | wakatime.com → Settings → API Key. Мөн VS Code-д **WakaTime** extension суулгаж API key-ээ оруулна. 7 хоног кодолсны дараа график гарна. |
| `METRICS_TOKEN` | github.com → Settings → Developer settings → Personal access tokens → **Tokens (classic)** → Generate new token. Scope: `public_repo`, `read:user`, `read:org` гэсэн 3-ыг л чагтал. Expiration: No expiration. |

`GITHUB_TOKEN` нь автоматаар байдаг, нэмэх шаардлагагүй.

## 4. Workflow-уудыг анх удаа ажиллуулах

Repo → **Actions** таб → зүүн талаас тус бүрийг нь сонгоод **Run workflow** дарна:
- Generate contribution snake
- Generate metrics
- Generate 3D contribution graph
- Update recent activity
- Update WakaTime stats (secret нэмсний дараа)

2–3 минутын дараа README дээр зураг бүгд гарч ирнэ. Дараа нь өдөр бүр өөрсдөө шинэчлэгдэнэ.

## 5. Spotify "Now Playing"

1. https://github.com/novatorem/novatorem репог **Fork** хийнэ.
2. https://developer.spotify.com/dashboard → Create app → Redirect URI: `http://localhost:3000/callback`
   → Client ID, Client Secret-ээ авна.
3. novatorem репогийн README дахь зааврын дагуу **Refresh Token** авна (нэг удаагийн ажил, 5 минут).
4. Fork хийсэн репогоо **Vercel**-д deploy хийнэ. Environment variables:
   `SPOTIFY_CLIENT_ID`, `SPOTIFY_SECRET_ID`, `SPOTIFY_REFRESH_TOKEN`
5. README.md дотор хоёр газрыг солино:
   - `https://YOUR-SPOTIFY-APP.vercel.app/api/spotify` → өөрийн Vercel URL
   - `https://open.spotify.com/user/YOUR_SPOTIFY_USER_ID` → Spotify профайлынхаа линк

Spotify хийхгүй бол README-ийн `## Now Playing` хэсгийг бүхэлд нь устгачих.

## 6. Заавал шалгах зүйлс

- **Journey хэсгийн огноонууд** — EduBuzz deploy хийсэн сар, PineQuest S3-ийн сарыг би мэдэхгүй тул
  `2026-07`, `2025-xx` гэж тавьсан. README.md дотроос зөв огноогоор нь соль.
- **Research club-ын нэр** — одоогоор "MUST International Research Club" гэсэн түр нэр.
- **CV** — `assets/Subeedei_CV_EN.pdf` (README-ийн товч үүн рүү заана), `assets/Subeedei_CV_MN.pdf`.
  Засах бол `scripts/build_cv.py` доторх текстийг засаад `pip install weasyprint` → `python3 scripts/build_cv.py`.
- **Pinned repos** — профайл дээрээ EduBuzz (QR-Kahoot), orshin, shivnee, ascend зэргийг **Customize your pins**-ээр pin хий.
