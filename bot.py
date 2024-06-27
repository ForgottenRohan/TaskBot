from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
from conf import TOKEN
# Список для хранения задач
tasks = []

# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    await update.message.reply_text(
        f"Привет, {user.first_name}! Я ваш личный бот для управления задачами.\n"
        "Используйте команду /add <описание задачи> для добавления новой задачи.\n"
        "Используйте команду /list для просмотра всех задач.\n"
        "Используйте команду /done <номер задачи> для отметки задачи как выполненной."
    )

# Обработчик команды /add
async def add_task(update: Update, context: CallbackContext) -> None:
    task_description = ' '.join(context.args)
    if task_description:
        tasks.append({"description": task_description, "completed": False})
        await update.message.reply_text(f"Задача '{task_description}' добавлена.")
    else:
        await update.message.reply_text("Пожалуйста, укажите описание задачи после команды /add.")

# Обработчик команды /list
async def list_tasks(update: Update, context: CallbackContext) -> None:
    if not tasks:
        await update.message.reply_text("Список задач пуст.")
        return

    message = "Список задач:\n"
    for i, task in enumerate(tasks):
        status = "✅" if task["completed"] else "❌"
        message += f"{i + 1}. {task['description']} - {status}\n"
    await update.message.reply_text(message)

# Обработчик команды /done
async def complete_task(update: Update, context: CallbackContext) -> None:
    try:
        task_number = int(context.args[0]) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            await update.message.reply_text(f"Задача '{tasks[task_number]['description']}' отмечена как выполненная.")
        else:
            await update.message.reply_text("Неверный номер задачи.")
    except (IndexError, ValueError):
        await update.message.reply_text("Пожалуйста, укажите правильный номер задачи после команды /done.")

def main() -> None:
    # Вставьте сюда ваш токен
    token = TOKEN

    # Создаем приложение
    application = ApplicationBuilder().token(token).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_task))
    application.add_handler(CommandHandler("list", list_tasks))
    application.add_handler(CommandHandler("done", complete_task))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
