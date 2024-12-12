#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from base.RagLlmImplemetation.create_database import DataStoreInit
from base.RagLlmImplemetation.query_data import Query
from dotenv import load_dotenv

def main():
    """Run administrative tasks."""
    load_dotenv()
    """Running the `create_database.py` script"""
    if(os.path.isdir("chroma")):
        print("Data base already created!!!", file=sys.stderr)
    else:
        database_creation = DataStoreInit()
        database_creation.generate_data_store()
    

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RagLLm.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
