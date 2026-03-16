import flet as ft

def main(page: ft.Page):
    page.title = "Tienda Unidad 2"
    page.scroll = "adaptive"
    
    # Lista de productos
    productos = [
        {"n": "Laptop Gamer", "p": 1200, "i": "laptop.jpg"},
        {"n": "Celular Pro", "p": 800, "i": "smartphone.jpg"},
        {"n": "Audifonos Bass", "p": 200, "i": "audífonos.jpg"},
        {"n": "Monitor 4K", "p": 500, "i": "monitor.jpg"},
        {"n": "Teclado RGB", "p": 100, "i": "teclado.jpg"}
    ]
    
    catalogo = ft.Row(wrap=True, spacing=20)
    
    for p in productos:
        # Todo esto tiene 8 espacios de sangría (está dentro del for)
        tarjeta = ft.Container(
            content=ft.Column([
                ft.Image(src=p["i"], width=150, height=150),
                ft.Text(p["n"], weight="bold"),
                ft.Text(f"${p['p']}"),
                ft.ElevatedButton("Comprar", icon="ADD")
            ], horizontal_alignment="center"),
            bgcolor="white",
            padding=10,
            border_radius=10,
            width=170
        )
        # ESTA LÍNEA DEBE ESTAR ALINEADA CON 'tarjeta'
        catalogo.controls.append(tarjeta)
    
    # page.add vuelve al nivel del for
    page.add(ft.Text("Catálogo", size=30), catalogo)

# Esta línea va pegada al borde izquierdo
ft.app(target=main)