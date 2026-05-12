import os
import pandas as pd
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel, tool

load_dotenv()
model = OpenAIServerModel(
    model_id="meta-llama/llama-4-scout-17b-16e-instruct",
    api_base="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

INJECTION_KEYWORDS = ["ignore", "forget", "system prompt", "override"]
DANGEROUS_KEYWORDS = [
    "os.", "subprocess", "sys.", "import os", "__import__",
    "eval(", "exec(", "open(", "shutil", "socket"
]


def check_safety(text: str):
    text_lower = text.lower()

    for bad_word in INJECTION_KEYWORDS:
        if bad_word in text_lower:
            raise ValueError(f"Обнаружена подозрительная команда: '{bad_word}'")

    for bad_word in DANGEROUS_KEYWORDS:
        if bad_word in text_lower:
            raise ValueError(f"Запрещённое действие в коде: '{bad_word}'")

@tool
def read_dataset(file_path: str) -> str:
    """
    Читает датасет и возвращает базовую информацию о нём.
    Используй этот инструмент первым чтобы понять структуру данных.
    НЕ считает статистику — для этого используй run_analysis.

    Args:
        file_path: путь к файлу CSV или Excel
    """

    import pandas as pd
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    cols = df.select_dtypes(include=['object', 'string']).columns
    pattern = "|".join(INJECTION_KEYWORDS)
    df[cols] = df[cols].replace(pattern, "[УДАЛЕНО]", regex=True)

    numeric_stats = df.describe().to_string()

    info = f"""
Размер: {df.shape[0]} строк, {df.shape[1]} столбцов
Колонки: {list(df.columns)}
Типы данных:
{df.dtypes.to_string()}
Дубликаты: {df.duplicated().sum()}
Статистика числовых колонок:
{numeric_stats}
    """
    return info


@tool
def run_analysis(file_path: str, code: str) -> str:
    """
    Выполняет произвольный Python-код для анализа датасета.
    Это основной инструмент анализа — вся аналитика делается здесь.

    Датасет доступен как переменная df (уже загружен).
    Для вывода результатов используй print().
    Доступны библиотеки: pandas (pd), numpy (np), scipy, statistics.

    Args:
        file_path: путь к файлу CSV или Excel
        code: Python код для выполнения
    """
    try:
        import traceback

        check_safety(code)

        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)

        output = []
        def custom_print(*args):
            output.append(" ".join(str(a) for a in args))

        local_vars = {
            "df": df,
            "pd": pd,
            "file_path": file_path,
            "print": custom_print
        }
        exec(code, local_vars)
        return "\n".join(output) if output else "Код выполнен, вывода нет"
    except ValueError as ve:
        return f"Защита: {ve}"
    except Exception:
        return f"Ошибка:\n{traceback.format_exc()}"


def create_agent():
    agent = CodeAgent(
        tools=[read_dataset, run_analysis],
        model=model,
        max_steps=12,
        additional_authorized_imports=[
            "json",
            "numpy",
            "scipy",
            "statistics"
        ]
    )
    return agent


def run_agent(dataset_path: str) -> dict:
    """
    Запускает агента на датасете.
    Возвращает текст отчёта и список графиков.
    """

    agent = create_agent()

    task = f"""
    Ты — профессиональный дата-саентист и аналитик. Проанализируй датасет по пути: {dataset_path}
    План действий:
    1. Прочитай датасет инструментом read_dataset.
    2. Напиши код для выявления корреляций и агрегаций через run_analysis.
    3. Сформируй итоговый ответ.

    ТРЕБОВАНИЯ К ИТОГОВОМУ ОТВЕТУ (ВЕРНИ ИМЕННО ЭТУ СТРУКТУРУ КАК ФИНАЛЬНЫЙ РЕЗУЛЬТАТ):
    Обязательно используй абазы и цифры для нумерации. Избегай знаков **

    Используй следующий шаблон для финального ответа:

    1. Общая структура данных
    Опиши размер датасета, типы колонок(каждая колонка на новой строке), качество данных (пропуски, дубликаты).
    каждая новая мысль в этом пункте идет с новой строки и со знаком -

    2. Ключевые статистики
    ОБЯЗАТЕЛЬНО опиши средние значения, максимумы и минимумы. 
    каждая новая мысль в этом пункте идет с новой строки и со знаком -

    3. Закономерности и инсайты
    ОБЯЗАТЕЛЬНО приведи 2-3 глубоких вывода по датасету и расскажи как данные связаны между собой?
    каждая новая мысль в этом пункте идет с новой строки и со знаком -

    ВАЖНО: Пиши красивым, понятным русским языком. Не пиши сплошным текстом.
    """

    result = agent.run(task)



    return {
        "text": str(result)
    }
