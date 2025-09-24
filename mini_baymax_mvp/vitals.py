 from dataclasses import dataclass

@dataclass
class Vitals:
    heart_rate_bpm: float | None = None
    spo2_percent: float | None = None
    body_temp_c: float | None = None
    notes: str | None = None

def load_vitals_from_dict(d: dict) -> Vitals:
    return Vitals(
        heart_rate_bpm=d.get("heart_rate_bpm"),
        spo2_percent=d.get("spo2_percent"),
        body_temp_c=d.get("body_temp_c"),
        notes=d.get("notes"),
    )

def simple_triage(v: Vitals) -> tuple[str, str]:
    """
    Mengembalikan (level, ringkasan).
    Level: GREEN (aman), YELLOW (waspada), RED (butuh perhatian).
    """
    flags = []
    level = "GREEN"

    if v.body_temp_c is not None:
        if v.body_temp_c >= 38.0:
            flags.append("demam")
            level = "YELLOW"
        elif v.body_temp_c <= 35.0:
            flags.append("hipotermia?")
            level = "RED"

    if v.heart_rate_bpm is not None:
        if v.heart_rate_bpm > 120:
            flags.append("denyut tinggi")
            level = "YELLOW"
        elif v.heart_rate_bpm < 45:
            flags.append("denyut rendah")
            level = "YELLOW"

    if v.spo2_percent is not None:
        if v.spo2_percent < 92:
            flags.append("SpO2 rendah")
            level = "RED"

    if not flags:
        summary = "Tanda vital dalam kisaran wajar."
    else:
        summary = " / ".join(flags)

    return level, summary
