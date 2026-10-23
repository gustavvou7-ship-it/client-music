# Client Music para Android

Este pacote contém o projeto Android completo, com o player incluído para funcionar sem conexão. Não é um APK compilado.

## Gerar o APK

1. Instale o Android Studio Meerkat ou mais recente em um computador.
2. Extraia o ZIP e abra a pasta `android` no Android Studio.
3. Nas configurações do Gradle, use JDK 17 e Gradle 8.11.1 (distribuição local). O projeto usa Android Gradle Plugin 8.9.2. Se solicitado, instale Android SDK 35. O primeiro sincronismo precisa de internet.
4. Aguarde o sincronismo e use **Build → Generate App Bundles or APKs → Generate APKs** (em algumas versões, **Build APK(s)**).
5. O APK de teste fica em `app/build/outputs/apk/debug/app-debug.apk`. Transfira-o para o Android, abra o arquivo e permita a instalação pela origem usada.

Para distribuir uma versão definitiva, use **Generate Signed App Bundle / APK → APK**, crie sua chave no seu computador e guarde-a em segurança. Atualizações precisam usar a mesma chave e um `versionCode` maior. O projeto não inclui chaves de assinatura.

## Uso e limites

Compatível com Android 8 ou superior. Importe músicas pelo botão Importar áudio; é possível escolher vários arquivos. O player usa o armazenamento privado do Android WebView. A biblioteca do navegador não é transferida automaticamente: importe os arquivos novamente no aplicativo. Desinstalar ou limpar os dados do app apaga essa biblioteca.

Os arquivos da interface estão em `app/src/main/assets`. Não há permissão de internet nem acesso amplo ao armazenamento: o seletor do Android concede acesso somente aos arquivos escolhidos. Formatos de áudio dependem dos codecs do aparelho.

Esta versão usa WebView e não implementa um serviço Android de reprodução em primeiro plano. A reprodução em segundo plano ou com tela bloqueada depende do sistema e pode ser interrompida. Não foi compilada nem testada em um dispositivo Android neste ambiente.

Para atualizar os arquivos web a partir do repositório do site, execute `python3 scripts/package-android.py` na raiz antes de baixar o novo ZIP.
