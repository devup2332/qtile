from libqtile import bar, widget
from libqtile.config import Screen
from constants import colors

screen_1 = Screen(
    top=bar.Bar(
        [
            widget.TextBox(
                text='  󰣇   ',
                fontsize=25,
                foreground=colors['blue'],
                background=colors["bg"]
            ),
            widget.Spacer(
                background=colors["bg"]
            ),
            widget.GroupBox(
                padding_x=10,
                fontsize=14,
                background=colors["bg"],
                foreground=colors["blue"],
                inactive=colors["inactive"],
                active=colors["fg"],
                highlight_method="line",
                other_current_screen_border=colors["yellow"],
                this_screen_border=colors["blue"],
                highlight_color=colors["subbg"],
            ),
            widget.Spacer(
                background=colors["bg"]
            ),
            widget.Systray(
                background=colors["bg"],
                icon_size=20
            ),
            widget.TextBox(
                text='   ',
                background=colors['bg'],
            ),
            widget.TextBox(
                text='   ',
                foreground=colors['green'],
                background=colors['bg'],
                fontsize=16
            ),
            widget.Volume(
                foreground=colors['fg'],
                background=colors['bg'],
                padding=5
            ),
            widget.TextBox(
                text='    ',
                foreground=colors['pink'],
                background=colors['bg'],
                fontsize=16
            ),
            widget.Net(
                background=colors['bg'],
                format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}'

            ),
            widget.TextBox(
                text='    ',
                foreground=colors['yellow'],
                background=colors['bg'],
                fontsize=16
            ),
            widget.Clock(format="%Y-%m-%d %a %I:%M %p",
                         background=colors['bg'], foreground=colors['fg']),
            widget.TextBox(
                text='             ',
                background=colors['bg'],
            ),
        ],
        40,
        margin=[20, 15, 0, 15],
    ),
)
