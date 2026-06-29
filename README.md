# Telegram Subscription Manager Bot

A Telegram bot for managing paid channel subscriptions with cryptocurrency payment integration. Built for real-world use with actual paying users.

## Features

**User Features**
- Multi-language support (Persian, English, Russian, Chinese, French, German, Spanish, Italian, Japanese, Dutch, Portuguese, Turkish)
- Purchase channel subscriptions with cryptocurrency (via Plisio)
- Check payment status
- Automatic channel access management after successful payment

**Admin Features**
- Full admin panel via Telegram commands
- Add/remove channels and subscription plans
- Ban/unban users
- Manage forced-join channels
- Add special users (users with free access)
- Export any database table to CSV
- Multi-admin support

## Tech Stack

- **Language:** Python 3
- **Bot Framework:** python-telegram-bot 21.3
- **Payment Gateway:** Plisio (cryptocurrency payments)
- **Database:** SQLite with custom ORM
- **Architecture:** Layered handler structure (command / conversation / callback / message)

## Project Structure

```
├── main.py                  # Entry point, handler registration
├── model.py                 # Custom ORM (BaseModel + all models)
├── settings.py              # Config loaded from environment variables
├── languages_*.py           # Localization files (12 languages)
├── api_client/              # Business logic layer
│   ├── user_client.py
│   ├── channel_client.py
│   ├── payment_client.py
│   ├── sub_client.py
│   └── ...
└── handlers/
    ├── command/             # Slash command handlers (/start, /admin, ...)
    ├── conversation/        # Multi-step conversation flows
    ├── callbackquery/       # Inline button handlers
    └── message/             # Channel message handler
```

## Architecture

The project follows a layered architecture:

- **Handlers layer** — receives Telegram updates and delegates to the API client layer
- **API client layer** — contains all business logic (user management, payment processing, subscription management)
- **Model layer** — custom lightweight ORM built on top of SQLite with `save()`, `delete()`, `filter()`, `get_all()`, and `export_to_csv()` methods

## Setup

1. Clone the repository:
```bash
git clone https://github.com/M-mehdiAhmadi/telegram-subscription-manager.git
cd telegram-subscription-manager
```

2. Install dependencies:
```bash
pip install -r requirments.txt
```

3. Create a `.env` file based on `.env-sample`:
```
BOT_TOKEN=your_telegram_bot_token
PLISIO_API=your_plisio_api_key
```

4. Run the bot:
```bash
python main.py
```

## Database Models

| Model | Description |
|---|---|
| `User` | Telegram users with language, admin, and special access flags |
| `Channel` | Managed Telegram channels |
| `Subscriptions` | Subscription plans (name, price, duration in days) |
| `Payment` | Payment records with Plisio invoice data |
| `User2subscriptions` | Active user subscriptions |
| `Joinforce` | Forced-join channels required before purchase |
| `Specialuser` | Users with free access to specific channels |

## Bot Commands

| Command | Access | Description |
|---|---|---|
| `/start` | All users | Start the bot, select language |
| `/admin` | Admins | Open admin panel |
| `/ban_user` | Admins | Ban a user |
| `/unban_user` | Admins | Unban a user |
| `/add_admin` | Super admin | Add a new admin |
| `/remove_admin` | Super admin | Remove an admin |
| `/exporttocsv` | Admins | Export database table to CSV |

## License

MIT