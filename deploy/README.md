# Deployment

| target                    | how                                                        |
|---------------------------|------------------------------------------------------------|
| Streamlit Community Cloud | connect repo, main file `app/streamlit/app.py`             |
| Docker (both services)    | `cd deploy && docker compose up --build`                   |
| Render / Railway / Fly    | use `Dockerfile.api`; set `PORT` env if required           |
| Hugging Face Spaces       | Streamlit space pointing at `app/streamlit/app.py`         |
| Static site               | push `app/web/` to GitHub Pages; set `API` in `app.js`     |
| Quarto website            | `quarto publish gh-pages`                                  |

Secrets go in the host's environment settings, never in the repo.
