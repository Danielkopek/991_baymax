# llm_client.py
import os
from openai import OpenAI

# 1) Baca API key dari environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2) Pilih model terbaru; bisa override via env var OPENAI_MODEL
MODEL = os.getenv("OPENAI_MODEL", "gpt-5")  # coba gpt-5; jika belum ada akses, set ke gpt-5-mini / gpt-5-nano

SYSTEM_PROMPT = (
    "Kamu adalah Baymax-mini: asisten empatik, tenang, dan aman. "
    "Berikan dukungan singkat dengan langkah praktis. Hindari klaim medis. "
    "Jika gejala berat/berbahaya → anjurkan hubungi tenaga medis."
)

def llm_reply(user_text: str, triage_summary: str | None = None) -> str:
    parts = []
    if triage_summary:
        parts.append(f"[Triage] {triage_summary}")
    parts.append(f"[User] {user_text}")

    # Responses API — simpel: model + instructions + input
    resp = client.responses.create(
        model=MODEL,
        instructions=SYSTEM_PROMPT,
        input="\n".join(parts),
    )
    return resp.output_text.strip()
