* { box-sizing: border-box; }

:root {
  --bg-dark: #3d2b1f;
  --bg-mid: #6a4a3a;
  --bg-soft: #d7b69d;
  --card-bg: #fdf5ef;
  --card-strong: #efe0d1;
  --text-main: #2d1f1a;
  --text-soft: #6a4d42;
  --primary: #8f5a3c;
  --primary-dark: #6e432e;
  --border: #d6b7a0;
  --shadow: rgba(61, 43, 31, 0.18);
}

body {
  margin: 0; min-height: 100vh; display: grid; place-items: center;
  padding: 28px; background: linear-gradient(135deg, var(--bg-dark), var(--bg-mid), var(--bg-soft));
  color: var(--text-main); font-family: Arial, Helvetica, sans-serif;
  animation: fadeInPage 0.8s ease-out;
}

.container {
  width: 100%; max-width: 720px; padding: 38px; background: rgba(253, 245, 239, 0.97);
  border: 1px solid var(--border); border-radius: 18px;
  box-shadow: 0 18px 55px var(--shadow);
  animation: riseIn 0.8s ease-out;
}

.eyebrow { color: var(--primary-dark); font-size: 12px; font-weight: 700; letter-spacing: 2px; }
h1 { margin: 12px 0 8px; font-size: clamp(28px, 5vw, 40px); }
.subtitle { margin: 0 0 28px; color: var(--text-soft); line-height: 1.6; }
.image-row {
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px; margin: 0 0 24px;
}
.image-row img {
  width: 100%; height: 120px; object-fit: cover; border-radius: 12px;
  border: 2px solid rgba(143, 90, 60, 0.18); box-shadow: 0 8px 18px rgba(61, 43, 31, 0.08);
  transition: transform 0.25s ease;
}
.image-row img:hover { transform: translateY(-2px) scale(1.01); }
label { display: block; margin-bottom: 10px; font-weight: 700; }
.sample-bar {
  display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 14px;
}
.sample-button {
  margin: 0; padding: 9px 12px; border: 1px solid #d7b7a3; border-radius: 999px;
  background: #f5e2d0; color: var(--primary-dark); font-size: 12px; font-weight: 700;
  cursor: pointer; transition: transform 0.2s ease, background 0.2s ease;
}
.sample-button:hover {
  background: #f0d6bf; transform: translateY(-1px);
}
textarea {
  width: 100%; min-height: 190px; resize: vertical; padding: 15px;
  border: 1px solid var(--border); border-radius: 10px; font: inherit; line-height: 1.5;
  background: #fffdfb; color: var(--text-main);
}
textarea:focus { outline: 3px solid #efd7c3; border-color: var(--primary); }
button[type="submit"] {
  margin-top: 16px; padding: 13px 22px; border: 0; border-radius: 9px;
  background: linear-gradient(135deg, var(--primary), var(--primary-dark)); color: white; font-size: 15px; font-weight: 700; cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
button[type="submit"]:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 18px rgba(111, 67, 46, 0.25);
}
.result { margin-top: 24px; padding: 20px; border-radius: 12px; }
.result h2 { margin: 6px 0; font-size: 26px; }
.result p { margin: 0; }
.result-label { font-size: 11px; font-weight: 700; letter-spacing: 1.5px; }
.keyword-panel, .history-panel {
  margin-top: 24px; padding: 18px 20px; background: #f7efe8; border: 1px solid var(--border); border-radius: 12px;
}
.keyword-panel h3, .history-panel h3 { margin: 0 0 12px; font-size: 16px; }
.keyword-list { display: flex; flex-wrap: wrap; gap: 8px; }
.keyword-chip {
  display: inline-flex; padding: 6px 10px; border-radius: 999px; background: #f9d9a8;
  color: #7b451d; font-size: 12px; font-weight: 700;
}
.spam { color: #991b1b; background: #fef2f2; border: 1px solid #fecaca; }
.ham { color: #166534; background: #f0fdf4; border: 1px solid #bbf7d0; }
.error { margin-top: 18px; color: #b42318; }
.history-header {
  display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 8px;
}
.clear-link { color: var(--primary-dark); text-decoration: none; font-size: 12px; font-weight: 700; }
.history-list {
  list-style: none; margin: 0; padding: 0; display: grid; gap: 12px;
}
.history-list li {
  border: 1px solid var(--border); border-radius: 10px; background: rgba(255,255,255,0.5); padding: 12px;
}
.history-list p { margin: 8px 0; color: #334155; line-height: 1.5; }
.history-list small { color: #64748b; }
.history-label {
  display: inline-block; padding: 4px 8px; border-radius: 999px; font-size: 10px; font-weight: 700; letter-spacing: 0.8px;
}
.note { margin: 24px 0 0; color: #6f4d3c; font-size: 12px; line-height: 1.5; }

@keyframes fadeInPage {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes riseIn {
  from {
    opacity: 0;
    transform: translateY(18px) scale(0.98);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@media (max-width: 520px) {
  .container { padding: 24px; }
  body { padding: 14px; }
  .sample-bar { flex-direction: column; }
}

