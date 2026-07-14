# Habilita+

Projeto desenvolvido para a matéria de Back-End da 5ª fase de Sistemas de Informação na UDESC.

A ideia é ser um sistema simples de autoescola digital feito em Django. Ele tem cadastro e login de aluno e agendamento de aulas e exames.

## Como o projeto está separado

- `backend/`: parte do back-end em Django.
- `templates/`: páginas HTML que aparecem para o usuário.
- `static/`: CSS, JavaScript e imagens.

Dentro de `apps/` cada funcionalidade ficou em um app separado:

- `accounts`: login, cadastro e perfil.
- `agendamentos`: aulas e exames.
- `progresso`: dashboard, histórico e certificados.
- `pagamentos`: boletos e comprovantes.
- `avaliacoes`: notas e feedback dos instrutores.
- `core`: página inicial e suporte.

## Como rodar

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

Depois é só abrir:

```text
http://127.0.0.1:8000/
```