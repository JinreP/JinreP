"""Builds Subeedei_CV_EN.pdf and Subeedei_CV_MN.pdf (two-column, dark sidebar)
with WeasyPrint (pip install weasyprint). Run from the repo root:  python3 scripts/build_cv.py"""

from weasyprint import HTML
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
TMP = ROOT / "scripts"

EN = dict(
    lang="en",
    name="SUBEEDEI",
    title="Junior Software Engineer",
    h_contact="Contact", h_skills="Skills", h_langs="Languages", h_awards="Awards",
    h_profile="Profile", h_projects="Projects", h_edu="Education",
    location="Ulaanbaatar, Mongolia",
    profile=("Full-stack developer and Software Engineering student at MUST. I ship complete web products "
             "— database, API, UI, deployment — with Next.js, TypeScript, Node.js and MongoDB/PostgreSQL. "
             "Pinecone Academy graduate, PineQuest S3 hackathon winner. Looking for an internship or junior "
             "role where I can build real features with an experienced team."),
    projects=[
        ("EduBuzz", "Real-time live quiz platform", "2026 – present",
         "Next.js · Tailwind · Socket.IO · Express · MongoDB · qr-kahoot.vercel.app",
         ["Kahoot-style quiz game: teachers create quizzes, students join a room by QR code and answer live over WebSockets",
          "Built teacher / student / admin roles, room lifecycle and live scoring; deployed on Vercel",
          "Designed the UI in Figma and v0.dev, implemented with shadcn/ui"]),
        ("Ascend", "Student club website for MUST", "Oct 2026 – present",
         "Next.js · TypeScript · Tailwind",
         ["Trilingual (MN / RU / EN) site built at a lecturer's request: online admissions, member profiles, admin panel and news"]),
        ("MUST International Research Club website", "", "Oct 2026 – present",
         "Next.js · TypeScript · 10-person student team",
         ["Own the UI/UX design (HTML prototype → Figma) and the proposed full-stack Next.js architecture"]),
    ],
    edu=[
        ("Mongolian University of Science and Technology (MUST)", "B.Sc. Software Engineering, Department of Computer Science", "2026 – 2029 (expected)"),
        ("Pinecone Academy", "Full-stack Software Engineering program, 10 months, certified — JavaScript, React, Next.js, Node.js, MongoDB", "Jun 2025 – Apr 2026"),
        ("School No. 2, Ulaanbaatar", "Secondary education", "2024"),
    ],
    skills=[
        ("Languages", "TypeScript, JavaScript, Python, C, C#"),
        ("Frontend", "Next.js, React, Tailwind CSS, shadcn/ui, HTML/CSS"),
        ("Backend", "Node.js, Express, REST APIs, Socket.IO, Prisma"),
        ("Databases", "MongoDB, PostgreSQL"),
        ("Tools", "Git/GitHub, Vercel, Figma, Postman, Unity, Roblox Studio"),
    ],
    langs=[("Mongolian", "Native"), ("English", "Intermediate")],
    awards=[("1st place — PineQuest S3", "Pinecone Academy hackathon, 2025")],
)

