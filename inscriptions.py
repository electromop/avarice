items = {"catalog": "📘 Каталог",
         "cart": "🛒 Корзина",
         "search": "🔍 Поиск",
         "orders": "📜 Заказы",
         "faq": "❓ FAQ",
         "contacts": "📱 Контакты"
         }
catalog = items["catalog"]
cart = items["cart"]
search = items["search"]
orders = items["orders"]
faq = items["faq"]
contacts = items["contacts"]

# FAQ text
faq_text = "Привет! \n\n<b>Q</b>: Почему бот неотвечает в группе?\n<b>A:</b> Чтобы бот ответил в группе, нужно " \
           "писать текст, отвечая на его сообщения\n\n<b>Варианты доставки:</b>\n\n- Новая почта\n\n<b>Варианты " \
           "оплаты:</b>\n\n- На карту (с помощью оператора; автоматическая проверка оплаты не реализована)\n- " \
           "Наложеный платеж "
# Contacts text
contacts_text = "Вы всегда можете написать нам!\n\n" \
                "Вот наш телефон: +38(095)-125-1673\n" \
                "Администратор: @ваш_айди" \
                "Email: вашапочта@gmail.com"

# If the message is unrecognized
unrecognized_message = "Мы не смогли распознать ваше сообщение :("

# If no one product in catalog
no_prods_in_catalog = "Тут пусто"

# Current currency
currency = "₴"

# Add to cart label
add_to_cart = "Купить"

# Search_text
search_text = "Функция в разработке"

# Cart
clear_cart = "Очистить корзину"
make_order = "Оформить заказ"
amount = "шт."
cart_is_empty = "Корзина пуста"

# Help
help_text = "Для начала работы с ботом требуется написать <b>/start</b>\n" \
    "Для работы нажимем кнопку <b>Каталог</b>, выбираем товар, заказываем через корзину\n" \
    "Для связи с нами есть кнопка <b>Контакты</b>, туда же отправлять найденные баги\n\n" \
    "<i><b>Удачного пользования!)</b></i>😊"

# Order
no_orders_text = "Сделайте заказ, чтобы увидеть его здесь!"
some_orders_here = "Ваши заказы:"
status = ["😶️️ Открыт", "⏺️Принят", "🤑 Закрыт"]

# Order making
city_of_dislocation = "Напишите, пожалуйста, город доставки"
number_of_departament = "Номер отделения"
full_name = "Напишите свое полное имя"
number = "Напишите свой номер телефона в формате +7вашномер"
payment_system = "Напишите, пожалуйста, как вам удобно оплачивать заказ:\n\n<b>- Наличиными\n- Картой</b>"
is_everything_right = "Все ли правильно?"
order_true_btn = "Да"
order_false_btn = "Нет, отмена"
order_true = "Спасибо, номер заказа {0}! Наш менеджер свяжется с вами для уточнения всех деталей."
order_false = "Мы перебросили вас в главное меню, но ваша корзина на месте"
params_text = {
                    "city": "Город",
                    "number_of_departament": "Почтовый индекс",
                    "full_name": "Полное имя",
                    "number": "Номер",
                    "payment_system": "Оплата"
                }
