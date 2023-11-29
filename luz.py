import subprocess

def set_brightness(brightness):
    # Valores típicos para brightness: 0.1 (mínimo) a 1.0 (máximo)
    brightness = min(1.0, max(0.1, brightness))

    # Obtém a lista de dispositivos de exibição
    display_list = subprocess.check_output(["xrandr"]).decode("utf-8").splitlines()

    # Procura o nome do dispositivo de exibição (normalmente eDP-1, VGA-1, etc.)
    display_name = None
    for line in display_list:
        if " connected" in line:
            display_name = line.split()[0]
            break

    if display_name:
        # Ajusta o brilho usando xrandr
        subprocess.run(["xrandr", "--output", display_name, "--brightness", str(brightness)])
    else:
        print("Não foi possível encontrar o dispositivo de exibição.")

# Ajusta o brilho para 80%
set_brightness(0.9)
