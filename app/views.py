from django.shortcuts import render
from django.http import request
from django.template import RequestContext
from datetime import datetime
from app.models import Curso
# Create your views here.

def index(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/index.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Home Page',
                      'year':datetime.now().year,
                  })
                  )

def page_lista_cursos(request):
        assert isinstance(request, HttpRequest)
        return render(request, "app/ListaCursos.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Lista de Cursos',
                      'year':datetime.now().year,
                      'cursos':Curso.objects.all()
                  })
                  )

def page_noticias(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/noticias.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Noticias',
                      'year':datetime.now().year,
                  })
                  )

def page_login(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/LoginPage.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Página de Login',
                      'year':datetime.now().year,
                  })
                  )

def page_nova_senha(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/ForgotPass.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Esqueci Minha Senha',
                      'year':datetime.now().year,
                  })
                  )

def page_cadastro_disciplina(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/CadastrarDisciplina.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Cadastrar Disciplina',
                      'year':datetime.now().year,
                  })
                  )

def page_contato(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/Contato.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Contato',
                      'year':datetime.now().year,
                  })
                  )

def page_cadastro_usuario(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/CadastroPage.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Cadastre-se',
                      'year':datetime.now().year,
                  })
                  )

def page_detalhes_cursos(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/DesCurso.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Detalhes dos Cursos',
                      'year':datetime.now().year,
                  })
                  )

def page_detalhes_segdainf(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/SegDaInf.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Detalhes Seg. Da Informação',
                      'year':datetime.now().year,
                  })
                  )

def page_disciplinas_segdainf(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/dSegDaInfo.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Disciplinas Seg. da Informação',
                      'year':datetime.now().year,
                  })
                  )

def page_disciplina_seginfoatualidade(request):
    assert isinstance(request, HttpRequest)
    return render(request, "app/SegInfoAtualidade.html",
                  context_instance = RequestContext(request,
                  {
                      'title':'Segurança da Informação na Atualidade',
                      'year':datetime.now().year,
                  })
                  )