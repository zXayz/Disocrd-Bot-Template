from __future__ import annotations

import logging
import aiosqlite
import asyncio
from pathlib import Path
logger = logging.getLogger(__name__)

"""
This is for MongoDB connection.
"""
# import motor.motor_asyncio
# class DataBase:
#     def __init__(self, DATABASE_URL: str , DATABASE_NAME: str | None = "Test") -> None:
#         logger.info(f"Trying to connect to DataBase {DATABASE_NAME}...")
#         mongo_client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
#         self.db = mongo_client[DATABASE_NAME]
#         logger.info(f"Connect to {DATABASE_NAME}")
        

"""
This is for sqlite connection.
"""      
class DataBase:
    def __init__(self, database_name: Path | None = "myDB.db") -> None:
        self.database_name = database_name
        self.connection = None
        
    async def connect(self, *args, **kwargs) -> None:
        logger.info(f"Trying to connect to DataBase {self.database_name}...")
        self.connection = await aiosqlite.connect(self.database_name)
        await asyncio.sleep(2)

        async with self.connection.cursor() as cursor:
            # Read SQL statements from SCHEMA.sql and execute
            schema_file_path = Path("database/SCHEMA.sql")
            if schema_file_path.exists():
                with schema_file_path.open(mode='r') as schema_file:
                    sql_statements = schema_file.read()

                await cursor.executescript(sql_statements)
                logger.info("All tables have been created successfully.")
            else:
                logger.warning("Schema file (SCHEMA.sql) not found.")

    async def close(self) -> None:
        """Close the database connection."""
        if self.connection:
            await self.connection.close()
            logger.info("Database connection closed.")