MN = dict(
    lang="mn",
    name="СҮБЭЭДЭЙ",
    title="Junior Software Engineer",
    h_contact="Холбоо барих", h_skills="Ур чадвар", h_langs="Хэл", h_awards="Шагнал",
    h_profile="Товч танилцуулга", h_projects="Төслүүд", h_edu="Боловсрол",
    location="Улаанбаатар, Сүхбаатар дүүрэг",
    profile=("ШУТИС-ийн Программ хангамжийн инженерчлэлийн оюутан, full-stack хөгжүүлэгч. Next.js, TypeScript, "
             "Node.js, MongoDB/PostgreSQL ашиглан өгөгдлийн сангаас deploy хүртэл бүрэн веб бүтээгдэхүүн хийж "
             "гаргадаг. Pinecone Academy төгсөгч, PineQuest S3 хакатоны 1-р байр. Туршлагатай багтай хамт бодит "
             "бүтээгдэхүүн хөгжүүлэх дадлага эсвэл junior ажлын байр хайж байна."),
    projects=[
        ("EduBuzz", "Бодит цагийн асуулт хариултын платформ", "2026 – одоо",
         "Next.js · Tailwind · Socket.IO · Express · MongoDB · qr-kahoot.vercel.app",
         ["Kahoot маягийн тоглоом: багш quiz үүсгэж, сурагчид QR кодоор өрөөнд орж WebSocket-оор бодит цагт хариулна",
          "Багш / сурагч / админ эрх, өрөөний амьдралын мөчлөг, шууд оноо тооцоолол; Vercel дээр deploy хийсэн",
          "UI-г Figma, v0.dev дээр зохиож shadcn/ui-аар хэрэгжүүлсэн"]),
        ("Ascend", "ШУТИС-ийн оюутны клубын вэбсайт", "2026.10 – одоо",
         "Next.js · TypeScript · Tailwind",
         ["Багшийн хүсэлтээр хийж буй 3 хэлтэй (MN / RU / EN) сайт: онлайн элсэлт, гишүүдийн профайл, админ хэсэг, мэдээ"]),
        ("ШУТИС Олон улсын судалгааны клубын вэбсайт", "", "2026.10 – одоо",
         "Next.js · TypeScript · 10 хүний оюутны баг",
         ["UI/UX дизайн (HTML прототип → Figma) болон full-stack Next.js архитектурын саналыг хариуцдаг"]),
    ],
    edu=[
        ("Шинжлэх Ухаан, Технологийн Их Сургууль (ШУТИС)", "Программ хангамжийн инженерчлэл, бакалавр — Мэдээлэл, холбооны технологийн сургууль", "2026 – 2029 (төлөвлөсөн)"),
        ("Pinecone Academy", "Full-stack Software Engineering хөтөлбөр, 10 сар, сертификаттай — JavaScript, React, Next.js, Node.js, MongoDB", "2025.06 – 2026.04"),
        ("2-р сургууль, Улаанбаатар", "Бүрэн дунд боловсрол", "2024"),
    ],
    skills=[
        ("Хэлүүд", "TypeScript, JavaScript, Python, C, C#"),
        ("Frontend", "Next.js, React, Tailwind CSS, shadcn/ui, HTML/CSS"),
        ("Backend", "Node.js, Express, REST API, Socket.IO, Prisma"),
        ("Өгөгдлийн сан", "MongoDB, PostgreSQL"),
        ("Хэрэгслүүд", "Git/GitHub, Vercel, Figma, Postman, Unity, Roblox Studio"),
    ],
    langs=[("Монгол", "Төрөлх"), ("Англи", "Дунд түвшин")],
    awards=[("1-р байр — PineQuest S3", "Pinecone Academy хакатон, 2025")],
)

CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body { font-family: "Inter", "DejaVu Sans", Arial, sans-serif; color: #1f2328; font-size: 10pt; line-height: 1.45; }
table.page { border-collapse: collapse; width: 210mm; height: 297mm; }
td { vertical-align: top; }
td.side { width: 66mm; background: #0d1117; color: #c9d1d9; padding: 15mm 7mm 12mm 9mm; height: 297mm; }
td.main { padding: 15mm 12mm 12mm 10mm; }
.side p.name { font-size: 25pt; font-weight: 700; letter-spacing: 1.5px; color: #ffffff; line-height: 1.1; margin: 0; }
.side p.title { color: #22c55e; font-size: 9pt; letter-spacing: 2px; text-transform: uppercase; margin: 6px 0 0; font-weight: 600; }
.side h3 { color: #22c55e; font-size: 8.3pt; letter-spacing: 2.2px; text-transform: uppercase; margin: 20px 0 7px; padding-bottom: 4px; border-bottom: 1px solid #30363d; }
.side p { margin: 0 0 5px; font-size: 8.8pt; color: #c9d1d9; word-wrap: break-word; }
.side .k { color: #8b949e; font-size: 7.8pt; text-transform: uppercase; letter-spacing: 1px; margin: 7px 0 1px; }
.side .v { color: #e6edf3; font-size: 8.8pt; margin: 0; }
.main h2 { font-size: 9pt; letter-spacing: 2.4px; text-transform: uppercase; color: #15803d; margin: 20px 0 9px; padding-bottom: 4px; border-bottom: 1.5px solid #0d1117; }
.main h2.first { margin-top: 0; }
.main p { margin: 0 0 6px; }
.proj { margin-bottom: 12px; }
.row { width: 100%; border-collapse: collapse; }
.row td { padding: 0; }
.when { text-align: right; color: #57606a; font-size: 8.6pt; white-space: nowrap; width: 32mm; }
.proj b { font-size: 10.2pt; color: #0d1117; }
.proj .sub { color: #57606a; font-size: 8.6pt; }
.proj .tech { color: #15803d; font-size: 8.4pt; margin: 1px 0 2px; }
ul { margin: 2px 0 0 13px; padding: 0; }
li { margin: 0 0 2.5px; }
.edu { margin-bottom: 8px; }
.edu b { color: #0d1117; }
.edu .sub { color: #57606a; font-size: 8.8pt; }
"""


def html(d):
    side = f"""
    <p class="name">{d['name']}</p>
    <p class="title">{d['title']}</p>
    <h3>{d['h_contact']}</h3>
    <p>{d['location']}</p>
    <p>+976 9898-7770</p>
    <p>subeegod@gmail.com</p>
    <p>github.com/JinreP</p>
    <p>subeedei.vercel.app</p>
    <p>linkedin.com/in/subeedei-dolgio-0b0725388</p>
    <h3>{d['h_skills']}</h3>
    {''.join(f'<p class="k">{k}</p><p class="v">{v}</p>' for k, v in d['skills'])}
    <h3>{d['h_langs']}</h3>
    {''.join(f'<p class="k">{k}</p><p class="v">{v}</p>' for k, v in d['langs'])}
    <h3>{d['h_awards']}</h3>
    {''.join(f'<p class="v"><b style="color:#fff">{a}</b></p><p>{b}</p>' for a, b in d['awards'])}
    """

    projects = ""
    for name, sub, when, tech, bullets in d["projects"]:
        subtxt = f' <span class="sub">— {sub}</span>' if sub else ""
        projects += f"""
        <div class="proj">
          <table class="row"><tr><td><b>{name}</b>{subtxt}</td><td class="when">{when}</td></tr></table>
          <div class="tech">{tech}</div>
          <ul>{''.join(f'<li>{b}</li>' for b in bullets)}</ul>
        </div>"""

    edu = ""
    for name, sub, when in d["edu"]:
        edu += f"""
        <div class="edu">
          <table class="row"><tr><td><b>{name}</b></td><td class="when">{when}</td></tr></table>
          <div class="sub">{sub}</div>
        </div>"""

    main = f"""
    <h2 class="first">{d['h_profile']}</h2>
    <p>{d['profile']}</p>
    <h2>{d['h_projects']}</h2>
    {projects}
    <h2>{d['h_edu']}</h2>
    {edu}
    """

    return f"""<!doctype html><html lang="{d['lang']}"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><table class="page"><tr><td class="side">{side}</td><td class="main">{main}</td></tr></table></body></html>"""


def build(d, out_name):
    src = TMP / f"cv_{d['lang']}.html"
    src.write_text(html(d), encoding="utf-8")
    HTML(string=html(d), base_url=str(TMP)).write_pdf(str(OUT / out_name))
    print("built", OUT / out_name)


if __name__ == "__main__":
    build(EN, "Subeedei_CV_EN.pdf")
    build(MN, "Subeedei_CV_MN.pdf")
