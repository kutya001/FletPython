from db_manager import DBManager
from db_utils import get_connection


def main():
    
    connection = get_connection()
    manager = DBManager(connection)
    manager.create('students', name='ssss')

if __name__ == "__main__":
    main()


