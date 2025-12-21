# Locale Files Implementation (Hybrid Translation Approach)

## Overview

We've implemented a **hybrid translation approach** that combines:
1. **Static Locale Files** (`.json`) - For UI elements (buttons, labels, messages)
2. **Dynamic OpenAI Translation** - For chapter content (real-time translation)

## Architecture

### Static Translations (Locale Files)
- **Location**: `i18n/en/translations.json` and `i18n/ur/translations.json`
- **Purpose**: Fast, pre-translated UI elements
- **Usage**: Components use `useTranslation()` hook
- **Performance**: Instant (no API calls)

### Dynamic Translations (OpenAI)
- **Location**: Backend API `/translate/chapter`
- **Purpose**: Real-time translation of chapter content
- **Usage**: `TranslatableContent` component
- **Performance**: 10-30 seconds (cached after first translation)

## File Structure

```
i18n/
├── en/
│   └── translations.json          # English translations
└── ur/
    └── translations.json          # Urdu translations

src/lib/
└── i18n.ts                # Translation utility hook
```

## Translation Keys Structure

```json
{
  "common": {
    "signIn": "Sign In",
    "signUp": "Sign Up",
    "profile": "Profile",
    ...
  },
  "auth": {
    "email": "Email",
    "password": "Password",
    ...
  },
  "profile": {
    "title": "Profile",
    "beginner": "Beginner",
    ...
  },
  "translation": {
    "translatingContent": "Translating content...",
    ...
  },
  "chat": {
    "askQuestion": "Ask a question...",
    ...
  }
}
```

## Usage in Components

### Basic Usage

```tsx
import { useTranslation } from '../lib/i18n';

function MyComponent() {
  const { t } = useTranslation();
  
  return (
    <button>{t('common.signIn')}</button>
  );
}
```

### With Language Context

The `useTranslation()` hook automatically uses the current language from `LanguageContext`:

```tsx
import { useLanguage } from '../context/LanguageContext';
import { useTranslation } from '../lib/i18n';

function MyComponent() {
  const { currentLanguage } = useLanguage(); // 'en' or 'ur'
  const { t } = useTranslation(); // Automatically uses currentLanguage
  
  return <div>{t('common.welcome')}</div>;
}
```

## Updated Components

The following components now use locale files:

1. ✅ **LanguageToggle** - Language switch button
2. ✅ **UserMenu** - User menu (Sign In, Sign Up, Profile, Sign Out)
3. ✅ **PersonalizeButton** - Personalization button
4. ✅ **TranslatableContent** - Loading/error messages
5. ✅ **SignInPage** - Sign in form labels and messages

## Docusaurus i18n Configuration

Updated `docusaurus.config.ts`:

```typescript
i18n: {
  defaultLocale: 'en',
  locales: ['en', 'ur'],
  localeConfigs: {
    en: {
      label: 'English',
      direction: 'ltr',
    },
    ur: {
      label: 'اردو',
      direction: 'rtl',
    },
  },
},
```

## Benefits

1. **Performance**: UI elements load instantly (no API calls)
2. **Consistency**: Pre-translated UI text is consistent
3. **Flexibility**: Dynamic content can be translated on-demand
4. **Maintainability**: All translations in one place (`translations.json`)
5. **Type Safety**: TypeScript types for translation keys

## Adding New Translations

1. Add key-value pair to `i18n/en/translations.json`
2. Add corresponding Urdu translation to `i18n/ur/translations.json`
3. Use in component: `t('namespace.key')`

## Example: Adding a New Translation

**Step 1**: Add to `i18n/en/translations.json`:
```json
{
  "common": {
    "newButton": "New Button"
  }
}
```

**Step 2**: Add to `i18n/ur/translations.json`:
```json
{
  "common": {
    "newButton": "نیا بٹن"
  }
}
```

**Step 3**: Use in component:
```tsx
const { t } = useTranslation();
<button>{t('common.newButton')}</button>
```

## Future Enhancements

- [ ] Add more translations for signup/profile pages
- [ ] Add translations for error messages
- [ ] Add translations for chat UI
- [ ] Support for more languages (if needed)
- [ ] Integration with Docusaurus built-in i18n for docs pages

