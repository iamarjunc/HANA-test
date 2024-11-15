from django.db.backends.base.base import BaseDatabaseWrapper  # Updated import path
from hdbcli import dbapi

class DatabaseWrapper(BaseDatabaseWrapper):
    """
    A custom Django database backend for SAP HANA using hdbcli.
    """

    def __init__(self, *args, **kwargs):
        self.connection = None
        super().__init__(*args, **kwargs)

    def get_connection_params(self):
        """
        Returns the connection parameters from Django settings.
        """
        params = {
            'user': self.settings_dict['USER'],
            'password': self.settings_dict['PASSWORD'],
            'host': self.settings_dict['HOST'],
            'port': self.settings_dict['PORT'],
            'database': self.settings_dict['NAME'],
        }
        return params

    def connect(self):
        """
        Establish the connection to the SAP HANA database.
        """
        if not self.connection:
            params = self.get_connection_params()
            try:
                # Establish the connection using the hdbcli client
                self.connection = dbapi.connect(
                    user=params['user'],
                    password=params['password'],
                    host=params['host'],
                    port=params['port'],
                    database=params['database']
                )
            except Exception as e:
                raise Exception(f"Error connecting to SAP HANA: {str(e)}")

    def close(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            self.connection = None

    def _cursor(self):
        """
        Returns a new cursor for executing queries.
        """
        self.connect()  # Ensure the connection is established
        return self.connection.cursor()

    def _commit(self):
        """
        Commit the current transaction.
        """
        if self.connection:
            self.connection.commit()

    def _rollback(self):
        """
        Rollback the current transaction.
        """
        if self.connection:
            self.connection.rollback()

    def is_usable(self):
        """
        Check if the database connection is usable.
        """
        try:
            self.connect()
            return True
        except Exception:
            return False
