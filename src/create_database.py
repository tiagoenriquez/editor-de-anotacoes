from src.connections.DatabaseConnection import connection
from src.tableDefinitions import TopioDefinition


with connection:
    connection.execute(TopioDefinition.definition)
