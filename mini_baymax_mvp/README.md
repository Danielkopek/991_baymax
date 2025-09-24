
# Mini Baymax — Software MVP (No IoT)

Target 2 hari:
1) **Triage kesehatan sederhana** dari data vital (simulasi).
2) **Chatbot empatik** berbasis rule + prompt sederhana.
3) **Output suara** (opsional, TTS lokal).

## Struktur
- `main.py` — CLI loop (chat + triage).
- `vitals.py` — parser & triage sederhana.
- `dialogue.py` — template respon empatik.
- `sample_vitals.json` — data dummy untuk simulasi.
- `prompts/empathetic_style.txt` — gaya bahasa Baymax-tenang.
- `requirements.txt` — dependency dasar.

## Cara jalan
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

## Catatan
- Ini versi **tanpa** LLM & tanpa sensor; fokus pada arsitektur & UX.
- Upgrade berikutnya: ganti rule-based dengan model ringan atau tambahkan STT (speech-to-text).
