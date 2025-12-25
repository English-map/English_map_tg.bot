# start_bot.py

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import FSInputFile
from vocab import router as vocab_router

# LOCAL MODULES
from texts import TEXTS
from storage import (
    get_user_lang,
    set_user_lang,
    get_user_level,
    set_user_level,
    get_vocab_words,
    get_vocab_lists
)
from test_logic import TestStates, start_test, process_answer
from test_logic import generate_test
import html

from vocab import (
    vocab_start,
    create_list,
    receive_list_name,
    show_lists,
    open_list,
    add_word,
    receive_words,
    choose_mode,
    set_mode,
    next_word,
    stop_learning,
    start_delete,
    receive_delete_number
)
from vocab import VocabStates
from db import init_db



# -----------------------------
# BOT CONFIG
# -----------------------------
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@the_english_map"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


# -------------------------
# Subscription & language helpers / handlers
# -------------------------

async def is_user_subscribed(user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception:
        return False


async def block_if_not_subscribed(message: Message) -> bool:
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    # Always allow /start
    if message.text and message.text.startswith("/start"):
        return True

    if await is_user_subscribed(user_id):
        return True

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="📢 English Map 🌍",
                url=f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}"
            )],
            [InlineKeyboardButton(
                text="✅ I Subscribed",
                callback_data="check_sub"
            )]
        ]
    )

    must_subscribe = {
        "en": "🔒 Please subscribe to use this bot.",
        "ru": "🔒 Пожалуйста, подпишитесь, чтобы использовать бота.",
        "uz": "🔒 Botdan foydalanish uchun obuna bo‘ling."
    }

    await message.answer(must_subscribe.get(lang, must_subscribe["en"]), reply_markup=keyboard)
    return False

# -------------------------------
# /start handler
# -------------------------------

@dp.message(CommandStart())
async def start(message: Message):
    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    start_text = TEXTS.get("start", {}).get(
        lang,
        TEXTS.get("start", {}).get("en", "Welcome!")
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📝 Start Test", callback_data="start_test")],
        [InlineKeyboardButton(text="🌍 Change language", callback_data="open_language")]
    ])

    await message.answer(start_text, reply_markup=keyboard)



# -------------------------------
# Check subscription callback
# -------------------------------

@dp.callback_query(F.data == "check_sub")
async def check_subscription(callback: CallbackQuery):
    user_id = int(callback.from_user.id)
    lang = get_user_lang(user_id)

    subscribed = await is_user_subscribed(user_id)
    if subscribed:

        # TRY TO DELETE the previous welcome message
        try:
            await callback.message.delete()
        except:
            pass  # if message already deleted – ignore

        # Show language selection prompt (localized)
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
            [InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz")]
        ])

        choose_text = TEXTS.get("choose_language", {}).get(lang, TEXTS.get("choose_language", {}).get("en"))
        await callback.message.answer(choose_text, reply_markup=keyboard)
        await callback.answer()
    else:
        not_sub_msg = {
            "en": "❗ You are not subscribed yet. Please join our channel and then press Check subscription ✔️.",
            "ru": "❗ Вы ещё не подписаны. Пожалуйста, присоединитесь к нашему каналу и затем нажмите «Проверить подписку ✔️».",
            "uz": "❗ Siz hali obuna bo‘lmagansiz. Iltimos kanalga qo‘shiling va keyin «Obunani tekshirish ✔️» tugmasini bosing."
        }
        await callback.message.answer(not_sub_msg.get(lang, not_sub_msg["en"]))
        await callback.answer()


# -------------------------------
# /language command (open language menu anytime)
# -------------------------------

@dp.message(Command("language"))
async def language_command(message: Message):
    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz")]
    ])

    # Reuse choose_language text
    choose_text = TEXTS.get("choose_language", {}).get(lang, TEXTS.get("choose_language", {}).get("en"))
    await message.answer(choose_text, reply_markup=keyboard)


# -------------------------------
# Language selection callback (global)
# -------------------------------

@dp.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery):
    user_id = int(callback.from_user.id)
    lang = callback.data.split("_")[1]

    # Save language globally
    set_user_lang(user_id, lang)

    # Delete the language selection message
    try:
        await callback.message.delete()
    except:
        pass  # in case message is already deleted

    # Prepare Start Test button in user's language
    start_label = TEXTS.get("start_test_button", {}).get(lang, TEXTS.get("start_test_button", {}).get("en", "Start test ▶️"))
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=start_label, callback_data="start_test")]
    ])

    saved_text = TEXTS.get("language_saved", {}).get(lang, TEXTS.get("language_saved", {}).get("en", "Language saved."))
    await callback.message.answer(saved_text, reply_markup=keyboard)
    await callback.answer()
# -------------------------------
# Extract language menu
# -------------------------------

