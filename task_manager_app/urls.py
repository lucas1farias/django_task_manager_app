

from django.urls import path  # 1_a
from .views import *  # 1_b

# 1_c
urlpatterns = [
    # PARTE 1 - CRUD, LOGIN, LOGOUT
    path('', Index.as_view(), name='index'),
    path('sign-up', SignUp.as_view(), name='sign-up'),  # criar conta
    path('sign-out', sign_out, name='sign-out'),        # deslogar da conta
    path('sign-in', SignIn.as_view(), name='sign-in'),  # logar na conta

    # PARTE 2 - CRUD TAREFAS
    path('user-tasks', UserTasks.as_view(), name='user-tasks'),           # ver tarefas
    path('create-task', NewTask.as_view(), name='create-task'),           # add tarefa
    path('alter-task/<int:pk>', AlterTask.as_view(), name='alter-task'),  # editar tarefa (tasks_table.html)
    path('erase-task/<int:pk>', EraseTask.as_view(), name='erase-task'),  # editar tarefa (tasks_table.html)
]
