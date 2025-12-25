# texts.py

TEXTS = {

    # ------------------------------
    # Welcome / Start messages
    # ------------------------------
    "start": {
        "en": (
        "Hello!\n\n"
        "I am your English Map bot — and your learning journey starts right here. 🌍\n\n"
        "Before we begin, let’s find out your current English level.\n"
        "If you need, change the language of the bot."
        ),
        "ru": (
        "Здравствуйте!\n\n"
        "Я бот English Map — и ваше путешествие в изучении английского начинается прямо здесь. 🌍\n\n"
        "Прежде чем мы начнём, давайте узнаем ваш текущий уровень английского.\n"
        "Если вам важно, измените язык бота."
        ),
        "uz": (
        "Salom!\n\n"
        "Men English Map botiman — va sizning ingliz tili bo‘yicha sayohatingiz aynan shu yerda boshlanadi. 🌍\n\n"
        "Boshlashdan oldin, keling, hozirgi ingliz tili darajangizni aniqlab olaylik."
        "Agar kerak bo'lsa, botning tilini o'zgartiring."
        ),
},

    # ------------------------------
    # Subscription check + language selection
    # ------------------------------
    "choose_language": {
        "en": "🎉 You are subscribed!\n\n🌍 Please choose your language:",
        "ru": "🎉 Вы подписаны!\n\n🌍 Пожалуйста, выберите язык:",
        "uz": "🎉 Siz obuna bo'lgansiz!\n\n🌍 Iltimos, tilni tanlang:"
    },

    "language_saved": {
        "en": "Great — language saved! ✅\nPress the button below to start the test.",
        "ru": "Отлично — язык сохранён! ✅\nНажмите кнопку ниже, чтобы начать тест.",
        "uz": "Ajoyib — til saqlandi! ✅\nTestni boshlash uchun pastdagi tugmani bosing."
    },

    "start_test_button": {
        "en": "Start test ▶️",
        "ru": "Начать тест ▶️",
        "uz": "Testni boshlash ▶️"
    },

    # ------------------------------
    # Test start message
    # ------------------------------
    "test_start": {
        "en": "🧪 Your English test is about to begin.\nYou’ll receive 20 questions one by one.\nDo your best — and good luck! 🍀",
        "ru": "🧪 Ваш тест по английскому начинается.\nВы получите 20 вопросов по одному.\nУдачи! 🍀",
        "uz": "🧪 Ingliz tili testi boshlanmoqda.\nSizga 20 ta savol navbatma-navbat beriladi.\nOmad! 🍀"
    },

    # ------------------------------
    # Test finished / results
    # ------------------------------
    "test_finished": {
        "en": "🎉 Test finished!\nYour score: {score} / 20\n📘 Your English level: *{level}*",
        "ru": "🎉 Тест завершён!\nВаш результат: {score} / 20\n📘 Ваш уровень английского: *{level}*",
        "uz": "🎉 Test tugadi!\nNatijangiz: {score} / 20\n📘 Ingliz tili darajangiz: *{level}*"
    },

    # ------------------------------
    # Profile section
    # ------------------------------
    "profile_title": {
        "en": "👤 Your Profile",
        "ru": "👤 Ваш профиль",
        "uz": "👤 Profilingiz"
    },

    "profile_level_not_tested": {
        "en": "Not tested yet ❔",
        "ru": "Тест ещё не проходили ❔",
        "uz": "Hali test topshirilmagan ❔"
    },

    "profile_text": {
        "en": (
            "👤 *Your Profile*\n"
            "━━━━━━━━━━━━━━\n"
            "🙋‍♂️ Name: {name}\n"
            "📘 Current English level: *{level}*\n\n"
            "✨ Keep learning and improving step by step!"
        ),
        "ru": (
            "👤 *Ваш профиль*\n"
            "━━━━━━━━━━━━━━\n"
            "🙋‍♂️ Имя: {name}\n"
            "📘 Текущий уровень английского: *{level}*\n\n"
            "✨ Продолжайте учиться и улучшать свои навыки!"
        ),
        "uz": (
            "👤 *Profilingiz*\n"
            "━━━━━━━━━━━━━━\n"
            "🙋‍♂️ Ism: {name}\n"
            "📘 Ingliz tili darajasi: *{level}*\n\n"
            "✨ O‘rganishda davom eting!"
        ),
    },

    # ------------------------------
    # Help command
    # ------------------------------
    "profile_name": {
        "en": "Name",
        "ru": "Имя",
        "uz": "Ism"
    },

    "profile_level": {
        "en": "Current English level",
        "ru": "Текущий уровень английского",
        "uz": "Ingliz tili darajangiz"
    },

    "profile_footer": {
        "en": "✨ Keep learning and improving step by step!",
        "ru": "✨ Продолжайте учиться и улучшать свой уровень!",
        "uz": "✨ O‘rganishda davom eting va o‘sishda davom eting!"
    },
    "help": {
    "en": (
        "<b>🆘 Available commands</b>\n\n"
        "/start — restart the bot\n"
        "/about — learn what this bot does\n"
        "/profile — view your profile\n"
        "/vocab — create and practice vocabulary lists\n"
        "/test — check your English level\n"
        "/help — show this help message\n\n"
        "Need more help? 😊\n"
        "If necessary, you can message the owner: @Abdulkayumov"
    ),

    "ru": (
        "<b>🆘 Доступные команды</b>\n\n"
        "/start — перезапустить бота\n"
        "/about — узнать о возможностях бота\n"
        "/profile — посмотреть ваш профиль\n"
        "/vocab — создавать и изучать списки слов\n"
        "/test — проверить уровень английского\n"
        "/help — показать это сообщение\n\n"
        "Нужна дополнительная помощь? 😊\nПри необходимости вы можете написать владельцу: @Abdulkayumov"
    ),

    "uz": (
        "<b>🆘 Mavjud buyruqlar</b>\n\n"
        "/start — botni qayta ishga tushirish\n"
        "/about — bot imkoniyatlari haqida ma’lumot\n"
        "/profile — profilingizni ko‘rish\n"
        "/vocab — lug‘atlar yaratish va mashq qilish\n"
        "/test — ingliz tili darajasini aniqlash\n"
        "/help — ushbu yordam xabarini ko‘rsatish\n\n"
        "Yana yordam kerakmi? 😊\nAgar kerak bo'lsa, egasiga xabar yuborishingiz mumkin: @Abdulkayumov"
    )
    },
    "choose_language": {
        "en": "🌍 Please choose your language:",
        "ru": "🌍 Пожалуйста, выберите язык:",
        "uz": "🌍 Iltimos, tilni tanlang:"
    },
    "language_updated": {
        "en": "✅ Language updated!",
        "ru": "✅ Язык обновлён!",
        "uz": "✅ Til o‘zgartirildi!"
    },
    "profile_vocab_title": {
    "en": "📚 Your vocabulary lists:",
    "ru": "📚 Ваши списки слов:",
    "uz": "📚 Sizning lug‘at ro‘yxatlaringiz:"
    },

"profile_vocab_empty": {
    "en": "You don’t have any vocabulary lists yet.",
    "ru": "У вас пока нет списков слов.",
    "uz": "Sizda hali lug‘at ro‘yxatlari yo‘q."
},
}

