"""Copy offline web assets and package Android sources; does not compile an APK."""
from pathlib import Path
import re
import shutil
import zipfile

root = Path(__file__).resolve().parent.parent
android = root / 'android'
assets = android / 'app/src/main/assets'
assets.mkdir(parents=True, exist_ok=True)
html = (root / 'index.html').read_text()
html = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com/[^>]+>\n', '', html)
html = re.sub(r'      <div class="settings-card" id="androidDownload">.*?</div>\n', '', html, flags=re.S)
html = re.sub(r"<script>if\('serviceWorker' in navigator\).*?</script>", '', html)
html = html.replace('Controles na tela de bloqueio', 'Reprodução local no aplicativo')
(assets / 'index.html').write_text(html)
for name in ('player.css', 'manifest.json', 'icon-192.png', 'icon-512.png'):
    shutil.copyfile(root / name, assets / name)
shutil.copyfile(root / 'icon-192.png', android / 'app/src/main/res/drawable/app_icon.png')
output = root / 'downloads/client-music-android.zip'
output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(android.rglob('*')):
        relative = path.relative_to(android)
        if any(part in ('build', '.gradle', '.idea') for part in relative.parts):
            continue
        if path.is_file() and path.name != 'local.properties':
            archive.write(path, Path('android') / relative)
print('Pacote de fontes Android atualizado: downloads/client-music-android.zip')
