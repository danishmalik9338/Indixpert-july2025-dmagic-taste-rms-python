def validate_table(table_id: str, total_tables: int = 20) -> bool:
    try:
        tid = int(table_id)
        return 1 <= tid <= total_tables
    except Exception:
        return False
