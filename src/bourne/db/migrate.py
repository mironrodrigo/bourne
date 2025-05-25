import os
from pathlib import Path
from cassandra.cluster import Cluster
from bourne.config.scylla import get_scylla_session


def run_migrations():
    session = get_scylla_session()
    migrations_dir = Path(__file__).parent / "migrations"

    for migration_file in sorted(os.listdir(migrations_dir)):
        if migration_file.endswith(".cql"):
            with open(migrations_dir / migration_file) as f:
                statements = f.read().split(";")
                for stmt in statements:
                    if stmt.strip():
                        session.execute(stmt + ";")


if __name__ == "__main__":
    run_migrations()