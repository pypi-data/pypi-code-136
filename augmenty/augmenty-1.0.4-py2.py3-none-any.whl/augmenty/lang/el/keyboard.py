from ...util import registry


@registry.keyboards("el.v1")
def create_qwerty_el():
    qwerty = {
        "default": [
            ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="],
            [";", "ς", "ε", "ρ", "τ", "υ", "θ", "ι", "ο", "π", "[", "]"],
            ["α", "σ", "δ", "φ", "γ", "η", "ξ", "κ", "λ", "΄", "'", "\\"],
            ["`", "ζ", "χ", "ψ", "ω", "β", "ν", "μ", ",", ".", "/"],
        ],
        "shift": [
            ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"],
            [":", "΅", "Ε", "Ρ", "Τ", "Υ", "Θ", "Ι", "Ο", "Π", "{", "}"],
            ["Α", "Σ", "Δ", "Φ", "Γ", "Η", "Ξ", "Κ", "Λ", "¨", '"', "|"],
            ["~", "Ζ", "Χ", "Ψ", "Ω", "Β", "Ν", "Μ", "<", ">", "?"],
        ],
    }
    return qwerty
