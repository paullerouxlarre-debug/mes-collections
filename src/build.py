"""Construit le site à partir de src/app.html.

- index.html : version autonome servie par GitHub Pages (données dans le navigateur).
- dist/mes-collections.html : la même page, telle que publiée dans Claude (Artifact).

Lancer depuis la racine du dépôt : python3 src/build.py
"""
import pathlib, re, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = (ROOT / "src" / "app.html").read_text(encoding="utf-8")

title = re.search(r"<title>(.*?)</title>", src).group(1)
head = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="theme-color" content="#1B6FB8">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Collections">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" href="icon-180.png">
<link rel="manifest" href="manifest.webmanifest">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
"""
(ROOT / "index.html").write_text(head + src + "\n</body>\n</html>\n", encoding="utf-8")
(ROOT / "dist").mkdir(exist_ok=True)
shutil.copyfile(ROOT / "src" / "app.html", ROOT / "dist" / "mes-collections.html")

# Vérifie la syntaxe du script principal si node est disponible.
script = re.findall(r"<script>(.*?)</script>", src, re.S)[-1]
tmp = ROOT / "dist" / ".check.js"
tmp.write_text(script, encoding="utf-8")
try:
    r = subprocess.run(["node", "--check", str(tmp)], capture_output=True, text=True)
    if r.returncode:
        print(r.stderr); sys.exit(1)
except FileNotFoundError:
    pass
finally:
    tmp.unlink(missing_ok=True)
print("index.html et dist/mes-collections.html à jour")
