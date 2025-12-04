# Configuration Management

This directory contains application configuration and settings management.

## Overview

The configuration system uses **Pydantic Settings** for type-safe environment variable loading with validation and default values.

## Files

- **`settings.py`**: Main configuration class that loads environment variables
- **`__init__.py`**: Package initialization

## Configuration Strategy

### Pydantic Settings

We use `pydantic-settings` to:
- Load environment variables with type validation
- Provide sensible defaults for optional values
- Support both uppercase and lowercase variable names
- Read from `.env` file automatically

### Environment Variables

All configuration comes from environment variables defined in `.env` file (or system environment).

See `../../.env.example` for the complete list of available variables.

## Usage

### Import Settings

```python
from app.config.settings import settings

# Access configuration
api_key = settings.openai_api_key
db_url = settings.database_url
```

### Available Settings

#### AI Services
- `openai_api_key`: OpenAI API key for GPT and embeddings
- `qdrant_url`: Qdrant vector database URL
- `qdrant_api_key`: Qdrant API key

#### Database
- `database_url`: PostgreSQL connection string (Neon Serverless)

#### Authentication
- `betterauth_secret`: Secret key for BetterAuth session encryption

#### Email
- `smtp_host`: SMTP server hostname
- `smtp_port`: SMTP port (default: 587)
- `smtp_user`: SMTP username
- `smtp_password`: SMTP password

#### Application
- `environment`: Environment name (development/production/test)
- `backend_port`: Backend server port (default: 8000)
- `cors_origins`: Allowed CORS origins (default: ["http://localhost:3000"])

## Adding New Configuration

To add a new configuration variable:

1. **Define in Settings class**:
   ```python
   class Settings(BaseSettings):
       # Add your new setting
       my_new_setting: str = "default_value"
   ```

2. **Add to `.env.example`**:
   ```bash
   # My New Setting
   MY_NEW_SETTING=example-value
   ```

3. **Update this documentation**

4. **Use in your code**:
   ```python
   from app.config.settings import settings
   
   value = settings.my_new_setting
   ```

## Validation

### Optional vs Required

In the initial scaffold phase, **all API keys are optional**:
- Application starts with warnings for missing credentials
- External services are gracefully skipped if not configured
- Useful for development without setting up all services

In production, required services will be enforced at startup.

### Type Safety

Pydantic validates types automatically:
```python
smtp_port: int = 587  # Must be an integer
cors_origins: list[str] = [...]  # Must be a list of strings
```

## Best Practices

1. **Never commit secrets**: Always use `.env` file (git-ignored)
2. **Use `.env.example`**: Document all variables with examples
3. **Provide defaults**: Use sensible defaults for optional values
4. **Type annotate**: Always specify types for settings
5. **Document purpose**: Add comments explaining what each setting does

## Troubleshooting

### "Field required" error

**Cause**: Required field is missing and has no default value.

**Solution**: Either:
- Set the environment variable in `.env`
- Add a default value in Settings class
- Make the field Optional

### Environment variables not loading

**Cause**: `.env` file not found or not in correct location.

**Solution**:
- Ensure `.env` file is in backend/ directory (same level as main.py)
- Check `Config.env_file` path in Settings class
- Verify file is not named `.env.example` (remove .example)

### Case sensitivity issues

**Cause**: Variable name doesn't match exactly.

**Solution**: We use `case_sensitive = False`, so both work:
- `OPENAI_API_KEY=...` ✅
- `openai_api_key=...` ✅

## References

- [Pydantic Settings Documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- [12-Factor App Config](https://12factor.net/config)
- [Environment Variables Best Practices](https://12factor.net/config)
