# vocab.py

import random
import re
from aiogram import F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram import F
from aiogram.types import CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext

router = Router()


from storage import (
    add_vocab_word,
    get_vocab_lists,
    get_vocab_words,
    delete_vocab_word,
    delete_vocab_word_by_id
)

from storage import get_user_lang
from texts import TEXTS


# ==================================================
# FSM STATES
# ==================================================

class VocabStates(StatesGroup):
    menu = State()
    waiting_list_name = State()
    viewing_list = State()
    adding_words = State()
    choosing_mode = State()
    deleting_word = State() 
    learning = State()



# ==================================================
# DELETE
# ==================================================

async def safe_delete(message):
    try:
        await message.delete()
    except:
        pass

# ==================================================
# HELPERS
# ==================================================
def is_valid_entry(entry: str) -> bool:
    entry = entry.strip()

    if '-' not in entry or not entry.endswith(';'):
        return False

    parts = entry.split('-', 1)
    if len(parts) != 2:
        return False

    word = parts[0].strip()
    meaning = parts[1].strip(';').strip()

    return bool(word) and bool(meaning)


def parse_and_validate_vocab(text: str):
    """
    Returns:
    - list of dicts [{"word": ..., "meaning": ...}] if ALL valid
    - None if ANY invalid
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    if not lines:
        return None

    for line in lines:
        if not is_valid_entry(line):
            return None

    result = []
    for line in lines:
        word, meaning = line.split('-', 1)
        result.append({
            "word": word.strip(),
            "meaning": meaning.strip().rstrip(';').strip()
        })

    return result





def menu_keyboard(lang):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=TEXTS["buttons"]["create_list"][lang], callback_data="vocab_create")],
        [InlineKeyboardButton(text=TEXTS["buttons"]["see_lists"][lang], callback_data="vocab_lists")]
    ])


def add_word_keyboard(lang):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=TEXTS["buttons"]["add_word"][lang], callback_data="vocab_add_word")],
        [InlineKeyboardButton(text=TEXTS["buttons"]["start_learning"][lang], callback_data="vocab_start_learning")]
    ])


def mode_keyboard(lang):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=TEXTS["buttons"]["mode_wm"][lang], callback_data="mode_wm")],
        [InlineKeyboardButton(text=TEXTS["buttons"]["mode_mw"][lang], callback_data="mode_mw")],
        [InlineKeyboardButton(text=TEXTS["buttons"]["mode_random"][lang], callback_data="mode_random")]
    ])


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def learning_keyboard(lang):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=TEXTS["buttons"]["next"][lang],
                callback_data="vocab_next"
            ),
            InlineKeyboardButton(
                text=TEXTS["buttons"]["stop"][lang],
                callback_data="vocab_stop"
            )
        ]
    ])

# ==================================================
# /vocab ENTRY
# ==================================================

async def vocab_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    await state.clear()
    await state.set_state(VocabStates.menu)

    await message.answer(
        TEXTS["vocab"]["menu"][lang],
        reply_markup=menu_keyboard(lang)
    )


# ==================================================
# CREATE LIST
# ==================================================

async def create_list(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    lang = get_user_lang(callback.from_user.id)

    await safe_delete(callback.message)

    await state.set_state(VocabStates.waiting_list_name)
    await callback.message.answer(TEXTS["vocab"]["create_list"][lang])


async def receive_list_name(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    list_name = message.text.strip()
    if not list_name:
        return

    await state.update_data(current_list=list_name)
    await state.set_state(VocabStates.viewing_list)

    await message.answer(
        TEXTS["vocab"]["list_created"][lang].format(list_name=list_name),
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=TEXTS["buttons"]["add_word"][lang], callback_data="vocab_add_word")]
        ])
    )


# ==================================================
# SEE ALL LISTS
# ==================================================

async def show_lists(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_user_lang(user_id)

    await safe_delete(callback.message)

    lists = get_vocab_lists(user_id)
    if not lists:
        await callback.message.answer(TEXTS["vocab"]["no_lists"][lang])
        return

    keyboard = [
        [InlineKeyboardButton(text=name, callback_data=f"open_{name}")]
        for name in lists
    ]
    keyboard.append([InlineKeyboardButton(text=TEXTS["buttons"]["create_list"][lang], callback_data="vocab_create")])

    await state.set_state(VocabStates.menu)
    await callback.message.answer(
        TEXTS["vocab"]["all_lists"][lang],
        reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
    )


# ==================================================
# OPEN ONE LIST
# ==================================================

async def open_list(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_user_lang(user_id)

    list_name = callback.data.replace("open_", "")
    words = get_vocab_words(user_id, list_name)

    await state.update_data(current_list=list_name)
    await state.set_state(VocabStates.viewing_list)

    text = f"{TEXTS['vocab']['list_title'][lang]} {list_name}\n\n"
    if not words:
        text += TEXTS["vocab"]["empty_list"][lang]
    else:
        for _, word, meaning in words:
            text += f"{word} — {meaning}\n"

    await callback.message.answer(text, reply_markup=list_actions_keyboard(lang))


# ==================================================
# ADD WORDS
# ==================================================

async def add_word(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    lang = get_user_lang(callback.from_user.id)

    await safe_delete(callback.message)

    await state.set_state(VocabStates.adding_words)
    await callback.message.answer(TEXTS["vocab"]["send_words"][lang],parse_mode="HTML")

def parse_vocab_text(text: str):
    pairs = []
    errors = []

    lines = text.split(";")

    for i, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue

        if "-" not in line:
            errors.append(i)
            continue

        word, meaning = line.split("-", 1)
        word = word.strip()
        meaning = meaning.strip()

        if not word or not meaning:
            errors.append(i)
            continue

        pairs.append({
            "word": word,
            "meaning": meaning
        })

    return pairs, errors

# ==================================================
# RECEIVE WORDS (CRITICAL)
# ==================================================

async def receive_words(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    data = await state.get_data()
    list_name = data.get("current_list")

    parsed = parse_and_validate_vocab(message.text)

    if parsed is None:
        await message.answer(TEXTS["vocab"]["wrong_input"][lang], parse_mode="HTML")
        return

    for item in parsed:
        add_vocab_word(
        user_id,
        list_name,
        item["word"],
        item["meaning"]
        )

    await state.set_state(VocabStates.viewing_list)

    await message.answer(
        TEXTS["vocab"]["word_added"][lang],
        reply_markup=after_add_keyboard(lang)
    )



# ==================================================
# START LEARNING
# ==================================================

async def choose_mode(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_user_lang(user_id)

    data = await state.get_data()
    list_name = data.get("current_list")

    if not list_name:
        await callback.message.answer(TEXTS["vocab"]["empty_list"][lang])
        return

    words = get_vocab_words(user_id, list_name)
    if not words:
        await callback.message.answer(TEXTS["vocab"]["empty_list"][lang])
        return

    # 🔥 THIS IS THE CORE FIX
    await state.update_data(words=words)

    await state.set_state(VocabStates.choosing_mode)
    await callback.message.answer(
        TEXTS["vocab"]["choose_mode"][lang],
        reply_markup=mode_keyboard(lang)
    )


async def set_mode(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    mode = callback.data.replace("mode_", "")
    await state.update_data(mode=mode)

    await send_question(callback.message, state)


# ==================================================
# LEARNING CORE
# ==================================================

async def send_question(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    data = await state.get_data()

    # ✅ READ FROM FSM ONLY
    words = data.get("words", [])
    mode = data.get("mode")

    if not words:
        await message.answer(TEXTS["vocab"]["empty_list"][lang])
        return

    pair = random.choice(words)

    if mode == "random":
        mode = random.choice(["wm", "mw"])

    await state.update_data(current_pair=pair)
    await state.set_state(VocabStates.learning)

    # 🧠 ONE MESSAGE — SPOILER STYLE
    _, word, meaning = pair  # tuple unpacking

    if mode == "wm":
        text = (
        f"📘 <b>{word}</b>\n\n"
        f"{TEXTS['vocab']['tap_to_reveal'][lang]}"
        f"<tg-spoiler>{meaning}</tg-spoiler>"
    )
    else:
        text = (
        f"🧠 <b>{meaning}</b>\n\n"
        f"{TEXTS['vocab']['tap_to_reveal'][lang]}"
        f"<tg-spoiler>{word}</tg-spoiler>"
    )


    await message.answer(
        text,
        parse_mode="HTML",
        reply_markup=learning_keyboard(lang)
    )


async def next_word(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await send_question(callback.message, state)


async def stop_learning(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    lang = get_user_lang(callback.from_user.id)

    await state.set_state(VocabStates.menu)
    await callback.message.answer(TEXTS["vocab"]["stopped"][lang], reply_markup=menu_keyboard(lang))


def after_add_keyboard(lang: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=TEXTS["vocab"]["add_word"][lang],
                callback_data="vocab_add"
            )
        ],
        [
            InlineKeyboardButton(
                text=TEXTS["vocab"]["start_learning"][lang],
                callback_data="vocab_start_learning"
            )
        ]
    ])


# ==================================================
# DELETING PROCESS
# ==================================================

@router.callback_query(F.data == "vocab_delete")
async def start_delete(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_user_lang(user_id)

    data = await state.get_data()
    list_name = data.get("current_list")

    words = get_vocab_words(user_id, list_name)

    if not words:
        await callback.message.answer(TEXTS["vocab"]["empty_list"][lang])
        return

    text = TEXTS['vocab']['choose_word_to_delete_title'][lang]

    for i, (_, word, meaning) in enumerate(words, start=1):
        text += f"{i}. <b>{word}</b> — {meaning}\n"

    text += f"\n{TEXTS['vocab']['send_number'][lang]}"

    await state.update_data(words=words)
    await state.set_state(VocabStates.deleting_word)

    await callback.message.answer(
        text,
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text=TEXTS["buttons"]["cancel"][lang],
                    callback_data="vocab_cancel"
                )]
            ]
        )
    )

@router.message(VocabStates.deleting_word)
async def receive_delete_number(message: Message, state: FSMContext):
    user_id = message.from_user.id
    lang = get_user_lang(user_id)

    if not message.text.isdigit():
        await wrong_delete_input(message, lang)
        return

    index = int(message.text)

    data = await state.get_data()
    words = data.get("words", [])
    list_name = data.get("current_list")

    if index < 1 or index > len(words):
        await wrong_delete_input(message, lang)
        return

    word_id, word, meaning = words[index - 1]
    delete_vocab_word_by_id(word_id)


    await state.set_state(VocabStates.viewing_list)

    await message.answer(
        TEXTS["vocab"]["word_deleted"][lang],
        reply_markup=list_actions_keyboard(lang)
    )

async def wrong_delete_input(message: Message, lang: str):
    await message.answer(
        TEXTS["vocab"]["wrong_choice"][lang],
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=TEXTS["buttons"]["delete_word"][lang],
                        callback_data="vocab_delete"
                    )
                ]
            ]
        )
    )


def list_actions_keyboard(lang):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=TEXTS["vocab"]["start_learning"][lang],
                callback_data="vocab_start_learning"
            )
        ],
        [
            InlineKeyboardButton(
                text=TEXTS["vocab"]["add_word"][lang],
                callback_data="vocab_add"
            ),
            InlineKeyboardButton(
                text=TEXTS["vocab"]["delete_word"][lang],
                callback_data="vocab_delete"
            )
        ]
    ])

async def show_lists_after_cancel(callback: CallbackQuery, state: FSMContext):
    user = callback.from_user
    if not user:
        return

    user_id = user.id
    lang = get_user_lang(user_id)

    lists = get_vocab_lists(user_id)
    if not lists:
        await callback.message.answer(
            TEXTS["vocab"]["no_lists"][lang]
        )
        return

    keyboard = [
        [InlineKeyboardButton(text=name, callback_data=f"open_{name}")]
        for name in lists
    ]
    keyboard.append(
        [InlineKeyboardButton(
            text=TEXTS["buttons"]["create_list"][lang],
            callback_data="vocab_create"
        )]
    )

    await state.set_state(VocabStates.menu)

    await callback.message.answer(
        TEXTS["vocab"]["all_lists"][lang],
        reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard)
    )
@router.callback_query(F.data == "vocab_cancel")
async def cancel_vocab_action(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    # clear FSM state
    await state.clear()

    # show lists again
    await show_lists_after_cancel(callback, state)




@router.callback_query(F.data == "vocab_create")
async def _(callback: CallbackQuery, state: FSMContext):
    await create_list(callback, state)


@router.callback_query(F.data == "vocab_lists")
async def _(callback: CallbackQuery, state: FSMContext):
    await show_lists(callback, state)


@router.callback_query(F.data.startswith("open_"))
async def _(callback: CallbackQuery, state: FSMContext):
    await open_list(callback, state)


@router.callback_query(F.data == "vocab_add")
async def _(callback: CallbackQuery, state: FSMContext):
    await add_word(callback, state)


@router.callback_query(F.data == "vocab_start_learning")
async def _(callback: CallbackQuery, state: FSMContext):
    await choose_mode(callback, state)


@router.callback_query(F.data.startswith("mode_"))
async def _(callback: CallbackQuery, state: FSMContext):
    await set_mode(callback, state)


@router.callback_query(F.data == "vocab_next")
async def _(callback: CallbackQuery, state: FSMContext):
    await next_word(callback, state)


@router.callback_query(F.data == "vocab_stop")
async def _(callback: CallbackQuery, state: FSMContext):
    await stop_learning(callback, state)

@router.message(VocabStates.adding_words)
async def _(message: Message, state: FSMContext):
    await receive_words(message, state)
