from flask import Flask, request, render_template
from lexer import lexer  # Importar el analizador léxico
from parser import parser  # Importar el analizador sintáctico

app = Flask(__name__)

# ---------------------------
#  FLASK
# ---------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            text = file.read().decode('utf-8')
        else:
            text = request.form.get('code', '')

        lexer.input(text)
        token_results = []
        for tok in lexer:
            token_results.append({
                'line': tok.lineno,
                'type': tok.value,
                'value': tok.value,
                'correct_structure': 'X' if tok.type == 'FOR' else '',
                'incorrect_structure': 'X' if tok.type != 'FOR' else ''
            })

        try:
            parse_result = parser.parse(text)
            parse_status = "Éxito en el parseo"
        except Exception as e:
            parse_status = f"Error en el parseo: {str(e)}"

        return render_template('index.html', results=token_results, parse_status=parse_status)

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
