# Gerar o APK sem Android Studio (pelo GitHub)

1. Crie uma conta e um repositório novo em github.com.
2. Envie TODO o conteúdo desta pasta (inclusive `.github/workflows/build-apk.yml`) para o repositório.
3. Abra a aba **Actions**, escolha **Gerar APK** e toque em **Run workflow**.
4. Quando terminar (3 a 6 minutos), abra a execução e baixe **client-music-apk** em Artifacts.
5. Dentro do arquivo baixado está o `app-debug.apk`. Instale no Android permitindo "fontes desconhecidas".

Observação: o GitHub entrega os artefatos dentro de um .zip; o APK fica dentro dele.
