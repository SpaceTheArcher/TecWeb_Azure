"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from django.conf.urls import patterns, url

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

from django.conf.urls import url
from django.contrib import admin
from core.views import index
from core.views import page_lista_cursos
from core.views import page_noticias
from core.views import page_login
from core.views import page_nova_senha
from core.views import page_cadastro_disciplina
from core.views import page_contato
from core.views import page_cadastro_usuario
from core.views import page_detalhes_cursos
from core.views import page_detalhes_segdainf
from core.views import page_disciplinas_segdainf
from core.views import page_disciplina_seginfoatualidade

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index), #index
    url(r'^home/', index), #index
    url(r'^Lista_Cursos/', page_lista_cursos), #Lista De Cursos
    url(r'^Noticias/', page_noticias), #Noticias
    url(r'^Login/', page_login), #Pag de Login
    url(r'^Nova_Senha/', page_nova_senha), #Esqueci Minha Senha
    url(r'^Disciplinas/Nova_Disciplina', page_cadastro_disciplina), #Cadastrar Disciplina
    url(r'^Contato/', page_contato), #Contato
    url(r'^Cadastre-se/', page_cadastro_usuario), #Cadastre-se
    url(r'^Detalhes/Cursos/$', page_detalhes_cursos), #Detalhes Cursos
    url(r'^Detalhes/Cursos/SegDaInformacao/', page_detalhes_segdainf), #Detalhes Seg. Da Informação
    url(r'^Disciplinas/SegDaInformacao/', page_disciplinas_segdainf), #Disciplinas Seg. Da Informação
    url(r'^Disciplinas/SegInfoAtualidade/', page_disciplina_seginfoatualidade), #Disciplina Seg. Da Informação na Atualidade
]


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