# =========================
# VOCAB TEXTS
# =========================

TEXTS["vocab"] = {
    "delete_word": {
    "en": "🗑 Delete word",
    "ru": "🗑 Удалить слово",
    "uz": "🗑 So‘zni o‘chirish"
},
"choose_word_to_delete": {
    "en": "Select a word to delete:",
    "ru": "Выберите слово для удаления:",
    "uz": "O‘chirish uchun so‘zni tanlang:"
},
"word_deleted": {
    "en": "✅ Word deleted successfully.",
    "ru": "✅ Слово удалено.",
    "uz": "✅ So‘z o‘chirildi."
},
    "tap_to_reveal": {
        "en": "👆 Tap to reveal the answer: ",
        "ru": "👆 Нажмите, чтобы увидеть ответ: ",
        "uz": "👆 Javobni ko‘rish uchun bosing: "
    },
    "menu": {
        "en": "📚 Vocabulary trainer\n\nWhat do you want to do?",
        "ru": "📚 Тренировка слов\n\nЧто вы хотите сделать?",
        "uz": "📚 So‘zlar mashqi\n\nNima qilmoqchisiz?"
    },
    "create_list": {
        "en": "Give the name for the list.",
        "ru": "Введите название списка.",
        "uz": "Ro‘yxat nomini kiriting."
    },
    "list_created": {
        "en": "✅ List \"{list_name}\" created!\n\nLet's add some words.",
        "ru": "✅ Список \"{list_name}\" создан!\n\nДобавим слова.",
        "uz": "✅ \"{list_name}\" ro‘yxati yaratildi!\n\nSo‘zlar qo‘shamiz."
    },
    "no_lists": {
        "en": "You don't have any vocabulary lists yet.",
        "ru": "У вас пока нет списков слов.",
        "uz": "Sizda hali lug‘at ro‘yxatlari yo‘q."
    },
    "all_lists": {
        "en": "📂 Your vocabulary lists:",
        "ru": "📂 Ваши списки слов:",
        "uz": "📂 Sizning lug‘at ro‘yxatlaringiz:"
    },
    "list_title": {
        "en": "📘 List:",
        "ru": "📘 Список:",
        "uz": "📘 Ro‘yxat:"
    },
    "empty_list": {
        "en": "This list is empty.",
        "ru": "Этот список пуст.",
        "uz": "Bu ro‘yxat bo‘sh."
    },
    "send_words": {
        "en": "Send your words in this format:\n\n<pre> word - meaning;\n word - meaning;</pre>",
        "ru": "Отправьте слова в формате:\n\n<pre>слово - значение;\nслово - значение;</pre>",
        "uz": "So‘zlarni shu formatda yuboring:\n\n<pre>so‘z - ma'no;\nso‘z - ma'no;</pre>"
    },
    "word_added": {
        "en": "✅ Word(s) added successfully.",
        "ru": "✅ Слово(а) успешно добавлено.",
        "uz": "✅ So‘z(lar) muvaffaqiyatli qo‘shildi."
    },
    "choose_mode": {
        "en": "✅ Words saved. Choose mode:",
        "ru": "✅ Слова сохранены. Выберите режим:",
        "uz": "✅ So‘zlar saqlandi. Rejimni tanlang:"
    },
    "word": {
        "en": "Word:\n",
        "ru": "Слово:\n",
        "uz": "So‘z:\n"
    },
    "meaning": {
        "en": "Meaning:\n",
        "ru": "Значение:\n",
        "uz": "Ma'no:\n"
    },
    "stopped": {
        "en": "Training stopped.",
        "ru": "Тренировка остановлена.",
        "uz": "Mashq to‘xtatildi."
    },
    "wrong_input": {
        "en": "❗ Wrong format.\n\nPlease send words like this:\n<pre>word - meaning;\nword - meaning;</pre>",
        "ru": "❗ Неверный формат.\n\nОтправьте слова так:\n<pre>слово - значение;\nслово - значение;</pre>",
        "uz": "❗ Noto‘g‘ri format.\n\nSo‘zlarni quyidagicha yuboring:\n<pre>so‘z - ma'no;\n> so‘z - ma'no;</pre>"
    },
    "parse_error": {
        "en": "❗ I couldn't find any valid word pairs.\n\nExample:\n<pre>book - kitob;</pre>",
        "ru": "❗ Не удалось найти корректные пары слов.\n\nПример:\n<pre>book - книга;</pre>",
        "uz": "❗ To‘g‘ri so‘z juftliklari topilmadi.\n\nMisol:\n<pre>book - kitob;</pre>"
    },
    "add_word": {
    "en": "➕ Add new word",
    "ru": "➕ Добавить слово",
    "uz": "➕ Yangi so‘z qo‘shish"
    },
    "start_learning": {
    "en": "▶️ Start learning",
    "ru": "▶️ Начать обучение",
    "uz": "▶️ O‘rganishni boshlash"
    },
        "send_number": {
        "en": "Send the number of the word you want to delete 👇",
        "ru": "Отправьте номер слова, которое хотите удалить 👇",
        "uz": "O‘chirmoqchi bo‘lgan so‘z raqamini yuboring 👇"
    },
    "wrong_choice": {
        "en": "❌ Wrong choice. Please try again.",
        "ru": "❌ Неверный выбор. Пожалуйста, попробуйте снова.",
        "uz": "❌ Noto‘g‘ri tanlov. Iltimos, qayta urinib ko‘ring."
    },
    "choose_word_to_delete_title": {
    "en": "🗑 <b>Choose a word to delete</b>\n\n",
    "ru": "🗑 <b>Выберите слово для удаления</b>\n\n",
    "uz": "🗑 <b>O‘chirish uchun so‘zni tanlang</b>\n\n"
    },
}

