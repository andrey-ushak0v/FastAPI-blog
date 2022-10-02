import uvicorn

from settings import settings

""""запуск приложения"""

uvicorn.run(
    'app:app',
    host=settings.server_host,
    port=settings.server_port,
   #  reload=True,
)