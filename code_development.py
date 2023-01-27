

def hierarquia():
    """
    =========================================== PARTE 1: CRUD, LOGIN, LOGOUT ===========================================
    Criação do dir (static) na raiz do projeto
    Criação do dir (templates) no pa do projeto
    Criação do arq (urls) no pa do projeto

    Seguir a ordem das views criadas em "views.py" e "urls.py" p/ saber como foram criadas
    Seguir a ordem dos templates abaixo p/ saber como foram criados

    Views = (
        'Index',
        'SignUp',
        'sign_out',
        'SignIn',
    )

    Urls = (
        path('', Index.as_view(), name='index'),
        path('sign-up', SignUp.as_view(), name='sign-up'),
        path('sign-out', SignOut.as_view(), name='sign-out'),
        path('sign-in', SignOut.as_view(), name='sign-in'),
    )

    -> 'sign_up_form.html' é anexado em 'sign_up.html', que é anexado em 'index.html'
    -> 'sign_up.html' é representado pelo comentário <!-- 2 -->
    -> 'sign_out.html' é anexado diretamente em 'index.html'
    -> 'sign_out.html' é representado pelo comentário <!-- 3 --> e não precisa de template
    -> 'sign_in_form.html' é anexado em 'sign_in.html', que é anexado em 'index.html'
    -> 'sign_in.html' é representado pelo comentário <!-- 4 -->

    Templates = (
        'index.html',
        'sign_up_form.html', 'sign_up.html',
        'sign_out.html',
        'sign_in_form.html', 'sign_in.html'
    )

    ============================================= PARTE 2: CRUD DE TAREFAS =============================================
    ETAPA 1: Exibição das tarefas          (índice 0)
    ETAPA 2: Configurar para criar tarefas (índice 1)

    Views = (
        'UserTasks',
        'NewTask',
        'AlterTask',
        'EraseTask'
    )

    Urls = (
        'path('user-tasks', UserTasks.as_view(), name='user-tasks')',
        'path('create-task', NewTask.as_view(), name='create-task')',
    )

    -> 'user_tasks.html' anexa 'tasks_table.html' & 'create_task.html'
    -> 'tasks_table.html' anexa 'update_task.html' & 'erase_task.html'

    Templates = (
        'user_tasks.html', 'tasks_table.html', 'create_task.html', 'alter_task.html', 'erase_task.html'
    )
    """
