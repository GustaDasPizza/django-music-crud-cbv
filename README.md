Catálogo de músicas

Este projeto demonstra a implementação completa de um sistema CRUD (Create, Read, Update, Delete) que é funcionalidade de manuseamento de dados em Django, utilizando as Class-Based Views (CBV)
genéricas do framework. Tendo como objetivo gerenciar um catálogo de músicas.

Modelo principal (`Song`)

| Campo | Tipo | Descrição |
| `title` | CharField | Título da música. |
| `artist` | CharField | Nome do artista/banda. |
| `album` | CharField | Álbum (opcional). |
| `genre` | CharField | Gênero musical (Rock, Pop, etc.). |
| `release_date` | DateField | Data de lançamento (opcional). |

Rotas principais
O app `catalogo` implementa o CRUD completo, utilizando uma CBV específica para cada operação.
<img width="1160" height="439" alt="Captura de tela 2025-11-04 092900" src="https://github.com/user-attachments/assets/e9074610-b947-46ff-8b31-a594be411da0" />


| Operação (CRUD) | Rota (URL Pattern) | View Utilizada | Template | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| **READ (Listar)** | `/catalogo/` | `SongListView` | `listar.html` | Exibe todas as músicas cadastradas em formato de lista/cards. |
| **READ (Detalhe)** | `/catalogo/song/<pk>/` | `SongDetailView` | `detalhe.html` | Exibe todos os dados de uma música específica (usando o `pk` - Primary Key). |
| **CREATE** | `/catalogo/song/create/` | `SongCreateView` | `form.html` | Formulário para adicionar uma nova música. |
| **UPDATE** | `/catalogo/song/<pk>/update/` | `SongUpdateView` | `form.html` | Formulário pré-preenchido para editar uma música existente. |
| **DELETE** | `/catalogo/song/<pk>/delete/` | `SongDeleteView` | `confirm_delete.html` | Tela de confirmação antes de excluir o registro permanentemente. |

Prints das páginas
<img width="1469" height="795" alt="Captura de tela 2025-11-04 092011" src="https://github.com/user-attachments/assets/6a7e466b-21b9-46c0-80a3-6e463c245e99" />
<img width="922" height="629" alt="Captura de tela 2025-11-04 094845" src="https://github.com/user-attachments/assets/95ac8af5-7842-4d42-b1aa-5365392c1ffb" />
<img width="1514" height="628" alt="Captura de tela 2025-11-04 095056" src="https://github.com/user-attachments/assets/e2fa36a7-b1ba-408a-8fbe-36b455b1231e" />


Executando o projeto localmente

1.  *Clone o repositório:*
    ```bash
    git clone [https://github.com/GustaDasPizza/django-music-crud-cbv.git](https://github.com/GustaDasPizza/django-music-crud-cbv.git)
    cd django-music-crud-cbv
2.  *Crie e ative o Ambiente Virtual:*
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate
3.  *Instale as Dependências:*
    ```bash
    pip install -r requirements.txt
4.  *Execute as Migrações do Banco de Dados:*
    ```bash
    python manage.py migrate
5.  *Inicie o Servidor:*
    ```bash
    python manage.py runserver
Acesse o projeto em `http://127.0.0.1:8000/`.
