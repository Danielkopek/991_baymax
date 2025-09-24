
import json, sys
from llm_client import llm_reply
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import pyttsx3


from vitals import load_vitals_from_dict, simple_triage
from dialogue import empathetic_reply

console = Console()

def tts_say(text: str):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        console.print(f"[yellow]TTS tidak aktif: {e}[/]")

def load_sample():
    with open("sample_vitals.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    console.rule("[bold cyan]Mini Baymax — Software MVP")
    console.print("Mode: simulasi tanpa sensor. Ketik 'cek' untuk triage, atau ketik pesan untuk curhat. Ketik 'keluar' untuk selesai.\n")

    sample = load_sample()
    v = load_vitals_from_dict(sample)

    while True:
        user = Prompt.ask("[bold]Kamu[/]")
        if user.strip().lower() in {"keluar", "exit", "quit"}:
            console.print("[green]Sampai jumpa. Jaga diri baik-baik.[/]")
            break
        elif user.strip().lower() in {"cek", "triage"}:
            level, summary = simple_triage(v)
            msg = f"Level: {level} — {summary}"
            console.print(Panel(msg, title="Cek Cepat", border_style="cyan"))
            reply = llm_reply("Tolong tanggapi hasil cek cepat saya.", triage_summary=msg)
        else:
            reply = llm_reply(user)

        console.print(Panel(reply, title="Mini Baymax", border_style="magenta"))
        # opsional: ucapkan kalimat pertama agar terdengar
        tts_say(reply.split("\n")[0])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
