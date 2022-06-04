// ---------- INICIALIZAÇÃO DO FIREBASE ----------

var firebaseConfig = {
    apiKey: "AIzaSyDVyPsRvmfFwH3hASMeqLrpMElyeP48RRw",
    authDomain: "projete-2022.firebaseapp.com",
    databaseURL: "https://projete-2022-default-rtdb.firebaseio.com",
    projectId: "projete-2022",
    storageBucket: "projete-2022.appspot.com",
    messagingSenderId: "392429305078",
    appId: "1:392429305078:web:31e7a9605638bbc20380d7",
    measurementId: "G-31C7LKYKWP"
  };

firebase.initializeApp(firebaseConfig)

db = firebase.database()

// ----------- RELATÓRIOS -----------

function BaixarImagensFunc(){
    nome_func = document.getElementById('nome').value
    data = document.getElementById('data').value

    img_file_name = nome_func+data
    console.log(img_file_name)
}

function relatorio_diario(){
    document.getElementById("texto_relatorio").innerHTML = "Digite ou selecione a data que deseja ver o relatório: "
    document.getElementById("data_relatorio").type = "date"
    var x = document.getElementById("divisao_mes");
    if (x.style.display === "block") {
        console.log("botoes visiveis")
        x.style.display = "none";
    } 
}
function relatorio_mensal(){
    document.getElementById("data_relatorio").type = "hidden"
    document.getElementById("texto_relatorio").innerHTML = "Selecione o mês que deseja ver o relatório: "
    var x = document.getElementById("divisao_mes");
    if (x.style.display === "none") {
        x.style.display = "block";
    }
}
function mostra_oculta(){

    var x = document.getElementById("myDIV");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }

}
function janeiro(){
    console.log("janeiro");

}

function fevereiro(){
    console.log("fevereiro");

}

function marco(){
    console.log("marco");

}

function abril(){
    console.log("abril");

}

function maio(){
    console.log("maio");

}

function junho(){
    console.log("junho");

}

function julho(){
    console.log("julho");

}

function agosto(){
    console.log("agosto");

}

function setembro(){
    console.log("setembro");

}

function outubro(){
    console.log("outubro");

}

function novembro(){
    console.log("novembro");

}

function dezembro(){
    console.log("dezembro");
}

// ----------- CADASTRO DAS EPI'S -----------
var usar_capacete = false, usar_luvas = false, usar_botas = false, usar_colete = false, usar_PA = false, usar_oculos = false;
var cadastro_concluido = false, resElement, i, empresa;

function ReceberNomeSetor(){
    empresa = localStorage.getItem('nome')
    NomeSetor = document.getElementById('input_nome_setor').value;
    return NomeSetor;
}

function CadastrarCapacete(){
    cor_botao = document.getElementById("botao_capacete");
    cor_botao.style.backgroundColor = "green";
    usar_capacete = true;

}
function CadastrarLuva(){
    
    cor_botao = document.getElementById("botao_luvas");
    cor_botao.style.backgroundColor = "green";
    usar_luvas = true;

}
function CadastrarBotas(){
   
    cor_botao = document.getElementById("botao_botas");
    cor_botao.style.backgroundColor = "green";
    usar_botas = true;

}
function CadastrarPA(){
   
    cor_botao = document.getElementById("botao_pa");
    cor_botao.style.backgroundColor = "green";
    usar_PA = true;

}
function CadastrarOculos(){
    
    cor_botao = document.getElementById("botao_oculos");
    cor_botao.style.backgroundColor = "green";
    usar_oculos = true;

}
function CadastrarColete(){
    
    cor_botao = document.getElementById("botao_colete");
    cor_botao.style.backgroundColor = "green";
    usar_colete = true;

}

function Concluir(){
    nome_setor = ReceberNomeSetor()
    local_cadastro_setor = empresa + '/Setores'

    try{
        db.ref(local_cadastro_setor).push({
            Setor: nome_setor
        })
    }
    catch(error){
        alert('Problema')
    }
    if (usar_capacete != true){
        cor_botao = document.getElementById("botao_capacete");
        cor_botao.style.backgroundColor = "red";
    }
    if (usar_luvas != true){
        cor_botao = document.getElementById("botao_luvas");
        cor_botao.style.backgroundColor = "red";

    }
    if (usar_PA != true){
        cor_botao = document.getElementById("botao_pa");
        cor_botao.style.backgroundColor = "red";

    }
    if (usar_oculos != true){
        cor_botao = document.getElementById("botao_oculos");
        cor_botao.style.backgroundColor = "red";

    }
    if (usar_colete != true){
        cor_botao = document.getElementById("botao_colete");
        cor_botao.style.backgroundColor = "red";

    }
    if (usar_botas != true){
        cor_botao = document.getElementById("botao_botas");
        cor_botao.style.backgroundColor = "red";

    }
    nome_setor = empresa+'/setores/'+nome_setor
    try{
        db.ref(nome_setor).set({
            epis: {capacete: usar_capacete, 
                   luvas: usar_luvas, 
                   botas: usar_botas, 
                   colete: usar_colete, 
                   oculos: usar_oculos, 
                   pa: usar_PA}
        })
    }
    catch(error){
        alert('Problema ao salvar as variáveis, recarregue a página e tente novamente!')
    }
    cadastro_concluido = true;
    
}

