import random
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.types import CallbackQuery

from storage import get_user_lang, set_user_level
from texts import TEXTS

from questions import (
    A1_QUESTIONS,
    A2_QUESTIONS,
    B1_QUESTIONS,
    B2_QUESTIONS,
    C1_QUESTIONS,
    C2_QUESTIONS,
)

# =====================
# FSM States
# =====================

class TestStates(StatesGroup):
    waiting_for_answer = State()


# =====================
# Generate Test
# =====================

def generate_test():
    test = []
    test.extend(random.sample(A1_QUESTIONS, 4))
    test.extend(random.sample(A2_QUESTIONS, 4))
    test.extend(random.sample(B1_QUESTIONS, 4))
    test.extend(random.sample(B2_QUESTIONS, 3))
    test.extend(random.sample(C1_QUESTIONS, 3))
    test.extend(random.sample(C2_QUESTIONS, 2))
    return test


# =====================
# Start Test
# =====================

async def start_test(callback: CallbackQuery, state: FSMContext):
    test = generate_test()

    await state.update_data(test=test, index=0, score=0)

    user_id = int(callback.from_user.id)
    lang = get_user_lang(user_id)

    await callback.bot.send_message(
        user_id,
        TEXTS["test_start"][lang]
    )

    await ask_next_question(callback, state)


# =====================
# Ask Question
# =====================

async def ask_next_question(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    test = data["test"]
    index = data["index"]

    if index >= len(test):
        return  # finished

    q = test[index]

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text=opt, callback_data=f"ans_{i}")]
            for i, opt in enumerate(q["options"])
        ]
    )

    await callback.bot.send_message(
        callback.from_user.id,
        f"{index+1}) {q['question']}",
        reply_markup=keyboard
    )

    await state.set_state(TestStates.waiting_for_answer)


# =====================
# Process Answer
# =====================

async def process_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    test = data["test"]
    index = data["index"]

    correct = test[index]["correct"]
    user_choice = int(callback.data.split("_")[1])

    # score update
    if user_choice == correct:
        data["score"] += 1

    data["index"] += 1
    await state.update_data(**data)

    # remove previous question
    try:
        await callback.message.delete()
    except:
        pass

    # finish test?
    if data["index"] >= len(test):

        score = data["score"]
        level = calculate_level(score)
        user_id = int(callback.from_user.id)
        lang = get_user_lang(user_id)

        set_user_level(user_id, level)

        text = TEXTS["test_finished"][lang].format(score=score, level=level)

        await callback.bot.send_message(
            user_id,
            text,
            parse_mode="Markdown"
        )

        await state.clear()
        return  # ❗ END HERE — NO MORE QUESTIONS

    # ask next question
    await ask_next_question(callback, state)


# =====================
# Level Calculation
# =====================

def calculate_level(score: int):
    if score <= 5:
        return "A1"
    elif score <= 9:
        return "A2"
    elif score <= 13:
        return "B1"
    elif score <= 16:
        return "B2"
    elif score <= 18:
        return "C1"
    else:
        return "C2"