async def send_language_menu(target, user_id: int):
    lang = get_user_lang(user_id)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz")]
    ])

    choose_text = TEXTS.get("choose_language", {}).get(
        lang, TEXTS["choose_language"]["en"]
    )

    await target.answer(
        choose_text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# -------------------------------
# Callback handler for button
# -------------------------------

@dp.callback_query(F.data == "open_language")
async def open_language_callback(callback: CallbackQuery):
    await send_language_menu(callback.message, callback.from_user.id)
    await callback.answer()

# ------------------------------ START TEST ---------------------------------

@dp.callback_query(F.data == "start_test")
async def begin_test(callback: CallbackQuery, state: FSMContext):
    # Delete the "Language saved" message (with button)
    try:
        await callback.message.delete()
    except Exception:
        pass
    # Start test
    await callback.answer()
    await start_test(callback, state)

# ------------------------------ /ABOUT -----------------------------------

@dp.message(Command("about"))
async def about(message: Message):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    photo = FSInputFile("english_map_logo.jpg")

    await message.answer_photo(
        photo=photo,
        caption=TEXTS["about"][lang],
        parse_mode="HTML"
    )

# ------------------------------ /PROFILE -----------------------------------

@dp.message(Command("profile"))
async def profile(message: Message):
    if not await block_if_not_subscribed(message):
        return

    user = message.from_user
    user_id = int(user.id)
    lang = get_user_lang(user_id)

    # Load stored level
    level = get_user_level(user_id)
    level_text = (
        TEXTS["profile_level_not_tested"][lang]
        if not level else level
    )

    # Clickable name
    safe_name = html.escape(user.full_name or "User")
    mention_link = f'<a href="tg://user?id={user_id}">{safe_name}</a>'

    # ---------- Vocabulary lists ----------
    lists = get_vocab_lists(user_id)

    if not lists:
        vocab_text = TEXTS["profile_vocab_empty"][lang]
    else:
        vocab_lines = []
        for list_name in lists:
            words = get_vocab_words(user_id, list_name)
            vocab_lines.append(
                f"• <b>{html.escape(list_name)}</b> ({len(words)})"
            )

        vocab_text = (
            f"{TEXTS['profile_vocab_title'][lang]}\n"
            + "\n".join(vocab_lines)
        )

    # ---------- Final message ----------
    text = (
        f"{TEXTS['profile_title'][lang]}\n"
        f"━━━━━━━━━━━━━━\n"
        f"🙋‍♂️ {TEXTS['profile_name'][lang]}: {mention_link}\n"
        f"📘 {TEXTS['profile_level'][lang]}: <b>{html.escape(str(level_text))}</b>\n\n"
        f"{vocab_text}\n\n"
        f"{TEXTS['profile_footer'][lang]}"
    )

    await message.answer(text, parse_mode="HTML")




# ------------------------------ /HELP --------------------------------------

@dp.message(Command("help"))
async def help_cmd(message: Message):

    if not await block_if_not_subscribed(message):
        return

    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    await message.answer(TEXTS["help"][lang],parse_mode="HTML")




# ------------------------------ /LANGUAGE ----------------------------------

@dp.message(Command("language"))
async def language(message: Message):

    user_id = int(message.from_user.id)
    lang = get_user_lang(user_id)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
            [InlineKeyboardButton(text="🇺🇿 O‘zbek", callback_data="lang_uz")]
        ]
    )

    await message.answer(
        TEXTS["choose_language"][lang],
        reply_markup=keyboard
    )

@dp.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery):
    lang = callback.data.split("_")[1]
    user_id = int(callback.from_user.id)

    set_user_lang(user_id, lang)

    await callback.answer()
    await callback.message.answer(TEXTS["language_updated"][lang])


# ------------------------------ /TEST --------------------------------------

@dp.message(Command("test"))
async def test_command(message: Message, state: FSMContext):
    if not await block_if_not_subscribed(message):
        return

    await start_test(message, state)


# ------------------------------ ANSWERS -------------------------------------

@dp.callback_query(F.data.startswith("ans_"))
async def answer_handler(callback: CallbackQuery, state: FSMContext):
    """
    A single clean handler for processing all answer buttons.
    """
    current_state = await state.get_state()

    # If the user isn't in waiting_for_answer state, ignore the tap
    if current_state != TestStates.waiting_for_answer.state:
        await callback.answer()
        return

    from test_logic import process_answer
    await process_answer(callback, state)

# ------------------------------ VOCABULARY -------------------------------------

dp.include_router(vocab_router)
dp.message.register(vocab_start, Command("vocab"))

dp.callback_query.register(create_list, F.data == "vocab_create")
dp.callback_query.register(show_lists, F.data == "vocab_lists")
dp.callback_query.register(add_word, F.data == "vocab_add_word")
dp.callback_query.register(choose_mode, F.data == "vocab_start_learning")

dp.callback_query.register(set_mode, F.data.startswith("mode_"))
dp.callback_query.register(next_word, F.data == "vocab_next")
dp.callback_query.register(stop_learning, F.data == "vocab_stop")

dp.callback_query.register(open_list, F.data.startswith("open_"))

dp.message.register(receive_list_name, VocabStates.waiting_list_name)
dp.message.register(receive_words, VocabStates.adding_words)

dp.callback_query(start_delete, F.data == "vocab_delete")
dp.callback_query(receive_delete_number, F.data.startswith("delete_"))

# ------------------------------ RUN BOT -------------------------------------

async def main():
    init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())