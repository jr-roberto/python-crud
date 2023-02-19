from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Funcionario:
    def __init__(self, nome, cargo, departamento) -> None:
        self.nome = nome
        self.cargo = cargo
        self.departamento = departamento

base_funcionarios = []

@app.route('/')
@app.route('/lista_funcionraios')
def index():
    return render_template( 'func/lista_funcionarios.html' , base_funcionarios=base_funcionarios )

@app.route('/func_novo', methods=['POST','GET'])
def novo_funcionario():

    if request.method == 'POST':
        dados_form = request.form.to_dict()

        base_funcionarios.append(
            Funcionario(
            nome=dados_form['func_nome'],
            cargo=dados_form['func_cargo'],
            departamento=dados_form['func_departamento']
            )
        )

        return redirect("/")

    return render_template('func/novo.html')

@app.route('/detalhes_func')
def detalhes_funcionario():
    return render_template('func/detalhes.html')

if __name__=='__main__':
    app.run(debug=True)
