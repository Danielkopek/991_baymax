
from datetime import datetime

def empathetic_reply(user_text: str, triage_summary: str|None=None) -> str:
    """
    Respon empatik berbasis aturan sederhana + konteks triage opsional.
    """
    text = user_text.lower()

    # intent sederhana
    if any(k in text for k in ["pusing", "sakit kepala", "nyeri kepala"]):
        core = "Kedengarannya kamu mengalami pusing."
        tips = "Coba minum air, istirahat 10–15 menit, dan kurangi layar sejenak."
    elif any(k in text for k in ["batuk", "pilek", "flu"]):
        core = "Sepertinya kamu sedang tidak enak badan."
        tips = "Jaga hidrasi, istirahat cukup, dan perhatikan suhu tubuh."
    elif any(k in text for k in ["cemas", "anx", "anxiety", "gelisah"]):
        core = "Aku mendengar kamu sedang cemas."
        tips = "Ambil 3 tarikan napas pelan; fokus buang napas lebih panjang."
    else:
        core = "Aku mengerti. Terima kasih sudah bercerita."
        tips = "Aku di sini untuk menemani dan membantumu mengambil langkah kecil."

    tri = f"\nCatatan cek cepat: {triage_summary}" if triage_summary else ""
    now = datetime.now().strftime("%H:%M")
    return (
        f"[{now}] Aku di sini untuk membantumu. {core} {tips}{tri}\n"
        "Jika gejala memburuk atau kamu merasa tidak aman, mohon hubungi tenaga medis."
    )
