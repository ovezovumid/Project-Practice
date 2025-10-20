const http = require('http');

const server = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 
      'Content-Type': 'text/html; charset=utf-8'
    });
    res.end(`
      <!DOCTYPE html>
      <html>
        <head>
          <meta charset="UTF-8">
          <title>Система мониторинга аудиторий Университета</title>
          <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .header { background: #f5f5f5; padding: 20px; border-radius: 8px; }
            .services { margin-top: 20px; }
            .service { padding: 10px; border-left: 4px solid #007acc; margin: 10px 0; }
          </style>
        </head>
        <body>
          <div class="header">
            <h1>🏢 Система мониторинга загруженности аудиторий</h1>
            <p>Платформа для отслеживания заполняемости аудиторий в реальном времени</p>
          </div>
          
          <div class="services">
            <h2>📊 Сервисы системы</h2>
            
            <div class="service">
              <strong>Основной API</strong> - Бэкенд система управления
              <br><a href="/api/">Документация API</a>
            </div>
            
            <div class="service">
              <strong>Сервис компьютерного зрения</strong> - Детекция и подсчет людей
              <br><a href="/ml/">ML модели и эндпоинты</a>
            </div>
            
            <div class="service">
              <strong>Мониторинг системы</strong> - Проверка состояния сервисов
              <br><a href="/health">Статус системы</a>
            </div>
          </div>
          
          <div style="margin-top: 30px; padding: 15px; background: #e8f4fd; border-radius: 6px;">
            <small>🚀 Статус: <strong>Работает</strong> | Архитектура: Микросервисы | Версия: 1.0.0</small>
          </div>
        </body>
      </html>
    `);
  } else {
    res.writeHead(200, { 
      'Content-Type': 'application/json; charset=utf-8'
    });
    res.end(JSON.stringify({ 
      service: "Фронтенд системы мониторинга аудиторий",
      status: "работает",
      endpoints: {
        api: "/api/",
        ml_service: "/ml/",
        health: "/health"
      }
    }));
  }
});

server.listen(5173, '0.0.0.0', () => {
  console.log('Фронтенд системы мониторинга запущен на http://0.0.0.0:5173');
});