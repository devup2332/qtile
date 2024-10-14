colors = {
    "bg": "#1a1b26",
    "subbg": "#282a3b",
    "fg": "#bec6ed",
    "blue": "#1563bd",
    "yellow": "#e0af68",
    "green": "#98be65",
    "pink": "#e2a8e6",
    "inactive": "#434459"
}

wallpaper_path = "~/.config/qtile/assets/wallpaper_main.png"

commands = [
    "pidof -q picom || { picom --config ~/.config/qtile/picom/picom.conf &}",
    "pidof -q xfce4-clipman || { xfce4-clipman & }",
    "pidof -q xset || { xset r rate 200 25 & }",
    "pidof -q dunst || { dunst -config ~/.config/qtile/dunstrc & }",
    "pidof -q sxhkd || { sxhkd -c ~/.config/qtile/sxhkdrc & }",
    f'feh --bg-fill {wallpaper_path} &',
    "setxkbmap us &",
]
