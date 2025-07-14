FROM python:3.13-alpine3.22

WORKDIR /app
RUN pip install uv

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen

COPY . .
EXPOSE 8000
CMD [                     \
    "uv",                 \
    "run",                \
    "python",             \
    "main.py",            \
    "--host", "0.0.0.0",  \
    "--port", "8000"      \
]
