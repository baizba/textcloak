# TextCloak.ai

A privacy-first text anonymizer landing/MVP page. Paste sensitive text, click **Anonymize**, and get a cleaned version — entirely in the browser with no accounts, no storage, and no server-side memory.

## Tech stack

- **Angular 22** — standalone components, `FormsModule` for two-way binding
- **SCSS** — plain component-scoped styles, no UI framework
- **Netlify** — static hosting with SPA redirect fallback

## Run locally – frontend

```bash
npm install
npm start
```

Open [http://localhost:4200](http://localhost:4200)

## Build

```bash
npm run build
```

Output lands in `dist/textcloak/browser/` — that's the folder Netlify serves (configured in `netlify.toml`).
