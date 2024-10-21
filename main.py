import flet as ft

def main(page: ft.Page):
    # Establecer tamaño de pantalla
    page.window_width = 800
    page.window_height = 800

    page.bgcolor = "black"
    page.title = "Mictlan"
    page.fgcolor = "gray"
    
    # Inicialización de audio
    Intro = ft.Audio(src="Intro.mp3", volume=10, balance=0)
    PrimerNivel = ft.Audio(src="Primer_Nivel.mp3", volume=10, balance=0)
    SegundoNivel = ft.Audio(src="Segundo_Nivel.mp3", volume=10, balance=0)
    TercerNivel = ft.Audio(src="Tercer_Nivel.mp3", volume=10, balance=0)
    CuartoNivel = ft.Audio(src="Cuarto_Nivel.mp3", volume=10, balance=0)
    QuintoNivel = ft.Audio(src="Quinto_Nivel.mp3", volume=10, balance=0)
    SextoNivel = ft.Audio(src="Sexto_Nivel.mp3", volume=10, balance=0)
    SeptimoNivel = ft.Audio(src="Septimo_Nivel.mp3", volume=10, balance=0)
    OctavoNivel = ft.Audio(src="Octavo_Nivel.mp3", volume=10, balance=0)
    NovenoNivel = ft.Audio(src="Noveno_Nivel.mp3", volume=10, balance=0)

    # Lista de todos los audios
    audios = [Intro, PrimerNivel, SegundoNivel, TercerNivel, CuartoNivel,
              QuintoNivel, SextoNivel, SeptimoNivel, OctavoNivel, NovenoNivel]

    # Agregar audio a la superposición
    page.overlay.extend(audios)

    # Función para pausar todos los audios
    def pause_all():
        for audio in audios:
            audio.pause()

    # Funciones para reproducir audio
    def play_intro(e):
        pause_all()
        Intro.play()

    def play_nivel1(e):
        pause_all()
        PrimerNivel.play()

    def play_nivel2(e):
        pause_all()
        SegundoNivel.play()

    def play_nivel3(e):
        pause_all()
        TercerNivel.play()

    def play_nivel4(e):
        pause_all()
        CuartoNivel.play()

    def play_nivel5(e):
        pause_all()
        QuintoNivel.play()

    def play_nivel6(e):
        pause_all()
        SextoNivel.play()

    def play_nivel7(e):
        pause_all()
        SeptimoNivel.play()

    def play_nivel8(e):
        pause_all()
        OctavoNivel.play()

    def play_nivel9(e):
        pause_all()
        NovenoNivel.play()

    # Se crea la interfaz
    btnIntro = ft.FilledButton(text="Escucha el Intro", on_click=play_intro)
    
    # Crear controles para cada nivel
    controls = [
        (btnNivel1 := ft.FilledButton(text="Primer Nivel", on_click=play_nivel1), ft.Image(src="Primer-Nivel.jpeg", width=150, height=150)),
        (btnNivel2 := ft.FilledButton(text="Segundo Nivel", on_click=play_nivel2), ft.Image(src="Segundo-Nivel.jpeg", width=150, height=150)),
        (btnNivel3 := ft.FilledButton(text="Tercer Nivel", on_click=play_nivel3), ft.Image(src="Tercer-Nivel.png", width=150, height=150)),
        (btnNivel4 := ft.FilledButton(text="Cuarto Nivel", on_click=play_nivel4), ft.Image(src="Cuarto-Nivel.jpeg", width=150, height=150)),
        (btnNivel5 := ft.FilledButton(text="Quinto Nivel", on_click=play_nivel5), ft.Image(src="Quinto-Nivel.jpeg", width=150, height=150)),
        (btnNivel6 := ft.FilledButton(text="Sexto Nivel", on_click=play_nivel6), ft.Image(src="Sexto-Nivel.jpeg", width=150, height=150)),
        (btnNivel7 := ft.FilledButton(text="Septimo Nivel", on_click=play_nivel7), ft.Image(src="Septimo-Nivel.jpeg", width=150, height=150)),
        (btnNivel8 := ft.FilledButton(text="Octavo Nivel", on_click=play_nivel8), ft.Image(src="Octavo-Nivel.png", width=150, height=150)),
        (btnNivel9 := ft.FilledButton(text="Noveno Nivel", on_click=play_nivel9), ft.Image(src="Noveno-Nivel.jpeg", width=150, height=150)),
    ]

    # Crear filas de 3 controles cada una
    rows = []
    for i in range(0, len(controls), 3):
        row_controls = controls[i:i + 3]
        row = ft.Row(alignment="CENTER", controls=[control for pair in row_controls for control in pair])
        rows.append(row)

    # Agregar las filas al page
    page.add(
        ft.Row(
            alignment="start",
            controls=[btnIntro]
        ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=rows
        )
    )

ft.app(main)