function CadastrarOutroSetor(){
    if(cadastro_concluido == true){
        location.reload()
    }
    else{
        alert('Conclua o cadastro desse setor primeiro clicando no botão concluido!')
    }
}

function CadastrarEpis(){
    console.log("função acessada");
    var cadastrar = document.getElementById("div_epi");

    if (cadastrar.style.display == "none") {
        cadastrar.style.display = "block";
    }

}
// ----------- CADASTRO DOS FUNCIONARIOS -----------
var json_setores;

function RecarregarPagina(){
    location.reload()
}

function DefinirSetor(){
    setor_funcionario = this.innerHTML
    nome_funcionario = document.getElementById('nome-funcionario').value
    
    console.log('Nome do funcionário: ', nome_funcionario, ', ', 'Setor: ', setor_funcionario)
    nome_funcionario = empresa+'/funcionarios/'+nome_funcionario
    try{
        db.ref(nome_funcionario).set({
            setor: setor_funcionario
        })
    }
    catch(error){
        alert('Problema ao cadastrar funcionário, recarregue a página e tente novamente')
    }

    quebra_de_linha = document.createElement('br')
    novo_botao_concluido = document.createElement('button')
    novo_botao_concluido.innerHTML = 'CONCLUÍDO'
    novo_botao_concluido.classList.add('botao_concluido', 'distancia_botao_concluido')
    novo_botao_concluido.addEventListener('click', RecarregarPagina)

    div_criar_botoes.appendChild(quebra_de_linha)
    div_criar_botoes.appendChild(novo_botao_concluido)

}

function BuscarDados(x){
    json_setores = x
    console.log(json_setores)

    div_criar_botoes = document.getElementById('div_botoes_setores')

    if (div_criar_botoes.style.display === "none") {
        div_criar_botoes.style.display = "block";
    }


    for(key in resElement){
        console.log(resElement[key].Setor)
        local = document.getElementById('div_botoes_setores');
        novo_item_local = document.createElement('button')

        novo_item_local.innerHTML = resElement[key].Setor

        novo_item_local.classList.add('botao_cadastro_epis')

        novo_item_local.addEventListener('click', DefinirSetor)

        local.appendChild(novo_item_local)
    }


    return
    
}
function CadastrarFuncionarios(){
    empresa = localStorage.getItem('nome')

    console.log(empresa)
    referencia_setores = empresa+'/Setores'
    try{
        db
         .ref(referencia_setores)
           .once('value')
           .then(function(snapshot){
               resElement = snapshot.val();
               BuscarDados(resElement)
        })
    }
    catch(error){
        alert('Problema!')
    }
    
}

// ----------- LOGIN -----------
var username, password;
var empresa;

function DadosEmpresa(resElement, senha_conta, nome_empresa){
    label_retorno_login = document.getElementById('retorno_login')
    if(resElement == null){
        label_retorno_login.innerHTML = 'Empresa não cadastrada, verifique seu usuário'
    }
    else if(resElement.Senha == senha_conta){
        empresa=nome_empresa
        window.location.href = "index_logado.html"
    }
    else{
        label_retorno_login.innerHTML = 'Senha incorreta'
    }
    
}

function LogarConta(){
    username = document.getElementById('username').value;
    password = document.getElementById('password').value;

    localStorage.setItem('nome', username)

    try{
        db
         .ref(username)
           .once('value')
           .then(function(snapshot){
               resElement = snapshot.val();
               
               DadosEmpresa(resElement, password, username)
        })
    }
    catch(error){
        console.log(error)
        alert('Problema!')
    }
    
}

function CadastrarConta(){
    usuario = document.getElementById('usuario').value
    senha = document.getElementById('senha').value
    email = document.getElementById('email').value
    label_retorno_cadastro = document.getElementById('retorno_cadastro')
    try{
        db.ref(usuario).set({
            Senha: senha,
            Email: email
        })
        label_retorno_cadastro.innerHTML = 'Empresa cadastrada com sucesso'

    }
    catch(error){
        console.log(error)
        alert('Problema ao cadastrar')
    }
}

