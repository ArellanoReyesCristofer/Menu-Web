from flask import Flask, render_template
from markupsafe import Markup

menu = {
    "Inicio": {},
    "Oferta Educativa": {
        "Licenciaturas e Ingenierías": {
            "Ing. Sistemas Computacionales": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Ing. Electrónica": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Ing. Industrial": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Ing. Química": {
                "Plan de Estudios": {},
                "Programa": {}
            }
        },
        "Posgrado": {}
    },
    "Contacto": {}
}

app = Flask(__name__)

def render_menu(menu_dict, level=0):
    """Función recursiva para renderizar el menú"""
    html = ""
    for key, value in menu_dict.items():
        if value:  # Si tiene submenús
            if level == 0:  # Nivel principal
                html += f'<li class="nav-item dropdown">'
                html += f'<a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">'
                html += f'{key}</a>'
                html += f'<ul class="dropdown-menu">'
                html += render_menu(value, level + 1)
                html += f'</ul></li>'
            else:  # Submenús anidados
                html += f'<li class="dropdown-submenu">'
                html += f'<a class="dropdown-item dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">'
                html += f'{key}</a>'
                html += f'<ul class="dropdown-menu">'
                html += render_menu(value, level + 1)
                html += f'</ul></li>'
        else:  # Si es un enlace simple
            if level == 0:
                html += f'<li class="nav-item">'
                html += f'<a class="nav-link" href="#">{key}</a></li>'
            else:
                html += f'<li><a class="dropdown-item" href="#">{key}</a></li>'
    return html

@app.template_filter('render_menu')
def render_menu_filter(menu_dict):
    """Filtro de template para renderizar el menú"""
    return Markup(render_menu(menu_dict))

@app.route('/')
def index():
     return render_template("menu.html", menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
