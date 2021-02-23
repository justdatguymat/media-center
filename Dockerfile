FROM python:3.9 AS base
WORKDIR /app

FROM base AS dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM dependencies AS dist
COPY . .
RUN pip install --user .

FROM python:3.9.2-slim
COPY --from=dist /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
CMD ["media-center-start"]

