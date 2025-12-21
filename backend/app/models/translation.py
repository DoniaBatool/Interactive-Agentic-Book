"""
Translation models for Urdu translation system.
"""
from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, DECIMAL, Index
from sqlalchemy.sql import func

from backend.app.core.database import Base


class Translation(Base):
    """
    Stores translated content with caching support.
    """
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    chapter_path = Column(String(255), nullable=False, index=True)
    source_language = Column(String(10), nullable=False, default="en")
    target_language = Column(String(10), nullable=False, index=True)
    source_content = Column(Text, nullable=False)
    translated_content = Column(Text, nullable=False)
    content_hash = Column(String(64), nullable=False, index=True)  # SHA-256 hash
    
    # Metadata
    word_count = Column(Integer, nullable=True)
    translation_time_ms = Column(Integer, nullable=True)
    is_cached = Column(Boolean, default=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Indexes for efficient lookups
    __table_args__ = (
        Index('idx_translation_lookup', 'chapter_path', 'target_language', 'content_hash'),
        Index('idx_translation_chapter_lang', 'chapter_path', 'target_language'),
    )

    def __repr__(self):
        return f"<Translation(chapter='{self.chapter_path}', lang='{self.target_language}')>"


class TranslationMetadata(Base):
    """
    Stores translation performance and quality metrics.
    """
    __tablename__ = "translation_metadata"

    id = Column(Integer, primary_key=True, index=True)
    chapter_path = Column(String(255), nullable=False, index=True)
    target_language = Column(String(10), nullable=False, default="ur")
    
    # Performance metrics
    total_words = Column(Integer, nullable=True)
    translation_time_ms = Column(Integer, nullable=True)
    api_calls_count = Column(Integer, default=1)
    
    # Quality metrics
    translation_quality_score = Column(DECIMAL(3, 2), nullable=True)  # 0.00 to 1.00
    user_rating = Column(DECIMAL(2, 1), nullable=True)  # 1.0 to 5.0
    
    # Status tracking
    translation_status = Column(String(20), default="completed")  # pending, completed, failed
    error_message = Column(Text, nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<TranslationMetadata(chapter='{self.chapter_path}', status='{self.translation_status}')>"


class TranslationCache(Base):
    """
    Lightweight cache for frequently accessed translations.
    """
    __tablename__ = "translation_cache"

    id = Column(Integer, primary_key=True, index=True)
    cache_key = Column(String(128), unique=True, nullable=False, index=True)
    chapter_path = Column(String(255), nullable=False, index=True)
    target_language = Column(String(10), nullable=False, default="ur")
    translated_content = Column(Text, nullable=False)
    
    # Cache metadata
    access_count = Column(Integer, default=0)
    last_accessed = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<TranslationCache(key='{self.cache_key}', chapter='{self.chapter_path}')>"
