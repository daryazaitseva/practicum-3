import openai
import json
from datetime import datetime


# Конфигурация
class Config:
    def __init__(self):
        self.OPENAI_API_KEY = "your-api-key-here"  # Замените на ваш ключ
        self.OPENAI_MODEL = "gpt-3.5-turbo"  # или "gpt-4"
        self.TEMPERATURE = 0.7
        self.MAX_TOKENS = 1000
        self.DATABASE_FILE = "conversations.json"

        # Контекст бота (можно адаптировать под вашу сферу)
        self.SYSTEM_PROMPT = """
        Ты - AI-ассистент компании. Твои задачи:
        1. Вежливо отвечать на вопросы клиентов
        2. Предлагать решения проблем
        3. При необходимости запрашивать дополнительную информацию
        4. Избегать спорных тем
        Твой стиль: дружелюбный, профессиональный, краткий.
        """


# Инициализация OpenAI
def init_openai(config):
    openai.api_key = config.OPENAI_API_KEY


# Обработчик запросов
class RequestHandler:
    def __init__(self, config):
        self.config = config
        self.conversations = self.load_conversations()

    def load_conversations(self):
        try:
            with open(self.config.DATABASE_FILE, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_conversations(self):
        with open(self.config.DATABASE_FILE, 'w') as file:
            json.dump(self.conversations, file, indent=2)

    def get_response(self, user_id, message):
        # Получаем или создаем историю диалога
        if user_id not in self.conversations:
            self.conversations[user_id] = {
                "history": [{"role": "system", "content": self.config.SYSTEM_PROMPT}],
                "timestamp": str(datetime.now())
            }

        # Добавляем новый запрос в историю
        self.conversations[user_id]["history"].append(
            {"role": "user", "content": message}
        )

        # Получаем ответ от OpenAI
        try:
            response = openai.ChatCompletion.create(
                model=self.config.OPENAI_MODEL,
                messages=self.conversations[user_id]["history"],
                temperature=self.config.TEMPERATURE,
                max_tokens=self.config.MAX_TOKENS
            )

            ai_response = response.choices[0].message['content']

            # Сохраняем ответ в историю
            self.conversations[user_id]["history"].append(
                {"role": "assistant", "content": ai_response}
            )
            self.conversations[user_id]["last_activity"] = str(datetime.now())

            self.save_conversations()
            return ai_response

        except Exception as e:
            return f"Произошла ошибка: {str(e)}"