TEXTS["buttons"] = {
    "create_list": {
        "en": "➕ Create new vocabulary list",
        "ru": "➕ Создать новый список",
        "uz": "➕ Yangi lug‘at ro‘yxati"
    },
    "see_lists": {
        "en": "📂 See all vocab lists",
        "ru": "📂 Посмотреть списки",
        "uz": "📂 Barcha ro‘yxatlar"
    },
    "add_word": {
        "en": "➕ Add new word",
        "ru": "➕ Добавить слово",
        "uz": "➕ Yangi so‘z"
    },
    "start_learning": {
        "en": "▶️ Start learning",
        "ru": "▶️ Начать обучение",
        "uz": "▶️ O‘rganishni boshlash"
    },
    "mode_wm": {
        "en": "Word → Meaning",
        "ru": "Слово → Значение",
        "uz": "So‘z → Ma'no"
    },
    "mode_mw": {
        "en": "Meaning → Word",
        "ru": "Значение → Слово",
        "uz": "Ma'no → So‘z"
    },
    "mode_random": {
        "en": "🔀 Random",
        "ru": "🔀 Случайно",
        "uz": "🔀 Tasodifiy"
    },
    "show_answer": {
        "en": "👀 Show answer",
        "ru": "👀 Показать ответ",
        "uz": "👀 Javobni ko‘rish"
    },
    "next": {
        "en": "➡️ Next word",
        "ru": "➡️ Следующее слово",
        "uz": "➡️ Keyingi so‘z"
    },
    "stop": {
        "en": "⏹ Stop learning",
        "ru": "⏹ Остановить",
        "uz": "⏹ To‘xtatish"
    },
    "back": {
        "en": "⬅️ Back",
        "ru": "⬅️ Назад",
        "uz": "⬅️ Orqaga"
    },
    "cancel": {
        "en": "Cancel",
        "ru": "Отмена",
        "uz": "Bekor qilish"
    },
    "delete_word": {
    "en": "🗑 Delete word",
    "ru": "🗑 Удалить слово",
    "uz": "🗑 So‘zni o‘chirish"
    },
}
TEXTS["about"] = {
    "en": (
        "<b>📘 About this bot</b>\n\n"
        "This bot helps you understand your current level, learn, and practice vocabulary "
        "in a simple and effective way.\n\n"
        "<b>✨ What you can do:</b>\n"
        "• Check your current English level\n"
        "• Create your own vocabulary lists\n"
        "• Practice words in different modes\n\n"
        "<b>🧠 How to use:</b>\n"
        "• Use /test to check your level\n"
        "• Use /vocab to create or open a vocabulary list\n"
        "• Start learning and reveal answers when you are ready\n\n"
        "<b>🚀 Planned improvements:</b>\n"
        "• Games and challenges\n"
        "• Progress tracking\n\n"
        "Made with ❤️ to help you learn better."
    ),

    "ru": (
        "<b>📘 О боте</b>\n\n"
        "Этот бот помогает определить ваш текущий уровень, изучать и практиковать слова "
        "простым и эффективным способом.\n\n"
        "<b>✨ Что вы можете делать:</b>\n"
        "• Узнать свой уровень английского\n"
        "• Создавать собственные списки слов\n"
        "• Практиковать слова в разных режимах\n\n"
        "<b>🧠 Как использовать:</b>\n"
        "• Используйте /test, чтобы проверить свой уровень\n"
        "• Используйте /vocab, чтобы создать или открыть список слов\n"
        "• Начните обучение и открывайте ответы, когда будете готовы\n\n"
        "<b>🚀 Планируемые улучшения:</b>\n"
        "• Игры и задания\n"
        "• Отслеживание прогресса\n\n"
        "Сделано с ❤️, чтобы помочь вам учиться лучше."
    ),

    "uz": (
        "<b>📘 Bot haqida</b>\n\n"
        "Ushbu bot sizning hozirgi darajangizni aniqlash, lug‘atlarni o‘rganish va "
        "mashq qilishda oddiy va samarali yordam beradi.\n\n"
        "<b>✨ Nimalar qila olasiz:</b>\n"
        "• Ingliz tili darajangizni bilish\n"
        "• O‘z lug‘at ro‘yxatlaringizni yaratish\n"
        "• So‘zlarni turli rejimlarda mashq qilish\n\n"
        "<b>🧠 Qanday foydalaniladi:</b>\n"
        "• /test buyrug‘i orqali darajangizni tekshiring\n"
        "• /vocab orqali lug‘at ro‘yxatini yarating yoki oching\n"
        "• O‘rganishni boshlang va javoblarni tayyor bo‘lganda oching\n\n"
        "<b>🚀 Rejalashtirilgan yangilanishlar:</b>\n"
        "• O‘yinlar va qiziqarli mashqlar\n"
        "• Progressni kuzatish\n\n"
        "Yaxshiroq o‘rganishingiz uchun ❤️ bilan yaratildi."
    )
}
